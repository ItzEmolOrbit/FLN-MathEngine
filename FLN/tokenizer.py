from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
import re


class TokenType(Enum):
    NUMBER = "number"
    VARIABLE = "variable"
    OPERATOR = "operator"
    FUNCTION = "function"
    PARENTHESIS_LEFT = "parenthesis_left"
    PARENTHESIS_RIGHT = "parenthesis_right"
    COMMA = "comma"
    WHITESPACE = "whitespace"
    INTEGRAL = "integral"
    DERIVATIVE = "derivative"
    DIFFERENTIAL = "differential"


@dataclass
class Token:
    token_type: TokenType
    value: str
    position: int


class Tokenizer:
    def __init__(self):
        self.functions = {
            'sqrt', 'sin', 'cos', 'tan', 'log', 'ln', 'abs', 'exp',
            'floor', 'ceil', 'round', 'factorial', 'asin', 'acos', 'atan',
            'sinh', 'cosh', 'tanh'
        }
        
        self.operators = {'+', '-', '*', '/', '^', '='}
        
        self.token_patterns = [
            (TokenType.INTEGRAL, r'∫'),
            (TokenType.DERIVATIVE, r'd/d[a-zA-Z]'),
            (TokenType.DIFFERENTIAL, r'd[a-zA-Z]'),
            (TokenType.FUNCTION, r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\('),
            (TokenType.NUMBER, r'\b\d+\.?\d*\b'),
            (TokenType.VARIABLE, r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            (TokenType.OPERATOR, r'[\+\-\*/^=]'),
            (TokenType.PARENTHESIS_LEFT, r'\('),
            (TokenType.PARENTHESIS_RIGHT, r'\)'),
            (TokenType.COMMA, r','),
            (TokenType.WHITESPACE, r'\s+')
        ]
    
    def tokenize(self, expression: str) -> List[Token]:
        tokens = []
        position = 0
        
        while position < len(expression):
            match = None
            
            for token_type, pattern in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(expression, position)
                
                if match:
                    value = match.group(0)
                    
                    if token_type == TokenType.FUNCTION:
                        func_name = value.rstrip('(').rstrip()
                        if func_name in self.functions:
                            tokens.append(Token(TokenType.FUNCTION, func_name, position))
                            tokens.append(Token(TokenType.PARENTHESIS_LEFT, '(', position + len(func_name)))
                            position += len(value)
                            break
                        else:
                            continue
                    
                    if token_type != TokenType.WHITESPACE:
                        tokens.append(Token(token_type, value, position))
                    
                    position += len(value)
                    break
            
            if not match:
                raise ValueError(f"Unexpected character at position {position}: {expression[position]}")
        
        return tokens
    
    def is_function(self, name: str) -> bool:
        return name in self.functions


class TokenStream:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0

    def current(self) -> Optional[Token]:
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def advance(self) -> Optional[Token]:
        if self.position < len(self.tokens):
            self.position += 1
            return self.current()
        return None

    def peek(self, offset: int = 1) -> Optional[Token]:
        peek_pos = self.position + offset
        if peek_pos < len(self.tokens):
            return self.tokens[peek_pos]
        return None

    def match(self, token_type: TokenType) -> Optional[Token]:
        if self.current() and self.current().type == token_type:
            return self.advance()
        return None

    def expect(self, token_type: TokenType, error_message: str = None) -> Token:
        token = self.match(token_type)
        if token is None:
            message = error_message or f"Expected {token_type}, got {self.current()}"
            raise ValueError(message)
        return token

    def is_at_end(self) -> bool:
        return self.position >= len(self.tokens) or self.current().type == TokenType.EOF
