from typing import List, Dict, Optional, Union, Tuple, Any
import math
from functools import lru_cache
from .ast_nodes import (
    ASTNode, NumberNode, VariableNode, OperatorNode, FunctionNode, 
    ParenthesesNode, UnaryNode, DerivativeNode, IntegralNode
)
from .data_structures import ComputationStep, EvaluationType, FormulaMatch


class EvaluationContext:
    def __init__(self, variables: Dict[str, float] = None):
        self.variables = variables or {}
        self.steps: List[ComputationStep] = []
        self.step_number = 0
        self.applied_formulas: List[FormulaMatch] = []
        self.cache: Dict[str, Union[float, str]] = {}  # Add caching
    
    def add_step(self, expression: str, result: str, operation: str, 
                 is_numeric: bool = False, explanation: str = None,
                 applied_formulas: List[FormulaMatch] = None) -> None:
        self.step_number += 1
        step = ComputationStep(
            step_number=self.step_number,
            expression=expression,
            result=result,
            operation=operation,
            applied_formulas=applied_formulas or [],
            is_numeric=is_numeric,
            explanation=explanation
        )
        self.steps.append(step)
    
    def add_formula_match(self, formula_match: FormulaMatch) -> None:
        self.applied_formulas.append(formula_match)
    
    def get_cached_result(self, expression: str) -> Optional[Union[float, str]]:
        """Get cached result for an expression"""
        return self.cache.get(expression)
    
    def cache_result(self, expression: str, result: Union[float, str]) -> None:
        """Cache a result for an expression"""
        self.cache[expression] = result


