# Group Name: SYDN 05 | HIT 137 Software Now | Assignment 2
##########################################################
# Group Members:
# Ashfaq Afzal Chowdhury - S399270
# Mahinur Rahman - S398451
# Tufayel Ahmed - S397780
# Ahnaf Hasnain Nahiun - S400103


# =============================================================================
# Question 2 - Mathematical Expression Evaluator
# =============================================================================
# Reads mathematical expressions from a text file (one per line), evaluates
# each expression using recursive descent parsing, and writes results to
# "output.txt" in the same directory as the input file.
#
# Each expression produces a four-line block:
#   Input:  the original expression
#   Tree:   the parse tree in prefix notation, or ERROR
#   Tokens: the list of tokens, or ERROR
#   Result: the computed value, or ERROR
#
# Supported:
#   - Binary operators: +, -, *, /
#   - Unary negation: -5, --5, -(3+4)
#   - Parentheses (nested to any depth)
#   - Operator precedence: * and / before + and -
#
# Not supported:
#   - Unary + (produces ERROR)
#   - Unknown characters like @ (produces ERROR)
#   - Division by zero (produces ERROR)
# =============================================================================


import os


# =============================================================================
# Question 1, PART 1 - Tokenizer 
# Solution by Ashfaq Afzal Chowdhury - S399270
# Breaks a raw expression string into a list of tokens.
# =============================================================================

def tokenize(expression):
    """
    Converts a raw expression string into a list of token dictionaries.
    Each token has a 'type' and a 'value'.

    Token types:
        NUM    - a numeric literal (integer or decimal)
        OP     - an operator: +, -, *, /
        LPAREN - opening parenthesis (
        RPAREN - closing parenthesis )
        END    - signals the end of the token stream

    Parameters:
        expression (str): the raw math expression string

    Returns:
        list of dicts: e.g. [{'type':'NUM','value':3}, {'type':'OP','value':'+'}, ...]

    Raises:
        ValueError: if an unknown character is encountered
    """
    tokens = []
    i = 0

    while i < len(expression):
        ch = expression[i]

        # Skip whitespace
        if ch == ' ' or ch == '\t':
            i += 1
            continue

        # Numeric literal (integer or float)
        if ch.isdigit() or (ch == '.' and i + 1 < len(expression) and expression[i+1].isdigit()):
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            tokens.append({'type': 'NUM', 'value': float(expression[i:j])})
            i = j
            continue

        # Operators
        if ch in ('+', '-', '*', '/'):
            tokens.append({'type': 'OP', 'value': ch})
            i += 1
            continue

        # Parentheses
        if ch == '(':
            tokens.append({'type': 'LPAREN', 'value': '('})
            i += 1
            continue

        if ch == ')':
            tokens.append({'type': 'RPAREN', 'value': ')'})
            i += 1
            continue

        # Unknown character — raise error
        raise ValueError(f"Unknown character: '{ch}'")

    # Always append END token to signal end of input
    tokens.append({'type': 'END', 'value': 'END'})
    return tokens


def format_tokens(tokens):
    """
    Formats a list of token dicts into a display string.
    Example: [NUM:3] [OP:+] [NUM:5] [END]

    Parameters:
        tokens (list): list of token dicts from tokenize()

    Returns:
        str: formatted token string
    """
    parts = []
    for tok in tokens:
        if tok['type'] == 'NUM':
            # Display as integer if whole number, else as float
            val = tok['value']
            display = str(int(val)) if val == int(val) else str(val)
            parts.append(f"[NUM:{display}]")
        elif tok['type'] == 'END':
            parts.append("[END]")
        else:
            parts.append(f"[{tok['type']}:{tok['value']}]")
    return ' '.join(parts)


# =============================================================================
# Question 2, PART 2 - Parser 
# Solution by Mahinur Rahman - S398451
# Builds a parse tree using recursive descent parsing.
# Each node is a dict: {'type': ..., ...}
# =============================================================================


# =============================================================================
# Question 2, PART 3 - Evaluator
# Solution by Tufayel Ahmed - S397780
# Walks the parse tree and computes the numeric result.
# =============================================================================



# =============================================================================
# Question 2, PART 4 - File Handling & Main Interface
# Solution by Ahnaf Hasnain Nahiun - S400103
# Reads input file, processes all expressions, writes output.txt.
# =============================================================================





# =============================================================================
# Main Entry Point
# =============================================================================
if __name__ == "__main__":
    input_path = input("Enter the path to the input file: ").strip()
    try:
        results = evaluate_file(input_path)
        print(f"\nProcessed {len(results)} expression(s):\n")
        for r in results:
            print(f"  Input:  {r['input']}")
            print(f"  Result: {r['result']}")
            print()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")