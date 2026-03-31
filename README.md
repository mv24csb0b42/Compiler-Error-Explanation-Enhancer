# Compiler Error Explanation System using AST and NLP

## 📌 Project Overview

This project enhances traditional Python compiler error messages by generating beginner-friendly explanations.

It combines:

* Abstract Syntax Tree (AST) analysis
* Lightweight Natural Language Processing (NLP)
* Structured error parsing

The system transforms technical compiler errors into human-readable explanations suitable for students and beginners.

---

## 🎯 Problem Statement

Standard compiler errors are often:

* Short and technical
* Difficult for beginners to understand
* Lacking contextual explanation

Example:

```
NameError: name 'z' is not defined
```

This message does not clearly explain:

* Why the error occurred
* Where the issue originated
* How to fix it

---

## 💡 Proposed Solution

The system performs the following steps:

1. Captures compiler error message
2. Extracts syntactic context using AST
3. Processes structured error information
4. Generates a natural language explanation using NLP templates

---

## 🛠 Technologies Used

* Python 3.x
* AST module
* Regular Expressions
* Rule-based NLP templates
* Virtual Environment (venv)

---

## 📂 Project Structure

```
CDProject/
│
├── main.py
├── explanation_model.py
├── models/
│   ├── templates.py
│   └── explanation_model.py (if modular version used)
│
├── data/
├── docs/
├── scripts/
├── venv/
└── README.txt
```

---

## ▶ How to Run the Project

### Step 1: Open Command Prompt

Navigate to project directory:

```
cd C:\Users\manne\OneDrive\Desktop\CDProject_24csb0b42_Mvenkatkoushik
```

### Step 2: Activate Virtual Environment

```
venv\Scripts\activate
```

### Step 3: Run the Program

```
python main.py
```

---

## 📌 Sample Output

### Compiler Error:

```
NameError: name 'z' is not defined
```

### Generated Explanation:

```
The variable 'z' is used before it is defined on line 3. 
You need to assign a value to 'z' before using it.
```

---

## 🔍 Supported Error Types

* NameError
* SyntaxError
* TypeError
* Generic fallback error

---

## 🧠 Key Features

* Modular design
* Dynamic explanation generation
* Beginner-friendly output
* Extendable to more error types
* Command-line executable

---

## 🚀 Future Improvements

* Automatic variable extraction from error message
* Support for additional error types
* Integration with real-time code editors
* Machine learning-based explanation generation

---

## 📎 Conclusion

This project demonstrates how compiler errors can be enhanced using AST-based structural analysis and NLP-based explanation generation to improve student understanding and debugging efficiency.

---


##Entire Flow (Very Important for Viva)

User Code
   ↓
Program Execution
   ↓
Exception Captured
   ↓
AST Parsing
   ↓
Variable Usage Analysis
   ↓
Error Context Extracted
   ↓
NLP Template Applied
   ↓
Human-Friendly Explanation

Key Idea To Must Remember

AST answers:

"What is happening in the structure of the program?"

NLP answers:

"How do we explain this clearly in English?"

One-Line Summary for Demo

You can say this confidently:

“AST is used to analyze the structure of the Python code and identify how variables are used, while NLP templates convert that structured information into beginner-friendly explanations.”

Q: Is this NLP?

Answer:

It uses rule-based Natural Language Generation, not machine learning NLP.

##Most Impactful Improvements, upcoming these 3:

1️⃣ Support more error types
2️⃣ Improve explanation structure
3️⃣ Add a simple GUI interface


