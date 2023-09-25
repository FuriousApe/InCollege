import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import home_
import jobs_


def test_success_story():
    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.show_success_story()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    #Test that entire text is in string
    assert "When I needed to find a job" in actual
    assert "after finishing school, all of" in actual
    assert "my friends made it seem impossible" in actual
    assert "But that's when InCollege made all" in actual
    assert "the difference. Now I have my dream job," in actual
    assert "and now I know that dreams really do come true." in actual
    assert "- Jane Witherby Smith" in actual

def test_play_video(monkeypatch):
    #Set input
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.watch_video()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that video is playing
    assert "Video is now playing" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[]))
def test_find_friend_invalid(monkeypatch):

    # Set input
    inputs = iter(['John', 'Smith'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.friend_status()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that user is part of InCollege
    assert "They are not a part of the InCollege system yet." in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }]))
def test_find_friend_valid(monkeypatch):

    # Set input
    inputs = iter(['John', 'Smith'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.friend_status()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that user is part of InCollege
    assert "They are a part of the InCollege system." in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }]))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_new_account_invalid_username(monkeypatch):

    # Set input
    inputs = iter(['Test', 'User', 'TestUser', 'TestUser2', 'Password123?'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    accounts_.create_account()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that username is invalid
    assert "This username already exists. Please choose a different one." in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[]))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_new_account_invalid_password(monkeypatch):

    # Set input
    inputs = iter(['Test', 'User', 'TestUser', 'password', 'Password123?'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    accounts_.create_account()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that password is invalid
    assert "Invalid password. Requirements:" in actual


@patch('accounts_.load_accounts', MagicMock(return_value=[]))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_new_account_valid(monkeypatch):
    # Set input
    inputs = iter(['Test', 'User', 'TestUser', 'Password123?'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    accounts_.create_account()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that password is invalid
    assert "Account created successfully." in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }]))
def test_connect_invalid(monkeypatch):

    # Set input
    inputs = iter(['Jane', 'Smith'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.connect()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that user is part of InCollege
    assert "This person is not in the system yet." in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 },
                                                  {"Username": "TestUser2",
                                                   "Password": "Password123!",
                                                   "First Name": "Jane",
                                                   "Last Name": "Smith"
                                                   }
                                                  ]))
def test_connect_valid(monkeypatch):

    # Set input
    inputs = iter(['John', 'Smith'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.connect()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that user is part of InCollege
    assert "Looks like they're in the system!" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }
                                                ]))
@patch('jobs_.load_jobs', MagicMock(return_value=[{"Id": "1",
                                                 "Job Title": "Software Developer",
                                                 "Description": "Develop software",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 }
                                                ]))
@patch('jobs_.save_job', MagicMock(return_value=True))
def test_post_job_valid(monkeypatch):

    # Set input
    inputs = iter(['Software Engineer', 'Engineer software', 'Tampa', 'Company Name', '100000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.post_job("John", "Smith")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that job is posted
    assert "Your job has been posted!" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }
                                                ]))
@patch('jobs_.load_jobs', MagicMock(return_value=[{"Id": "1",
                                                 "Job Title": "Software Developer",
                                                 "Description": "Develop software",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 }
                                                ]))
@patch('jobs_.save_job', MagicMock(return_value=True))
def test_post_job_invalid(monkeypatch):

    # Set input
    inputs = iter(['Software Engineer', 'Engineer software', 'Tampa', 'Company Name', 'Not a salary', '100000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.post_job("John", "Smith")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that salary is invalid
    assert "Invalid salary - please input only numeric values." in actual

@patch('accounts_.load_accounts', MagicMock(return_value=[{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }
                                                ]))
@patch('jobs_.load_jobs', MagicMock(return_value=[{"Id": "1",
                                                 "Job Title": "Software Developer",
                                                 "Description": "Develop software",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 },
                                                 {"Id": "2",
                                                 "Job Title": "Software Developer2",
                                                 "Description": "Develop software2",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 },
                                                 {"Id": "3",
                                                 "Job Title": "Software Developer3",
                                                 "Description": "Develop software3",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 },
                                                 {"Id": "4",
                                                 "Job Title": "Software Developer4",
                                                 "Description": "Develop software4",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 },
                                                 {"Id": "5",
                                                 "Job Title": "Software Developer5",
                                                 "Description": "Develop software5",
                                                 "Location": "Tampa",
                                                 "Employer": "Company Name",
                                                 "Salary": "1000000",
                                                 "First Name": "John",
                                                 "Last Name": "Smith",
                                                 },
                                                ]))
def test_post_job_full(monkeypatch):
    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.post_job("John", "Smith")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that database is full
    assert "We're sorry. Our 'Jobs' database is currently full." in actual

