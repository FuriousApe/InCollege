import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import connections_
import home_
import config
import requests_


@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser4",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser5",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser6",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser7",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser8",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser9",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser10",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
]))
def test_num_accounts():

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    accounts_.create_account()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that account can't be created
    assert "All permitted accounts have been created, please come back later." in actual


@patch('config.User', {"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 })
@patch('connections_.load_connections', MagicMock(return_value=[]))
@patch('connections_.save_connection', MagicMock(return_value=True))
def test_empty_friends_list():

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    connections_.view_connections()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that there are no connections
    assert "You currently have no connections." in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "USF",
    "Major": "Computer Science"
    }
]))
def test_search_last_name(monkeypatch):
    # Set input
    inputs = iter(['Doe', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.search_lname()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that correct user is printed
    assert "John Doe" in actual

    # Test that other user is not printed
    assert "John Johnson" not in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "UF",
    "Major": "Computer Science"
    }
]))
def test_search_university(monkeypatch):
    # Set input
    inputs = iter(['USF', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.search_university()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that correct user is printed
    assert "John Doe" in actual

    # Test that other user is not printed
    assert "John Johnson" not in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "USF",
    "Major": "Marketing"
    }
]))
def test_search_major(monkeypatch):
    # Set input
    inputs = iter(['Computer Science', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.search_major()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that correct user is printed
    assert "John Doe" in actual

    # Test that other user is not printed
    assert "John Johnson" not in actual


@patch('config.Accounts', [{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 },
                                                 {"Username": "TestUser2",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }
                                                ])
@patch('config.User', {"Username": "TestUser2",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 })
@patch('config.Connections', [])
@patch('requests_.load_requests', MagicMock(return_value=[{
    "Requester": "TestUser",
    "Recipient": "TestUser2"
}]))
@patch('connections_.save_connection', MagicMock(return_value=True))
def test_accept_connection_request(monkeypatch):
    # Set input
    inputs = iter(['1', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    requests_.view_requests()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test request is listed
    assert "TestUser" in actual

    # Test that request is sent
    assert "TestUser is now a connection!" in actual

@patch('config.Accounts', [{"Username": "TestUser",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 },
                                                 {"Username": "TestUser2",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 }
                                                ])
@patch('config.User', {"Username": "TestUser2",
                                                 "Password": "Password123!",
                                                 "First Name": "John",
                                                 "Last Name": "Smith"
                                                 })
@patch('config.Connections', [])
@patch('requests_.load_requests', MagicMock(return_value=[{
    "Requester": "TestUser",
    "Recipient": "TestUser2"
}]))
@patch('connections_.save_connection', MagicMock(return_value=True))
def test_reject_connection_request(monkeypatch):
    # Set input
    inputs = iter(['1', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    requests_.view_requests()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test request is listed
    assert "TestUser" in actual

    # Test that request is deleted
    assert "Request is deleted!" in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
]))
def test_send_connection_request(monkeypatch):
    # Set input
    inputs = iter(['Doe', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.search_lname()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that request is sent
    assert "Connection request made!" in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "USF",
    "Major": "Computer Science"
    }
]))
@patch('requests_.load_requests', MagicMock(return_value=
[
    {
        "Requester": "TestUser2",
        "Recipient": "TestUser"
    },
    {
        "Requester": "TestUser3",
        "Recipient": "TestUser"
    }
]))
def test_view_incoming_requests(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    requests_.view_requests()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that all requests are listed
    assert "TestUser2" in actual
    assert "TestUser3" in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "USF",
    "Major": "Computer Science"
    }
]))
@patch('requests_.load_requests', MagicMock(return_value=
[]))
def test_view_incoming_requests_none(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    requests_.view_requests()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that no requests are listed
    assert "You have no incoming connection requests." in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "USF",
    "Major": "Computer Science"
    }
]))
@patch('connections_.load_connections', MagicMock(return_value=
[
    {
        "Person1": "TestUser",
        "Person2": "TestUser2"
    },
    {
        "Person1": "TestUser3",
        "Person2": "TestUser"
    }
]))
@patch('connections_.delete_connection', MagicMock(return_value=True))
def test_view_connections(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    connections_.view_connections()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test all users are listed
    assert "TestUser2" in actual
    assert "TestUser3" in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser3",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Johnson",
    "University": "USF",
    "Major": "Computer Science"
    }
]))
@patch('connections_.load_connections', MagicMock(return_value=
[
    {
        "Person1": "TestUser",
        "Person2": "TestUser2"
    },
    {
        "Person1": "TestUser3",
        "Person2": "TestUser"
    }
]))
@patch('connections_.delete_connection', MagicMock(return_value=True))
def test_view_connections(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    connections_.view_connections()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test all users are listed
    assert "TestUser2" in actual
    assert "TestUser3" in actual

@patch('config.User',
{
    "Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith"
})
@patch('accounts_.load_accounts', MagicMock(return_value=
[
    {"Username": "TestUser",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Smith",
    "University": "USF",
    "Major": "Computer Science"
    },
    {"Username": "TestUser2",
    "Password": "Password123!",
    "First Name": "John",
    "Last Name": "Doe",
    "University": "USF",
    "Major": "Computer Science"
    },
]))
@patch('connections_.load_connections', MagicMock(return_value=
[
    {
        "Person1": "TestUser",
        "Person2": "TestUser2"
    }
]))
@patch('connections_.delete_connection', MagicMock(return_value=True))
def test_delete_connection(monkeypatch):
    # Set input
    inputs = iter(['1', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    connections_.view_connections()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that connection is deleted
    assert "Connection is deleted!" in actual
