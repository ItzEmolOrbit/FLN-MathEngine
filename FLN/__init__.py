"""
FLN Math Engine - A lightweight, blazing-fast math engine
with automatic formula detection and step-by-step computation.
"""

from .engine import MathEngine
from .ast_nodes import ASTNode, NumberNode, VariableNode, OperatorNode, FunctionNode
from .data_structures import EvaluationResult, ComputationStep, FormulaMatch, EvaluationType
from .tokenizer import Tokenizer, Token, TokenType
from .parser import Parser
from .folex import Folex
from .natix import Natix
from .monitor import ComputationMonitor
from .cache import ExpressionCache, LazyEvaluator, get_global_cache, get_cache_stats
from .formula_database import FormulaDatabase, get_formula_database, get_formulas_by_grade, search_formulas, get_formula_count

__version__ = "1.0.0"
__author__ = "KrythFoundation"

__all__ = [
    "MathEngine",
    "ASTNode",
    "NumberNode",
    "VariableNode",
    "OperatorNode",
    "FunctionNode",
    "EvaluationResult",
    "ComputationStep",
    "FormulaMatch",
    "EvaluationType",
    "Tokenizer",
    "Token",
    "TokenType",
    "Parser",
    "Folex",
    "Natix",
    "ComputationMonitor",
    "ExpressionCache",
    "LazyEvaluator",
    "get_global_cache",
    "get_cache_stats",
    "FormulaDatabase",
    "get_formula_database",
    "get_formulas_by_grade",
    "search_formulas",
    "get_formula_count"
]

