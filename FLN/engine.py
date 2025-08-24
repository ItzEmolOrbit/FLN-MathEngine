from typing import List, Dict, Optional, Union, Tuple, Any
from .parser import Parser
from .folex import Folex
from .natix import Natix
from .monitor import ComputationMonitor
from .ast_nodes import ASTNode
from .data_structures import EvaluationResult, ComputationStep, FormulaMatch, FormulaDefinition
from .cache import ExpressionCache, LazyEvaluator, get_global_cache
from .formula_database import FormulaDatabase, get_formula_database


class MathEngine:
    def __init__(self, enable_caching: bool = True, enable_lazy_evaluation: bool = True):
        self.parser = Parser()
        self.folex = Folex()
        self.natix = Natix()
        self.monitor = ComputationMonitor()
        
        self.enable_caching = enable_caching
        self.enable_lazy_evaluation = enable_lazy_evaluation
        
        if enable_caching:
            self.cache = get_global_cache()
        else:
            self.cache = None
            
        if enable_lazy_evaluation:
            self.lazy_evaluator = LazyEvaluator(self.cache) if self.cache else None
        else:
            self.lazy_evaluator = None
        
        self.formula_database = get_formula_database()
        self._load_all_formulas()
    
    def evaluate(self, expression: str, variables: Dict[str, float] = None) -> EvaluationResult:
        try:
            if self.enable_caching and self.cache:
                cached_result = self.cache.get_cached_evaluation(expression, variables)
                if cached_result is not None:
                    return cached_result
            
            # Detect formulas first
            detected_formulas = self.detect_formulas(expression)
            
            ast = self._parse_with_cache(expression)
            result = self.monitor.monitor_evaluation(ast, variables)
            
            # Apply detected formulas to the result
            if detected_formulas:
                result.applied_formulas = detected_formulas
                # Try to apply the highest confidence formula
                best_formula = max(detected_formulas, key=lambda f: f.confidence)
                if best_formula.confidence > 0.7:  # Only apply high-confidence formulas
                    try:
                        applied_result = self.apply_formula(expression, best_formula.formula_name)
                        if applied_result != expression:
                            result.final_result = applied_result
                    except:
                        pass  # If formula application fails, keep original result
            
            if self.enable_caching and self.cache:
                self.cache.cache_evaluation(expression, variables, result)
            
            return result
            
        except Exception as e:
            return EvaluationResult(
                original_expression=expression,
                final_result="ERROR",
                evaluation_type=None,
                applied_formulas=[],
                computation_steps=[],
                is_exact=False,
                error_message=str(e)
            )
    
    def evaluate_with_steps(self, expression: str, variables: Dict[str, float] = None) -> List[ComputationStep]:
        result = self.evaluate(expression, variables)
        return result.computation_steps
    
    def parse_expression(self, expression: str) -> ASTNode:
        return self._parse_with_cache(expression)
    
    def detect_formulas(self, expression: str) -> List[FormulaMatch]:
        ast = self.parse_expression(expression)
        return self.folex.detect_formulas(expression)
    
    def apply_formula(self, expression: str, formula_name: str) -> str:
        ast = self.parse_expression(expression)
        formula = self.folex.get_formula_by_name(formula_name)
        
        if formula:
            formula_matches = self.folex.detect_formulas(expression)
            if formula_matches:
                new_ast = self.folex.apply_formula_to_ast(ast, formula_matches[0])
                return new_ast.to_string()
        
        return expression
    
    def _load_all_formulas(self):
        all_formulas = self.formula_database.formulas
        self.folex.reload_formulas(all_formulas)
        self.monitor.reload_formulas(all_formulas)
    
    def _parse_with_cache(self, expression: str) -> ASTNode:
        if self.enable_caching and self.cache:
            cached_ast = self.cache.get_cached_ast(expression)
            if cached_ast is not None:
                return cached_ast
        
        ast = self.parser.parse(expression)
        
        if self.enable_caching and self.cache:
            self.cache.cache_ast(expression, ast)
        
        return ast
    
    def get_cache_stats(self) -> Dict[str, Any]:
        if self.cache:
            return self.cache.get_stats()
        return {}
    
    def clear_cache(self):
        if self.cache:
            self.cache.clear_all()
    
    def enable_caching(self, enabled: bool = True):
        self.enable_caching = enabled
        if enabled and not self.cache:
            self.cache = get_global_cache()
        elif not enabled:
            self.cache = None
    
    def add_to_lazy_queue(self, expression: str, variables: Dict[str, float] = None, priority: int = 0) -> str:
        if self.lazy_evaluator:
            return self.lazy_evaluator.add_to_queue(expression, variables, priority)
        raise RuntimeError("Lazy evaluation is not enabled")
    
    def evaluate_next_lazy(self) -> Optional[Tuple[str, Any]]:
        if self.lazy_evaluator:
            return self.lazy_evaluator.evaluate_next(self.evaluate)
        raise RuntimeError("Lazy evaluation is not enabled")
    
    def get_lazy_queue_status(self) -> Dict[str, Any]:
        if self.lazy_evaluator:
            return self.lazy_evaluator.get_queue_status()
        return {"queue_length": 0, "partial_results_count": 0}
    
    def clear_lazy_queue(self):
        if self.lazy_evaluator:
            self.lazy_evaluator.clear_queue()
    
    def enable_lazy_evaluation(self, enabled: bool = True):
        self.enable_lazy_evaluation = enabled
        if enabled and not self.lazy_evaluator and self.cache:
            self.lazy_evaluator = LazyEvaluator(self.cache)
        elif not enabled:
            self.lazy_evaluator = None
    
    def get_formulas_by_grade(self, grade: int) -> List[FormulaDefinition]:
        return self.formula_database.get_formulas_by_grade(grade)
    
    def get_formulas_by_category(self, category: str) -> List[FormulaDefinition]:
        return self.formula_database.get_formulas_by_category(category)
    
    def search_formulas(self, query: str) -> List[FormulaDefinition]:
        return self.formula_database.search_formulas(query)
    
    def get_formula_count(self) -> int:
        return self.formula_database.get_formula_count()
    
    def get_all_categories(self) -> List[str]:
        return self.formula_database.get_all_categories()
    
    def get_formula_by_name(self, name: str) -> Optional[FormulaDefinition]:
        return self.formula_database.get_formula_by_name(name)
    
    def reload_formulas(self):
        self.formula_database.reload_formulas()
        self._load_all_formulas()
    
    def get_performance_stats(self) -> Dict[str, Any]:
        stats = {
            "caching_enabled": self.enable_caching,
            "lazy_evaluation_enabled": self.enable_lazy_evaluation,
            "formula_count": self.get_formula_count(),
        }
        
        if self.cache:
            stats["cache_stats"] = self.get_cache_stats()
        
        if self.lazy_evaluator:
            stats["lazy_queue_stats"] = self.get_lazy_queue_status()
        
        return stats
    
    def __repr__(self) -> str:
        return f"MathEngine(caching={self.enable_caching}, lazy_eval={self.enable_lazy_evaluation})"
