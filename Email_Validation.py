"""
Basic Email Format Validation
Implements the assignment's stated checks:
- Exactly one @ symbol.
- Non-empty username and domain.
- Domain contains a dot.
- Domain does not start or end with a dot.
- No spaces or consecutive dots.
This is a basic format checker, not full email-standard validation.
"""

def validate_email(email: str) -> bool:
    if not email or any(ch.isspace() for ch in email):
        return False

    if email.count("@") != 1 or ".." in email:
        return False

    username, domain = email.split("@")
    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


if __name__ == "__main__":
    test_cases = [
        ("student@gmail.com", True),
        ("vaishnavi@srm.edu", True),
        ("hello@yahoo.com", True),
        ("user123@outlook.com", True),
        ("name.test@gmail.com", True),
        ("studentgmail.com", False),
        ("student@", False),
        ("@gmail.com", False),
        ("hello gmail.com", False),
        ("user@gmail", False),
    ]

    print("Email Format Validation")
    for value, expected in test_cases:
        result = validate_email(value)
        print(f"{value!r:28} -> {'ACCEPTED' if result else 'REJECTED'} "
              f"(expected {'ACCEPTED' if expected else 'REJECTED'})")
