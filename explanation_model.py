import re

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


# ---------------------------------------------------------
# This function is used by the GUI
# ---------------------------------------------------------
#def explain_error(error, code):
 #   """
 #   Wrapper function for GUI.
  #  Converts Python exception into the format required
   # by generate_explanation().
   # """

  #  error_type = type(error).__name__
  #  error_message = str(error)

  #  # Try to extract line number
  #  line_number = "unknown"
  #  if hasattr(error, "lineno"):
  #      line_number = error.lineno

  #  ast_context = {
  #      "error_type": error_type,
  #      "variable": "",
  #      "line": line_number
 #   }

   # return generate_explanation(error_message, ast_context)


def explain_error(error, code):
    error_type = type(error).__name__
    error_message = str(error)

    # Extract variable name (for NameError)
    variable = ""
    if error_type == "NameError":
        match = re.search(r"name '(.+?)' is not defined", error_message)
        if match:
            variable = match.group(1)

    # Extract line number
    line_number = "unknown"
    if hasattr(error, "lineno") and error.lineno:
        line_number = error.lineno
    else:
        import traceback
        tb = traceback.extract_tb(error.__traceback__)
        if tb:
            line_number = tb[-1].lineno

    ast_context = {
        "error_type": error_type,
        "variable": variable,
        "line": line_number
    }

    return generate_explanation(error_message, ast_context)