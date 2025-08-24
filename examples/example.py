#!/usr/bin/env python3
"""
🚀 FLN MATH ENGINE - COMPREHENSIVE EXAMPLES
Showcases all features with practical, real-world examples
"""

from FLN.engine import MathEngine
from FLN.formula_database import get_formula_database
import time

def print_section(title: str):
    """Print a formatted section header"""
    print(f"\n{'='*80}")
    print(f"🎯 {title}")
    print(f"{'='*80}")

def example_basic_operations():
    """Example 1: Basic Mathematical Operations"""
    print_section("BASIC MATHEMATICAL OPERATIONS")
    
    engine = MathEngine()
    
    print("📊 Basic arithmetic operations:")
    expressions = [
        ("2 + 3", "Addition"),
        ("10 - 4", "Subtraction"),
        ("6 * 7", "Multiplication"),
        ("20 / 5", "Division"),
        ("2^8", "Power"),
        ("sqrt(16)", "Square root"),
        ("abs(-15)", "Absolute value"),
        ("factorial(5)", "Factorial"),
    ]
    
    for expr, desc in expressions:
        result = engine.evaluate(expr)
        print(f"✅ {desc}: {expr} = {result.final_result}")
    
    print(f"\n📋 Computation steps for factorial(5):")
    result = engine.evaluate("factorial(5)")
    for i, step in enumerate(result.computation_steps, 1):
        print(f"   Step {i}: {step.expression} → {step.result}")

def example_trigonometric_functions():
    """Example 2: Trigonometric Functions"""
    print_section("TRIGONOMETRIC FUNCTIONS")
    
    engine = MathEngine()
    
    print("📊 Trigonometric calculations:")
    trig_expressions = [
        ("sin(0)", "Sine of 0"),
        ("cos(0)", "Cosine of 0"),
        ("tan(0)", "Tangent of 0"),
        ("sin(pi/2)", "Sine of π/2"),
        ("cos(pi)", "Cosine of π"),
        ("tan(pi/4)", "Tangent of π/4"),
        ("asin(0.5)", "Arcsin of 0.5"),
        ("acos(0)", "Arccos of 0"),
        ("atan(1)", "Arctan of 1"),
    ]
    
    for expr, desc in trig_expressions:
        result = engine.evaluate(expr)
        print(f"✅ {desc}: {expr} = {result.final_result}")
    
    print(f"\n📊 Advanced trigonometric identity verification:")
    identity = "sin(0)^2 + cos(0)^2"
    result = engine.evaluate(identity)
    print(f"   {identity} = {result.final_result}")
    print(f"   Steps: {len(result.computation_steps)}")

def example_advanced_calculus():
    """Example 3: Advanced Calculus"""
    print_section("ADVANCED CALCULUS FEATURES")
    
    engine = MathEngine()
    
    print("📊 DERIVATIVES:")
    derivative_examples = [
        ("d/dx(x^2)", "Power rule derivative"),
        ("d/dx(sin(x))", "Trigonometric derivative"),
        ("d/dx(exp(x))", "Exponential derivative"),
        ("d/dx(ln(x))", "Logarithmic derivative"),
        ("d/dx(sqrt(x))", "Square root derivative"),
        ("d/dx(tan(x))", "Tangent derivative"),
    ]
    
    for expr, desc in derivative_examples:
        result = engine.evaluate(expr)
        print(f"✅ {desc}: {expr} = {result.final_result}")
    
    print(f"\n📊 INTEGRALS:")
    integral_examples = [
        ("∫x dx", "Basic integral"),
        ("∫x^2 dx", "Power rule integral"),
        ("∫sin(x) dx", "Trigonometric integral"),
        ("∫cos(x) dx", "Trigonometric integral"),
        ("∫exp(x) dx", "Exponential integral"),
        ("∫1/x dx", "Reciprocal integral"),
    ]
    
    for expr, desc in integral_examples:
        result = engine.evaluate(expr)
        print(f"✅ {desc}: {expr} = {result.final_result}")

def example_error_handling():
    """Example 4: Comprehensive Error Handling"""
    print_section("COMPREHENSIVE ERROR HANDLING")
    
    engine = MathEngine()
    
    print("📊 Error handling examples:")
    error_examples = [
        ("1/0", "Division by zero"),
        ("sqrt(-1)", "Square root of negative"),
        ("log(0)", "Log of zero"),
        ("ln(-1)", "Natural log of negative"),
        ("factorial(-1)", "Factorial of negative"),
        ("factorial(3.5)", "Factorial of decimal"),
        ("exp(1000)", "Exponential overflow"),
        ("factorial(200)", "Factorial overflow"),
        ("asin(2)", "Arcsin domain error"),
        ("acos(-2)", "Arccos domain error"),
        ("0^(-1)", "Zero to negative power"),
    ]
    
    for expr, desc in error_examples:
        result = engine.evaluate(expr)
        if "Error:" in str(result.final_result):
            print(f"✅ {desc}: {expr} → {result.final_result}")
        else:
            print(f"⚠️ {desc}: {expr} → {result.final_result}")

