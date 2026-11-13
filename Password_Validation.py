"""
Password Policy Validation
Requirements from the assignment:
- Length from 8 through 16 characters, inclusive.
- At least one uppercase letter, lowercase letter, digit,
  and special character (anything that is not a letter or digit).
"""

def validate_password(password: str) -> bool:
    if not 8 <= len(password) <= 16:
        return False

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalpha() and not ch.isdigit()
                      for ch in password)

    return has_upper and has_lower and has_digit and has_special


if __name__ == "__main__":
    test_cases = [
        ("Hello@123", True), ("Welcome1!", True),
        ("Password@123", True), ("Abcd@123", True),
        ("Test@Pass9", True), ("hello123", False),
        ("HELLO@123", False), ("Hi@1", False),
        ("password123", False), ("NoSpecial9", False),
    ]

    print("Password Validation")
    for value, expected in test_cases:
        result = validate_password(value)
        print(f"{value!r:18} -> {'ACCEPTED' if result else 'REJECTED'} "
              f"(expected {'ACCEPTED' if expected else 'REJECTED'})")
