import time
import random

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def parse_term(term_str):
    sign = 1
    i = 0
    if term_str.startswith('-'):
        sign = -1
        i += 1

    coeff_str = ''
    while i < len(term_str) and term_str[i] in digits:
        coeff_str += term_str[i]
        i += 1

    coeff = int(coeff_str) if coeff_str else 1
    coeff *= sign

    variable_map = {}
    while i < len(term_str):
        if term_str[i] in alphabet:
            var = term_str[i]
            i += 1
            if i < len(term_str) and term_str[i] == '^':
                i += 1
                exp_str = ''
                while i < len(term_str) and term_str[i] in digits:
                    exp_str += term_str[i]
                    i += 1
                exp = int(exp_str) if exp_str else 1
            else:
                exp = 1
            if var in variable_map:
                variable_map[var] += exp  
            else:
                variable_map[var] = exp
        else:
            i += 1  

    if not variable_map:
        return coeff, "Constant"

    name = ''
    for var in sorted(variable_map):
        exp = variable_map[var]
        if exp == 1:
            name += var
        else:
            name += f"{var}^{exp}"

    return coeff, name

class Term:
    def __init__(self, name, coefficient):
        self.name = name
        self.place = 0
        self.coefficient = coefficient
        self.variable_value_list = {}
        if self.name != "Constant":
            # print(f"The term is {self.name}, its coefficient is {self.coefficient}, making it formally look like {self.coefficient}{self.name}")
            pass
        else:
            # print(f"The term is a constant. It formally looks like {self.coefficient}")
            pass

    def add_vari_value(self, vari_name, vari_value):
        self.variable_value_list[vari_name] = int(vari_value)

    def print_values(self):
        return self.variable_value_list

next_number = ""
all_terms = []
variables_and_values = {}

while next_number != "end":
    next_number = input("Please send the first term in the polynomial:  ")
    if next_number != "end":
        all_terms.append(next_number)

for item in all_terms:
    coeff, name = parse_term(item)
    if name in variables_and_values:
        variables_and_values[name] += coeff
    else:
        variables_and_values[name] = coeff

# print(variables_and_values)

just_varis = list(variables_and_values.keys())
# print(just_varis)

alphabet_appearances = []
for char in "".join([v for v in just_varis if v != "Constant"]):
    if char in alphabet and char not in alphabet_appearances:
        alphabet_appearances.append(char)
if "Constant" in just_varis:
    just_varis.remove("Constant")
    just_varis.append("Constant")

classified_terms = []
count = 0
letter_count = 0

for item in just_varis:
    classified_terms.append(Term(just_varis[count], variables_and_values[just_varis[count]]))
    for letter in (char for char in just_varis[count]):
        for item in alphabet_appearances:
            if (f"{alphabet_appearances[letter_count]}^") not in just_varis[count]:
                if (f"{alphabet_appearances[letter_count]}^") not in just_varis[count] and alphabet_appearances[letter_count] not in just_varis[count]:
                    classified_terms[count].add_vari_value(alphabet_appearances[letter_count], 0)
                else:
                    classified_terms[count].add_vari_value(alphabet_appearances[letter_count], 1)
            else:
                string_split_point = f"{alphabet_appearances[letter_count]}^"
                exponent_split = just_varis[count].split(string_split_point)
                exponent_digits = ''
                for ch in exponent_split[1]:
                    if ch in digits:
                        exponent_digits += ch
                    else:
                        break
                classified_terms[count].add_vari_value(alphabet_appearances[letter_count], int(exponent_digits))
            letter_count += 1
        letter_count = 0
    count += 1

for term in classified_terms:
    # print(term.print_values())
    pass

def algebra2_sort(terms, variable_order):
    def get_main_var(term):
        for var in variable_order:
            if term.variable_value_list.get(var, 0) > 0:
                return var
        return None

    def sort_key(term):
        main_var = get_main_var(term)
        if main_var is None:
            return (len(variable_order), 0)
        return (variable_order.index(main_var), -term.variable_value_list[main_var])

    return sorted(terms, key=sort_key)

sorted_terms = algebra2_sort(classified_terms, alphabet_appearances)

polynomial = ""
for term in sorted_terms:
    if term.name == "Constant":
        polynomial += f"{term.coefficient}"
    else:
        if term.coefficient == 1:
            polynomial += f"{term.name}"
        elif term.coefficient == -1:
            polynomial += f"-{term.name}"
        else:
            polynomial += f"{term.coefficient}{term.name}"
    polynomial += " + "
polynomial = polynomial.rstrip(" + ")

print("\nFinal Polynomial:")
print(polynomial)
