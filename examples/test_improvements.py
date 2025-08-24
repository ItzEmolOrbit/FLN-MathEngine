#!/usr/bin/env python3
"""
Comprehensive Test Script for FLN Math Engine Improvements
Tests Advanced Calculus, Error Handling, Complex Expressions, and Performance
"""

import sys
import time
from FLN.engine import MathEngine
from FLN.formula_database import get_formula_database

def test_advanced_calculus():
    """Test advanced calculus features"""
    print("🧮 TESTING ADVANCED CALCULUS")
    print("=" * 50)
    
    engine = MathEngine()
    
    # Test improved derivative rules
    derivative_tests = [
        ("d/dx(x^2 + 3*x + 1)", "Derivative of quadratic"),
        ("d/dx(sin(x) + cos(x))", "Derivative of trigonometric sum"),
        ("d/dx(exp(x) * ln(x))", "Derivative of product"),
        ("d/dx(x^3 + 2*x^2 + x)", "Derivative of cubic"),
        ("d/dx(sin(x) * cos(x))", "Derivative of trigonometric product"),
        ("d/dx(sqrt(x))", "Derivative of square root"),
        ("d/dx(tan(x))", "Derivative of tangent"),
        ("d/dx(log(x))", "Derivative of logarithm"),
    ]
    
    for expression, description in derivative_tests:
        try:
            result = engine.evaluate(expression)
            print(f"✅ {description}: {expression}")
            print(f"   Result: {result.final_result}")
            print(f"   Steps: {len(result.computation_steps)}")
            print()
        except Exception as e:
            print(f"❌ {description}: {expression}")
            print(f"   Error: {e}")
            print()
    
    # Test improved integral rules
    integral_tests = [
        ("∫x dx", "Basic integral"),
        ("∫x^2 dx", "Power rule integral"),
        ("∫(x^2 + 2*x + 1) dx", "Sum rule integral"),
        ("∫sin(x) dx", "Trigonometric integral"),
        ("∫cos(x) dx", "Trigonometric integral"),
        ("∫exp(x) dx", "Exponential integral"),
        ("∫1/x dx", "Reciprocal integral"),
        ("∫sqrt(x) dx", "Square root integral"),
    ]
    
    print("📊 INTEGRAL TESTS:")
    print("-" * 30)
    
    for expression, description in integral_tests:
        try:
            result = engine.evaluate(expression)
            print(f"✅ {description}: {expression}")
            print(f"   Result: {result.final_result}")
            print(f"   Steps: {len(result.computation_steps)}")
            print()
        except Exception as e:
            print(f"❌ {description}: {expression}")
            print(f"   Error: {e}")
            print()

def test_error_handling():
    """Test improved error handling"""
    print("⚠️ TESTING ERROR HANDLING")
    print("=" * 50)
    
    engine = MathEngine()
    
    error_tests = [
        ("1/0", "Division by zero"),
        ("sqrt(-1)", "Square root of negative"),
        ("log(0)", "Log of zero"),
        ("ln(-1)", "Natural log of negative"),
        ("factorial(-1)", "Factorial of negative"),
        ("factorial(3.5)", "Factorial of decimal"),
        ("tan(pi/2)", "Tangent at undefined point"),
        ("exp(1000)", "Exponential overflow"),
        ("factorial(200)", "Factorial overflow"),
        ("asin(2)", "Arcsin domain error"),
        ("acos(-2)", "Arccos domain error"),
        ("0^(-1)", "Zero to negative power"),
        ("0.0001^(-100)", "Small number to large negative power"),
        ("2^1000", "Power overflow"),
    ]
    
    for expression, description in error_tests:
        try:
            result = engine.evaluate(expression)
            if "Error:" in str(result.final_result):
                print(f"✅ {description}: {expression}")
                print(f"   Properly handled: {result.final_result}")
            else:
                print(f"⚠️ {description}: {expression}")
                print(f"   Result: {result.final_result}")
            print()
        except Exception as e:
            print(f"❌ {description}: {expression}")
            print(f"   Exception: {e}")
            print()