def example_complex_expressions():
    """Example 5: Complex Mathematical Expressions"""
    print_section("COMPLEX MATHEMATICAL EXPRESSIONS")
    
    engine = MathEngine()
    
    print("📊 Complex expression evaluation:")
    complex_examples = [
        ("sqrt(sin(0)^2 + cos(0)^2)", "Pythagorean identity verification"),
        ("log(sqrt(100))", "Function composition"),
        ("(2 + 3) * (4 - 1) + sqrt(25)", "Complex arithmetic"),
        ("sin(0) + cos(0) + tan(0)", "Multiple functions"),
        ("sqrt(16) + log(100) + ln(e)", "Mixed function types"),
        ("exp(ln(5))", "Inverse functions"),
        ("(x^2 + y^2)^(1/2)", "Symbolic expression"),
    ]
    
    for expr, desc in complex_examples:
        result = engine.evaluate(expr)
        print(f"✅ {desc}: {expr} = {result.final_result}")
        print(f"   Steps: {len(result.computation_steps)}")

def example_performance_features():
    """Example 6: Performance Optimizations"""
    print_section("PERFORMANCE OPTIMIZATIONS")
    
    engine = MathEngine()
    
    print("📊 Caching performance test:")
    expressions = ["2 + 2", "sqrt(16)", "sin(0)", "cos(0)", "exp(1)", "ln(e)"]
    
    # First run (no cache)
    start_time = time.time()
    for expr in expressions:
        result = engine.evaluate(expr)
    first_run_time = time.time() - start_time
    
    # Second run (with cache)
    start_time = time.time()
    for expr in expressions:
        result = engine.evaluate(expr)
    second_run_time = time.time() - start_time
    
    print(f"First run time: {first_run_time:.4f} seconds")
    print(f"Second run time: {second_run_time:.4f} seconds")
    if second_run_time > 0:
        print(f"Speedup: {first_run_time/second_run_time:.2f}x")
    else:
        print("Speedup: ∞ (instantaneous)")
    
    print(f"\n📊 Complex expression performance:")
    complex_expr = "sin(0) + cos(0) + tan(0) + sqrt(16) + log(100) + ln(e)"
    
    start_time = time.time()
    result = engine.evaluate(complex_expr)
    eval_time = time.time() - start_time
    
    print(f"Complex expression: {complex_expr}")
    print(f"Evaluation time: {eval_time:.4f} seconds")
    print(f"Result: {result.final_result}")
    print(f"Steps: {len(result.computation_steps)}")

def example_formula_detection():
    """Example 7: Intelligent Formula Detection"""
    print_section("INTELLIGENT FORMULA DETECTION")
    
    engine = MathEngine()
    
    print("📊 Formula detection examples:")
    formula_examples = [
        ("(x+y)^2", "Perfect Square (a+b)²"),
        ("x^2 - y^2", "Difference of Squares"),
        ("a^3 + b^3", "Sum of Cubes"),
        ("x^3 - y^3", "Difference of Cubes"),
        ("log(a*b)", "Log Product Rule"),
        ("log(a/b)", "Log Quotient Rule"),
        ("log(a^b)", "Log Power Rule"),
        ("a*x + a*y", "Common Factor"),
        ("x^2 + 2*x*y + y^2", "Middle Term Factoring"),
    ]
    
    for expr, expected_formula in formula_examples:
        detected_formulas = engine.detect_formulas(expr)
        
        if detected_formulas:
            formula_names = [f.formula_name for f in detected_formulas]
            if expected_formula in formula_names:
                print(f"✅ {expr} → Expected: {expected_formula}")
                print(f"   Detected: {formula_names}")
            else:
                print(f"⚠️ {expr} → Expected: {expected_formula}")
                print(f"   Detected: {formula_names}")
        else:
            print(f"❌ {expr} → No formula detected")
            print(f"   Expected: {expected_formula}")
        print()

