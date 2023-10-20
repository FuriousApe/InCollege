import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import connections_
import home_
import config
import requests_
import profiles_

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": False
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_create_profile(monkeypatch):
    # Set input
    inputs = iter(['7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.home()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that create a profile is listed
    assert "[6] Create a Profile" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_edit_profile(monkeypatch):
    # Set input
    inputs = iter(['7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.home()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that edit my profile is listed
    assert "[6] Edit my Profile" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_edit_profile_sections(monkeypatch):
    # Set input
    inputs = iter(['i', '<', 'e', '<', '1', '<', '2', '<', '3', '<', '<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_profile()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that everything is listed
    assert "[i] Bio" in actual
    assert "[e] Education" in actual
    assert "[1] Job 1" in actual
    assert "[2] Job 2" in actual
    assert "[3] Job 3" in actual

    # Test that correct info is listed in each section
    assert "[1] Title: 3rd Year CS Student" in actual
    assert "[1] University: Usf" in actual
    assert "[1] Title: Software Engineer" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_edit_section(monkeypatch):
    # Set input
    inputs = iter(['i', '1', "4th Year CS Student", "<", "<"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_profile()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that previous title is listed
    assert "[1] Title: 3rd Year CS Student" in actual

    # Test that new title is listed
    assert "[1] Title: 4th Year CS Student" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_create_section(monkeypatch):
    # Set input
    inputs = iter(['2', '1', "Data Scientist", "<", "<"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_profile()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that previous title is empty
    assert "[1] Title:" in actual

    # Test that new title is listed
    assert "[1] Title: Data Scientist" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.Accounts',
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
])
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_edit_major(monkeypatch):
    # Set input
    inputs = iter(['e', '2', "ComPutEr scIEnce", "<", "<"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_profile()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that previous major is empty
    assert "[2] Major:" in actual

    # Test that new major is correctly formatted
    assert "[2] Major: Computer Science" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.Accounts',
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
])
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_edit_university(monkeypatch):
    # Set input
    inputs = iter(['e', '1', "uniVERsity OF SouTh FLorida", "<", "<"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_profile()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that previous university is empty
    assert "[1] University:" in actual

    # Test that new university is correctly formatted
    assert "[1] University: University Of South" in actual
    assert "Florida" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_jobs_sections(monkeypatch):
    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_job(2)
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all sections are listed
    assert "[1] Title:" in actual
    assert "[2] Employer:" in actual
    assert "[3] Date Started:" in actual
    assert "[4] Date Ended:" in actual
    assert "[5] Location:" in actual
    assert "[6] Description:" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_education_sections(monkeypatch):
    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.edit_ed()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all sections are listed
    assert "[1] University:" in actual
    assert "[2] Major:" in actual
    assert "[3] Years Attended:" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    }
]))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_display_profile(monkeypatch):
    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    profiles_.display_profile("TestUser")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all sections are listed
    assert "|=============================" in actual
    assert "John Smith" in actual
    assert "|-----------------------------" in actual
    assert "Title : 3rd Year CS Student" in actual
    assert "|::::::::::::::::::::::::::::|" in actual
    assert "About Me : I am passionate about CS" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": True
    },
    {
        "Username": "TestUser2",
        "Password": "Password123!",
        "First Name": "Jane",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": False
    }
]))
@patch('accounts_.get_account', MagicMock(return_value=
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": True
}))
@patch('profiles_.load_profiles', MagicMock(return_value=
[
    {
        'Username': "TestUser",
        'Title': "3rd Year CS Student",
        'About Me': "I am passionate about CS",
        'University': "Usf",
        'Major': "Cs",
        'Years Attended': "3",
        'Job 1 : Title': "Software Engineer",
        'Job 1 : Employer': "Company Name",
        'Job 1 : Date Started': "June 2023",
        'Job 1 : Date Ended': "August 2023",
        'Job 1 : Location': "Tampa, FL",
        'Job 1 : Description': "Engineered software",
        'Job 2 : Title': "",
        'Job 2 : Employer': "",
        'Job 2 : Date Started': "",
        'Job 2 : Date Ended': "",
        'Job 2 : Location': "",
        'Job 2 : Description': "",
        'Job 3 : Title': "",
        'Job 3 : Employer': "",
        'Job 3 : Date Started': "",
        'Job 3 : Date Ended': "",
        'Job 3 : Location': "",
        'Job 3 : Description': ""
    }
]))
@patch('connections_.load_connections', MagicMock(return_value=
[
    {
        "Person1": "TestUser",
        "Person2": "TestUser2"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "Jane",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('config.UserProfile',
{
    'Username': "TestUser",
    'Title': "3rd Year CS Student",
    'About Me': "I am passionate about CS",
    'University': "Usf",
    'Major': "Cs",
    'Years Attended': "3",
    'Job 1 : Title': "Software Engineer",
    'Job 1 : Employer': "Company Name",
    'Job 1 : Date Started': "June 2023",
    'Job 1 : Date Ended': "August 2023",
    'Job 1 : Location': "Tampa, FL",
    'Job 1 : Description': "Engineered software",
    'Job 2 : Title': "",
    'Job 2 : Employer': "",
    'Job 2 : Date Started': "",
    'Job 2 : Date Ended': "",
    'Job 2 : Location': "",
    'Job 2 : Description': "",
    'Job 3 : Title': "",
    'Job 3 : Employer': "",
    'Job 3 : Date Started': "",
    'Job 3 : Date Ended': "",
    'Job 3 : Location': "",
    'Job 3 : Description': ""
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_display_friend_profile(monkeypatch):
    # Set input
    inputs = iter(['4', '2', '<', '<', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.home()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all sections are listed
    assert "|=============================" in actual
    assert "John Smith" in actual
    assert "|-----------------------------" in actual
    assert "Title : 3rd Year CS Student" in actual
    assert "|::::::::::::::::::::::::::::|" in actual
    assert "About Me : I am passionate about CS" in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": False
    },
    {
        "Username": "TestUser2",
        "Password": "Password123!",
        "First Name": "Jane",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": False
    }
]))
@patch('accounts_.get_account', MagicMock(return_value=
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
}))
@patch('connections_.load_connections', MagicMock(return_value=
[
    {
        "Person1": "TestUser",
        "Person2": "TestUser2"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "Jane",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_friend_no_profile(monkeypatch):
    # Set input
    inputs = iter(['4', '', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.home()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that friend is listed
    assert "[ 1 ]  TestUser" in actual

    # Test that there is not option to view profile
    assert "View Profile" not in actual

@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {
        "Username": "TestUser",
        "Password": "Password123!",
        "First Name": "John",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": False
    },
    {
        "Username": "TestUser2",
        "Password": "Password123!",
        "First Name": "Jane",
        "Last Name": "Smith",
        "University": "USF",
        "Major": "Computer Science",
        "Created a Profile": False
    }
]))
@patch('accounts_.get_account', MagicMock(return_value=
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
}))
@patch('connections_.load_connections', MagicMock(return_value=[]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "Jane",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('profiles_.save_profile', MagicMock(return_value=True))
@patch('accounts_.save_accounts', MagicMock(return_value=True))
def test_not_friends_no_profile(monkeypatch):
    # Set input
    inputs = iter(['4', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.home()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that there is not option to view profile
    assert "View Profile" not in actual