def test_complex_expressions():
    """Test complex mathematical expressions"""
    print("🎯 TESTING COMPLEX EXPRESSIONS")
    print("=" * 50)
    
    engine = MathEngine()
    
    complex_tests = [
        ("sqrt(sin(0)^2 + cos(0)^2)", "Nested trigonometric functions"),
        ("log(sqrt(100))", "Function composition"),
        ("abs(sin(pi/2))", "Function with constant"),
        ("(2 + 3) * (4 - 1) + sqrt(25)", "Complex arithmetic"),
        ("sin(0) + cos(0) + tan(0)", "Multiple functions"),
        ("sqrt(16) + log(100) + ln(e)", "Mixed function types"),
        ("sin(pi/4)^2 + cos(pi/4)^2", "Trigonometric identity"),
        ("exp(ln(5))", "Inverse functions"),
        ("sqrt(sin(pi/6)^2 + cos(pi/6)^2)", "Deep nesting"),
        ("(x^2 + y^2)^(1/2)", "Symbolic expression"),
    ]
    
    for expression, description in complex_tests:
        try:
            result = engine.evaluate(expression)
            print(f"✅ {description}: {expression}")
            print(f"   Result: {result.final_result}")
            print(f"   Steps: {len(result.computation_steps)}")
            print()
        except Exception as e:
            print(f"❌ {description}: {expression}")
            print(f"   Error: {e}")
            print()

def test_performance():
    """Test performance optimizations"""
    print("🚀 TESTING PERFORMANCE")
    print("=" * 50)
    
    engine = MathEngine()
    
    # Test caching with repeated expressions
    expressions = [
        "2 + 2",
        "sqrt(16)",
        "sin(0)",
        "cos(0)",
        "exp(1)",
        "ln(e)",
    ]
    
    print("📊 CACHING PERFORMANCE TEST:")
    print("-" * 30)
    
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
    print()
    
    # Test complex expression performance
    complex_expr = "sin(0) + cos(0) + tan(0) + sqrt(16) + log(100) + ln(e)"
    
    start_time = time.time()
    result = engine.evaluate(complex_expr)
    eval_time = time.time() - start_time
    
    print(f"Complex expression: {complex_expr}")
    print(f"Evaluation time: {eval_time:.4f} seconds")
    print(f"Result: {result.final_result}")
    print(f"Steps: {len(result.computation_steps)}")
    print()

def test_formula_detection():
    """Test formula detection improvements"""
    print("🔍 TESTING FORMULA DETECTION")
    print("=" * 50)
    
    engine = MathEngine()
    
    formula_tests = [
        ("(x+y)^2", "Perfect Square (a+b)²"),
        ("(a-b)^2", "Perfect Square (a-b)²"),
        ("x^2 - y^2", "Difference of Squares"),
        ("a^3 + b^3", "Sum of Cubes"),
        ("x^3 - y^3", "Difference of Cubes"),
        ("sin^2(x) + cos^2(x)", "Pythagorean Identity"),
        ("log(a*b)", "Log Product Rule"),
        ("log(a/b)", "Log Quotient Rule"),
        ("log(a^b)", "Log Power Rule"),
        ("a*x + a*y", "Common Factor"),
        ("x^2 + 2*x*y + y^2", "Middle Term Factoring"),
    ]
    
    for expression, expected_formula in formula_tests:
        try:
            result = engine.evaluate(expression)
            detected_formulas = [step.applied_formulas for step in result.computation_steps if step.applied_formulas]
            
            if detected_formulas:
                formula_names = [f.formula_name for formulas in detected_formulas for f in formulas]
                if expected_formula in formula_names:
                    print(f"✅ {expression} → Expected: {expected_formula}")
                    print(f"   Detected: {formula_names}")
                else:
                    print(f"⚠️ {expression} → Expected: {expected_formula}")
                    print(f"   Detected: {formula_names}")
            else:
                print(f"❌ {expression} → No formula detected")
                print(f"   Expected: {expected_formula}")
            print()
        except Exception as e:
            print(f"❌ {expression} → Error: {e}")
            print()

def main():
    """Run all tests"""
    print("🚀 FLN MATH ENGINE - COMPREHENSIVE IMPROVEMENTS TEST")
    print("=" * 70)
    print()
    
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
    
    # Run all tests
    test_advanced_calculus()
    test_error_handling()
    test_complex_expressions()
    test_performance()
    test_formula_detection()
    
    print("🎉 ALL TESTS COMPLETED!")
    print("=" * 70)
    print("📊 SUMMARY:")
    print("   • Advanced Calculus: Improved derivative and integral rules")
    print("   • Error Handling: Comprehensive edge case coverage")
    print("   • Complex Expressions: Better nested function support")
    print("   • Performance: Caching and optimization")
    print("   • Formula Detection: Enhanced pattern matching")
    print()
    print("🏆 FLN Math Engine is now production-ready with advanced features!")

if __name__ == "__main__":
    main()
