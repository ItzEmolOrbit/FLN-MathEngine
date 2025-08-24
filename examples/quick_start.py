#!/usr/bin/env python3
"""
🚀 FLN MATH ENGINE - QUICK START GUIDE
Simple examples to get you started immediately
"""

from FLN.engine import MathEngine

def quick_examples():
    """Quick examples to get started"""
    print("🚀 FLN MATH ENGINE - QUICK START")
    print("=" * 50)
    
    # Create engine
    engine = MathEngine()
    
    # Basic operations
    print("\n📊 BASIC OPERATIONS:")
    print(f"2 + 3 = {engine.evaluate('2 + 3').final_result}")
    print(f"sqrt(16) = {engine.evaluate('sqrt(16)').final_result}")
    print(f"factorial(5) = {engine.evaluate('factorial(5)').final_result}")
    
    # Trigonometry
    print("\n📊 TRIGONOMETRY:")
    print(f"sin(0) = {engine.evaluate('sin(0)').final_result}")
    print(f"cos(0) = {engine.evaluate('cos(0)').final_result}")
    print(f"tan(0) = {engine.evaluate('tan(0)').final_result}")
    
    # Calculus
    print("\n📊 CALCULUS:")
    print(f"d/dx(x^2) = {engine.evaluate('d/dx(x^2)').final_result}")
    print(f"∫x dx = {engine.evaluate('∫x dx').final_result}")
    
    # Complex expressions
    print("\n📊 COMPLEX EXPRESSIONS:")
    complex_expr = "sqrt(sin(0)^2 + cos(0)^2)"
    result = engine.evaluate(complex_expr)
    print(f"{complex_expr} = {result.final_result}")
    print(f"Steps: {len(result.computation_steps)}")
    
    # Error handling
    print("\n📊 ERROR HANDLING:")
    try:
        result = engine.evaluate("1/0")
        print(f"1/0 = {result.final_result}")
    except:
        print("Error caught properly")
    
    # Formula detection
    print("\n📊 FORMULA DETECTION:")
    detected = engine.detect_formulas("(x+y)^2")
    if detected:
        print(f"(x+y)^2 → {[f.formula_name for f in detected]}")
    
    print("\n✅ Quick start completed! Run 'python example.py' for comprehensive examples.")

if __name__ == "__main__":
    quick_examples()