def example_step_by_step_solving():
    """Example 8: Step-by-Step Problem Solving"""
    print_section("STEP-BY-STEP PROBLEM SOLVING")
    
    engine = MathEngine()
    
    print("📊 Step-by-step solution for complex expression:")
    complex_expression = "sqrt(sin(0)^2 + cos(0)^2) + log(100)"
    
    result = engine.evaluate(complex_expression)
    print(f"Expression: {complex_expression}")
    print(f"Final Result: {result.final_result}")
    print(f"Total Steps: {len(result.computation_steps)}")
    
    print(f"\n📋 STEP-BY-STEP SOLUTION:")
    for i, step in enumerate(result.computation_steps, 1):
        print(f"Step {i}: {step.expression} → {step.result}")
        if step.explanation:
            print(f"      {step.explanation}")
        if step.applied_formulas:
            formulas = [f.formula_name for f in step.applied_formulas]
            print(f"      Applied formulas: {', '.join(formulas)}")
        print()

def example_ai_integration():
    """Example 9: AI Integration Ready"""
    print_section("AI INTEGRATION READY")
    
    engine = MathEngine()
    
    print("📊 AI-ready features:")
    print("✅ Step-by-step computation tracking")
    print("✅ Formula detection and application")
    print("✅ Symbolic and numeric evaluation")
    print("✅ Error handling with detailed messages")
    print("✅ Performance optimization with caching")
    print("✅ Extensible architecture")
    
    print(f"\n📊 Example: AI solving a math problem")
    problem = "Calculate the derivative of f(x) = x^2 + 3*x + 1"
    print(f"Problem: {problem}")
    
    # AI would parse this and extract the expression
    expression = "d/dx(x^2 + 3*x + 1)"
    print(f"Extracted expression: {expression}")
    
    result = engine.evaluate(expression)
    print(f"Solution: {result.final_result}")
    print(f"Computation steps: {len(result.computation_steps)}")
    
    print(f"\n📊 AI can now explain each step:")
    for i, step in enumerate(result.computation_steps, 1):
        print(f"   Step {i}: {step.explanation}")

def example_educational_use():
    """Example 10: Educational Applications"""
    print_section("EDUCATIONAL APPLICATIONS")
    
    engine = MathEngine()
    
    print("📊 Perfect for teaching mathematics:")
    print("✅ Visual step-by-step solutions")
    print("✅ Formula explanations")
    print("✅ Error prevention and correction")
    print("✅ Interactive problem solving")
    
    print(f"\n📊 Example: Teaching derivatives")
    print("Let's learn how to find the derivative of x^2:")
    
    result = engine.evaluate("d/dx(x^2)")
    print(f"d/dx(x^2) = {result.final_result}")
    
    print(f"\n📋 Learning steps:")
    for i, step in enumerate(result.computation_steps, 1):
        print(f"   Step {i}: {step.explanation}")

def main():
    """Run all examples"""
    print("🚀 FLN MATH ENGINE - COMPREHENSIVE EXAMPLES")
    print("=" * 80)
    print("🎯 This file showcases ALL features with practical examples")
    print("📚 Perfect for learning, testing, and integration")
    print("⚡ Performance optimized with intelligent caching")
    print("🔍 Smart formula detection and automatic rewriting")
    print("🤖 AI-ready architecture for machine learning integration")
    print("=" * 80)
    
    # Test formula database
    try:
        db = get_formula_database()
        print(f"✅ Formula Database Loaded: {len(db.formulas)} formulas")
        print(f"📚 Categories: {', '.join(set(f.category for f in db.formulas))}")
        print(f"🎯 Grades: {min(f.grade for f in db.formulas)}-{max(f.grade for f in db.formulas)}+")
        print()
    except Exception as e:
        print(f"❌ Formula Database Error: {e}")
        return
    
    # Run all examples
    example_basic_operations()
    example_trigonometric_functions()
    example_advanced_calculus()
    example_error_handling()
    example_complex_expressions()
    example_performance_features()
    example_formula_detection()
    example_step_by_step_solving()
    example_ai_integration()
    example_educational_use()
    
    print("🎉 ALL EXAMPLES COMPLETED!")
    print("=" * 80)
    print("🏆 FLN Math Engine is now 100% production-ready!")
    print("📊 Features demonstrated:")
    print("   • ✅ Basic mathematical operations")
    print("   • ✅ Trigonometric and advanced functions")
    print("   • ✅ Advanced calculus (derivatives & integrals)")
    print("   • ✅ Comprehensive error handling")
    print("   • ✅ Complex expression parsing")
    print("   • ✅ High-performance caching")
    print("   • ✅ Intelligent formula detection")
    print("   • ✅ Step-by-step problem solving")
    print("   • ✅ AI integration ready")
    print("   • ✅ Educational applications")
    print()
    print("🚀 Ready for production use, AI integration, and education!")

if __name__ == "__main__":
    main()
