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

# Additional Error Templates

INDEX_ERROR_TEMPLATE = (
    "You are trying to access an index that is out of range on line {line}. "
    "Make sure the index exists in the list."
)

KEY_ERROR_TEMPLATE = (
    "The key you are trying to access does not exist in the dictionary on line {line}."
)

ATTRIBUTE_ERROR_TEMPLATE = (
    "The object does not have the attribute or method you are trying to use on line {line}."
)

VALUE_ERROR_TEMPLATE = (
    "An invalid value is used in an operation on line {line}."
)

IMPORT_ERROR_TEMPLATE = (
    "The module you are trying to import cannot be found on line {line}."
)

FILE_NOT_FOUND_TEMPLATE = (
    "The file you are trying to access does not exist on line {line}."
)

ZERO_DIVISION_TEMPLATE = (
    "Division by zero is not allowed on line {line}."
)

INDENTATION_ERROR_TEMPLATE = (
    "There is an indentation issue in your code on line {line}. Check spacing and alignment."
)

MODULE_NOT_FOUND_TEMPLATE = (
    "The specified module could not be found on line {line}."
)

OVERFLOW_ERROR_TEMPLATE = (
    "A numerical operation exceeded the allowed limit on line {line}."
)