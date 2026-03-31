import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from explanation_model import generate_explanation


def main():
    # Example compiler error
    error_message = "NameError: name 'z' is not defined"

    # Example AST context (normally comes from ast_extractor)
    ast_context = {
        "error_type": "NameError",
        "variable": "z",
        "line": 3
    }

    explanation = generate_explanation(error_message, ast_context)

    print("\n--- Compiler Error ---")
    print(error_message)

    print("\n--- Generated Explanation ---")
    print(explanation)


if __name__ == "__main__":
    main()
