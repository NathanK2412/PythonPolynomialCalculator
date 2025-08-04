# PythonPolynomialCalculator

How It Works
This project processes a polynomial expression by combining like terms and arranging the result in standard form (descending order of exponents). Terms are entered one at a time, and input ends when the user types "end".
Each term is parsed into its coefficient, variable group, and individual exponents. Terms with identical variable/exponent structures are combined by adding their coefficients. The resulting terms are then sorted in standard form, with variables ordered alphabetically and exponents in descending order. The final output is displayed in mathematically correct standard form.

Algorithm
The program uses a custom-built classification and sorting algorithm that represents each term as an object containing its coefficient, variables, and exponents. Variable–exponent mappings allow efficient combination of like terms, and a custom sorting routine ensures proper ordering of multi-variable expressions.
The algorithm was designed and implemented by me. ChatGPT assisted only in refining certain final steps and debugging, but the core logic, structure, and methodology are entirely my own. This project utilizes Python, object-oriented programming, and custom sorting/parsing logic.

License
This project is licensed under the MIT License. You may use, modify, and distribute it with proper credit.
