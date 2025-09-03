"""
KRISPER + Bio_Poetica
Natural language programming and executable poetry
"""

from .krisper import KrisperCompiler, compile_text
from .bio_poetica import BioPoeticaParser, BioPoeticaCompiler
from .whitespace_intron_encoder import WhitespaceIntronEncoder
from .biopoetica_parser import parse_biopoetica
from .krisper_lowering import lower_to_krsp

__version__ = "0.2.0"
__all__ = [
    "KrisperCompiler",
    "compile_text",
    "BioPoeticaParser", 
    "BioPoeticaCompiler",
    "WhitespaceIntronEncoder",
    "parse_biopoetica",
    "lower_to_krsp"
]