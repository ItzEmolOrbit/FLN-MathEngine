from typing import List, Optional
from .tokenizer import Token, TokenType
from .ast_nodes import (
    ASTNode, NumberNode, VariableNode, OperatorNode, FunctionNode, 
    ParenthesesNode, UnaryNode, DerivativeNode, IntegralNode
)


class Parser:
    def __init__(self):
        self.tokens: List[Token] = []
        self.current_position: int = 0
    
    def parse(self, expression: str) -> ASTNode:
        from .tokenizer import Tokenizer
        tokenizer = Tokenizer()
        self.tokens = tokenizer.tokenize(expression)
        self.current_position = 0
        
        # Check for special calculus expressions first
        if expression.startswith('d/d'):
            # Handle derivative format: d/dx(expression)
            return self._parse_derivative_from_string(expression)
        elif expression.startswith('∫'):
            return self._parse_integral_from_string(expression)
        else:
            return self._parse_expression()
    
    def _parse_expression(self) -> ASTNode:
        left = self._parse_term()
        
        while (self.current_position < len(self.tokens) and 
               self.tokens[self.current_position].token_type == TokenType.OPERATOR and
               self.tokens[self.current_position].value in ['+', '-']):
            
            operator = self.tokens[self.current_position].value
            self.current_position += 1
            right = self._parse_term()
            
            left = OperatorNode(operator, left, right)
        
        return left
    
    def _parse_term(self) -> ASTNode:
        left = self._parse_factor()
        
        while (self.current_position < len(self.tokens) and 
               self.tokens[self.current_position].token_type == TokenType.OPERATOR and
               self.tokens[self.current_position].value in ['*', '/', '%']):
            
            operator = self.tokens[self.current_position].value
            self.current_position += 1
            right = self._parse_factor()
            
            left = OperatorNode(operator, left, right)
        
        return left
    
    def _parse_factor(self) -> ASTNode:
        # Check for unary operators first
        if (self.current_position < len(self.tokens) and 
            self.tokens[self.current_position].token_type == TokenType.OPERATOR and
            self.tokens[self.current_position].value in ['+', '-']):
            
            operator = self.tokens[self.current_position].value
            self.current_position += 1
            operand = self._parse_power()
            return UnaryNode(operator, operand)
        
        return self._parse_power()
    
    def _parse_power(self) -> ASTNode:
        left = self._parse_primary()
        
        while (self.current_position < len(self.tokens) and 
               self.tokens[self.current_position].token_type == TokenType.OPERATOR and
               self.tokens[self.current_position].value == '^'):
            
            operator = self.tokens[self.current_position].value
            self.current_position += 1
            right = self._parse_primary()
            
            left = OperatorNode(operator, left, right)
        
        return left
    
    def _parse_primary(self) -> ASTNode:
        if self.current_position >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        
        token = self.tokens[self.current_position]
        
        if token.token_type == TokenType.NUMBER:
            self.current_position += 1
            try:
                if '.' in token.value:
                    return NumberNode(float(token.value))
                else:
                    return NumberNode(int(token.value))
            except ValueError:
                return NumberNode(float(token.value))
        
        elif token.token_type == TokenType.VARIABLE:
            self.current_position += 1
            return VariableNode(token.value)
        
        elif token.token_type == TokenType.FUNCTION:
            return self._parse_function()
        
        elif token.token_type == TokenType.PARENTHESIS_LEFT:
            return self._parse_parentheses()
        
        elif token.token_type == TokenType.INTEGRAL:
            return self._parse_integral()
        
        elif token.token_type == TokenType.DERIVATIVE:
            return self._parse_derivative()
        
        elif token.token_type == TokenType.DIFFERENTIAL:
            return self._parse_differential()
        
        else:
            raise ValueError(f"Unexpected token type: {token.token_type} at position {token.position}")
    
    def _parse_function(self) -> FunctionNode:
        if (self.current_position >= len(self.tokens) or 
            self.tokens[self.current_position].token_type != TokenType.FUNCTION):
            raise ValueError("Expected function")
        
        function_name = self.tokens[self.current_position].value
        self.current_position += 1
        
        if (self.current_position >= len(self.tokens) or 
            self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_LEFT):
            raise ValueError("Expected '(' after function name")
        
        self.current_position += 1  # Skip '('
        argument = self._parse_expression()
        
        if (self.current_position >= len(self.tokens) or 
            self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_RIGHT):
            raise ValueError("Expected ')' after function argument")
        
        self.current_position += 1  # Skip ')'
        return FunctionNode(function_name, argument)
    
    def _parse_parentheses(self) -> ParenthesesNode:
        if (self.current_position >= len(self.tokens) or 
            self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_LEFT):
            raise ValueError("Expected '('")
        
        self.current_position += 1  # Skip '('
        expression = self._parse_expression()
        
        if (self.current_position >= len(self.tokens) or 
            self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_RIGHT):
            raise ValueError("Expected ')'")
        
        self.current_position += 1  # Skip ')'
        return ParenthesesNode(expression)
    
    def _parse_integral(self) -> IntegralNode:
        # Parse ∫expression dx format
        if self.current_position >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        
        # Check for definite integral ∫_a^b expression dx
        if (self.current_position + 1 < len(self.tokens) and
            self.tokens[self.current_position + 1].value == '_'):
            # Definite integral
            self.current_position += 2  # Skip '∫_'
            lower_bound = self._parse_expression()
            
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].value != '^'):
                raise ValueError("Expected '^' in definite integral")
            
            self.current_position += 1
            upper_bound = self._parse_expression()
            
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_LEFT):
                raise ValueError("Expected '(' after integral bounds")
            
            self.current_position += 1
            expression = self._parse_expression()
            
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_RIGHT):
                raise ValueError("Expected ')' after integral expression")
            
            self.current_position += 1
            
            # Parse dx
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].value != 'dx'):
                raise ValueError("Expected 'dx' after integral expression")
            
            self.current_position += 1
            return IntegralNode("x", expression, lower_bound, upper_bound)
        else:
            # Indefinite integral
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_LEFT):
                raise ValueError("Expected '(' after integral symbol")
            
            self.current_position += 1
            expression = self._parse_expression()
            
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_RIGHT):
                raise ValueError("Expected ')' after integral expression")
            
            self.current_position += 1
            
            # Parse dx
            if (self.current_position >= len(self.tokens) or
                self.tokens[self.current_position].value != 'dx'):
                raise ValueError("Expected 'dx' after integral expression")
            
            self.current_position += 1
            return IntegralNode("x", expression)
    
    def _parse_derivative(self) -> DerivativeNode:
        # Parse d/dx(expression) format
        if (self.current_position >= len(self.tokens) or
            self.tokens[self.current_position].token_type != TokenType.DERIVATIVE):
            raise ValueError("Expected derivative format")
        
        derivative_token = self.tokens[self.current_position]
        self.current_position += 1
        
        # Extract variable from d/dx
        variable = derivative_token.value[3:]  # Skip 'd/d'
        
        if (self.current_position >= len(self.tokens) or
            self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_LEFT):
            raise ValueError("Expected '(' after derivative")
        
        self.current_position += 1  # Skip '('
        expression = self._parse_expression()
        
        if (self.current_position >= len(self.tokens) or
            self.tokens[self.current_position].token_type != TokenType.PARENTHESIS_RIGHT):
            raise ValueError("Expected ')' after derivative expression")
        
        self.current_position += 1  # Skip ')'
        return DerivativeNode(variable, expression)
    
    def _parse_differential(self) -> VariableNode:
        # Parse dx, dy, etc.
        if (self.current_position >= len(self.tokens) or
            self.tokens[self.current_position].token_type != TokenType.DIFFERENTIAL):
            raise ValueError("Expected differential")
        
        differential_token = self.tokens[self.current_position]
        self.current_position += 1
        
        # Extract variable from dx
        variable = differential_token.value[1:]  # Skip 'd'
        return VariableNode(variable)
    
    def _parse_derivative_from_string(self, expression: str) -> DerivativeNode:
        """Parse derivative directly from string to avoid tokenization issues"""
        # Extract variable from d/dx format
        if not expression.startswith('d/d'):
            raise ValueError("Invalid derivative format: expected d/dx(expression)")
        
        # Find the variable after d/d
        var_start = 3  # Skip 'd/d'
        var_end = var_start
        while var_end < len(expression) and expression[var_end] != '(':
            var_end += 1
        
        if var_end >= len(expression):
            raise ValueError("Expected '(' after d/dx")
        
        variable = expression[var_start:var_end]
        
        # Find the expression inside parentheses
        expr_start = var_end + 1  # Skip '('
        expr_end = len(expression) - 1  # Skip ')'
        
        if expr_end < expr_start:
            raise ValueError("Expected ')' after derivative expression")
        
        inner_expression = expression[expr_start:expr_end]
        
        # Create a new parser instance to parse the inner expression
        from .tokenizer import Tokenizer
        inner_tokenizer = Tokenizer()
        inner_tokens = inner_tokenizer.tokenize(inner_expression)
        
        # Create a new parser for the inner expression
        inner_parser = Parser()
        inner_parser.tokens = inner_tokens
        inner_parser.current_position = 0
        
        # Use the full expression parsing to handle operators like ^
        inner_ast = inner_parser._parse_expression()
        
        return DerivativeNode(variable, inner_ast)
    
    def _parse_integral_from_string(self, expression: str) -> IntegralNode:
        """Parse integral directly from string to avoid tokenization issues"""
        # Extract the expression inside ∫...dx format
        if not expression.startswith('∫'):
            raise ValueError("Invalid integral format: expected ∫expression dx")
        
        # Find the expression inside ∫...dx
        expr_start = 1  # Skip '∫'
        expr_end = expression.rfind(' dx')
        
        if expr_end == -1:
            raise ValueError("Expected 'dx' at end of integral")
        
        inner_expression = expression[expr_start:expr_end]
        
        # Create a new parser instance to parse the inner expression
        from .tokenizer import Tokenizer
        inner_tokenizer = Tokenizer()
        inner_tokens = inner_tokenizer.tokenize(inner_expression)
        
        # Create a new parser for the inner expression
        inner_parser = Parser()
        inner_parser.tokens = inner_tokens
        inner_parser.current_position = 0
        
        # Use the full expression parsing to handle operators like ^
        inner_ast = inner_parser._parse_expression()
        
        return IntegralNode("x", inner_ast)
    
    def parse_advanced_expression(self, expression: str) -> ASTNode:
        """Parse advanced mathematical expressions including derivatives and integrals"""
        # Handle special cases
        if expression.startswith('d/d'):
            return self._parse_derivative()
        elif expression.startswith('∫'):
            return self._parse_integral()
        else:
            return self.parse(expression)
