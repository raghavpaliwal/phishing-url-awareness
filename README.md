# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly cybersecurity mini project developed using Python.

It analyses URLs as text and identifies common warning signs that may indicate a suspicious or phishing URL.

**Note:** This project does not open or visit any website. It only analyses the entered URL text.

## 2. Objectives

- To understand common characteristics of suspicious URLs.
- To identify possible phishing warning signs.
- To create a simple Python-based cybersecurity awareness tool.
- To promote safe internet browsing habits.

## 3. Features

The program checks for the following six warning signs:

1. Presence of the `@` symbol.
2. URL length greater than 100 characters.
3. IP address used as the hostname.
4. Five or more hostname segments.
5. Presence of punycode (`xn--`).
6. Use of HTTP instead of HTTPS.

It displays the detected warning signs and a caution message.

## 4. Technologies Used

- Programming Language: Python 3
- Module: `re`
- Module: `urllib.parse`
- Concepts: Functions, Loops, Conditional Statements and Regular Expressions.

## 5. System Requirements

- Python 3.10 or above.
- VS Code or Python IDLE.
- Windows, Linux or macOS.

No external Python packages are required.

## 6. Project Structure

```text
phishing-url-awareness/
│
├── phishing_checker.py
├── README.md
├── requirements.txt
│
├── tests/
│   └── test_samples.md
│
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## 7. How to Run the Project

1. Install Python 3.10 or above.
2. Open the project folder in VS Code or terminal.
3. Run the following command:

```bash
python phishing_checker.py
```

4. Enter a URL when prompted.
5. View the warning signs displayed by the program.
6. Enter `q` to exit the program.

## 8. Sample Run

The following URL is used for the sample run:

```text
http://login-secure.example.invalid@192.0.2.25/verify
```

Expected warning signs:

- `@` symbol detected.
- IP address hostname detected.
- HTTP instead of HTTPS detected.

The actual program output is provided in the `screenshots/sample_run.png` file.

## 9. Testing

The project contains six test cases to check different URL warning signs.

All test inputs and their expected results are documented in:

`tests/test_samples.md`

The actual test results are shown in:

`screenshots/test_results.png`

## 10. Limitations

- The program only analyses URL text.
- It does not visit or scan websites.
- It cannot confirm whether a URL is safe or malicious.
- Absence of warning signs does not guarantee that a URL is