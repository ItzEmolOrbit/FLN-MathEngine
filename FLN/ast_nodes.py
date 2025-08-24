from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Union
import math
import re


@dataclass
class ASTNode:
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        pass
    
    def to_string(self) -> str:
        pass
    
    def clone(self) -> 'ASTNode':
        pass


@dataclass
class NumberNode(ASTNode):
    value: Union[int, float]
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        return self.value
    
    def to_string(self) -> str:
        return str(self.value)
    
    def clone(self) -> 'NumberNode':
        return NumberNode(self.value)


@dataclass
class VariableNode(ASTNode):
    name: str
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        if variables and self.name in variables:
            return variables[self.name]
        return self.name
    
    def to_string(self) -> str:
        return self.name
    
    def clone(self) -> 'VariableNode':
        return VariableNode(self.name)


@dataclass
class OperatorNode(ASTNode):
    operator: str
    left: ASTNode
    right: ASTNode
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        left_val = self.left.evaluate(variables)
        right_val = self.right.evaluate(variables)
        
        # Handle symbolic expressions
        if isinstance(left_val, str) or isinstance(right_val, str):
            return f"({left_val} {self.operator} {right_val})"
        
        # Handle numeric operations
        try:
            if self.operator == "+":
                return left_val + right_val
            elif self.operator == "-":
                return left_val - right_val
            elif self.operator == "*":
                return left_val * right_val
            elif self.operator == "/":
                if right_val == 0:
                    return "Error: Division by zero"
                return left_val / right_val
            elif self.operator == "^":
                if left_val < 0 and right_val != int(right_val):
                    return f"({left_val})^{right_val}"  # Keep symbolic for complex powers
                
                # Check for overflow
                if right_val > 1000:
                    return f"Error: Power too large ({left_val}^{right_val})"
                if right_val < -1000:
                    return f"Error: Power too small ({left_val}^{right_val})"
                
                try:
                    result = left_val ** right_val
                    if abs(result) > 1e308:  # Python's float limit
                        return f"Error: Power overflow ({left_val}^{right_val})"
                    # Check if result is too large for practical use
                    if abs(result) > 1e50:
                        return f"Warning: Power result extremely large ({left_val}^{right_val})"
                    return result
                except OverflowError:
                    return f"Error: Power overflow ({left_val}^{right_val})"
            elif self.operator == "%":
                return left_val % right_val
            else:
                return f"Error: Unknown operator {self.operator}"
        except (ValueError, OverflowError) as e:
            return f"Error: {str(e)}"
    
    def to_string(self) -> str:
        return f"({self.left.to_string()} {self.operator} {self.right.to_string()})"
    
    def clone(self) -> 'OperatorNode':
        return OperatorNode(self.operator, self.left.clone(), self.right.clone())


@dataclass
class FunctionNode(ASTNode):
    function_name: str
    argument: ASTNode
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        arg_value = self.argument.evaluate(variables)
        
        # Handle symbolic arguments
        if isinstance(arg_value, str):
            return f"{self.function_name}({arg_value})"
        
        # Handle numeric arguments
        try:
            if self.function_name == "sqrt":
                if arg_value < 0:
                    return f"sqrt({arg_value})"  # Keep symbolic for negative
                return math.sqrt(arg_value)
            elif self.function_name == "sin":
                return math.sin(arg_value)
            elif self.function_name == "cos":
                return math.cos(arg_value)
            elif self.function_name == "tan":
                # Check for undefined values (π/2 + kπ)
                if abs(math.cos(arg_value)) < 1e-10:
                    return f"Error: Tangent undefined at {arg_value} (cos({arg_value}) = 0)"
                # Check specifically for pi/2
                if abs(arg_value - math.pi/2) < 1e-10:
                    return f"Error: Tangent undefined at π/2"
                return math.tan(arg_value)
            elif self.function_name == "log":
                if arg_value <= 0:
                    return f"log({arg_value})"  # Keep symbolic for non-positive
                return math.log10(arg_value)
            elif self.function_name == "ln":
                if arg_value <= 0:
                    return f"ln({arg_value})"  # Keep symbolic for non-positive
                return math.log(arg_value)
            elif self.function_name == "abs":
                return abs(arg_value)
            elif self.function_name == "floor":
                return math.floor(arg_value)
            elif self.function_name == "ceil":
                return math.ceil(arg_value)
            elif self.function_name == "round":
                return round(arg_value)
            elif self.function_name == "exp":
                return math.exp(arg_value)
            elif self.function_name == "factorial":
                if arg_value < 0 or arg_value != int(arg_value):
                    return f"factorial({arg_value})"  # Keep symbolic for invalid
                return math.factorial(int(arg_value))
            elif self.function_name == "asin":
                if arg_value < -1 or arg_value > 1:
                    return f"asin({arg_value})"  # Keep symbolic for invalid
                return math.asin(arg_value)
            elif self.function_name == "acos":
                if arg_value < -1 or arg_value > 1:
                    return f"acos({arg_value})"  # Keep symbolic for invalid
                return math.acos(arg_value)
            elif self.function_name == "atan":
                return math.atan(arg_value)
            elif self.function_name == "sinh":
                return math.sinh(arg_value)
            elif self.function_name == "cosh":
                return math.cosh(arg_value)
            elif self.function_name == "tanh":
                return math.tanh(arg_value)
            elif self.function_name == "cbrt":
                return arg_value ** (1/3)
            elif self.function_name == "root":
                # For nth root, we need to handle this differently
                return f"root({arg_value})"
            else:
                return f"{self.function_name}({arg_value})"
        except (ValueError, OverflowError) as e:
            return f"{self.function_name}({arg_value})"
    
    def to_string(self) -> str:
        return f"{self.function_name}({self.argument.to_string()})"
    
    def clone(self) -> 'FunctionNode':
        return FunctionNode(self.function_name, self.argument.clone())


