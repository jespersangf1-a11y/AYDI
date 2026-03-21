"""Custom error types for AYDI backend.

Provides a hierarchy of domain-specific exceptions for handling various
failure modes: data validation, module analysis, visual/AI analysis,
and CAD file import.
"""


class AYDIError(Exception):
    """Base error class for all AYDI domain exceptions."""
    pass


class ModuleAnalysisError(AYDIError):
    """Raised when an analysis module fails during execution."""
    pass


class DataValidationError(AYDIError):
    """Raised when input data fails validation requirements."""
    pass


class VisualAnalysisError(AYDIError):
    """Raised when visual or AI-based analysis fails."""
    pass


class CADImportError(AYDIError):
    """Raised when CAD file import or parsing fails."""
    pass
