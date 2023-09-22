import sys
import io
import pytest
import sqlite3
from io import StringIO
from unittest import mock

import week1


def test_username():
    # create mock account
    accounts = [{"username": "TestUser", "password": "Password123!"}]

    # Try to create account with same username
    actual = week1.create_username(accounts[0]["username"], accounts)
    expected = "This username already exists. Please choose a different one."
    assert actual == expected

def test_password():
    # Try to create account with invalid password
    actual = week1.create_password("password")
    expected = "Invalid password"
    assert actual == expected

    # Try to create account with valid password
    actual = week1.create_password("Password123!")
    expected = "Valid password"
    assert actual == expected

def test_num_accounts():
    # Mock 5 accounts:
    accounts = [{"username": "TestUser1", "password": "Password123!"},
                {"username": "TestUser2", "password": "Password123!"},
                {"username": "TestUser3", "password": "Password123!"},
                {"username": "TestUser4", "password": "Password123!"},
                {"username": "TestUser5", "password": "Password123!"}]

    # Check number of accounts
    actual = week1.check_num_accounts(accounts)
    expected = "All permitted accounts have been created, please come back later."
    assert actual == expected

    # Mock 1 account:
    accounts = [{"username": "TestUser", "password": "Password123!"}]

    # Check number of accounts
    actual = week1.check_num_accounts(accounts)
    expected = "Account slots available."
    assert actual == expected

def test_valid_credentials():
    # create mock account
    accounts = [{"username": "TestUser", "password": "Password123!"}]

    actual = week1.validate_credentials("TestUser", "Password123!", accounts)
    expected = "You have successfully logged in."
    assert actual == expected

def test_invalid_credentials():
    # create mock account
    accounts = [{"username": "TestUser", "password": "Password123!"}]

    actual = week1.validate_credentials("TestUser", "Password123?", accounts)
    expected = "Incorrect username/password, please try again."
    assert actual == expected

def test_search_job():
    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.search_job()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected

def test_find_someone():
    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.find_someone()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected

def test_learn_skill():
    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.time_management()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.communication()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.networking()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.team_building()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    week1.organization()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")
    expected = "Under construction"
    assert actual == expected


