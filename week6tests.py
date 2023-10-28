import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import home_
import config
import jobs_
import applications_
import notifications_


@patch('jobs_.load_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "3",
        "Job Title": "Job3",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "4",
        "Job Title": "Job4",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "5",
        "Job Title": "Job5",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "6",
        "Job Title": "Job6",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "7",
        "Job Title": "Job7",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "8",
        "Job Title": "Job8",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "9",
        "Job Title": "Job9",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "10",
        "Job Title": "Job10",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
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
def test_num_jobs():

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.post_job("TestUser")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that job can't be created
    assert "We're sorry. Our 'Jobs' database is currently full." in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
])
@patch('applications_.is_own_job', MagicMock(return_value=True))
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
@patch('jobs_.delete_job', MagicMock(return_value=True))
def test_delete_job(monkeypatch):
    # Set input
    inputs = iter(['3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that job is deleted
    assert "Job deleted successfully." in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
])
@patch('applications_.is_own_job', MagicMock(return_value=False))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
def test_delete_job_invalid_user(monkeypatch):
    # Set input
    inputs = iter(['3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that job can't be deleted ( not an option in menu )
    assert "Invalid choice. Please enter an available option." in actual

@patch('config.User',
{
    "Username": "TestUser1",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('notifications_.load_notifications', MagicMock(return_value=
[
    {
        "TestUser1"
    }
]))
def test_deleted_job_notification(monkeypatch):
    # Set input
    inputs = iter(['6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.job_menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that job can't be deleted ( not an option in menu )
    assert "We're sorry. Jobs you applied for have been deleted since your last visit." in actual

@patch('jobs_.load_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
def test_job_list(monkeypatch):
    # Set input
    inputs = iter(['1', '<', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.job_menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all jobs are listed
    assert "Job1" in actual
    assert "Job2" in actual

@patch('jobs_.load_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
def test_job_information(monkeypatch):
    # Set input
    inputs = iter(['1', '1', '<', '<', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.job_menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all job info is listed
    assert "Job1" in actual
    assert "desc" in actual
    assert "Tampa" in actual
    assert "Company Name" in actual
    assert "100000" in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
])
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('applications_.add_job', MagicMock(return_value=True))
@patch('applications_.is_own_job', MagicMock(return_value=False))
def test_apply_for_job(monkeypatch):
    # Set input
    inputs = iter(['2', '12/08/2023', '01/01/2024', 'Because of Reasons'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all application is completed
    assert "Application completed!" in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
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
    "Created a Profile": False
})
@patch('applications_.add_job', MagicMock(return_value=True))
@patch('applications_.is_own_job', MagicMock(return_value=True))
def test_apply_for_my_job(monkeypatch):
    # Set input
    inputs = iter(['2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test warning message
    assert "You can't apply to your own job." in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
])
@patch('applications_.get_applied_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('applications_.add_job', MagicMock(return_value=True))
@patch('applications_.is_own_job', MagicMock(return_value=False))
def test_apply_for_same_job(monkeypatch):
    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that apply option not listed
    assert "[2] Apply for this Job" not in actual

@patch('jobs_.load_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('applications_.get_applied_jobs', MagicMock(return_value=
[
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
def test_applied_job_list(monkeypatch):
    # Set input
    inputs = iter(['5', '<', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.job_menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test unapplied job is not listed
    assert "Job1" not in actual

    # Test applied job is not listed
    assert "Job2" in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
])
@patch('applications_.get_saved_jobs', MagicMock(return_value=
[
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('applications_.add_job', MagicMock(return_value=True))
@patch('applications_.is_own_job', MagicMock(return_value=False))
def test_save_job(monkeypatch):
    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that save option is listed
    assert "[1] Save this Job" in actual

@patch('config.Jobs',
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
])
@patch('applications_.get_saved_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
@patch('applications_.add_job', MagicMock(return_value=True))
@patch('applications_.is_own_job', MagicMock(return_value=False))
def test_unsave_job(monkeypatch):
    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.display_job_details("Job1", "1")
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that save option is listed
    assert "[1] Unsave this Job" in actual

@patch('jobs_.load_jobs', MagicMock(return_value=
[
    {
        "Id": "1",
        "Job Title": "Job1",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    },
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('applications_.get_saved_jobs', MagicMock(return_value=
[
    {
        "Id": "2",
        "Job Title": "Job2",
        "Description": "desc",
        "Location": "Tampa",
        "Employer": "Company Name",
        "Salary": "100000",
        "Username": "TestUser"
    }
]))
@patch('config.User',
{
    "Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science",
    "Created a Profile": False
})
def test_saved_job_list(monkeypatch):
    # Set input
    inputs = iter(['4', '<', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    jobs_.job_menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test unsaved job is not listed
    assert "Job1" not in actual

    # Test saved job is listed
    assert "Job2" in actual