class Natix:
    def __init__(self):
        self.context: Optional[EvaluationContext] = None
        self._function_cache: Dict[str, Any] = {}
    
    def evaluate(self, ast: ASTNode, variables: Dict[str, float] = None) -> Tuple[Union[float, str], List[ComputationStep]]:
        self.context = EvaluationContext(variables)
        result = self._evaluate_node(ast)
        return result, self.context.steps
    
    def evaluate_with_formulas(self, ast: ASTNode, variables: Dict[str, float] = None,
                             formula_matches: List[FormulaMatch] = None) -> Tuple[Union[float, str], List[ComputationStep]]:
        self.context = EvaluationContext(variables)
        if formula_matches:
            self.context.applied_formulas.extend(formula_matches)
        
        result = self._evaluate_node(ast)
        return result, self.context.steps
    
    def _evaluate_node(self, node: ASTNode) -> Union[float, str]:
        # Check cache first
        node_str = node.to_string()
        cached_result = self.context.get_cached_result(node_str)
        if cached_result is not None:
            self.context.add_step(
                expression=node_str,
                result=str(cached_result),
                operation="cached_result",
                is_numeric=isinstance(cached_result, (int, float)),
                explanation=f"Cached result: {cached_result}"
            )
            return cached_result
        
        # Evaluate the node
        if isinstance(node, NumberNode):
            result = self._evaluate_number(node)
        elif isinstance(node, VariableNode):
            result = self._evaluate_variable(node)
        elif isinstance(node, OperatorNode):
            result = self._evaluate_operator(node)
        elif isinstance(node, FunctionNode):
            result = self._evaluate_function(node)
        elif isinstance(node, ParenthesesNode):
            result = self._evaluate_parentheses(node)
        elif isinstance(node, UnaryNode):
            result = self._evaluate_unary(node)
        elif isinstance(node, DerivativeNode):
            result = self._evaluate_derivative(node)
        elif isinstance(node, IntegralNode):
            result = self._evaluate_integral(node)
        else:
            raise ValueError(f"Unknown node type: {type(node)}")
        
        # Cache the result
        self.context.cache_result(node_str, result)
        return result
    
    def _evaluate_number(self, node: NumberNode) -> float:
        result = node.value
        self.context.add_step(
            expression=str(result),
            result=str(result),
            operation="number",
            is_numeric=True,
            explanation=f"Number value: {result}"
        )
        return result
    
    def _evaluate_variable(self, node: VariableNode) -> Union[float, str]:
        var_name = node.name
        
        if var_name in self.context.variables:
            result = self.context.variables[var_name]
            self.context.add_step(
                expression=var_name,
                result=str(result),
                operation="variable_substitution",
                is_numeric=True,
                explanation=f"Substituted {var_name} = {result}"
            )
            return result
        else:
            self.context.add_step(
                expression=var_name,
                result=var_name,
                operation="variable_symbolic",
                is_numeric=False,
                explanation=f"Variable {var_name} kept symbolic"
            )
            return var_name
    
    def _evaluate_operator(self, node: OperatorNode) -> Union[float, str]:
        # Evaluate left and right operands
        left = self._evaluate_node(node.left)
        right = self._evaluate_node(node.right)
        
        # Handle symbolic operands
        if isinstance(left, str) or isinstance(right, str):
            result = f"{left} {node.operator} {right}"
            self.context.add_step(
                expression=f"{left} {node.operator} {right}",
                result=result,
                operation="symbolic_operation",
                is_numeric=False,
                explanation=f"Symbolic operation: {left} {node.operator} {right}"
            )
            return result
        
        # Handle numeric operands
        try:
            if node.operator == "+":
                result = left + right
                operation = "addition"
                explanation = f"Added {left} and {right}"
            elif node.operator == "-":
                result = left - right
                operation = "subtraction"
                explanation = f"Subtracted {right} from {left}"
            elif node.operator == "*":
                result = left * right
                operation = "multiplication"
                explanation = f"Multiplied {left} by {right}"
            elif node.operator == "/":
                if right == 0:
                    error_msg = f"Error: Division by zero ({left} / {right})"
                    self.context.add_step(
                        expression=f"{left} {node.operator} {right}",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = left / right
                operation = "division"
                explanation = f"Divided {left} by {right}"
            elif node.operator == "^":
                if right == 0:
                    result = 1
                    operation = "power"
                    explanation = f"Any number to power 0 equals 1"
                elif right == 1:
                    result = left
                    operation = "power"
                    explanation = f"Any number to power 1 equals itself"
                elif right < 0 and left == 0:
                    error_msg = f"Error: Cannot raise 0 to negative power {right}"
                    self.context.add_step(
                        expression=f"{left} {node.operator} {right}",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                elif right < 0 and abs(left) < 1e-10:
                    error_msg = f"Error: Cannot raise very small number {left} to negative power {right}"
                    self.context.add_step(
                        expression=f"{left} {node.operator} {right}",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                else:
                    try:
                        result = left ** right
                        if math.isinf(result):
                            error_msg = f"Error: Power overflow: {left}^{right}"
                            self.context.add_step(
                                expression=f"{left} {node.operator} {right}",
                                result=error_msg,
                                operation="error",
                                is_numeric=False,
                                explanation=error_msg
                            )
                            return error_msg
                    except OverflowError:
                        error_msg = f"Error: Power overflow: {left}^{right}"
                        self.context.add_step(
                            expression=f"{left} {node.operator} {right}",
                            result=error_msg,
                            operation="error",
                            is_numeric=False,
                            explanation=error_msg
                        )
                        return error_msg
                    operation = "power"
                    explanation = f"Raised {left} to power {right}"
            elif node.operator == "%":
                if right == 0:
                    error_msg = f"Error: Modulo by zero ({left} % {right})"
                    self.context.add_step(
                        expression=f"{left} {node.operator} {right}",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = left % right
                operation = "modulo"
                explanation = f"Modulo of {left} by {right}"
            else:
                error_msg = f"Error: Unknown operator '{node.operator}'"
                self.context.add_step(
                    expression=f"{left} {node.operator} {right}",
                    result=error_msg,
                    operation="error",
                    is_numeric=False,
                    explanation=error_msg
                )
                return error_msg
            
            self.context.add_step(
                expression=f"{left} {node.operator} {right}",
                result=str(result),
                operation=operation,
                is_numeric=isinstance(result, (int, float)),
                explanation=explanation
            )
            
            return result
            
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            error_msg = f"Error in {node.operator} operation: {str(e)}"
            self.context.add_step(
                expression=f"{left} {node.operator} {right}",
                result=error_msg,
                operation="error",
                is_numeric=False,
                explanation=error_msg
            )
            return error_msg
    
    def _evaluate_function(self, node: FunctionNode) -> Union[float, str]:
        # Evaluate the argument
        arg_value = self._evaluate_node(node.argument)
        
        # Handle symbolic arguments
        if isinstance(arg_value, str):
            result = f"{node.function_name}({arg_value})"
            self.context.add_step(
                expression=f"{node.function_name}({arg_value})",
                result=result,
                operation="symbolic_function",
                is_numeric=False,
                explanation=f"Symbolic function: {node.function_name}({arg_value})"
            )
            return result
        
        # Handle numeric arguments
        try:
            if node.function_name == "sqrt":
                if arg_value < 0:
                    error_msg = f"Error: Cannot take square root of negative number {arg_value}"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.sqrt(arg_value)
                operation = "sqrt"
                explanation = f"Square root of {arg_value}"
            elif node.function_name == "sin":
                result = math.sin(arg_value)
                operation = "sin"
                explanation = f"Sine of {arg_value}"
            elif node.function_name == "cos":
                result = math.cos(arg_value)
                operation = "cos"
                explanation = f"Cosine of {arg_value}"
            elif node.function_name == "tan":
                # Check for undefined values (π/2 + kπ)
                if abs(math.cos(arg_value)) < 1e-10:
                    error_msg = f"Error: Tangent is undefined at {arg_value} (cos({arg_value}) = 0)"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.tan(arg_value)
                operation = "tan"
                explanation = f"Tangent of {arg_value}"
            elif node.function_name == "log":
                if arg_value <= 0:
                    error_msg = f"Error: Cannot take logarithm of non-positive number {arg_value}"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.log10(arg_value)
                operation = "log"
                explanation = f"Log base 10 of {arg_value}"
            elif node.function_name == "ln":
                if arg_value <= 0:
                    error_msg = f"Error: Cannot take natural logarithm of non-positive number {arg_value}"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.log(arg_value)
                operation = "ln"
                explanation = f"Natural logarithm of {arg_value}"
            elif node.function_name == "abs":
                result = abs(arg_value)
                operation = "abs"
                explanation = f"Absolute value of {arg_value}"
            elif node.function_name == "exp":
                try:
                    result = math.exp(arg_value)
                    if math.isinf(result):
                        error_msg = f"Error: Exponential overflow for {arg_value}"
                        self.context.add_step(
                            expression=f"{node.function_name}({arg_value})",
                            result=error_msg,
                            operation="error",
                            is_numeric=False,
                            explanation=error_msg
                        )
                        return error_msg
                except OverflowError:
                    error_msg = f"Error: Exponential overflow for {arg_value}"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                operation = "exp"
                explanation = f"Exponential of {arg_value}"
            elif node.function_name == "factorial":
                if arg_value < 0 or arg_value != int(arg_value):
                    error_msg = f"Error: Cannot take factorial of {arg_value} (must be non-negative integer)"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                if arg_value > 170:  # Python's limit for factorial
                    error_msg = f"Error: Factorial overflow for {arg_value} (max: 170)"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.factorial(int(arg_value))
                operation = "factorial"
                explanation = f"Factorial of {int(arg_value)}"
            elif node.function_name == "asin":
                if arg_value < -1 or arg_value > 1:
                    error_msg = f"Error: Arcsin domain error: {arg_value} not in [-1, 1]"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.asin(arg_value)
                operation = "asin"
                explanation = f"Arcsin of {arg_value}"
            elif node.function_name == "acos":
                if arg_value < -1 or arg_value > 1:
                    error_msg = f"Error: Arccos domain error: {arg_value} not in [-1, 1]"
                    self.context.add_step(
                        expression=f"{node.function_name}({arg_value})",
                        result=error_msg,
                        operation="error",
                        is_numeric=False,
                        explanation=error_msg
                    )
                    return error_msg
                result = math.acos(arg_value)
                operation = "acos"
                explanation = f"Arccos of {arg_value}"
            elif node.function_name == "atan":
                result = math.atan(arg_value)
                operation = "atan"
                explanation = f"Arctan of {arg_value}"
            elif node.function_name == "sinh":
                result = math.sinh(arg_value)
                operation = "sinh"
                explanation = f"Hyperbolic sine of {arg_value}"
            elif node.function_name == "cosh":
                result = math.cosh(arg_value)
                operation = "cosh"
                explanation = f"Hyperbolic cosine of {arg_value}"
            elif node.function_name == "tanh":
                result = math.tanh(arg_value)
                operation = "tanh"
                explanation = f"Hyperbolic tangent of {arg_value}"
            elif node.function_name == "cbrt":
                result = arg_value ** (1/3)
                operation = "cbrt"
                explanation = f"Cube root of {arg_value}"
            elif node.function_name == "floor":
                result = math.floor(arg_value)
                operation = "floor"
                explanation = f"Floor of {arg_value}"
            elif node.function_name == "ceil":
                result = math.ceil(arg_value)
                operation = "ceil"
                explanation = f"Ceiling of {arg_value}"
            elif node.function_name == "round":
                result = round(arg_value)
                operation = "round"
                explanation = f"Round of {arg_value}"
            else:
                error_msg = f"Error: Unknown function '{node.function_name}'"
                self.context.add_step(
                    expression=f"{node.function_name}({arg_value})",
                    result=error_msg,
                    operation="error",
                    is_numeric=False,
                    explanation=error_msg
                )
                return error_msg
            
            self.context.add_step(
                expression=f"{node.function_name}({arg_value})",
                result=str(result),
                operation=operation,
                is_numeric=isinstance(result, (int, float)),
                explanation=explanation
            )
            
            return result
            
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            error_msg = f"Error in {node.function_name} function: {str(e)}"
            self.context.add_step(
                expression=f"{node.function_name}({arg_value})",
                result=error_msg,
                operation="error",
                is_numeric=False,
                explanation=error_msg
            )
            return error_msg
    
    def _evaluate_parentheses(self, node: ParenthesesNode) -> Union[float, str]:
        result = self._evaluate_node(node.expression)
        self.context.add_step(
            expression=f"({node.expression.to_string()})",
            result=str(result),
            operation="parentheses",
            is_numeric=isinstance(result, (int, float)),
            explanation=f"Evaluated expression in parentheses: {node.expression.to_string()}"
        )
        return result
    
    def _evaluate_unary(self, node: UnaryNode) -> Union[float, str]:
        operand_value = self._evaluate_node(node.operand)
        
        if isinstance(operand_value, str):
            result = f"{node.operator}{operand_value}"
            self.context.add_step(
                expression=f"{node.operator}{operand_value}",
                result=result,
                operation="unary_symbolic",
                is_numeric=False,
                explanation=f"Symbolic unary operation: {node.operator}{operand_value}"
            )
            return result
        
        try:
            if node.operator == "-":
                result = -operand_value
                operation = "negation"
                explanation = f"Negated {operand_value}"
            elif node.operator == "+":
                result = operand_value
                operation = "positive"
                explanation = f"Positive {operand_value}"
            else:
                raise ValueError(f"Unknown unary operator: {node.operator}")
            
            self.context.add_step(
                expression=f"{node.operator}{operand_value}",
                result=str(result),
                operation=operation,
                is_numeric=True,
                explanation=explanation
            )
            
            return result
            
        except (ValueError, OverflowError) as e:
            error_msg = f"Error in unary operation: {str(e)}"
            self.context.add_step(
                expression=f"{node.operator}{operand_value}",
                result=error_msg,
                operation="error",
                is_numeric=False,
                explanation=error_msg
            )
            return error_msg
    
    def _evaluate_derivative(self, node: DerivativeNode) -> Union[float, str]:
        result = node.evaluate(self.context.variables)
        self.context.add_step(
            expression=f"d/d{node.variable}({node.expression.to_string()})",
            result=str(result),
            operation="derivative",
            is_numeric=isinstance(result, (int, float)),
            explanation=f"Derivative with respect to {node.variable}"
        )
        return result
    
    def _evaluate_integral(self, node: IntegralNode) -> Union[float, str]:
        result = node.evaluate(self.context.variables)
        self.context.add_step(
            expression=node.to_string(),
            result=str(result),
            operation="integral",
            is_numeric=isinstance(result, (int, float)),
            explanation=f"Integral with respect to {node.variable}"
        )
        return result
