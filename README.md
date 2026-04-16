# HIT137 Software Now — Assignment 2
**Group Name:** SYDN 05

---

## 👥 Group Members

| Name | Student ID |
|------|------------|
| Ashfaq Afzal Chowdhury | S399270 |
| Mahinur Rahman | S398451 |
| Tufayel Ahmed | S397780 |
| Ahnaf Hasnain Nahiun | S400103 |

---

## 📁 Repository Structure

```
📁 repository/
├── README.md
├── question1/
│   ├── encryption.py
│   └── raw_text.txt
└── question2/
    ├── evaluator.py
    └── sample_input.txt
```

---

## ❓ Question 1 — File Encryption & Decryption

### Description
A program that reads `raw_text.txt`, encrypts its contents using a custom shift-based cipher, writes the result to `encrypted_text.txt`, decrypts it back to `decrypted_text.txt`, and verifies the decryption matches the original.

### Encryption Rules
| Character Group | Rule |
|----------------|------|
| Lowercase `a–m` | Shift **forward** by `shift1 × shift2` |
| Lowercase `n–z` | Shift **backward** by `shift1 + shift2` |
| Uppercase `A–M` | Shift **backward** by `shift1` |
| Uppercase `N–Z` | Shift **forward** by `shift2²` |
| Numbers, symbols, spaces | Unchanged |

### How to Run
1. Place `encryption.py` and `raw_text.txt` in the same folder
2. Open terminal in that folder and run:
```bash
python encryption.py
```
3. Enter shift values when prompted:
```
Enter shift1: 26
Enter shift2: 26
```

### Output Files
| File | Description |
|------|-------------|
| `encrypted_text.txt` | Encrypted version of the input |
| `decrypted_text.txt` | Decrypted version (should match original) |

### Code Structure
| Part | Contributor | Functions |
|------|-------------|-----------|
| Part 1 | Ashfaq Afzal Chowdhury | `build_encrypt_map()` |
| Part 2 | Mahinur Rahman | `build_decrypt_map()` |
| Part 3 | Tufayel Ahmed | `encrypt()`, `decrypt()` |
| Part 4 | Ahnaf Hasnain Nahiun | `verify()`, main block |

> ⚠️ **Note:** Due to the nature of the encryption rules, only specific shift value pairs produce collision-free results. Use `shift1=26, shift2=26` for guaranteed success.

---

## ❓ Question 2 — Mathematical Expression Evaluator

### Description
A program that reads mathematical expressions from a text file (one per line), evaluates each using recursive descent parsing, and writes the results to `output.txt`.

### Supported Features
- Binary operators: `+`, `-`, `*`, `/`
- Unary negation: `-5`, `--5`, `-(3+4)`
- Parentheses (nested to any depth)
- Correct operator precedence (`*` and `/` before `+` and `-`)
- Division by zero detection
- Unknown character detection (e.g. `@`)

### How to Run
1. Place `evaluator.py` and your input file in the same folder
2. Open terminal in that folder and run:
```bash
python evaluator.py
```
3. Enter the input file path when prompted:
```
Enter the path to the input file: sample_input.txt
```

### Output Format
Each expression produces a four-line block in `output.txt`:
```
Input: 3 + 5
Tree: (+ 3 5)
Tokens: [NUM:3] [OP:+] [NUM:5] [END]
Result: 8
```

### Code Structure
| Part | Contributor | Functions |
|------|-------------|-----------|
| Part 1 | Ashfaq Afzal Chowdhury | `tokenize()`, `format_tokens()` |
| Part 2 | Mahinur Rahman | `Parser` class, `tree_to_string()` |
| Part 3 | Tufayel Ahmed | `evaluate_tree()`, `format_result()`, `process_expression()` |
| Part 4 | Ahnaf Hasnain Nahiun | `evaluate_file()`, main block |

---

## ⚙️ Requirements
- Python 3.x
- No external libraries required (standard library only)

---

## 🚀 How to Clone This Repository
```bash
git clone <your-repo-url>
cd <repo-folder>
```
