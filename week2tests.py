import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import home_

#

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
