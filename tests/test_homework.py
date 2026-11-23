import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_discount():
    assert calculate_discount(200, 20) == 160


# bug report 2
def test_r2_valid_age():
    assert is_valid_age(18) is True


# bug report 3
def test_r3_empty_scores():
    assert average_scores([]) == 0


# bug report 4
def test_r4_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    try:
        db.execute("CREATE TABLE users (id INTEGER, username TEXT)")
        db.execute("INSERT INTO users VALUES (1, 'admin')")
        result = find_user(db, "'; DROP TABLE users; --")
        assert result is None
    finally:
        db.close()


# bug report 5
def test_r5_path_traversal():
    import pytest
    base = "/home"
    filename = "../etc/passwd"
    with pytest.raises((ValueError, PermissionError)):
        safe_read_file(base, filename)
