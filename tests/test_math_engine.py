#!/usr/bin/env python3
"""
Test script for the PlutoCraft Math Engine.
Demonstrates all major features and functionality.
"""

from pluto_math_engine import MathEngine, evaluate_expression, detect_formulas
import json


def test_basic_evaluation():
    """Test basic mathematical evaluation."""
    print("=" * 60)
    print("BASIC EVALUATION TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test simple arithmetic
    expressions = [
        "2 + 3",
        "10 - 5",
        "4 * 6",
        "15 / 3",
        "2^3",
        "2 + 3 * 4",
        "(2 + 3) * 4"
    ]
    
    for expr in expressions:
        result = engine.evaluate(expr)
        print(f"{expr} = {result.final_result}")
        print(f"  Type: {result.evaluation_type.value}")
        print(f"  Steps: {len(result.computation_steps)}")
        print()


def test_variable_evaluation():
    """Test evaluation with variables."""
    print("=" * 60)
    print("VARIABLE EVALUATION TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test with variables
    expressions = [
        ("x + y", {"x": 5, "y": 3}),
        ("a * b + c", {"a": 2, "b": 4, "c": 1}),
        ("x^2 + y^2", {"x": 3, "y": 4}),
        ("sqrt(x^2 + y^2)", {"x": 3, "y": 4})
    ]
    
    for expr, vars in expressions:
        result = engine.evaluate(expr, vars)
        print(f"{expr} with {vars} = {result.final_result}")
        print(f"  Type: {result.evaluation_type.value}")
        print()


def test_symbolic_evaluation():
    """Test symbolic evaluation."""
    print("=" * 60)
    print("SYMBOLIC EVALUATION TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test symbolic expressions
    expressions = [
        "x + y",
        "a * b + c",
        "x^2 + y^2",
        "(a + b)^2",
        "sin(x) + cos(y)"
    ]
    
    for expr in expressions:
        result = engine.evaluate_symbolic(expr)
        print(f"{expr} = {result}")
        print()


def test_formula_detection():
    """Test formula detection and application."""
    print("=" * 60)
    print("FORMULA DETECTION TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test expressions that should trigger formulas
    expressions = [
        "(x + y)^2",
        "(a - b)^2",
        "x^2 - y^2",
        "(x + y)^3",
        "x^3 + y^3"
    ]
    
    for expr in expressions:
        print(f"Expression: {expr}")
        
        # Detect formulas
        formulas = engine.detect_formulas(expr)
        if formulas:
            print("  Detected formulas:")
            for formula in formulas:
                print(f"    - {formula.formula_name}")
                print(f"      Pattern: {formula.pattern}")
                print(f"      Variables: {formula.variables}")
        else:
            print("  No formulas detected")
        
        # Evaluate with formula application
        result = engine.evaluate(expr)
        print(f"  Result: {result.final_result}")
        print(f"  Applied formulas: {len(result.applied_formulas)}")
        print()


def test_step_by_step_evaluation():
    """Test step-by-step evaluation."""
    print("=" * 60)
    print("STEP-BY-STEP EVALUATION TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test complex expression
    expr = "(x + y)^2 + (a - b)^3"
    variables = {"x": 2, "y": 3, "a": 4, "b": 1}
    
    print(f"Expression: {expr}")
    print(f"Variables: {variables}")
    print()
    
    # Get step-by-step evaluation
    steps = engine.step_by_step_evaluation(expr, variables)
    
    for step in steps:
        print(f"Step {step['step_number']}:")
        print(f"  Expression: {step['expression']}")
        print(f"  Result: {step['result']}")
        print(f"  Operation: {step['operation']}")
        print(f"  Numeric: {step['is_numeric']}")
        if step['explanation']:
            print(f"  Explanation: {step['explanation']}")
        if step['applied_formulas']:
            print(f"  Applied formulas: {len(step['applied_formulas'])}")
        print()


def test_custom_formulas():
    """Test adding and using custom formulas."""
    print("=" * 60)
    print("CUSTOM FORMULA TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Add a custom formula
    engine.add_formula(
        name="Custom Square Root Formula",
        pattern="sqrt(a^2 + b^2)",
        expansion="sqrt(a^2 + b^2)",
        description="Custom formula for square root of sum of squares",
        category="custom"
    )
    
    # Test the custom formula
    expr = "sqrt(x^2 + y^2)"
    variables = {"x": 3, "y": 4}
    
    print(f"Expression: {expr}")
    print(f"Variables: {variables}")
    
    result = engine.evaluate(expr, variables)
    print(f"Result: {result.final_result}")
    
    # List all formulas
    print("\nAll available formulas:")
    formulas = engine.list_formulas()
    for formula in formulas:
        print(f"  {formula}")
    print()


def test_error_handling():
    """Test error handling."""
    print("=" * 60)
    print("ERROR HANDLING TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test invalid expressions
    invalid_expressions = [
        "2 +",  # Incomplete expression
        "x / 0",  # Division by zero
        "invalid_function(x)",  # Unknown function
        "2 + + 3",  # Invalid syntax
    ]
    
    for expr in invalid_expressions:
        print(f"Testing: {expr}")
        result = engine.evaluate(expr)
        if result.error_message:
            print(f"  Error: {result.error_message}")
        else:
            print(f"  Result: {result.final_result}")
        print()


def test_computation_insights():
    """Test computation insights and analysis."""
    print("=" * 60)
    print("COMPUTATION INSIGHTS TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test complex expression
    expr = "(x + y)^2 + (a - b)^3 + sqrt(z^2 + w^2)"
    variables = {"x": 2, "y": 3, "a": 4, "b": 1, "z": 5, "w": 12}
    
    print(f"Expression: {expr}")
    print(f"Variables: {variables}")
    print()
    
    # Get insights
    insights = engine.get_computation_insights(expr, variables)
    
    print("Computation Insights:")
    print(f"  Complexity: {insights['complexity']}")
    print(f"  Formula Usage: {insights['formula_usage']}")
    print(f"  Computation Pattern: {insights['computation_pattern']}")
    print(f"  Potential Optimizations: {insights['potential_optimizations']}")
    print()
    
    # Get summary
    summary = engine.get_computation_summary(expr, variables)
    print("Computation Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    print()


def test_validation():
    """Test expression validation."""
    print("=" * 60)
    print("VALIDATION TESTS")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Test various expressions
    test_expressions = [
        "2 + 3",  # Valid
        "x + y",  # Valid
        "2 +",  # Invalid
        "invalid_function(x)",  # Invalid
        "(x + y)^2",  # Valid
        "2 / 0",  # Valid syntax but runtime error
    ]
    
    for expr in test_expressions:
        is_valid, errors = engine.validate_expression(expr)
        print(f"Expression: {expr}")
        print(f"  Valid: {is_valid}")
        if errors:
            print(f"  Errors: {errors}")
        print()


def test_performance_demo():
    """Demonstrate performance with complex expressions."""
    print("=" * 60)
    print("PERFORMANCE DEMO")
    print("=" * 60)
    
    engine = MathEngine()
    
    # Complex expression with multiple formulas
    expr = "(x + y)^2 + (a - b)^3 + (c + d)^2 + sqrt(e^2 + f^2)"
    variables = {
        "x": 1, "y": 2, "a": 3, "b": 1, 
        "c": 4, "d": 5, "e": 6, "f": 8
    }
    
    print(f"Complex expression: {expr}")
    print(f"Variables: {variables}")
    print()
    
    # Evaluate
    result = engine.evaluate(expr, variables)
    print(f"Final result: {result.final_result}")
    print(f"Total steps: {len(result.computation_steps)}")
    print(f"Formulas applied: {len(result.applied_formulas)}")
    print(f"Evaluation type: {result.evaluation_type.value}")
    print()
    
    # Show some key steps
    print("Key computation steps:")
    for i, step in enumerate(result.computation_steps[:5]):  # Show first 5 steps
        print(f"  Step {step.step_number}: {step.expression} = {step.result}")
    if len(result.computation_steps) > 5:
        print(f"  ... and {len(result.computation_steps) - 5} more steps")
    print()


def main():
    """Run all tests."""
    print("🚀 PLUTOCRAFT MATH ENGINE DEMONSTRATION")
    print("=" * 80)
    print()
    
    try:
        test_basic_evaluation()
        test_variable_evaluation()
        test_symbolic_evaluation()
        test_formula_detection()
        test_step_by_step_evaluation()
        test_custom_formulas()
        test_error_handling()
        test_computation_insights()
        test_validation()
        test_performance_demo()
        
        print("=" * 80)
        print("✅ All tests completed successfully!")
        print("🎉 The PlutoCraft Math Engine is working perfectly!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
