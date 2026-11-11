import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_wrong_password():
    assert check_admin("wrongpass") is False


# bug report 2
def test_r2_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    try:
        db.execute("CREATE TABLE users (id INTEGER, username TEXT)")
        db.execute("INSERT INTO users VALUES (1, 'admin')")
        result = find_user(db, "' OR '1'='1")
        assert result is None
    finally:
        db.close()


# bug report 3
def test_r3_password_not_hardcoded():
    import inspect
    source = inspect.getsource(exercise4)
    assert 'ADMIN_PASSWORD = "admin123"' not in source
