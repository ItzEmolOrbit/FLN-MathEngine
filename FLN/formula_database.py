#!/usr/bin/env python3
"""
Formula Database for FLN Math Engine
Contains 200+ important mathematical formulas with simple, working patterns
"""

from FLN.data_structures import FormulaDefinition

class FormulaDatabase:
    def __init__(self):
        self.formulas = []
        self._load_all_formulas()
    
    def _load_all_formulas(self):
        """Load all formulas into the database"""
        # ============================================================================
        # ALGEBRAIC IDENTITIES (Grade 6-10)
        # ============================================================================
        
        # Perfect Squares
        self.formulas.append(FormulaDefinition(
            "Perfect Square (a+b)²", 
            r"\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)\^2", 
            r"(\1)^2 + 2*(\1)*(\2) + (\2)^2", 
            8, "Algebraic Identities", "Square of a sum", "Algebra"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Perfect Square (a-b)²", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\^2", 
            r"(\1)^2 - 2*(\1)*(\2) + (\2)^2", 
            8, "Algebraic Identities", "Square of a difference", "Algebra"
        ))
        
        # Difference of Squares
        self.formulas.append(FormulaDefinition(
            "Difference of Squares", 
            r"([a-zA-Z])\^2\s*-\s*([a-zA-Z])\^2", 
            r"((\1) + (\2))*((\1) - (\2))", 
            8, "Algebraic Identities", "Difference of squares", "Algebra"
        ))
        
        # Sum and Difference of Cubes
        self.formulas.append(FormulaDefinition(
            "Sum of Cubes", 
            r"([a-zA-Z])\^3\s*\+\s*([a-zA-Z])\^3", 
            r"((\1) + (\2))*((\1)^2 - (\1)*(\2) + (\2)^2)", 
            9, "Algebraic Identities", "Sum of cubes", "Algebra"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Difference of Cubes", 
            r"([a-zA-Z])\^3\s*-\s*([a-zA-Z])\^3", 
            r"((\1) - (\2))*((\1)^2 + (\1)*(\2) + (\2)^2)", 
            9, "Algebraic Identities", "Difference of cubes", "Algebra"
        ))
        
        # Common Factor
        self.formulas.append(FormulaDefinition(
            "Common Factor", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"(\1)*((\2) + (\4))", 
            7, "Algebraic Identities", "Common factor extraction", "Algebra"
        ))
        
        # Middle Term Factoring
        self.formulas.append(FormulaDefinition(
            "Middle Term Factoring", 
            r"([a-zA-Z])\^2\s*\+\s*2\s*\*\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\+\s*([a-zA-Z])\^2", 
            r"((\1) + (\3))^2", 
            8, "Algebraic Identities", "Middle term factoring", "Algebra"
        ))
        
        # ============================================================================
        # TRIGONOMETRY (Grade 9-10)
        # ============================================================================
        
        # Pythagorean Identity
        self.formulas.append(FormulaDefinition(
            "Pythagorean Identity", 
            r"sin\^2\(([a-zA-Z])\)\s*\+\s*cos\^2\(([a-zA-Z])\)", 
            r"1", 
            9, "Trigonometry", "Pythagorean identity", "Trigonometry"
        ))
        
        # Double Angle Formulas
        self.formulas.append(FormulaDefinition(
            "Double Angle Sine", 
            r"sin\(2\s*\*\s*([a-zA-Z])\)", 
            r"2*sin((\1))*cos((\1))", 
            10, "Trigonometry", "Double angle sine", "Trigonometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Double Angle Cosine", 
            r"cos\(2\s*\*\s*([a-zA-Z])\)", 
            r"cos((\1))^2 - sin((\1))^2", 
            10, "Trigonometry", "Double angle cosine", "Trigonometry"
        ))
        
        # ============================================================================
        # LOGARITHMS (Grade 9-10)
        # ============================================================================
        
        # Log Rules
        self.formulas.append(FormulaDefinition(
            "Log Product Rule", 
            r"log\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"log((\1)) + log((\2))", 
            9, "Logarithms", "Log of product", "Logarithms"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Log Quotient Rule", 
            r"log\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"log((\1)) - log((\2))", 
            9, "Logarithms", "Log of quotient", "Logarithms"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Log Power Rule", 
            r"log\(([a-zA-Z])\s*\^\s*([a-zA-Z])\)", 
            r"(\2)*log((\1))", 
            9, "Logarithms", "Log of power", "Logarithms"
        ))
        
        # ============================================================================
        # BASIC ARITHMETIC (Grade 6-7)
        # ============================================================================
        
        # Addition Properties
        self.formulas.append(FormulaDefinition(
            "Commutative Addition", 
            r"([a-zA-Z])\s*\+\s*([a-zA-Z])", 
            r"(\2) + (\1)", 
            6, "Arithmetic", "Commutative property of addition", "Arithmetic"
        ))
        
        # Multiplication Properties
        self.formulas.append(FormulaDefinition(
            "Commutative Multiplication", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"(\2) * (\1)", 
            6, "Arithmetic", "Commutative property of multiplication", "Arithmetic"
        ))
        
        # ============================================================================
        # FRACTIONS (Grade 6-8)
        # ============================================================================
        
        # Fraction Addition
        self.formulas.append(FormulaDefinition(
            "Fraction Addition", 
            r"([a-zA-Z])/([a-zA-Z])\s*\+\s*([a-zA-Z])/([a-zA-Z])", 
            r"((\1)*(\4) + (\3)*(\2))/((\2)*(\4))", 
            7, "Fractions", "Addition of fractions", "Fractions"
        ))
        
        # ============================================================================
        # POWERS AND ROOTS (Grade 7-9)
        # ============================================================================
        
        # Power Rules
        self.formulas.append(FormulaDefinition(
            "Power of Zero", 
            r"([a-zA-Z])\^0", 
            r"1", 
            7, "Powers", "Any number to power 0", "Powers"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Power of One", 
            r"([a-zA-Z])\^1", 
            r"(\1)", 
            7, "Powers", "Any number to power 1", "Powers"
        ))
        
        # ============================================================================
        # GEOMETRY (Grade 6-10)
        # ============================================================================
        
        # Area Formulas
        self.formulas.append(FormulaDefinition(
            "Rectangle Area", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"length * width", 
            6, "Geometry", "Rectangle area", "Geometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Triangle Area", 
            r"\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)\s*/\s*2", 
            r"(base * height)/2", 
            7, "Geometry", "Triangle area", "Geometry"
        ))
        
        # ============================================================================
        # STATISTICS (Grade 7-10)
        # ============================================================================
        
        # Mean
        self.formulas.append(FormulaDefinition(
            "Arithmetic Mean", 
            r"\(([a-zA-Z])\s*\+\s*([a-zA-Z])\s*\+\s*([a-zA-Z])\)\s*/\s*3", 
            r"(sum of values)/(number of values)", 
            7, "Statistics", "Arithmetic mean", "Statistics"
        ))
        
        # ============================================================================
        # PROBABILITY (Grade 7-10)
        # ============================================================================
        
        # Basic Probability
        self.formulas.append(FormulaDefinition(
            "Probability", 
            r"([a-zA-Z])\s*/\s*([a-zA-Z])", 
            r"favorable outcomes / total outcomes", 
            7, "Probability", "Basic probability", "Probability"
        ))
        
        # ============================================================================
        # SEQUENCES AND SERIES (Grade 9-10)
        # ============================================================================
        
        # Arithmetic Sequence
        self.formulas.append(FormulaDefinition(
            "Arithmetic Term", 
            r"([a-zA-Z])\s*\+\s*\(([a-zA-Z])\s*-\s*1\)\s*\*\s*([a-zA-Z])", 
            r"first term + (n-1) * common difference", 
            9, "Sequences", "Arithmetic sequence term", "Sequences"
        ))
        
        # ============================================================================
        # CALCULUS BASICS (Grade 10+)
        # ============================================================================
        
        # Derivative Rules
        self.formulas.append(FormulaDefinition(
            "Power Rule", 
            r"d/dx\(([a-zA-Z])\^([a-zA-Z])\)", 
            r"(\2)*(\1)^((\2)-1)", 
            10, "Calculus", "Power rule for derivatives", "Calculus"
        ))
        
        # ============================================================================
        # ADDITIONAL ALGEBRAIC IDENTITIES (Grade 8-10)
        # ============================================================================
        
        # Binomial Expansion
        self.formulas.append(FormulaDefinition(
            "Binomial Expansion (a+b)^3", 
            r"\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)\^3", 
            r"(\1)^3 + 3*(\1)^2*(\2) + 3*(\1)*(\2)^2 + (\2)^3", 
            9, "Algebraic Identities", "Binomial expansion", "Algebra"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Binomial Expansion (a-b)^3", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\^3", 
            r"(\1)^3 - 3*(\1)^2*(\2) + 3*(\1)*(\2)^2 - (\2)^3", 
            9, "Algebraic Identities", "Binomial expansion", "Algebra"
        ))
        
        # Trinomial Square
        self.formulas.append(FormulaDefinition(
            "Trinomial Square", 
            r"\(([a-zA-Z])\s*\+\s*([a-zA-Z])\s*\+\s*([a-zA-Z])\)\^2", 
            r"(\1)^2 + (\2)^2 + (\3)^2 + 2*(\1)*(\2) + 2*(\1)*(\3) + 2*(\2)*(\3)", 
            9, "Algebraic Identities", "Trinomial square", "Algebra"
        ))
        
        # ============================================================================
        # ADDITIONAL TRIGONOMETRY (Grade 9-10)
        # ============================================================================
        
        # Half Angle Formulas
        self.formulas.append(FormulaDefinition(
            "Half Angle Sine", 
            r"sin\(([a-zA-Z])/2\)", 
            r"+-sqrt((1-cos((\1)))/2)", 
            10, "Trigonometry", "Half angle sine", "Trigonometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Half Angle Cosine", 
            r"cos\(([a-zA-Z])/2\)", 
            r"+-sqrt((1+cos((\1)))/2)", 
            10, "Trigonometry", "Half angle cosine", "Trigonometry"
        ))
        
        # Product to Sum
        self.formulas.append(FormulaDefinition(
            "Product to Sum Sine", 
            r"sin\(([a-zA-Z])\)\s*\*\s*sin\(([a-zA-Z])\)", 
            r"(cos((\1)-(\2)) - cos((\1)+(\2)))/2", 
            10, "Trigonometry", "Product to sum sine", "Trigonometry"
        ))
        
        # ============================================================================
        # ADDITIONAL LOGARITHMS (Grade 9-10)
        # ============================================================================
        
        # Natural Log
        self.formulas.append(FormulaDefinition(
            "Natural Log Product", 
            r"ln\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"ln((\1)) + ln((\2))", 
            10, "Logarithms", "Natural log of product", "Logarithms"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Natural Log Quotient", 
            r"ln\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"ln((\1)) - ln((\2))", 
            10, "Logarithms", "Natural log of quotient", "Logarithms"
        ))
        
        # ============================================================================
        # ADDITIONAL EXPONENTIALS (Grade 9-10)
        # ============================================================================
        
        # Exponential Rules
        self.formulas.append(FormulaDefinition(
            "Exponential Product", 
            r"([a-zA-Z])\^([a-zA-Z])\s*\*\s*([a-zA-Z])\^([a-zA-Z])", 
            r"(\1)^((\2) + (\4))", 
            9, "Exponentials", "Product of exponentials", "Exponentials"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Exponential Quotient", 
            r"([a-zA-Z])\^([a-zA-Z])\s*/\s*([a-zA-Z])\^([a-zA-Z])", 
            r"(\1)^((\2) - (\4))", 
            9, "Exponentials", "Quotient of exponentials", "Exponentials"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Power of Power", 
            r"\(([a-zA-Z])\^([a-zA-Z])\)\^([a-zA-Z])", 
            r"(\1)^((\2)*(\3))", 
            9, "Exponentials", "Power of power", "Exponentials"
        ))
        
        # ============================================================================
        # ADDITIONAL ARITHMETIC (Grade 6-7)
        # ============================================================================
        
        # Addition Properties
        self.formulas.append(FormulaDefinition(
            "Associative Addition", 
            r"\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)\s*\+\s*([a-zA-Z])", 
            r"(\1) + ((\2) + (\3))", 
            6, "Arithmetic", "Associative property of addition", "Arithmetic"
        ))
        
        # Multiplication Properties
        self.formulas.append(FormulaDefinition(
            "Associative Multiplication", 
            r"\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)\s*\*\s*([a-zA-Z])", 
            r"(\1) * ((\2) * (\3))", 
            6, "Arithmetic", "Associative property of multiplication", "Arithmetic"
        ))
        
        # Distributive Property
        self.formulas.append(FormulaDefinition(
            "Distributive Property", 
            r"([a-zA-Z])\s*\*\s*\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)", 
            r"(\1)*(\2) + (\1)*(\3)", 
            7, "Arithmetic", "Distributive property", "Arithmetic"
        ))
        
        # ============================================================================
        # ADDITIONAL FRACTIONS (Grade 6-8)
        # ============================================================================
        
        # Fraction Multiplication
        self.formulas.append(FormulaDefinition(
            "Fraction Multiplication", 
            r"([a-zA-Z])/([a-zA-Z])\s*\*\s*([a-zA-Z])/([a-zA-Z])", 
            r"((\1)*(\3))/((\2)*(\4))", 
            7, "Fractions", "Multiplication of fractions", "Fractions"
        ))
        
        # Fraction Division
        self.formulas.append(FormulaDefinition(
            "Fraction Division", 
            r"([a-zA-Z])/([a-zA-Z])\s*/\s*([a-zA-Z])/([a-zA-Z])", 
            r"((\1)*(\4))/((\2)*(\3))", 
            7, "Fractions", "Division of fractions", "Fractions"
        ))
        
        # ============================================================================
        # ADDITIONAL POWERS (Grade 7-9)
        # ============================================================================
        
        # Power Rules
        self.formulas.append(FormulaDefinition(
            "Negative Power", 
            r"([a-zA-Z])\^-([a-zA-Z])", 
            r"1/((\1)^(\2))", 
            8, "Powers", "Negative power", "Powers"
        ))
        
        # Root Rules
        self.formulas.append(FormulaDefinition(
            "Square Root of Square", 
            r"sqrt\(([a-zA-Z])\^2\)", 
            r"abs((\1))", 
            8, "Roots", "Square root of square", "Roots"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Root of Product", 
            r"sqrt\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"sqrt((\1))*sqrt((\2))", 
            8, "Roots", "Root of product", "Roots"
        ))
        
        # ============================================================================
        # ADDITIONAL LINEAR EQUATIONS (Grade 7-8)
        # ============================================================================
        
        # Slope Formula
        self.formulas.append(FormulaDefinition(
            "Slope Formula", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*/\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"((\1) - (\2))/((\3) - (\4))", 
            8, "Linear Equations", "Slope formula", "Linear Equations"
        ))
        
        # Point-Slope Form
        self.formulas.append(FormulaDefinition(
            "Point-Slope Form", 
            r"([a-zA-Z])\s*-\s*([a-zA-Z])\s*=\s*([a-zA-Z])\s*\*\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"(\1) = (\3)*((\4) - (\5)) + (\2)", 
            8, "Linear Equations", "Point-slope form", "Linear Equations"
        ))
        
        # ============================================================================
        # ADDITIONAL GEOMETRY (Grade 6-10)
        # ============================================================================
        
        # Area Formulas
        self.formulas.append(FormulaDefinition(
            "Circle Area", 
            r"pi\s*\*\s*([a-zA-Z])\^2", 
            r"π * radius^2", 
            8, "Geometry", "Circle area", "Geometry"
        ))
        
        # Perimeter Formulas
        self.formulas.append(FormulaDefinition(
            "Rectangle Perimeter", 
            r"2\s*\*\s*\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)", 
            r"2 * (length + width)", 
            6, "Geometry", "Rectangle perimeter", "Geometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Circle Circumference", 
            r"2\s*\*\s*pi\s*\*\s*([a-zA-Z])", 
            r"2 * π * radius", 
            8, "Geometry", "Circle circumference", "Geometry"
        ))
        
        # Volume Formulas
        self.formulas.append(FormulaDefinition(
            "Cube Volume", 
            r"([a-zA-Z])\^3", 
            r"side^3", 
            7, "Geometry", "Cube volume", "Geometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Cylinder Volume", 
            r"pi\s*\*\s*([a-zA-Z])\^2\s*\*\s*([a-zA-Z])", 
            r"π * radius^2 * height", 
            9, "Geometry", "Cylinder volume", "Geometry"
        ))
        
        # ============================================================================
        # ADDITIONAL STATISTICS (Grade 7-10)
        # ============================================================================
        
        # Variance
        self.formulas.append(FormulaDefinition(
            "Sample Variance", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*\+\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2", 
            r"sum of squared deviations", 
            9, "Statistics", "Sample variance", "Statistics"
        ))
        
        # ============================================================================
        # ADDITIONAL PROBABILITY (Grade 7-10)
        # ============================================================================
        
        # Independent Events
        self.formulas.append(FormulaDefinition(
            "Independent Events", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"P(A) * P(B)", 
            8, "Probability", "Independent events", "Probability"
        ))
        
        # ============================================================================
        # ADDITIONAL SEQUENCES (Grade 9-10)
        # ============================================================================
        
        # Geometric Sequence
        self.formulas.append(FormulaDefinition(
            "Geometric Term", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^\s*\(([a-zA-Z])\s*-\s*1\)", 
            r"first term * common ratio^(n-1)", 
            9, "Sequences", "Geometric sequence term", "Sequences"
        ))
        
        # ============================================================================
        # ADDITIONAL CALCULUS (Grade 10+)
        # ============================================================================
        
        # Derivative Rules
        self.formulas.append(FormulaDefinition(
            "Constant Rule", 
            r"d/dx\(([a-zA-Z])\)", 
            r"0", 
            10, "Calculus", "Derivative of constant", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Sum Rule", 
            r"d/dx\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)", 
            r"d/dx((\1)) + d/dx((\2))", 
            10, "Calculus", "Derivative of sum", "Calculus"
        ))
        
        # Integration Rules
        self.formulas.append(FormulaDefinition(
            "Power Rule Integration", 
            r"∫([a-zA-Z])\^([a-zA-Z])\s*dx", 
            r"((\1)^((\2)+1))/((\2)+1) + C", 
            10, "Calculus", "Power rule for integration", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Constant Integration", 
            r"∫([a-zA-Z])\s*dx", 
            r"(\1)*x + C", 
            10, "Calculus", "Integration of constant", "Calculus"
        ))
        
        # ============================================================================
        # ADVANCED ALGEBRAIC IDENTITIES (Grade 9-10)
        # ============================================================================
        
        # Sum and Difference of Powers
        self.formulas.append(FormulaDefinition(
            "Sum of Fourth Powers", 
            r"([a-zA-Z])\^4\s*\+\s*([a-zA-Z])\^4", 
            r"((\1)^2 + (\2)^2)*((\1)^2 - (\2)^2)", 
            10, "Algebraic Identities", "Sum of fourth powers", "Algebra"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Difference of Fourth Powers", 
            r"([a-zA-Z])\^4\s*-\s*([a-zA-Z])\^4", 
            r"((\1)^2 + (\2)^2)*((\1) + (\2))*((\1) - (\2))", 
            10, "Algebraic Identities", "Difference of fourth powers", "Algebra"
        ))
        
        # Quadratic Forms
        self.formulas.append(FormulaDefinition(
            "Quadratic Formula", 
            r"([a-zA-Z])\s*=\s*\(-([a-zA-Z])\s*\+\s*-\s*sqrt\(([a-zA-Z])\^2\s*-\s*4\s*\*\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\)\)\s*/\s*\(2\s*\*\s*([a-zA-Z])\)", 
            r"(-b ± sqrt(b^2 - 4ac))/(2a)", 
            9, "Algebraic Identities", "Quadratic formula", "Algebra"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Complete the Square", 
            r"([a-zA-Z])\^2\s*\+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\+\s*([a-zA-Z])", 
            r"((\1) + (\2)/(2))^2 + (\4) - (\2)^2/4", 
            9, "Algebraic Identities", "Complete the square", "Algebra"
        ))
        
        # ============================================================================
        # ADVANCED TRIGONOMETRY (Grade 10+)
        # ============================================================================
        
        # Sum and Difference Formulas
        self.formulas.append(FormulaDefinition(
            "Sine Sum", 
            r"sin\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)", 
            r"sin((\1))*cos((\2)) + cos((\1))*sin((\2))", 
            10, "Trigonometry", "Sine of sum", "Trigonometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Cosine Sum", 
            r"cos\(([a-zA-Z])\s*\+\s*([a-zA-Z])\)", 
            r"cos((\1))*cos((\2)) - sin((\1))*sin((\2))", 
            10, "Trigonometry", "Cosine of sum", "Trigonometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Sine Difference", 
            r"sin\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"sin((\1))*cos((\2)) - cos((\1))*sin((\2))", 
            10, "Trigonometry", "Sine of difference", "Trigonometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Cosine Difference", 
            r"cos\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"cos((\1))*cos((\2)) + sin((\1))*sin((\2))", 
            10, "Trigonometry", "Cosine of difference", "Trigonometry"
        ))
        
        # Tangent Formulas
        self.formulas.append(FormulaDefinition(
            "Tangent Sum", 
            r"tan\(([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"(tan((\1)) + tan((\2)))/(1 - tan((\1))*tan((\2)))", 
            10, "Trigonometry", "Tangent of sum", "Trigonometry"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Tangent Difference", 
            r"tan\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"(tan((\1)) - tan((\2)))/(1 + tan((\1))*tan((\2)))", 
            10, "Trigonometry", "Tangent of difference", "Trigonometry"
        ))
        
        # ============================================================================
        # ADVANCED LOGARITHMS (Grade 10+)
        # ============================================================================
        
        # Change of Base
        self.formulas.append(FormulaDefinition(
            "Change of Base", 
            r"log_([a-zA-Z])\(([a-zA-Z])\)", 
            r"ln((\2))/ln((\1))", 
            10, "Logarithms", "Change of base", "Logarithms"
        ))
        
        # ============================================================================
        # ADVANCED EXPONENTIALS (Grade 10+)
        # ============================================================================
        
        # Euler's Formula
        self.formulas.append(FormulaDefinition(
            "Euler's Formula", 
            r"e\^\(([a-zA-Z])\s*\*\s*i\)", 
            r"cos((\1)) + i*sin((\1))", 
            10, "Exponentials", "Euler's formula", "Exponentials"
        ))
        
        # ============================================================================
        # ADVANCED ARITHMETIC (Grade 8-10)
        # ============================================================================
        
        # Divisibility Rules
        self.formulas.append(FormulaDefinition(
            "Divisible by 2", 
            r"([a-zA-Z])\s*mod\s*2\s*=\s*0", 
            r"last digit is even", 
            8, "Arithmetic", "Divisibility by 2", "Arithmetic"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Divisible by 3", 
            r"sum of digits divisible by 3", 
            r"sum of digits mod 3 = 0", 
            8, "Arithmetic", "Divisibility by 3", "Arithmetic"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Divisible by 5", 
            r"([a-zA-Z])\s*mod\s*5\s*=\s*0", 
            r"last digit is 0 or 5", 
            8, "Arithmetic", "Divisibility by 5", "Arithmetic"
        ))
        
        # ============================================================================
        # ADVANCED FRACTIONS (Grade 8-10)
        # ============================================================================
        
        # Complex Fractions
        self.formulas.append(FormulaDefinition(
            "Complex Fraction", 
            r"\(([a-zA-Z])\s*/\s*([a-zA-Z])\)\s*/\s*\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"((\1)*(\4))/((\2)*(\3))", 
            8, "Fractions", "Complex fraction", "Fractions"
        ))
        
        # ============================================================================
        # ADVANCED POWERS (Grade 9-10)
        # ============================================================================
        
        # Rational Exponents
        self.formulas.append(FormulaDefinition(
            "Rational Exponent", 
            r"([a-zA-Z])\^\(([a-zA-Z])/([a-zA-Z])\)", 
            r"((\1)^(\2))^(1/(\3))", 
            9, "Powers", "Rational exponent", "Powers"
        ))
        
        # ============================================================================
        # ADVANCED LINEAR EQUATIONS (Grade 9-10)
        # ============================================================================
        
        # Slope-Intercept Form
        self.formulas.append(FormulaDefinition(
            "Slope-Intercept Form", 
            r"([a-zA-Z])\s*=\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*+\s*([a-zA-Z])", 
            r"y = mx + b", 
            9, "Linear Equations", "Slope-intercept form", "Linear Equations"
        ))
        
        # Two-Point Form
        self.formulas.append(FormulaDefinition(
            "Two-Point Form", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*/\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*=\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*/\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"(y-y1)/(x-x1) = (y2-y1)/(x2-x1)", 
            9, "Linear Equations", "Two-point form", "Linear Equations"
        ))
        
        # ============================================================================
        # ADVANCED GEOMETRY (Grade 9-10)
        # ============================================================================
        
        # Pythagorean Theorem
        self.formulas.append(FormulaDefinition(
            "Pythagorean Theorem", 
            r"([a-zA-Z])\^2\s*+\s*([a-zA-Z])\^2\s*=\s*([a-zA-Z])\^2", 
            r"a^2 + b^2 = c^2", 
            8, "Geometry", "Pythagorean theorem", "Geometry"
        ))
        
        # Heron's Formula
        self.formulas.append(FormulaDefinition(
            "Heron's Formula", 
            r"sqrt\(s\s*\*\s*\(s\s*-\s*([a-zA-Z])\)\s*\*\s*\(s\s*-\s*([a-zA-Z])\)\s*\*\s*\(s\s*-\s*([a-zA-Z])\)\)", 
            r"sqrt(s*(s-a)*(s-b)*(s-c))", 
            10, "Geometry", "Heron's formula", "Geometry"
        ))
        
        # Distance Formula
        self.formulas.append(FormulaDefinition(
            "Distance Formula", 
            r"sqrt\(\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*+\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\)", 
            r"sqrt((x2-x1)^2 + (y2-y1)^2)", 
            9, "Geometry", "Distance formula", "Geometry"
        ))
        
        # Midpoint Formula
        self.formulas.append(FormulaDefinition(
            "Midpoint Formula", 
            r"\(\(([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*/\s*2\s*,\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*/\s*2\)", 
            r"((x1+x2)/2, (y1+y2)/2)", 
            9, "Geometry", "Midpoint formula", "Geometry"
        ))
        
        # ============================================================================
        # ADVANCED STATISTICS (Grade 9-10)
        # ============================================================================
        
        # Standard Deviation
        self.formulas.append(FormulaDefinition(
            "Standard Deviation", 
            r"sqrt\(\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*+\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*+\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\)", 
            r"sqrt(sum of squared deviations)", 
            9, "Statistics", "Standard deviation", "Statistics"
        ))
        
        # Correlation Coefficient
        self.formulas.append(FormulaDefinition(
            "Correlation Coefficient", 
            r"([a-zA-Z])\s*/\s*sqrt\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"covariance/(std_dev_x * std_dev_y)", 
            10, "Statistics", "Correlation coefficient", "Statistics"
        ))
        
        # ============================================================================
        # ADVANCED PROBABILITY (Grade 9-10)
        # ============================================================================
        
        # Conditional Probability
        self.formulas.append(FormulaDefinition(
            "Conditional Probability", 
            r"([a-zA-Z])\s*/\s*([a-zA-Z])", 
            r"P(A|B) = P(A∩B)/P(B)", 
            9, "Probability", "Conditional probability", "Probability"
        ))
        
        # Bayes' Theorem
        self.formulas.append(FormulaDefinition(
            "Bayes' Theorem", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*/\s*([a-zA-Z])", 
            r"P(A|B) = P(B|A)*P(A)/P(B)", 
            10, "Probability", "Bayes' theorem", "Probability"
        ))
        
        # ============================================================================
        # ADVANCED SEQUENCES (Grade 10+)
        # ============================================================================
        
        # Arithmetic Series Sum
        self.formulas.append(FormulaDefinition(
            "Arithmetic Series Sum", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*\*\s*([a-zA-Z])\s*/\s*2", 
            r"(first + last)*n/2", 
            10, "Sequences", "Arithmetic series sum", "Sequences"
        ))
        
        # Geometric Series Sum
        self.formulas.append(FormulaDefinition(
            "Geometric Series Sum", 
            r"([a-zA-Z])\s*\*\s*\(1\s*-\s*([a-zA-Z])\s*\^\s*([a-zA-Z])\)\s*/\s*\(1\s*-\s*([a-zA-Z])\)", 
            r"a*(1-r^n)/(1-r)", 
            10, "Sequences", "Geometric series sum", "Sequences"
        ))
        
        # ============================================================================
        # ADVANCED CALCULUS (Grade 10+)
        # ============================================================================
        
        # Chain Rule
        self.formulas.append(FormulaDefinition(
            "Chain Rule", 
            r"d/dx\(sin\(([a-zA-Z])\)\)", 
            r"cos((\1))*d/dx((\1))", 
            10, "Calculus", "Chain rule for sine", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Chain Rule Cosine", 
            r"d/dx\(cos\(([a-zA-Z])\)\)", 
            r"-sin((\1))*d/dx((\1))", 
            10, "Calculus", "Chain rule for cosine", "Calculus"
        ))
        
        # Integration by Parts
        self.formulas.append(FormulaDefinition(
            "Integration by Parts", 
            r"∫([a-zA-Z])\s*\*\s*d\(([a-zA-Z])\)", 
            r"u*v - ∫v*du", 
            10, "Calculus", "Integration by parts", "Calculus"
        ))
        
        # Advanced Derivative Rules
        self.formulas.append(FormulaDefinition(
            "Quotient Rule", 
            r"d/dx\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"((\2)*d/dx((\1)) - (\1)*d/dx((\2)))/((\2)^2)", 
            10, "Calculus", "Quotient rule", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Product Rule Extended", 
            r"d/dx\(([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"(\2)*(\3)*d/dx((\1)) + (\1)*(\3)*d/dx((\2)) + (\1)*(\2)*d/dx((\3))", 
            10, "Calculus", "Extended product rule", "Calculus"
        ))
        
        # Advanced Integration Rules
        self.formulas.append(FormulaDefinition(
            "Integration by Substitution", 
            r"∫([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\*\s*d\(([a-zA-Z])\)", 
            r"substitute u = (\3), du = d(\3)", 
            10, "Calculus", "Integration by substitution", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Partial Fractions Integration", 
            r"∫([a-zA-Z])\s*/\s*\(([a-zA-Z])\s*\*\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\)", 
            r"decompose into partial fractions", 
            10, "Calculus", "Partial fractions integration", "Calculus"
        ))
        
        # Trigonometric Integration
        self.formulas.append(FormulaDefinition(
            "Trigonometric Integration", 
            r"∫sin\^2\(([a-zA-Z])\)\s*dx", 
            r"(\1)/2 - sin(2*(\1))/4 + C", 
            10, "Calculus", "Trigonometric integration", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Trigonometric Integration Cos", 
            r"∫cos\^2\(([a-zA-Z])\)\s*dx", 
            r"(\1)/2 + sin(2*(\1))/4 + C", 
            10, "Calculus", "Trigonometric integration", "Calculus"
        ))
        
        # Exponential and Logarithmic Integration
        self.formulas.append(FormulaDefinition(
            "Exponential Integration", 
            r"∫([a-zA-Z])\s*\*\s*exp\(([a-zA-Z])\)\s*dx", 
            r"integration by parts: u = (\1), dv = exp((\2))dx", 
            10, "Calculus", "Exponential integration", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Logarithmic Integration", 
            r"∫ln\(([a-zA-Z])\)\s*dx", 
            r"(\1)*ln((\1)) - (\1) + C", 
            10, "Calculus", "Logarithmic integration", "Calculus"
        ))
        
        # Definite Integration
        self.formulas.append(FormulaDefinition(
            "Definite Integration", 
            r"∫_([a-zA-Z])\^([a-zA-Z])\s*([a-zA-Z])\s*dx", 
            r"F((\2)) - F((\1)) where F is antiderivative", 
            10, "Calculus", "Definite integration", "Calculus"
        ))
        
        # Improper Integration
        self.formulas.append(FormulaDefinition(
            "Improper Integration", 
            r"∫_([a-zA-Z])\^infinity\s*([a-zA-Z])\s*dx", 
            r"lim_{b->infinity} ∫_(\1)^b (\2) dx", 
            10, "Calculus", "Improper integration", "Calculus"
        ))
        
        # Multiple Integration
        self.formulas.append(FormulaDefinition(
            "Double Integration", 
            r"∫∫([a-zA-Z])\s*dx\s*dy", 
            r"integrate with respect to x first, then y", 
            10, "Calculus", "Double integration", "Calculus"
        ))
        
        # Line Integration
        self.formulas.append(FormulaDefinition(
            "Line Integration", 
            r"∫_C\s*([a-zA-Z])\s*ds", 
            r"integrate along curve C", 
            10, "Calculus", "Line integration", "Calculus"
        ))
        
        # Surface Integration
        self.formulas.append(FormulaDefinition(
            "Surface Integration", 
            r"∫∫_S\s*([a-zA-Z])\s*dS", 
            r"integrate over surface S", 
            10, "Calculus", "Surface integration", "Calculus"
        ))
        
        # Volume Integration
        self.formulas.append(FormulaDefinition(
            "Volume Integration", 
            r"∫∫∫_V\s*([a-zA-Z])\s*dV", 
            r"integrate over volume V", 
            10, "Calculus", "Volume integration", "Calculus"
        ))
        
        # Differential Equations
        self.formulas.append(FormulaDefinition(
            "First Order Linear DE", 
            r"dy/dx\s*+\s*([a-zA-Z])\s*\*\s*y\s*=\s*([a-zA-Z])", 
            r"y = e^(-∫P(x)dx) * ∫Q(x)*e^(∫P(x)dx)dx + C", 
            10, "Calculus", "First order linear differential equation", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Separable Variables DE", 
            r"dy/dx\s*=\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"∫(1/g(y))dy = ∫f(x)dx + C", 
            10, "Calculus", "Separable variables differential equation", "Calculus"
        ))
        
        # Series and Sequences
        self.formulas.append(FormulaDefinition(
            "Taylor Series", 
            r"f\(([a-zA-Z])\)\s*=\s*sum_([a-zA-Z])\s*=\s*0\s*to\s*infinity\s*of\s*\(f\^\(([a-zA-Z])\)\s*\(([a-zA-Z])\)\s*/\s*([a-zA-Z])!\)\s*\*\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\^([a-zA-Z])", 
            r"f(x) = Σ_{n=0}^∞ (f^(n)(a)/n!) * (x-a)^n", 
            10, "Calculus", "Taylor series expansion", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Maclaurin Series", 
            r"f\(([a-zA-Z])\)\s*=\s*sum_([a-zA-Z])\s*=\s*0\s*to\s*infinity\s*of\s*\(f\^\(([a-zA-Z])\)\s*\(0\)\s*/\s*([a-zA-Z])!\)\s*\*\s*([a-zA-Z])\^([a-zA-Z])", 
            r"f(x) = Σ_{n=0}^∞ (f^(n)(0)/n!) * x^n", 
            10, "Calculus", "Maclaurin series expansion", "Calculus"
        ))
        
        # Limits
        self.formulas.append(FormulaDefinition(
            "L'Hôpital's Rule", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*([a-zA-Z])/([a-zA-Z])\s*=\s*0/0", 
            r"lim_{x->a} f(x)/g(x) = lim_{x->a} f'(x)/g'(x)", 
            10, "Calculus", "L'Hôpital's rule", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Limit of Sum", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"lim_{x->a} f(x) + lim_{x->a} g(x)", 
            10, "Calculus", "Limit of sum", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Limit of Product", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"lim_{x->a} f(x) * lim_{x->a} g(x)", 
            10, "Calculus", "Limit of product", "Calculus"
        ))
        
        # Vector Calculus
        self.formulas.append(FormulaDefinition(
            "Gradient", 
            r"∇f\s*=\s*\(d/dx\s*,\s*d/dy\s*,\s*d/dz\)", 
            r"gradient operator", 
            10, "Calculus", "Gradient operator", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Divergence", 
            r"∇\s*\*\s*F\s*=\s*d/dx\s*\+\s*d/dy\s*\+\s*d/dz", 
            r"divergence operator", 
            10, "Calculus", "Divergence operator", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Curl", 
            r"∇\s*\*\s*F\s*=\s*\(d/dy\s*-\s*d/dz\s*,\s*d/dz\s*-\s*d/dx\s*,\s*d/dx\s*-\s*d/dy\)", 
            r"curl operator", 
            10, "Calculus", "Curl operator", "Calculus"
        ))
        
        # ============================================================================
        # COMPLEX NUMBERS (Grade 10+)
        # ============================================================================
        
        # Complex Conjugate
        self.formulas.append(FormulaDefinition(
            "Complex Conjugate", 
            r"([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*i", 
            r"a + bi", 
            10, "Complex Numbers", "Complex number form", "Complex Numbers"
        ))
        
        # Complex Modulus
        self.formulas.append(FormulaDefinition(
            "Complex Modulus", 
            r"sqrt\(([a-zA-Z])\^2\s*+\s*([a-zA-Z])\^2\)", 
            r"sqrt(a^2 + b^2)", 
            10, "Complex Numbers", "Complex modulus", "Complex Numbers"
        ))
        
        # ============================================================================
        # VECTORS (Grade 10+)
        # ============================================================================
        
        # Vector Addition
        self.formulas.append(FormulaDefinition(
            "Vector Addition", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*,\s*([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"(x1+x2, y1+y2)", 
            10, "Vectors", "Vector addition", "Vectors"
        ))
        
        # Vector Magnitude
        self.formulas.append(FormulaDefinition(
            "Vector Magnitude", 
            r"sqrt\(([a-zA-Z])\^2\s*+\s*([a-zA-Z])\^2\)", 
            r"sqrt(x^2 + y^2)", 
            10, "Vectors", "Vector magnitude", "Vectors"
        ))
        
        # ============================================================================
        # MATRICES (Grade 10+)
        # ============================================================================
        
        # Matrix Addition
        self.formulas.append(FormulaDefinition(
            "Matrix Addition", 
            r"\[([a-zA-Z])\s*([a-zA-Z])\]\s*+\s*\[([a-zA-Z])\s*([a-zA-Z])\]", 
            r"[a+b c+d]", 
            10, "Matrices", "Matrix addition", "Matrices"
        ))
        
        # 2x2 Determinant
        self.formulas.append(FormulaDefinition(
            "2x2 Determinant", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*-\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"ad - bc", 
            10, "Matrices", "2x2 determinant", "Matrices"
        ))
        
        # ============================================================================
        # POLYNOMIALS (Grade 9-10)
        # ============================================================================
        
        # Polynomial Addition
        self.formulas.append(FormulaDefinition(
            "Polynomial Addition", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*+\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"combine like terms", 
            9, "Polynomials", "Polynomial addition", "Polynomials"
        ))
        
        # Polynomial Multiplication
        self.formulas.append(FormulaDefinition(
            "Polynomial Multiplication", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*\*\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"FOIL method", 
            9, "Polynomials", "Polynomial multiplication", "Polynomials"
        ))
        
        # ============================================================================
        # RATIONAL EXPRESSIONS (Grade 9-10)
        # ============================================================================
        
        # Rational Addition
        self.formulas.append(FormulaDefinition(
            "Rational Addition", 
            r"([a-zA-Z])/([a-zA-Z])\s*+\s*([a-zA-Z])/([a-zA-Z])", 
            r"(ad + bc)/(bd)", 
            9, "Rational Expressions", "Rational addition", "Rational Expressions"
        ))
        
        # Rational Multiplication
        self.formulas.append(FormulaDefinition(
            "Rational Multiplication", 
            r"([a-zA-Z])/([a-zA-Z])\s*\*\s*([a-zA-Z])/([a-zA-Z])", 
            r"(ac)/(bd)", 
            9, "Rational Expressions", "Rational multiplication", "Rational Expressions"
        ))
        
        # ============================================================================
        # RADICALS (Grade 8-10)
        # ============================================================================
        
        # Radical Addition
        self.formulas.append(FormulaDefinition(
            "Radical Addition", 
            r"sqrt\(([a-zA-Z])\)\s*+\s*sqrt\(([a-zA-Z])\)", 
            r"sqrt(a) + sqrt(b)", 
            8, "Radicals", "Radical addition", "Radicals"
        ))
        
        # Radical Multiplication
        self.formulas.append(FormulaDefinition(
            "Radical Multiplication", 
            r"sqrt\(([a-zA-Z])\)\s*\*\s*sqrt\(([a-zA-Z])\)", 
            r"sqrt(a*b)", 
            8, "Radicals", "Radical multiplication", "Radicals"
        ))
        
        # ============================================================================
        # ABSOLUTE VALUES (Grade 8-10)
        # ============================================================================
        
        # Absolute Value Product
        self.formulas.append(FormulaDefinition(
            "Absolute Value Product", 
            r"abs\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"abs(a)*abs(b)", 
            8, "Absolute Values", "Absolute value of product", "Absolute Values"
        ))
        
        # Absolute Value Quotient
        self.formulas.append(FormulaDefinition(
            "Absolute Value Quotient", 
            r"abs\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"abs(a)/abs(b)", 
            8, "Absolute Values", "Absolute value of quotient", "Absolute Values"
        ))
        
        # ============================================================================
        # INEQUALITIES (Grade 8-10)
        # ============================================================================
        
        # Inequality Addition
        self.formulas.append(FormulaDefinition(
            "Inequality Addition", 
            r"([a-zA-Z])\s*<\s*([a-zA-Z])\s*+\s*([a-zA-Z])", 
            r"a < b + c", 
            8, "Inequalities", "Inequality addition", "Inequalities"
        ))
        
        # Inequality Multiplication
        self.formulas.append(FormulaDefinition(
            "Inequality Multiplication", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*>\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"a*b > c*d", 
            8, "Inequalities", "Inequality multiplication", "Inequalities"
        ))
        
        # ============================================================================
        # FUNCTIONS (Grade 9-10)
        # ============================================================================
        
        # Function Composition
        self.formulas.append(FormulaDefinition(
            "Function Composition", 
            r"f\(g\(([a-zA-Z])\)\)", 
            r"f(g(x))", 
            9, "Functions", "Function composition", "Functions"
        ))
        
        # Inverse Function
        self.formulas.append(FormulaDefinition(
            "Inverse Function", 
            r"f\^-1\(([a-zA-Z])\)", 
            r"f^(-1)(x)", 
            10, "Functions", "Inverse function", "Functions"
        ))
        
        # ============================================================================
        # LIMITS (Grade 10+)
        # ============================================================================
        
        # Limit of Constant
        self.formulas.append(FormulaDefinition(
            "Limit of Constant", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*([a-zA-Z])", 
            r"constant value", 
            10, "Limits", "Limit of constant", "Limits"
        ))
        
        # Limit of Sum
        self.formulas.append(FormulaDefinition(
            "Limit of Sum", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"limit of sum", 
            10, "Limits", "Limit of sum", "Limits"
        ))
        
        # ============================================================================
        # DIFFERENTIAL EQUATIONS (Grade 10+)
        # ============================================================================
        
        # First Order Linear
        self.formulas.append(FormulaDefinition(
            "First Order Linear", 
            r"dy/dx\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*=\s*([a-zA-Z])", 
            r"dy/dx + P(x)y = Q(x)", 
            10, "Differential Equations", "First order linear", "Differential Equations"
        ))
        
        # Separable Variables
        self.formulas.append(FormulaDefinition(
            "Separable Variables", 
            r"dy/dx\s*=\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"dy/dx = f(x)*g(y)", 
            10, "Differential Equations", "Separable variables", "Differential Equations"
        ))
        
        # ============================================================================
        # SERIES EXPANSIONS (Grade 10+)
        # ============================================================================
        
        # Taylor Series
        self.formulas.append(FormulaDefinition(
            "Taylor Series", 
            r"([a-zA-Z])\s*=\s*([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^2\s*/\s*2", 
            r"f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2", 
            10, "Series", "Taylor series", "Series"
        ))
        
        # Geometric Series
        self.formulas.append(FormulaDefinition(
            "Geometric Series", 
            r"([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^2", 
            r"a + ar + ar^2", 
            10, "Series", "Geometric series", "Series"
        ))
        
        # ============================================================================
        # NUMBER THEORY (Grade 8-10)
        # ============================================================================
        
        # Prime Test
        self.formulas.append(FormulaDefinition(
            "Prime Test", 
            r"([a-zA-Z])\s*>\s*1\s*and\s*no\s*divisors", 
            r"check divisibility up to sqrt(n)", 
            8, "Number Theory", "Prime number test", "Number Theory"
        ))
        
        # ============================================================================
        # ADDITIONAL TRIGONOMETRIC IDENTITIES (Grade 10+)
        # ============================================================================
        
        # Cosecant
        self.formulas.append(FormulaDefinition(
            "Cosecant", 
            r"csc\(([a-zA-Z])\)", 
            r"1/sin((\1))", 
            10, "Trigonometry", "Cosecant function", "Trigonometry"
        ))
        
        # Secant
        self.formulas.append(FormulaDefinition(
            "Secant", 
            r"sec\(([a-zA-Z])\)", 
            r"1/cos((\1))", 
            10, "Trigonometry", "Secant function", "Trigonometry"
        ))
        
        # Cotangent
        self.formulas.append(FormulaDefinition(
            "Cotangent", 
            r"cot\(([a-zA-Z])\)", 
            r"1/tan((\1))", 
            10, "Trigonometry", "Cotangent function", "Trigonometry"
        ))
        
        # Tangent
        self.formulas.append(FormulaDefinition(
            "Tangent", 
            r"tan\(([a-zA-Z])\)", 
            r"sin((\1))/cos((\1))", 
            10, "Trigonometry", "Tangent function", "Trigonometry"
        ))
        
        # ============================================================================
        # HYPERBOLIC FUNCTIONS (Grade 10+)
        # ============================================================================
        
        # Hyperbolic Sine
        self.formulas.append(FormulaDefinition(
            "Hyperbolic Sine", 
            r"sinh\(([a-zA-Z])\)", 
            r"(e^((\1)) - e^(-(\1)))/2", 
            10, "Hyperbolic Functions", "Hyperbolic sine", "Hyperbolic Functions"
        ))
        
        # Hyperbolic Cosine
        self.formulas.append(FormulaDefinition(
            "Hyperbolic Cosine", 
            r"cosh\(([a-zA-Z])\)", 
            r"(e^((\1)) + e^(-(\1)))/2", 
            10, "Hyperbolic Functions", "Hyperbolic cosine", "Hyperbolic Functions"
        ))
        
        # Hyperbolic Tangent
        self.formulas.append(FormulaDefinition(
            "Hyperbolic Tangent", 
            r"tanh\(([a-zA-Z])\)", 
            r"sinh((\1))/cosh((\1))", 
            10, "Hyperbolic Functions", "Hyperbolic tangent", "Hyperbolic Functions"
        ))
        
        # ============================================================================
        # SPECIAL FUNCTIONS (Grade 10+)
        # ============================================================================
        
        # Gamma Function
        self.formulas.append(FormulaDefinition(
            "Gamma Function", 
            r"Γ\(([a-zA-Z])\)", 
            r"integral from 0 to infinity", 
            10, "Special Functions", "Gamma function", "Special Functions"
        ))
        
        # Beta Function
        self.formulas.append(FormulaDefinition(
            "Beta Function", 
            r"B\(([a-zA-Z])\s*,\s*([a-zA-Z])\)", 
            r"Γ((\1))*Γ((\2))/Γ((\1)+(\2))", 
            10, "Special Functions", "Beta function", "Special Functions"
        ))
        
        # ============================================================================
        # FINANCIAL MATHEMATICS (Grade 9-10)
        # ============================================================================
        
        # Simple Interest
        self.formulas.append(FormulaDefinition(
            "Simple Interest", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"P * r * t", 
            9, "Financial Math", "Simple interest", "Financial Math"
        ))
        
        # Compound Interest
        self.formulas.append(FormulaDefinition(
            "Compound Interest", 
            r"([a-zA-Z])\s*\*\s*\(1\s*+\s*([a-zA-Z])\)\s*\^\s*([a-zA-Z])", 
            r"P * (1 + r)^t", 
            10, "Financial Math", "Compound interest", "Financial Math"
        ))
        
        # ============================================================================
        # OPTIMIZATION (Grade 10+)
        # ============================================================================
        
        # Critical Points
        self.formulas.append(FormulaDefinition(
            "Critical Points", 
            r"f\'\(([a-zA-Z])\)\s*=\s*0", 
            r"derivative equals zero", 
            10, "Optimization", "Critical points", "Optimization"
        ))
        
        # Lagrange Multipliers
        self.formulas.append(FormulaDefinition(
            "Lagrange Multipliers", 
            r"∇f\s*=\s*λ\s*\*\s*∇g", 
            r"gradient of f equals lambda times gradient of g", 
            10, "Optimization", "Lagrange multipliers", "Optimization"
        ))
        
        # ============================================================================
        # ADDITIONAL CALCULUS RULES (Grade 10+)
        # ============================================================================
        
        # Product Rule
        self.formulas.append(FormulaDefinition(
            "Product Rule", 
            r"d/dx\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"(\1)*d/dx((\2)) + (\2)*d/dx((\1))", 
            10, "Calculus", "Product rule", "Calculus"
        ))
        
        # Quotient Rule
        self.formulas.append(FormulaDefinition(
            "Quotient Rule", 
            r"d/dx\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"((\2)*d/dx((\1)) - (\1)*d/dx((\2)))/((\2)^2)", 
            10, "Calculus", "Quotient rule", "Calculus"
        ))
        
        # ============================================================================
        # ADDITIONAL INTEGRATION (Grade 10+)
        # ============================================================================
        
        # Function Integration
        self.formulas.append(FormulaDefinition(
            "Sine Integration", 
            r"∫sin\(([a-zA-Z])\)\s*dx", 
            r"-cos((\1)) + C", 
            10, "Calculus", "Integration of sine", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Cosine Integration", 
            r"∫cos\(([a-zA-Z])\)\s*dx", 
            r"sin((\1)) + C", 
            10, "Calculus", "Integration of cosine", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Exponential Integration", 
            r"∫e\^([a-zA-Z])\s*dx", 
            r"e^((\1)) + C", 
            10, "Calculus", "Integration of exponential", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Reciprocal Integration", 
            r"∫1/([a-zA-Z])\s*dx", 
            r"ln|(\1)| + C", 
            10, "Calculus", "Integration of reciprocal", "Calculus"
        ))
        
        # ============================================================================
        # ADDITIONAL GEOMETRIC TRANSFORMATIONS (Grade 9-10)
        # ============================================================================
        
        # Translation
        self.formulas.append(FormulaDefinition(
            "Translation", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*,\s*([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"(x+h, y+k)", 
            9, "Geometry", "Translation", "Geometry"
        ))
        
        # Reflection over x-axis
        self.formulas.append(FormulaDefinition(
            "Reflection over x-axis", 
            r"\(([a-zA-Z])\s*,\s*-([a-zA-Z])\)", 
            r"(x, -y)", 
            9, "Geometry", "Reflection over x-axis", "Geometry"
        ))
        
        # Rotation 90°
        self.formulas.append(FormulaDefinition(
            "Rotation 90°", 
            r"\(-([a-zA-Z])\s*,\s*([a-zA-Z])\)", 
            r"(-y, x)", 
            10, "Geometry", "Rotation 90 degrees", "Geometry"
        ))
        
        # Dilation
        self.formulas.append(FormulaDefinition(
            "Dilation", 
            r"\(([a-zA-Z])\s*\*\s*([a-zA-Z])\s*,\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"(k*x, k*y)", 
            10, "Geometry", "Dilation", "Geometry"
        ))
        
        # ============================================================================
        # CONIC SECTIONS (Grade 10+)
        # ============================================================================
        
        # Circle Equation
        self.formulas.append(FormulaDefinition(
            "Circle Equation", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*+\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*=\s*([a-zA-Z])\s*\^2", 
            r"(x-h)^2 + (y-k)^2 = r^2", 
            10, "Conic Sections", "Circle equation", "Conic Sections"
        ))
        
        # Parabola Equation
        self.formulas.append(FormulaDefinition(
            "Parabola Equation", 
            r"([a-zA-Z])\s*=\s*([a-zA-Z])\s*\*\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*+\s*([a-zA-Z])", 
            r"y = a(x-h)^2 + k", 
            10, "Conic Sections", "Parabola equation", "Conic Sections"
        ))
        
        # Ellipse Equation
        self.formulas.append(FormulaDefinition(
            "Ellipse Equation", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*/\s*([a-zA-Z])\s*\^2\s*+\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*/\s*([a-zA-Z])\s*\^2\s*=\s*1", 
            r"(x-h)^2/a^2 + (y-k)^2/b^2 = 1", 
            10, "Conic Sections", "Ellipse equation", "Conic Sections"
        ))
        
        # Hyperbola Equation
        self.formulas.append(FormulaDefinition(
            "Hyperbola Equation", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*/\s*([a-zA-Z])\s*\^2\s*-\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\s*\^2\s*/\s*([a-zA-Z])\s*\^2\s*=\s*1", 
            r"(x-h)^2/a^2 - (y-k)^2/b^2 = 1", 
            10, "Conic Sections", "Hyperbola equation", "Conic Sections"
        ))
        
        # ============================================================================
        # ADDITIONAL TRIGONOMETRIC IDENTITIES (Grade 10+)
        # ============================================================================
        
        # Sum to Product
        self.formulas.append(FormulaDefinition(
            "Sum to Product Sine", 
            r"sin\(([a-zA-Z])\)\s*+\s*sin\(([a-zA-Z])\)", 
            r"2*sin(((1)+(\2))/2)*cos(((1)-(\2))/2)", 
            10, "Trigonometry", "Sum to product sine", "Trigonometry"
        ))
        
        # Hyperbolic Identity
        self.formulas.append(FormulaDefinition(
            "Hyperbolic Identity", 
            r"cosh\^2\(([a-zA-Z])\)\s*-\s*sinh\^2\(([a-zA-Z])\)", 
            r"1", 
            10, "Hyperbolic Functions", "Hyperbolic identity", "Hyperbolic Functions"
        ))
        
        # ============================================================================
        # ADDITIONAL SPECIAL FUNCTIONS (Grade 10+)
        # ============================================================================
        
        # Error Function
        self.formulas.append(FormulaDefinition(
            "Error Function", 
            r"erf\(([a-zA-Z])\)", 
            r"2/sqrt(π) * integral from 0 to x of e^(-t^2) dt", 
            10, "Special Functions", "Error function", "Special Functions"
        ))
        
        # ============================================================================
        # ADDITIONAL FINANCIAL FORMULAS (Grade 10+)
        # ============================================================================
        
        # Present Value
        self.formulas.append(FormulaDefinition(
            "Present Value", 
            r"([a-zA-Z])\s*/\s*\(1\s*+\s*([a-zA-Z])\)\s*\^\s*([a-zA-Z])", 
            r"FV/(1+r)^n", 
            10, "Financial Math", "Present value", "Financial Math"
        ))
        
        # ============================================================================
        # ADDITIONAL NUMBER THEORY (Grade 9-10)
        # ============================================================================
        
        # GCD Property
        self.formulas.append(FormulaDefinition(
            "GCD Property", 
            r"gcd\(([a-zA-Z])\s*,\s*([a-zA-Z])\)\s*=\s*gcd\(([a-zA-Z])\s*,\s*([a-zA-Z])\s*mod\s*([a-zA-Z])\)", 
            r"gcd(a,b) = gcd(b, a mod b)", 
            9, "Number Theory", "GCD property", "Number Theory"
        ))
        
        # LCM Property
        self.formulas.append(FormulaDefinition(
            "LCM Property", 
            r"lcm\(([a-zA-Z])\s*,\s*([a-zA-Z])\)\s*=\s*\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)\s*/\s*([a-zA-Z])", 
            r"lcm(a,b) = (a*b)/gcd(a,b)", 
            9, "Number Theory", "LCM property", "Number Theory"
        ))
        
        # ============================================================================
        # ADDITIONAL ALGEBRAIC TECHNIQUES (Grade 8-10)
        # ============================================================================
        
        # Synthetic Division
        self.formulas.append(FormulaDefinition(
            "Synthetic Division", 
            r"([a-zA-Z])\s*\|\s*([a-zA-Z])\s*([a-zA-Z])\s*([a-zA-Z])\s*([a-zA-Z])\s*([a-zA-Z])", 
            r"polynomial division", 
            9, "Algebraic Techniques", "Synthetic division", "Algebraic Techniques"
        ))
        
        # Remainder Theorem
        self.formulas.append(FormulaDefinition(
            "Remainder Theorem", 
            r"([a-zA-Z])\s*mod\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"P(a) mod (x-a)", 
            9, "Algebraic Techniques", "Remainder theorem", "Algebraic Techniques"
        ))
        
        # Partial Fractions
        self.formulas.append(FormulaDefinition(
            "Partial Fractions", 
            r"([a-zA-Z])\s*/\s*\(([a-zA-Z])\s*\*\s*\(([a-zA-Z])\s*-\s*([a-zA-Z])\)\)", 
            r"decompose into partial fractions", 
            10, "Algebraic Techniques", "Partial fractions", "Algebraic Techniques"
        ))
        
        # Rationalize Denominator
        self.formulas.append(FormulaDefinition(
            "Rationalize Denominator", 
            r"([a-zA-Z])\s*/\s*\(([a-zA-Z])\s*+\s*sqrt\(([a-zA-Z])\)\)", 
            r"multiply by conjugate", 
            9, "Algebraic Techniques", "Rationalize denominator", "Algebraic Techniques"
        ))
        
        # ============================================================================
        # ADDITIONAL INEQUALITIES (Grade 9-10)
        # ============================================================================
        
        # Triangle Inequality
        self.formulas.append(FormulaDefinition(
            "Triangle Inequality", 
            r"abs\(([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*<=\s*abs\(([a-zA-Z])\)\s*+\s*abs\(([a-zA-Z])\)", 
            r"|a+b| ≤ |a| + |b|", 
            9, "Inequalities", "Triangle inequality", "Inequalities"
        ))
        
        # Absolute Value Sum
        self.formulas.append(FormulaDefinition(
            "Absolute Value Sum", 
            r"abs\(([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"|a + b|", 
            9, "Absolute Values", "Absolute value of sum", "Absolute Values"
        ))
        
        # ============================================================================
        # ADDITIONAL FUNCTION PROPERTIES (Grade 10+)
        # ============================================================================
        
        # Even Function
        self.formulas.append(FormulaDefinition(
            "Even Function", 
            r"f\(-([a-zA-Z])\)\s*=\s*f\(([a-zA-Z])\)", 
            r"f(-x) = f(x)", 
            10, "Functions", "Even function", "Functions"
        ))
        
        # Odd Function
        self.formulas.append(FormulaDefinition(
            "Odd Function", 
            r"f\(-([a-zA-Z])\)\s*=\s*-f\(([a-zA-Z])\)", 
            r"f(-x) = -f(x)", 
            10, "Functions", "Odd function", "Functions"
        ))
        
        # ============================================================================
        # ADDITIONAL LIMIT TECHNIQUES (Grade 10+)
        # ============================================================================
        
        # L'Hôpital's Rule
        self.formulas.append(FormulaDefinition(
            "L'Hôpital's Rule", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*([a-zA-Z])/([a-zA-Z])\s*=\s*0/0", 
            r"use L'Hôpital's rule", 
            10, "Limits", "L'Hôpital's rule", "Limits"
        ))
        
        # ============================================================================
        # ADDITIONAL DIFFERENTIAL EQUATIONS (Grade 10+)
        # ============================================================================
        
        # Homogeneous Equation
        self.formulas.append(FormulaDefinition(
            "Homogeneous Equation", 
            r"dy/dx\s*=\s*f\(([a-zA-Z])/([a-zA-Z])\)", 
            r"dy/dx = f(y/x)", 
            10, "Differential Equations", "Homogeneous equation", "Differential Equations"
        ))
        
        # ============================================================================
        # ADDITIONAL SERIES EXPANSIONS (Grade 10+)
        # ============================================================================
        
        # Maclaurin Series
        self.formulas.append(FormulaDefinition(
            "Maclaurin Series", 
            r"([a-zA-Z])\s*=\s*([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^2\s*/\s*2\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^3\s*/\s*6", 
            r"f(x) = f(0) + f'(0)x + f''(0)x^2/2 + f'''(0)x^3/6", 
            10, "Series", "Maclaurin series", "Series"
        ))
        
        # ============================================================================
        # ADDITIONAL COMPLEX NUMBER OPERATIONS (Grade 10+)
        # ============================================================================
        
        # Complex Division
        self.formulas.append(FormulaDefinition(
            "Complex Division", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*i\)\s*/\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*i\)", 
            r"multiply by conjugate", 
            10, "Complex Numbers", "Complex division", "Complex Numbers"
        ))
        
        # De Moivre's Theorem
        self.formulas.append(FormulaDefinition(
            "De Moivre's Theorem", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*i\)\s*\^\s*([a-zA-Z])", 
            r"r^n(cos(nθ) + i*sin(nθ))", 
            10, "Complex Numbers", "De Moivre's theorem", "Complex Numbers"
        ))
        
        # ============================================================================
        # ADDITIONAL VECTOR OPERATIONS (Grade 10+)
        # ============================================================================
        
        # Dot Product
        self.formulas.append(FormulaDefinition(
            "Dot Product", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])", 
            r"a1*b1 + a2*b2", 
            10, "Vectors", "Dot product", "Vectors"
        ))
        
        # Cross Product
        self.formulas.append(FormulaDefinition(
            "Cross Product", 
            r"\(([a-zA-Z])\s*\*\s*([a-zA-Z])\s*-\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*,\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*-\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*,\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*-\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"(a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)", 
            10, "Vectors", "Cross product", "Vectors"
        ))
        
        # ============================================================================
        # ADDITIONAL MATRIX OPERATIONS (Grade 10+)
        # ============================================================================
        
        # 2x2 Matrix Multiplication
        self.formulas.append(FormulaDefinition(
            "2x2 Matrix Multiplication", 
            r"\[([a-zA-Z])\s*([a-zA-Z])\]\s*\*\s*\[([a-zA-Z])\s*([a-zA-Z])\]", 
            r"[a b] * [e f] = [ae+bg af+bh]", 
            10, "Matrices", "2x2 matrix multiplication", "Matrices"
        ))
        
        # 2x2 Matrix Inverse
        self.formulas.append(FormulaDefinition(
            "2x2 Matrix Inverse", 
            r"1\s*/\s*\(([a-zA-Z])\s*\*\s*([a-zA-Z])\s*-\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\)\s*\*\s*\[([a-zA-Z])\s*-([a-zA-Z]);-([a-zA-Z])\s*([a-zA-Z])\]", 
            r"1/(ad-bc) * [d -b; -c a]", 
            10, "Matrices", "2x2 matrix inverse", "Matrices"
        ))
        
        # ============================================================================
        # ADDITIONAL BASIC ARITHMETIC (Grade 6-7)
        # ============================================================================
        
        # Power Rules
        self.formulas.append(FormulaDefinition(
            "Power of Zero", 
            r"([a-zA-Z])\^0", 
            r"1", 
            6, "Arithmetic", "Any number to power 0", "Arithmetic"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Power of One", 
            r"([a-zA-Z])\^1", 
            r"(\1)", 
            6, "Arithmetic", "Any number to power 1", "Arithmetic"
        ))
        
        # ============================================================================
        # ADDITIONAL FRACTION OPERATIONS (Grade 6-8)
        # ============================================================================
        
        # Fraction Addition
        self.formulas.append(FormulaDefinition(
            "Fraction Addition", 
            r"([a-zA-Z])/([a-zA-Z])\s*+\s*([a-zA-Z])/([a-zA-Z])", 
            r"((\1)*(\4) + (\3)*(\2))/((\2)*(\4))", 
            7, "Fractions", "Addition of fractions", "Fractions"
        ))
        
        # ============================================================================
        # ADDITIONAL ROOT OPERATIONS (Grade 8-9)
        # ============================================================================
        
        # Cube Root
        self.formulas.append(FormulaDefinition(
            "Cube Root", 
            r"cbrt\(([a-zA-Z])\)", 
            r"(\1)^(1/3)", 
            8, "Roots", "Cube root", "Roots"
        ))
        
        # Nth Root
        self.formulas.append(FormulaDefinition(
            "Nth Root", 
            r"root\(([a-zA-Z])\s*,\s*([a-zA-Z])\)", 
            r"(\1)^(1/(\2))", 
            9, "Roots", "Nth root", "Roots"
        ))
        
        # ============================================================================
        # ADDITIONAL TRIGONOMETRIC IDENTITIES (Grade 10+)
        # ============================================================================
        
        # Sum to Product Cosine
        self.formulas.append(FormulaDefinition(
            "Sum to Product Cosine", 
            r"cos\(([a-zA-Z])\)\s*+\s*cos\(([a-zA-Z])\)", 
            r"2*cos(((1)+(\2))/2)*cos(((1)-(\2))/2)", 
            10, "Trigonometry", "Sum to product cosine", "Trigonometry"
        ))
        
        # Product to Sum Cosine
        self.formulas.append(FormulaDefinition(
            "Product to Sum Cosine", 
            r"cos\(([a-zA-Z])\)\s*\*\s*cos\(([a-zA-Z])\)", 
            r"(cos((\1)-(\2)) + cos((\1)+(\2)))/2", 
            10, "Trigonometry", "Product to sum cosine", "Trigonometry"
        ))
        
        # ============================================================================
        # ADDITIONAL LOGARITHMIC IDENTITIES (Grade 10+)
        # ============================================================================
        
        # Log Power Rule
        self.formulas.append(FormulaDefinition(
            "Log Power Rule", 
            r"log\(([a-zA-Z])\s*\^\s*([a-zA-Z])\)", 
            r"(\2)*log((\1))", 
            10, "Logarithms", "Logarithm of power", "Logarithms"
        ))
        
        # ============================================================================
        # ADDITIONAL EXPONENTIAL IDENTITIES (Grade 9-10)
        # ============================================================================
        
        # Exponential Sum
        self.formulas.append(FormulaDefinition(
            "Exponential Sum", 
            r"([a-zA-Z])\^([a-zA-Z])\s*+\s*([a-zA-Z])\^([a-zA-Z])", 
            r"(\1)^(\2) + (\3)^(\4)", 
            9, "Exponentials", "Sum of exponentials", "Exponentials"
        ))
        
        # ============================================================================
        # ADDITIONAL GEOMETRIC FORMULAS (Grade 7-10)
        # ============================================================================
        
        # Sphere Volume
        self.formulas.append(FormulaDefinition(
            "Sphere Volume", 
            r"4\s*/\s*3\s*\*\s*pi\s*\*\s*([a-zA-Z])\^3", 
            r"(4/3) * π * radius^3", 
            9, "Geometry", "Sphere volume", "Geometry"
        ))
        
        # Cone Volume
        self.formulas.append(FormulaDefinition(
            "Cone Volume", 
            r"1\s*/\s*3\s*\*\s*pi\s*\*\s*([a-zA-Z])\^2\s*\*\s*([a-zA-Z])", 
            r"(1/3) * π * radius^2 * height", 
            9, "Geometry", "Cone volume", "Geometry"
        ))
        
        # Sphere Surface Area
        self.formulas.append(FormulaDefinition(
            "Sphere Surface Area", 
            r"4\s*\*\s*pi\s*\*\s*([a-zA-Z])\^2", 
            r"4 * π * radius^2", 
            9, "Geometry", "Sphere surface area", "Geometry"
        ))
        
        # ============================================================================
        # ADDITIONAL STATISTICAL FORMULAS (Grade 9-10)
        # ============================================================================
        
        # Population Variance
        self.formulas.append(FormulaDefinition(
            "Population Variance", 
            r"sum\(\(([a-zA-Z])\s*-\s*([a-zA-Z])\s*\)\s*\^2\)\s*/\s*([a-zA-Z])", 
            r"sum of squared deviations / n", 
            9, "Statistics", "Population variance", "Statistics"
        ))
        
        # Z-Score
        self.formulas.append(FormulaDefinition(
            "Z-Score", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\s*\)\s*/\s*([a-zA-Z])", 
            r"(x - μ) / σ", 
            10, "Statistics", "Z-score", "Statistics"
        ))
        
        # ============================================================================
        # ADDITIONAL PROBABILITY FORMULAS (Grade 9-10)
        # ============================================================================
        
        # Union Probability
        self.formulas.append(FormulaDefinition(
            "Union Probability", 
            r"([a-zA-Z])\s*+\s*([a-zA-Z])\s*-\s*([a-zA-Z])", 
            r"P(A) + P(B) - P(A∩B)", 
            9, "Probability", "Union probability", "Probability"
        ))
        
        # Conditional Probability Extended
        self.formulas.append(FormulaDefinition(
            "Conditional Probability Extended", 
            r"([a-zA-Z])\s*\*\s*([a-zA-Z])\s*/\s*([a-zA-Z])", 
            r"P(A∩B) / P(B)", 
            10, "Probability", "Conditional probability", "Probability"
        ))
        
        # ============================================================================
        # ADDITIONAL SEQUENCE FORMULAS (Grade 10+)
        # ============================================================================
        
        # Fibonacci Sequence
        self.formulas.append(FormulaDefinition(
            "Fibonacci Sequence", 
            r"([a-zA-Z])\s*=\s*([a-zA-Z])\s*+\s*([a-zA-Z])", 
            r"F(n) = F(n-1) + F(n-2)", 
            10, "Sequences", "Fibonacci sequence", "Sequences"
        ))
        
        # ============================================================================
        # ADDITIONAL CALCULUS FORMULAS (Grade 10+)
        # ============================================================================
        
        # Chain Rule Extended
        self.formulas.append(FormulaDefinition(
            "Chain Rule Extended", 
            r"d/dx\(exp\(([a-zA-Z])\)\)", 
            r"exp((\1))*d/dx((\1))", 
            10, "Calculus", "Chain rule for exponential", "Calculus"
        ))
        
        self.formulas.append(FormulaDefinition(
            "Chain Rule Natural Log", 
            r"d/dx\(ln\(([a-zA-Z])\)\)", 
            r"(1/(\1))*d/dx((\1))", 
            10, "Calculus", "Chain rule for natural log", "Calculus"
        ))
        
        # ============================================================================
        # ADDITIONAL COMPLEX NUMBER FORMULAS (Grade 10+)
        # ============================================================================
        
        # Complex Multiplication
        self.formulas.append(FormulaDefinition(
            "Complex Multiplication", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*i\)\s*\*\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*\*\s*i\)", 
            r"(ac-bd) + (ad+bc)i", 
            10, "Complex Numbers", "Complex multiplication", "Complex Numbers"
        ))
        
        # ============================================================================
        # ADDITIONAL VECTOR FORMULAS (Grade 10+)
        # ============================================================================
        
        # Vector Subtraction
        self.formulas.append(FormulaDefinition(
            "Vector Subtraction", 
            r"\(([a-zA-Z])\s*-\s*([a-zA-Z])\s*,\s*([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"(x1-x2, y1-y2)", 
            10, "Vectors", "Vector subtraction", "Vectors"
        ))
        
        # Vector Scalar Multiplication
        self.formulas.append(FormulaDefinition(
            "Vector Scalar Multiplication", 
            r"([a-zA-Z])\s*\*\s*\(([a-zA-Z])\s*,\s*([a-zA-Z])\)", 
            r"(k*x, k*y)", 
            10, "Vectors", "Vector scalar multiplication", "Vectors"
        ))
        
        # ============================================================================
        # ADDITIONAL MATRIX FORMULAS (Grade 10+)
        # ============================================================================
        
        # Matrix Scalar Multiplication
        self.formulas.append(FormulaDefinition(
            "Matrix Scalar Multiplication", 
            r"([a-zA-Z])\s*\*\s*\[([a-zA-Z])\s*([a-zA-Z])\]", 
            r"[k*a k*b]", 
            10, "Matrices", "Matrix scalar multiplication", "Matrices"
        ))
        
        # ============================================================================
        # ADDITIONAL POLYNOMIAL FORMULAS (Grade 9-10)
        # ============================================================================
        
        # Polynomial Subtraction
        self.formulas.append(FormulaDefinition(
            "Polynomial Subtraction", 
            r"\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*+\s*([a-zA-Z])\)\s*-\s*\(([a-zA-Z])\s*+\s*([a-zA-Z])\s*+\s*([a-zA-Z])\)", 
            r"subtract like terms", 
            9, "Polynomials", "Polynomial subtraction", "Polynomials"
        ))
        
        # ============================================================================
        # ADDITIONAL RATIONAL EXPRESSION FORMULAS (Grade 9-10)
        # ============================================================================
        
        # Rational Subtraction
        self.formulas.append(FormulaDefinition(
            "Rational Subtraction", 
            r"([a-zA-Z])/([a-zA-Z])\s*-\s*([a-zA-Z])/([a-zA-Z])", 
            r"((\1)*(\4) - (\3)*(\2))/((\2)*(\4))", 
            9, "Rational Expressions", "Rational subtraction", "Rational Expressions"
        ))
        
        # ============================================================================
        # ADDITIONAL RADICAL FORMULAS (Grade 8-10)
        # ============================================================================
        
        # Radical Subtraction
        self.formulas.append(FormulaDefinition(
            "Radical Subtraction", 
            r"sqrt\(([a-zA-Z])\)\s*-\s*sqrt\(([a-zA-Z])\)", 
            r"sqrt(a) - sqrt(b)", 
            8, "Radicals", "Radical subtraction", "Radicals"
        ))
        
        # Radical Division
        self.formulas.append(FormulaDefinition(
            "Radical Division", 
            r"sqrt\(([a-zA-Z])\)\s*/\s*sqrt\(([a-zA-Z])\)", 
            r"sqrt(a/b)", 
            8, "Radicals", "Radical division", "Radicals"
        ))
        
        # ============================================================================
        # ADDITIONAL ABSOLUTE VALUE FORMULAS (Grade 8-10)
        # ============================================================================
        
        # Absolute Value Difference
        self.formulas.append(FormulaDefinition(
            "Absolute Value Difference", 
            r"abs\(([a-zA-Z])\s*-\s*([a-zA-Z])\)", 
            r"|a - b|", 
            8, "Absolute Values", "Absolute value of difference", "Absolute Values"
        ))
        
        # ============================================================================
        # ADDITIONAL INEQUALITY FORMULAS (Grade 8-10)
        # ============================================================================
        
        # Inequality Subtraction
        self.formulas.append(FormulaDefinition(
            "Inequality Subtraction", 
            r"([a-zA-Z])\s*>\s*([a-zA-Z])\s*-\s*([a-zA-Z])", 
            r"a > b - c", 
            8, "Inequalities", "Inequality subtraction", "Inequalities"
        ))
        
        # ============================================================================
        # ADDITIONAL FUNCTION FORMULAS (Grade 9-10)
        # ============================================================================
        
        # Function Addition
        self.formulas.append(FormulaDefinition(
            "Function Addition", 
            r"f\(([a-zA-Z])\)\s*+\s*g\(([a-zA-Z])\)", 
            r"(f+g)(x)", 
            9, "Functions", "Function addition", "Functions"
        ))
        
        # Function Multiplication
        self.formulas.append(FormulaDefinition(
            "Function Multiplication", 
            r"f\(([a-zA-Z])\)\s*\*\s*g\(([a-zA-Z])\)", 
            r"(f*g)(x)", 
            9, "Functions", "Function multiplication", "Functions"
        ))
        
        # ============================================================================
        # ADDITIONAL LIMIT FORMULAS (Grade 10+)
        # ============================================================================
        
        # Limit of Product
        self.formulas.append(FormulaDefinition(
            "Limit of Product", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*\(([a-zA-Z])\s*\*\s*([a-zA-Z])\)", 
            r"limit of product", 
            10, "Limits", "Limit of product", "Limits"
        ))
        
        # Limit of Quotient
        self.formulas.append(FormulaDefinition(
            "Limit of Quotient", 
            r"lim_([a-zA-Z]->([a-zA-Z]))\s*\(([a-zA-Z])\s*/\s*([a-zA-Z])\)", 
            r"limit of quotient", 
            10, "Limits", "Limit of quotient", "Limits"
        ))
        
        # ============================================================================
        # ADDITIONAL DIFFERENTIAL EQUATION FORMULAS (Grade 10+)
        # ============================================================================
        
        # Bernoulli Equation
        self.formulas.append(FormulaDefinition(
            "Bernoulli Equation", 
            r"dy/dx\s*+\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*=\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^\s*([a-zA-Z])", 
            r"dy/dx + P(x)y = Q(x)y^n", 
            10, "Differential Equations", "Bernoulli equation", "Differential Equations"
        ))
        
        # ============================================================================
        # ADDITIONAL SERIES FORMULAS (Grade 10+)
        # ============================================================================
        
        # Power Series
        self.formulas.append(FormulaDefinition(
            "Power Series", 
            r"sum\s*from\s*([a-zA-Z])\s*=\s*0\s*to\s*infinity\s*of\s*([a-zA-Z])\s*\*\s*([a-zA-Z])\s*\^\s*([a-zA-Z])", 
            r"Σ from n=0 to ∞ of a_n * x^n", 
            10, "Series", "Power series", "Series"
        ))
        
        # ============================================================================
        # ADDITIONAL NUMBER THEORY FORMULAS (Grade 9-10)
        # ============================================================================
        
        # Fermat's Little Theorem
        self.formulas.append(FormulaDefinition(
            "Fermat's Little Theorem", 
            r"([a-zA-Z])\s*\^\s*\(([a-zA-Z])\s*-\s*1\)\s*mod\s*([a-zA-Z])\s*=\s*1", 
            r"a^(p-1) mod p = 1", 
            10, "Number Theory", "Fermat's little theorem", "Number Theory"
        ))
        
        # ============================================================================
        # FINAL COUNT AND SUMMARY
        # ============================================================================
        
        print(f"✅ Formula Database Loaded: {len(self.formulas)} formulas")
        print(f"📚 Categories: Algebraic Identities, Trigonometry, Logarithms, Exponentials, Arithmetic, Fractions, Powers, Linear Equations, Geometry, Statistics, Probability, Sequences, Calculus, Complex Numbers, Vectors, Matrices, Polynomials, Rational Expressions, Radicals, Absolute Values, Inequalities, Functions, Limits, Differential Equations, Series, Number Theory, Hyperbolic Functions, Special Functions, Financial Math, Optimization, Conic Sections, Algebraic Techniques, Roots")
        print(f"🎯 Grades: 6-10+")
        print(f"🚀 Ready for use in FLN Math Engine!")

# Global instance
_formula_database = None

def get_formula_database() -> FormulaDatabase:
    """Get the global formula database instance"""
    global _formula_database
    if _formula_database is None:
        _formula_database = FormulaDatabase()
    return _formula_database

def get_formulas_by_grade(grade: int) -> list:
    """Get all formulas for a specific grade"""
    db = get_formula_database()
    return [f for f in db.formulas if f.grade == grade]

def search_formulas(query: str) -> list:
    """Search formulas by name, description, or topic"""
    db = get_formula_database()
    query = query.lower()
    results = []
    for formula in db.formulas:
        if (query in formula.name.lower() or 
            query in formula.description.lower() or 
            query in formula.topic.lower()):
            results.append(formula)
    return results

def get_formula_count() -> int:
    """Get the total number of formulas"""
    db = get_formula_database()
    return len(db.formulas)