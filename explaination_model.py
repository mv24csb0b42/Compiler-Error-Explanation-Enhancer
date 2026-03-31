"""
explanation_model.py

Generates human-readable explanations using
error message + AST context.
"""

from models.templates import (
    NAME_ERROR_TEMPLATE,
    SYNTAX_ERROR_TEMPLATE,
    TYPE_ERROR_TEMPLATE,
    GENERIC_ERROR_TEMPLATE
)

def explain_error(error, code):
    error_type = type(error).__name__

    if error_type == "NameError":
        return "The variable used is not defined. Define it before use."

    if error_type == "ZeroDivisionError":
        return "Division by zero is not allowed."

    return f"Error occurred: {error}"


def generate_explanation(error_message, ast_context):
    """
    Parameters:
        error_message (str): Compiler error string
        ast_context (dict): Extracted AST information
                            Example:
                            {
                                "error_type": "NameError",
                                "variable": "z",
                                "line": 3
                            }

    Returns:
        str: Human-readable explanation
    """

    error_message = error_message.lower()

    error_type = ast_context.get("error_type", "")
    variable = ast_context.get("variable", "")
    line = ast_context.get("line", "unknown")

    # -------- NameError --------
    if "nameerror" in error_message or error_type == "NameError":
        return NAME_ERROR_TEMPLATE.format(var=variable, line=line)

    # -------- SyntaxError --------
    elif "syntaxerror" in error_message or error_type == "SyntaxError":
        return SYNTAX_ERROR_TEMPLATE.format(line=line)

    # -------- TypeError --------
    elif "typeerror" in error_message or error_type == "TypeError":
        return TYPE_ERROR_TEMPLATE.format(line=line)

    # -------- Fallback --------
    else:
        return GENERIC_ERROR_TEMPLATE.format(line=line)

