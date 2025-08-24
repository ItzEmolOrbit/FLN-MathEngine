from typing import List, Dict, Optional, Union, Tuple, Any
from .ast_nodes import ASTNode
from .data_structures import ComputationStep, EvaluationResult, EvaluationType, FormulaMatch, FormulaDefinition
from .folex import Folex
from .natix import Natix


class ComputationMonitor:
    def __init__(self):
        self.folex = Folex()
        self.natix = Natix()
        self.error_log: List[str] = []
        self.warning_log: List[str] = []
    
    def monitor_evaluation(self, ast: ASTNode, variables: Dict[str, float] = None) -> EvaluationResult:
        try:
            formula_matches = self.folex.detect_formulas(ast.to_string())
            
            if formula_matches:
                rewritten_ast = self.folex.apply_formula_to_ast(ast, formula_matches[0])
                applied_formulas = formula_matches
            else:
                rewritten_ast = ast
                applied_formulas = []
            
            result, steps = self.natix.evaluate_with_formulas(
                rewritten_ast, variables, applied_formulas
            )
            
            enhanced_steps = self._enhance_steps_with_formulas(steps)
            
            evaluation_type = self._get_evaluation_type(result)
            
            eval_result = EvaluationResult(
                original_expression=ast.to_string(),
                final_result=str(result),
                evaluation_type=evaluation_type,
                applied_formulas=applied_formulas,
                computation_steps=enhanced_steps,
                is_exact=True,
                error_message=None
            )
            
            return eval_result
            
        except Exception as e:
            self.error_log.append(f"Evaluation error: {e}")
            return EvaluationResult(
                original_expression=ast.to_string(),
                final_result="ERROR",
                evaluation_type=EvaluationType.SYMBOLIC,
                applied_formulas=[],
                computation_steps=[],
                is_exact=False,
                error_message=str(e)
            )
    
    def _enhance_steps_with_formulas(self, steps: List[ComputationStep]) -> List[ComputationStep]:
        enhanced_steps = []
        
        for step in steps:
            try:
                step_formulas = self.folex.detect_formulas(step.result)
                
                if step_formulas:
                    enhanced_step = ComputationStep(
                        step_number=step.step_number,
                        expression=step.expression,
                        result=step.result,
                        operation=step.operation,
                        applied_formulas=step_formulas,
                        is_numeric=step.is_numeric,
                        explanation=step.explanation
                    )
                    enhanced_steps.append(enhanced_step)
                else:
                    enhanced_steps.append(step)
                    
            except Exception:
                enhanced_steps.append(step)
        
        return enhanced_steps
    
    def _get_evaluation_type(self, result: Union[float, str]) -> EvaluationType:
        if isinstance(result, (int, float)):
            return EvaluationType.NUMERIC
        elif isinstance(result, str):
            if any(c.isalpha() for c in result):
                return EvaluationType.SYMBOLIC
            else:
                return EvaluationType.NUMERIC
        else:
            return EvaluationType.MIXED
    
    def validate_expression(self, expression: str) -> Tuple[bool, List[str]]:
        errors = []
        
        try:
            from .parser import Parser
            
            parser = Parser()
            ast = parser.parse(expression)
            
            if not ast:
                errors.append("Failed to parse expression")
                return False, errors
            
            return True, errors
            
        except Exception as e:
            errors.append(f"Validation error: {e}")
            return False, errors
    
    def check_mathematical_correctness(self, ast: ASTNode) -> Tuple[bool, List[str]]:
        warnings = []
        
        try:
            expression_str = ast.to_string()
            
            if "0/0" in expression_str:
                warnings.append("Potential division by zero")
            
            if "sqrt(-" in expression_str:
                warnings.append("Square root of negative number")
            
            if "log(0" in expression_str or "log(-" in expression_str:
                warnings.append("Logarithm of non-positive number")
            
            return len(warnings) == 0, warnings
            
        except Exception as e:
            warnings.append(f"Correctness check error: {e}")
            return False, warnings
    
    def get_error_log(self) -> List[str]:
        return self.error_log.copy()
    
    def get_warning_log(self) -> List[str]:
        return self.warning_log.copy()
    
    def clear_logs(self):
        self.error_log.clear()
        self.warning_log.clear()
    
    def add_formula(self, formula: FormulaDefinition):
        self.folex.add_formula(formula)
    
    def get_formula_count(self) -> int:
        return self.folex.get_formula_count()
    
    def reload_formulas(self, formulas: List[FormulaDefinition]):
        self.folex.reload_formulas(formulas)
