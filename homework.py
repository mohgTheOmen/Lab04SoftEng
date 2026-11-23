from pathlib import Path


def calculate_discount(price, discount_percent):
    """Return the price after applying a percentage discount."""
    return price - (price * discount_percent / 100)


def is_valid_age(age):
    """Return True if age is at least 18."""
    return age >= 18


def average_scores(scores):
    """Return the arithmetic mean, or 0 for an empty list."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def find_user(db, username):
    """Return the matching user row, or None if not found."""
    return db.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()


def safe_read_file(base_dir, filename):
    """Read a UTF-8 file inside base_dir; reject paths outside it."""
    base_path = Path(base_dir).resolve()
    requested_path = (base_path / filename).resolve()
    if not requested_path.relative_to(base_path):
        raise ValueError("Path traversal attempted")
    return requested_path.read_text(encoding="utf-8")