@dataclass
class ParenthesesNode(ASTNode):
    expression: ASTNode
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        return self.expression.evaluate(variables)
    
    def to_string(self) -> str:
        return f"({self.expression.to_string()})"
    
    def clone(self) -> 'ParenthesesNode':
        return ParenthesesNode(self.expression.clone())


@dataclass
class UnaryNode(ASTNode):
    operator: str
    operand: ASTNode
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        operand_value = self.operand.evaluate(variables)
        
        if isinstance(operand_value, str):
            return f"{self.operator}{operand_value}"
        
        try:
            if self.operator == "-":
                return -operand_value
            elif self.operator == "+":
                return operand_value
            else:
                return f"Error: Unknown unary operator {self.operator}"
        except (ValueError, OverflowError) as e:
            return f"Error: {str(e)}"
    
    def to_string(self) -> str:
        return f"{self.operator}{self.operand.to_string()}"
    
    def clone(self) -> 'UnaryNode':
        return UnaryNode(self.operator, self.operand.clone())


@dataclass
class DerivativeNode(ASTNode):
    variable: str
    expression: ASTNode
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        # Basic derivative rules
        expr_str = self.expression.to_string()
        
        # Power rule: d/dx(x^n) = n*x^(n-1)
        # Handle both x^n and (x^n) formats
        power_match = re.match(r'\(?(\w+)\s*\^\s*(\d+)\)?', expr_str)
        if power_match and power_match.group(1) == self.variable:
            base = power_match.group(1)
            power = int(power_match.group(2))
            if power == 1:
                return "1"
            elif power == 0:
                return "0"
            else:
                return f"{power}*{base}^{power-1}"
        
        # Constant rule: d/dx(c) = 0
        if expr_str.isdigit() or (expr_str.startswith('-') and expr_str[1:].isdigit()):
            return "0"
        
        # Variable rule: d/dx(x) = 1
        if expr_str == self.variable:
            return "1"
        
        # Sum rule: d/dx(f + g) = d/dx(f) + d/dx(g)
        if '+' in expr_str and not self._is_inside_function(expr_str):
            parts = self._split_expression(expr_str, '+')
            derivatives = []
            for part in parts:
                part = part.strip()
                if part:  # Skip empty parts
                    # Create a simple variable node for the part
                    if part.isdigit() or (part.startswith('-') and part[1:].isdigit()):
                        derivatives.append("0")  # Constant
                    elif part == self.variable:
                        derivatives.append("1")  # Variable
                    elif '^' in part:
                        # Handle power expressions
                        power_match = re.match(r'(\w+)\^(\d+)', part)
                        if power_match and power_match.group(1) == self.variable:
                            base = power_match.group(1)
                            power = int(power_match.group(2))
                            if power == 1:
                                derivatives.append("1")
                            elif power == 0:
                                derivatives.append("0")
                            else:
                                derivatives.append(f"{power}*{base}^{power-1}")
                        else:
                            derivatives.append(f"d/d{self.variable}({part})")
                    elif '*' in part:
                        # Handle simple products
                        prod_parts = self._split_expression(part, '*')
                        if len(prod_parts) == 2:
                            f, g = prod_parts[0].strip(), prod_parts[1].strip()
                            if f == self.variable and g.isdigit():
                                derivatives.append(g)  # d/dx(x*c) = c
                            elif g == self.variable and f.isdigit():
                                derivatives.append(f)  # d/dx(c*x) = c
                            else:
                                derivatives.append(f"d/d{self.variable}({part})")
                        else:
                            derivatives.append(f"d/d{self.variable}({part})")
                    else:
                        derivatives.append(f"d/d{self.variable}({part})")
            return ' + '.join(derivatives)
        
        # Product rule: d/dx(f * g) = f * d/dx(g) + g * d/dx(f)
        if '*' in expr_str and not self._is_inside_function(expr_str):
            parts = self._split_expression(expr_str, '*')
            if len(parts) == 2:
                f, g = parts[0].strip(), parts[1].strip()
                # Handle simple cases first
                if f == self.variable and g.isdigit():
                    return g  # d/dx(x*c) = c
                elif g == self.variable and f.isdigit():
                    return f  # d/dx(c*x) = c
                elif f == self.variable and g == self.variable:
                    return f"2*{self.variable}"  # d/dx(x*x) = 2x
                else:
                    # General product rule
                    deriv_f = self._simple_derivative(f)
                    deriv_g = self._simple_derivative(g)
                    return f"{f}*{deriv_g} + {g}*{deriv_f}"
        
        # Chain rule for functions: d/dx(f(g(x))) = f'(g(x)) * g'(x)
        if '(' in expr_str and ')' in expr_str:
            # Handle basic function derivatives
            if expr_str.startswith(f"sin({self.variable})"):
                return f"cos({self.variable})"
            elif expr_str.startswith(f"cos({self.variable})"):
                return f"-sin({self.variable})"
            elif expr_str.startswith(f"tan({self.variable})"):
                return f"sec^2({self.variable})"
            elif expr_str.startswith(f"exp({self.variable})"):
                return f"exp({self.variable})"
            elif expr_str.startswith(f"ln({self.variable})"):
                return f"1/{self.variable}"
            elif expr_str.startswith(f"sqrt({self.variable})"):
                return f"1/(2*sqrt({self.variable}))"
            elif expr_str.startswith(f"log({self.variable})"):
                return f"1/({self.variable}*ln(10))"
        
        # Default: keep symbolic
        return f"d/d{self.variable}({expr_str})"
    
    def _is_inside_function(self, expr_str: str) -> bool:
        """Check if the expression is inside a function call"""
        return expr_str.count('(') > expr_str.count(')')
    
    def _split_expression(self, expr_str: str, operator: str) -> List[str]:
        """Split expression by operator, respecting parentheses"""
        parts = []
        current_part = ""
        paren_count = 0
        
        for char in expr_str:
            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
            elif char == operator and paren_count == 0:
                parts.append(current_part)
                current_part = ""
                continue
            current_part += char
        
        if current_part:
            parts.append(current_part)
        
        return parts
    
    def _simple_derivative(self, expr: str) -> str:
        """Calculate simple derivatives for product rule"""
        if expr.isdigit() or (expr.startswith('-') and expr[1:].isdigit()):
            return "0"  # Constant
        elif expr == self.variable:
            return "1"  # Variable
        elif '^' in expr:
            power_match = re.match(r'(\w+)\^(\d+)', expr)
            if power_match and power_match.group(1) == self.variable:
                base = power_match.group(1)
                power = int(power_match.group(2))
                if power == 1:
                    return "1"
                elif power == 0:
                    return "0"
                else:
                    return f"{power}*{base}^{power-1}"
        return f"d/d{self.variable}({expr})"
    
    def to_string(self) -> str:
        return f"d/d{self.variable}({self.expression.to_string()})"
    
    def clone(self) -> 'DerivativeNode':
        return DerivativeNode(self.variable, self.expression.clone())


