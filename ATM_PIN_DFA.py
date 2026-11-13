"""
ATM PIN Validation using DFA
Language: all strings containing exactly four decimal digits.
States: q0, q1, q2, q3, q4 (accepting), qD (dead).
"""

def validate_pin(pin: str) -> bool:
    state = "q0"

    for ch in pin:
        if state == "qD":
            continue

        if state in {"q0", "q1", "q2", "q3"}:
            if ch.isascii() and ch.isdigit():
                state = {"q0": "q1", "q1": "q2",
                         "q2": "q3", "q3": "q4"}[state]
            else:
                state = "qD"
        elif state == "q4":  # Any extra character is invalid.
            state = "qD"

    return state == "q4"


if __name__ == "__main__":
    test_cases = [
        ("4821", True), ("1234", True), ("0000", True),
        ("9876", True), ("5555", True), ("482", False),
        ("48211", False), ("48a1", False), ("12@4", False),
        ("abcd", False),
    ]

    print("ATM PIN DFA")
    for value, expected in test_cases:
        result = validate_pin(value)
        print(f"{value!r:10} -> {'ACCEPTED' if result else 'REJECTED'} "
              f"(expected {'ACCEPTED' if expected else 'REJECTED'})")
