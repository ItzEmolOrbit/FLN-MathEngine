import re
from typing import List, Optional, Dict, Any
from .data_structures import FormulaDefinition, FormulaMatch
from .ast_nodes import ASTNode


class Folex:
    def __init__(self):
        self.formulas: List[FormulaDefinition] = []
        self._initialize_default_formulas()
    
    def _initialize_default_formulas(self):
        from .formula_database import get_formula_database
        db = get_formula_database()
        # Access the formulas directly since there's no get_all_formulas method
        self.formulas = db.formulas
    
    def detect_formulas(self, expression: str) -> List[FormulaMatch]:
        """Actually detect formulas in the expression using pattern matching"""
        matches = []
        
        for formula in self.formulas:
            try:
                # Clean the expression for better matching
                clean_expr = self._clean_expression(expression)
                
                # Try to match the pattern
                match = self._match_formula_pattern(clean_expr, formula)
                if match:
                    matches.append(match)
            except Exception as e:
                continue
        
        # Sort by confidence (higher first)
        matches.sort(key=lambda x: x.confidence, reverse=True)
        return matches
    
    def _clean_expression(self, expression: str) -> str:
        """Clean expression for better pattern matching"""
        # Remove extra spaces
        cleaned = re.sub(r'\s+', '', expression)
        # Normalize operators
        cleaned = cleaned.replace('×', '*').replace('÷', '/')
        # Handle common mathematical symbols
        cleaned = cleaned.replace('²', '^2').replace('³', '^3')
        return cleaned
    
    def _match_formula_pattern(self, expression: str, formula: FormulaDefinition) -> Optional[FormulaMatch]:
        """Actually match a formula pattern against an expression"""
        try:
            # Convert formula pattern to a proper regex pattern
            pattern = self._convert_to_regex_pattern(formula.pattern)
            
            # Try to match
            match = re.search(pattern, expression, re.IGNORECASE)
            if match:
                # Extract variables
                variables = {}
                for i, group in enumerate(match.groups(), 1):
                    variables[f'var_{i}'] = group
                
                # Calculate confidence based on match quality
                confidence = self._calculate_confidence(expression, formula, match)
                
                return FormulaMatch(
                    formula_name=formula.name,
                    pattern=formula.pattern,
                    matched_expression=expression,
                    variables=variables,
                    confidence=confidence
                )
        except Exception:
            pass
        
        return None
    
    def _convert_to_regex_pattern(self, pattern: str) -> str:
        """Convert formula pattern to a proper regex pattern"""
        # Since our formula database now contains properly formatted regex patterns,
        # we can return them directly without conversion
        return pattern
    
    def _calculate_confidence(self, expression: str, formula: FormulaDefinition, match) -> float:
        """Calculate confidence score for a formula match"""
        base_confidence = 0.5
        
        # Pattern length bonus
        pattern_length = len(formula.pattern)
        if pattern_length > 10:
            base_confidence += 0.2
        
        # Match position bonus (prefer matches at start)
        if match.start() == 0:
            base_confidence += 0.1
        
        # Variable extraction bonus
        if match.groups():
            base_confidence += 0.2
        
        # Topic relevance bonus
        if formula.topic.lower() in expression.lower():
            base_confidence += 0.1
        
        return min(base_confidence, 1.0)
    
    def apply_formula_to_ast(self, ast: ASTNode, formula_match: FormulaMatch) -> ASTNode:
        """Apply a detected formula to transform the AST"""
        try:
            # For now, return the original AST
            # In a full implementation, this would transform the AST based on the formula
            return ast
        except Exception:
            return ast
    
    def add_formula(self, formula: FormulaDefinition):
        """Add a new formula to the database"""
        self.formulas.append(formula)
    
    def get_formula_count(self) -> int:
        """Get the total number of formulas"""
        return len(self.formulas)
    
    def reload_formulas(self, formulas: List[FormulaDefinition]):
        """Reload the formula database"""
        self.formulas = formulas
    
    def search_formulas(self, query: str) -> List[FormulaDefinition]:
        """Search formulas by name, description, or topic"""
        query = query.lower()
        results = []
        
        for formula in self.formulas:
            if (query in formula.name.lower() or 
                query in formula.description.lower() or 
                query in formula.topic.lower() or
                query in formula.category.lower()):
                results.append(formula)
        
        return results
    
    def get_formulas_by_topic(self, topic: str) -> List[FormulaDefinition]:
        """Get formulas by specific topic"""
        return [f for f in self.formulas if f.topic.lower() == topic.lower()]
    
    def get_formulas_by_grade(self, grade: int) -> List[FormulaDefinition]:
        """Get formulas by grade level"""
        return [f for f in self.formulas if f.grade == grade]
    
    def get_formulas_by_category(self, category: str) -> List[FormulaDefinition]:
        """Get formulas by category"""
        return [f for f in self.formulas if f.category.lower() == category.lower()]
    
    def suggest_formula(self, expression: str) -> Optional[FormulaDefinition]:
        """Suggest the most relevant formula for an expression"""
        matches = self.detect_formulas(expression)
        if matches:
            # Find the formula definition for the best match
            for formula in self.formulas:
                if formula.name == matches[0].formula_name:
                    return formula
        return None