@dataclass
class IntegralNode(ASTNode):
    variable: str
    expression: ASTNode
    lower_bound: Optional[ASTNode] = None
    upper_bound: Optional[ASTNode] = None
    
    def evaluate(self, variables: Dict[str, float] = None) -> Union[float, str]:
        expr_str = self.expression.to_string()
        
        # Basic integration rules
        # Power rule: ∫x^n dx = x^(n+1)/(n+1) + C
        power_match = re.match(r'(\w+)\^(\d+)', expr_str)
        if power_match and power_match.group(1) == self.variable:
            base = power_match.group(1)
            power = int(power_match.group(2))
            if power == -1:
                return f"ln({base}) + C"
            else:
                new_power = power + 1
                return f"{base}^{new_power}/{new_power} + C"
        
        # Constant rule: ∫c dx = c*x + C
        if expr_str.isdigit() or (expr_str.startswith('-') and expr_str[1:].isdigit()):
            return f"{expr_str}*{self.variable} + C"
        
        # Variable rule: ∫x dx = x^2/2 + C
        if expr_str == self.variable:
            return f"{self.variable}^2/2 + C"
        
        # Sum rule: ∫(f + g) dx = ∫f dx + ∫g dx
        if '+' in expr_str and not self._is_inside_function(expr_str):
            parts = self._split_expression(expr_str, '+')
            integrals = []
            for part in parts:
                part = part.strip()
                if part:  # Skip empty parts
                    if part.isdigit() or (part.startswith('-') and part[1:].isdigit()):
                        integrals.append(f"{part}*{self.variable}")  # Constant
                    elif part == self.variable:
                        integrals.append(f"{self.variable}^2/2")  # Variable
                    elif '^' in part:
                        # Handle power expressions
                        power_match = re.match(r'(\w+)\^(\d+)', part)
                        if power_match and power_match.group(1) == self.variable:
                            base = power_match.group(1)
                            power = int(power_match.group(2))
                            if power == -1:
                                integrals.append(f"ln({base})")
                            else:
                                new_power = power + 1
                                integrals.append(f"{base}^{new_power}/{new_power}")
                        else:
                            integrals.append(f"∫{part} d{self.variable}")
                    elif '*' in part:
                        # Handle simple products
                        prod_parts = self._split_expression(part, '*')
                        if len(prod_parts) == 2:
                            f, g = prod_parts[0].strip(), prod_parts[1].strip()
                            if f.isdigit() and g == self.variable:
                                integrals.append(f"{f}*{g}^2/2")  # ∫c*x dx = c*x^2/2
                            elif g.isdigit() and f == self.variable:
                                integrals.append(f"{g}*{f}^2/2")  # ∫x*c dx = c*x^2/2
                            else:
                                integrals.append(f"∫{part} d{self.variable}")
                        else:
                            integrals.append(f"∫{part} d{self.variable}")
                    else:
                        integrals.append(f"∫{part} d{self.variable}")
            return ' + '.join(integrals) + " + C"
        
        # Function rule: ∫f(x) dx
        if '(' in expr_str and ')' in expr_str:
            if expr_str.startswith(f"sin({self.variable})"):
                return f"-cos({self.variable}) + C"
            elif expr_str.startswith(f"cos({self.variable})"):
                return f"sin({self.variable}) + C"
            elif expr_str.startswith(f"tan({self.variable})"):
                return f"-ln(cos({self.variable})) + C"
            elif expr_str.startswith(f"exp({self.variable})"):
                return f"exp({self.variable}) + C"
            elif expr_str.startswith(f"1/{self.variable}"):
                return f"ln({self.variable}) + C"
            elif expr_str.startswith(f"sqrt({self.variable})"):
                return f"(2/3)*{self.variable}^(3/2) + C"
            elif expr_str.startswith(f"ln({self.variable})"):
                return f"{self.variable}*ln({self.variable}) - {self.variable} + C"
            elif expr_str.startswith(f"log({self.variable})"):
                return f"{self.variable}*log({self.variable}) - {self.variable}/ln(10) + C"
        
        # Default: keep symbolic
        return f"∫{expr_str} d{self.variable}"
    
    def _is_inside_function(self, expr_str: str) -> bool:
        """Check if the expression is inside a function call"""
        return expr_str.count('(') > expr_str.count(')')
    
    def _split_expression(self, expr_str: str, operator: str) -> List[str]:
        """Split expression by operator, respecting parentheses"""
        parts = []
        current_part = ""
        paren_count = 0
        
        for char in expr_str:
            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
            elif char == operator and paren_count == 0:
                parts.append(current_part)
                current_part = ""
                continue
            current_part += char
        
        if current_part:
            parts.append(current_part)
        
        return parts
    
    def to_string(self) -> str:
        if self.lower_bound and self.upper_bound:
            return f"∫_{self.lower_bound.to_string()}^{self.upper_bound.to_string()} {self.expression.to_string()} d{self.variable}"
        else:
            return f"∫{self.expression.to_string()} d{self.variable}"
    
    def clone(self) -> 'IntegralNode':
        return IntegralNode(
            self.variable, 
            self.expression.clone(),
            self.lower_bound.clone() if self.lower_bound else None,
            self.upper_bound.clone() if self.upper_bound else None
        )
