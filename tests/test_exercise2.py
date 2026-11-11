import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_boundary():
    assert is_passing(5) is True


# bug report 2
def test_r2_valid_password_minimum_length():
    assert is_valid_password("pass123") is False


# bug report 3
def test_r3_clamp_low_bound_bug():
    assert clamp(10, 1, 10) == 10
