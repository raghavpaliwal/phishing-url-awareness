# Test Cases - Phishing URL Awareness Checker

## Test Case 1: Normal HTTPS URL

**Input:**
```text
https://www.example.com/login
```

**Expected Output:**
No listed warning signs found.

---

## Test Case 2: IP Address and HTTP

**Input:**
```text
http://192.0.2.10/account
```

**Expected Output:**
- IP address instead of a familiar domain detected.
- HTTP instead of HTTPS detected.

---

## Test Case 3: @ Symbol in URL

**Input:**
```text
http://example.com@sample.invalid/login
```

**Expected Output:**
- @ symbol detected.
- HTTP instead of HTTPS detected.

---

## Test Case 4: Multiple Hostname Segments

**Input:**
```text
https://a.b.c.d.e.example.invalid/path
```

**Expected Output:**
- Many hostname segments detected.

---

## Test Case 5: Punycode URL

**Input:**
```text
https://xn--example.invalid/
```

**Expected Output:**
- Punycode-style hostname detected.

---

## Test Case 6: Multiple Warning Signs (Sample Run)

**Input:**
```text
http://login-secure.example.invalid@192.0.2.25/verify
```

**Expected Output:**
- @ symbol detected.
- IP address hostname detected.
- HTTP instead of HTTPS detected.

**Purpose:** This test case is also used as the sample run to demonstrate the working of the project.

---

## Testing Summary

- Total Test Cases: 6
- Test Case 1–5: Individual warning-sign checks.
- Test Case 6: Multiple warning-sign check and sample run.
- Actual Status: To be verified by executing the program.

**Note:** Expected outputs are written for reference. Actual PASS/FAIL status should be recorded after running each test case.