# Task 2 – Finite Automata for Real-Time Validation

This folder contains the three Python validators described in the CLA-2 report.

## Programs
- `ATM_PIN_DFA.py` – accepts exactly four decimal digits.
- `Password_Validation.py` – requires 8–16 characters and at least one uppercase letter, lowercase letter, digit, and special character.
- `Email_Validation.py` – checks the basic email-format conditions listed in the report.

## Run
Use Python 3:

```bash
python ATM_PIN_DFA.py
python Password_Validation.py
python Email_Validation.py
```

Each program includes sample test cases and prints ACCEPTED or REJECTED.

**Note:** The email program performs only the basic checks stated in the assignment; it does not verify mailbox ownership or full email-standard compliance.
