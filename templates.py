"""
templates.py

Contains natural language templates for explaining compiler errors.
"""

# Template for NameError
NAME_ERROR_TEMPLATE = (
    "The variable '{var}' is used before it is defined on line {line}. "
    "You need to assign a value to '{var}' before using it."
)

# Template for SyntaxError
SYNTAX_ERROR_TEMPLATE = (
    "There is a syntax error on line {line}. "
    "Please check the structure of your statement for missing symbols or incorrect formatting."
)

# Template for TypeError
TYPE_ERROR_TEMPLATE = (
    "A type mismatch occurred on line {line}. "
    "This usually happens when incompatible data types are used together."
)

# Generic fallback template
GENERIC_ERROR_TEMPLATE = (
    "An error occurred on line {line}. "
    "Please review the code near this line for possible mistakes."
)