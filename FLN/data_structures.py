from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Union
from enum import Enum


class EvaluationType(Enum):
    NUMERIC = "numeric"
    SYMBOLIC = "symbolic"
    MIXED = "mixed"


@dataclass
class FormulaMatch:
    formula_name: str
    pattern: str
    matched_expression: str
    variables: Dict[str, str]
    confidence: float = 1.0


@dataclass
class ComputationStep:
    step_number: int
    expression: str
    result: str
    operation: str
    applied_formulas: List[FormulaMatch] = field(default_factory=list)
    is_numeric: bool = False
    explanation: Optional[str] = None


@dataclass
class EvaluationResult:
    original_expression: str
    final_result: str
    evaluation_type: EvaluationType
    applied_formulas: List[FormulaMatch] = field(default_factory=list)
    computation_steps: List[ComputationStep] = field(default_factory=list)
    is_exact: bool = True
    error_message: Optional[str] = None


@dataclass
class FormulaDefinition:
    name: str
    pattern: str
    replacement: str
    grade: int
    category: str = "General"
    description: str = ""
    topic: str = ""


@dataclass
class ParsingContext:
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    line_number: int = 1
    column_number: int = 1
