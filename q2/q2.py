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
def evaluate_tree(node):
    """
    Recursively evaluates a parse tree node and returns the numeric result.

    Parameters:
        node (dict): a parse tree node built by the Parser

    Returns:
        float: the computed result

    Raises:
        ZeroDivisionError: if division by zero is detected
        ValueError: if an unknown node type is encountered
    """
    # Base case: number literal
    if node['type'] == 'num':
        return node['value']

    # Unary negation
    if node['type'] == 'neg':
        return -evaluate_tree(node['operand'])

    # Binary operation
    if node['type'] == 'binop':
        left  = evaluate_tree(node['left'])
        right = evaluate_tree(node['right'])
        op    = node['op']

        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right

    raise ValueError(f"Unknown node type: {node['type']}")


def format_result(value):
    """
    Formats a numeric result for output.
    - If the result is a whole number (e.g. 8.0), display without decimal (e.g. 8)
    - Otherwise, round to 4 decimal places

    Parameters:
        value (float): the computed result

    Returns:
        str: formatted result string
    """
    if value == int(value):
        return str(int(value))
    return str(round(value, 4))


def process_expression(expression):
    """
    Processes a single expression string end-to-end:
        tokenize → parse → evaluate

    Parameters:
        expression (str): one line from the input file

    Returns:
        dict with keys: 'input', 'tree', 'tokens', 'result'
        On any error, 'tree', 'tokens', and 'result' are set to "ERROR"
    """
    result = {
        'input':  expression,
        'tree':   'ERROR',
        'tokens': 'ERROR',
        'result': 'ERROR'
    }

    try:
        # Step 1: Tokenize
        tokens = tokenize(expression)
        result['tokens'] = format_tokens(tokens)

        # Step 2: Parse into tree
        parser = Parser(tokens)
        tree = parser.parse()
        result['tree'] = tree_to_string(tree)

        # Step 3: Evaluate
        value = evaluate_tree(tree)
        result['result'] = format_result(value)

    except ZeroDivisionError:
        # Division by zero — tree and tokens may already be set
        result['result'] = 'ERROR'

    except ValueError:
        # Tokenizer or parser error — reset all to ERROR
        result['tree']   = 'ERROR'
        result['tokens'] = 'ERROR'
        result['result'] = 'ERROR'

    return result



# =============================================================================
# Question 2, PART 4 - File Handling & Main Interface
# Solution by Ahnaf Hasnain Nahiun - S400103
# Reads input file, processes all expressions, writes output.txt.
# =============================================================================


def evaluate_file(input_path: str) -> list:
    """
    Reads a file of mathematical expressions (one per line), evaluates each,
    writes results to "output.txt" in the same directory, and returns a list
    of result dictionaries.

    Parameters:
        input_path (str): path to the input .txt file

    Returns:
        list[dict]: one dict per expression with keys:
                    'input', 'tree', 'tokens', 'result'
                    'result' is a float on success, or the string "ERROR"
    """
    # --- Validate input file ---
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: '{input_path}'")

    if not input_path.endswith('.txt'):
        raise ValueError(f"Input file must be a .txt file, got: '{input_path}'")

    # --- Read all lines from input file ---
    with open(input_path, 'r') as f:
        lines = f.readlines()

    # Filter out completely empty lines (keep lines with at least some content)
    expressions = [line.rstrip('\n') for line in lines if line.strip() != '']

    if not expressions:
        raise ValueError(f"Input file '{input_path}' is empty or has no expressions.")

    # --- Process each expression ---
    results = []
    for expr in expressions:
        result = process_expression(expr)
        results.append(result)

    # --- Write output.txt to same directory as input file ---
    output_dir  = os.path.dirname(os.path.abspath(input_path))
    output_path = os.path.join(output_dir, 'output.txt')

    with open(output_path, 'w') as f:
        for i, r in enumerate(results):
            f.write(f"Input: {r['input']}\n")
            f.write(f"Tree: {r['tree']}\n")
            f.write(f"Tokens: {r['tokens']}\n")
            f.write(f"Result: {r['result']}\n")
            # Blank line between blocks, but not after the last one
            if i < len(results) - 1:
                f.write("\n")

    print(f"Done! Results written to: {output_path}")

    # --- Convert result to correct return type ---
    # 'result' should be float on success, "ERROR" string on failure
    return_list = []
    for r in results:
        entry = {
            'input':  r['input'],
            'tree':   r['tree'],
            'tokens': r['tokens'],
            'result': float(r['result']) if r['result'] != 'ERROR' else 'ERROR'
        }
        return_list.append(entry)

    return return_list


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