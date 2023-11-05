import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import classes.User
import home_
import config
import jobs_
import applications_
import mail_


def test_standard_or_plus(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Patching the function to return the mock object
    mocker.patch('classes.User.User.create', return_value=mock_obj)

    # Patch get number of accounts
    mocker.patch('classes.User.User.has_room_for_new_account', return_value=True)

    # Set input
    inputs = iter(['James', 'Smith', 'USF', 'CS', 'JamesSmith', 'Password123!', 'Yes', 'N'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    accounts_.create_account()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test account is created (with plus input)
    assert "Account created successfully." in actual

def test_standard_message_friend(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Patch object attributes
    mock_obj.plus = False
    mock_obj.friends = ["TestUser"]

    # Patch object methods
    mocker.patch('classes.User.User.fetch', return_value = {
            "Username": "TestUser",
            "Password": "Password123!",
            "First Name": "John",
            "Last Name": "Smith",
            "University": "USF",
            "Major": "Computer Science",
            "Created a Profile": False,
            "Plus": False
        })
    mocker.patch('classes.User.User.send_message', return_value=True)

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['2', 'TestUser', 'Hi', 'Hello', '<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    mail_.menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test message is sent
    assert "Message sent" in actual

def test_standard_message_non_friend(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Patch object attributes
    mock_obj.plus = False
    mock_obj.friends = []

    # Patch object methods
    mocker.patch('classes.User.User.send_message', return_value=True)

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['2', 'TestUser', '<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    mail_.menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test message is not sent
    assert "Only Plus members can send messages to non-friends!" in actual

def test_plus_message_friend(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Patch object attributes
    mock_obj.plus = True
    mock_obj.friends = ["TestUser"]

    # Patch object methods
    mocker.patch('classes.User.User.fetch', return_value = {
            "Username": "TestUser",
            "Password": "Password123!",
            "First Name": "John",
            "Last Name": "Smith",
            "University": "USF",
            "Major": "Computer Science",
            "Created a Profile": False,
            "Plus": False
        })
    mocker.patch('classes.User.User.send_message', return_value=True)

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['2', 'TestUser', 'Hi', 'Hello', '<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    mail_.menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test message is sent
    assert "Message sent" in actual

def test_plus_message_non_friend(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Patch object attributes
    mock_obj.plus = True
    mock_obj.friends = []

    # Patch object methods
    mocker.patch('classes.User.User.fetch', return_value = {
            "Username": "TestUser",
            "Password": "Password123!",
            "First Name": "John",
            "Last Name": "Smith",
            "University": "USF",
            "Major": "Computer Science",
            "Created a Profile": False,
            "Plus": False
        })
    mocker.patch('classes.User.User.send_message', return_value=True)

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['2', 'TestUser', 'Hi', 'Hello', '<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    mail_.menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test message is sent
    assert "Message sent" in actual

def test_inbox(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Create mock message
    mock_message = mocker.MagicMock()
    mock_message.sender = "TestUser"
    mock_message.subject = "Hello!"
    mock_message.body = "How are you?"

    # Mock fetch all function
    mocker.patch('classes.Message.Message.fetch_all', return_value=[mock_message])

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    classes.User.User.view_inbox(mock_obj)
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test message is listed in inbox
    assert "From: TestUser | Subject: Hello!" in actual

def test_empty_inbox(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Create mock message
    mock_message = mocker.MagicMock()
    mock_message.sender = "TestUser"
    mock_message.subject = "Hello!"
    mock_message.body = "How are you?"

    # Mock fetch all function
    mocker.patch('classes.Message.Message.fetch_all', return_value=[])

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    classes.User.User.view_inbox(mock_obj)
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that there are no messages

    assert "Your inbox is empty." in actual

def test_read_message(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Create mock message
    mock_message = mocker.MagicMock()
    mock_message.sender = "TestUser"
    mock_message.subject = "Hello!"
    mock_message.body = "How are you?"

    # Set input
    inputs = iter(['N'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    classes.User.User.read_message(mock_obj, mock_message)
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that message is listed in inbox
    assert "Hello!" in actual
    assert "How are you?" in actual

def test_delete_message(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Create mock message
    mock_message = mocker.MagicMock()
    mock_message.sender = "TestUser"
    mock_message.subject = "Hello!"
    mock_message.body = "How are you?"

    # Set input
    inputs = iter(['Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    classes.User.User.read_message(mock_obj, mock_message)
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that message is deleted
    assert "Message deleted." in actual

def test_message_notification(mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Create mock message
    mock_message = mocker.MagicMock()
    mock_message.sender = "TestUser"
    mock_message.subject = "Hello!"
    mock_message.body = "How are you?"
    mock_message.is_read = False

    # Set inbox for mock object
    mock_obj.inbox = [mock_message]

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    classes.User.User.receive_notifications(mock_obj)
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that message is deleted
    assert "You have 1 unread messages!" in actual

def test_message_reply(monkeypatch, mocker):
    # Create mock object
    mock_obj = mocker.MagicMock()

    # Create mock message
    mock_message = mocker.MagicMock()
    mock_message.sender = "TestUser"
    mock_message.subject = "Hello!"
    mock_message.body = "How are you?"
    mock_message.is_read = False

    # Set inbox for mock object
    mock_obj.inbox = [mock_message]

    # Patching the user to be the object
    mocker.patch('config.user', mock_obj)

    # Set input
    inputs = iter(['1', '1', 'Y', 'Hi', '<'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    mail_.menu()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that message is deleted
    assert "Message sent!" in actual