import io
import sys

import pytest
from mock import patch, MagicMock

import accounts_
import home_
import jobs_
import policies_


def test_important_links(monkeypatch):
    # Set input
    inputs = iter(['<', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that links are listed
    assert "Copyright Notice" in actual
    assert "About" in actual
    assert "Accessibility" in actual
    assert "User Agreement" in actual
    assert "Privacy Policy" in actual
    assert "Cookie Policy" in actual
    assert "Copyright Policy" in actual
    assert "Brand Policy" in actual

def test_useful_links(monkeypatch):
    # Set input
    inputs = iter(['>', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that links are listed
    assert "General" in actual
    assert "Browse InCollege" in actual
    assert "Business Solutions" in actual
    assert "Directories" in actual

def test_general(monkeypatch):
    # Set input
    inputs = iter(['>', 'a', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that links are listed
    assert "Help Center" in actual
    assert "About" in actual
    assert "Press" in actual
    assert "Blog" in actual
    assert "Careers" in actual
    assert "Developers" in actual

def test_about_link(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.about()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test that about information is listed
    assert "InCollege is the largest college student network" in actual
    assert "in the world. Our mission and purpose is to help" in actual
    assert "newcomers to the professional workplace as they" in actual
    assert "prepare to begin their careers." in actual
    assert "We help students find jobs without the stress of" in actual
    assert "competing against seasoned professionals. If a" in actual
    assert "student needs help getting connected, they can" in actual
    assert "come to InCollege, where we level the playing field." in actual

def test_help_center(monkeypatch):
    # Set input
    inputs = iter(['a', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_general()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test help message
    assert "We're here to help." in actual

def test_about_general(monkeypatch):
    # Set input
    inputs = iter(['b', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_general()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test about message
    assert "The world's largest college student network" in actual
    assert "with many users in many countries and territories worldwide." in actual

def test_press(monkeypatch):
    # Set input
    inputs = iter(['c', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_general()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test press message
    assert "InCollege Pressroom:" in actual
    assert "Stay on top of the latest news, updates, and reports." in actual

def test_blog(monkeypatch):
    # Set input
    inputs = iter(['d', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_general()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test blog message
    assert "UNDER CONSTRUCTION" in actual

def test_careers(monkeypatch):
    # Set input
    inputs = iter(['e', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_general()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test careers message
    assert "UNDER CONSTRUCTION" in actual

def test_developers(monkeypatch):
    # Set input
    inputs = iter(['f', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_general()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test developers message
    assert "UNDER CONSTRUCTION" in actual

def test_browse_incollege(monkeypatch):
    # Set input
    inputs = iter(['b', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_useful()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test browse incollege message
    assert "UNDER CONSTRUCTION" in actual

def test_business_solutions(monkeypatch):
    # Set input
    inputs = iter(['c', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_useful()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test businesss solutions message
    assert "UNDER CONSTRUCTION" in actual

def test_directories(monkeypatch):
    # Set input
    inputs = iter(['d', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    home_.linkster_useful()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test directories message
    assert "UNDER CONSTRUCTION" in actual

def test_copyright_notice(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.notice()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test copyright notice message
    assert "(C) 2023 Team Colorado. All rights reserved." in actual
    assert "InCollege, the InCollege Logo and InCollege apps" in actual
    assert "are trademarks of Team Colorado Inc." in actual

def test_accessibility(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.accessibility()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test accessibility message
    assert "InCollege, and the Team Colorado group, are" in actual
    assert "dedicated to providing accessible content and" in actual
    assert "services." in actual
    assert "Contact us at support@InCollege.com if you have" in actual
    assert "questions, comments, or concerns." in actual

def test_user_agreement(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.user_agreement()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test user agreement message
    assert "InCollege and its affiliates are responsible" in actual
    assert "for maintaining confidentiality and discretion" in actual
    assert "when collecting personal information from" in actual
    assert "from its users." in actual
    assert "By using the InCollege app and accepting its" in actual
    assert "services, you hereby agree to comply with our" in actual
    assert "policies and all applicable rules and regulations." in actual

def test_cookie_policy(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.cookies()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test cookie policy message
    assert "InCollege may, at any point in time, resort to" in actual
    assert "the use of cookies or other forms of digital" in actual
    assert "tracking when you use our app or visit our site." in actual
    assert "The use of the aforementioned tracking is to" in actual
    assert "improve our user experience and better our services." in actual
    assert "We reserve the right to alter this policy at any" in actual
    assert "given time or for any given reason. We agree to" in actual
    assert "notify you of any changes made via this page." in actual

def test_copyright_policy(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.copy_right()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test copyright policy message
    assert "At InCollege, as well as the entire Team Colorado" in actual
    assert "group and all its affiliates, present and future," in actual
    assert "respect the rights of others, including those that" in actual
    assert "pertain to intellectual property." in actual
    assert "This application obeys the standards laid out by" in actual
    assert "the Digital Millennium Copyright Act of 1998." in actual
    assert "We also expect any and all users to conduct" in actual
    assert "themselves in the same manner. Infringing on the" in actual
    assert "rights of others will result in the immediate" in actual
    assert "termination of said user's account and the" in actual
    assert "notification of a DMCA Registered Agent." in actual

def test_brand_policy(monkeypatch):
    # Set input
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Get output from console and run function
    output = io.StringIO()
    sys.stdout = output
    policies_.brand()
    sys.stdout = sys.__stdout__

    actual = output.getvalue().replace("\n", "")

    # Test brand policy message
    assert "It is the policy of the entire InCollege team" in actual
    assert "to help ensure the betterment of college students" in actual
    assert "across the globe, as well as the solidification" in actual
    assert "of their professional future." in actual
    assert "By helping students to connect with one another," in actual
    assert "and with professional peers, we hope to see a" in actual
    assert "far greater number of recent college graduates" in actual
    assert "secure the life that they, and their loved ones," in actual
    assert "hope they might one day achieve." in actual
