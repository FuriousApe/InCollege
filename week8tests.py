import io
import sys

import pytest
from mock import patch, MagicMock
from datetime import datetime, timedelta

import accounts_
import classes.User
import home_
import config
import jobs_
import applications_
import mail_


def test_apply_for_jobs_notification_true(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=True)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is listed
    assert "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!" in concatenated_string

def test_apply_for_jobs_notification_false(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!" not in concatenated_string

def test_create_profile_notification_true(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = False

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is listed
    assert "Don't forget to create a profile" in concatenated_string

def test_create_profile_notification_false(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "Don't forget to create a profile" not in concatenated_string

def test_inbox_notification_true(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=["Message"])
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is listed
    assert "You have messages waiting for you" in concatenated_string

def test_inbox_notification_false(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "You have messages waiting for you" not in concatenated_string

def test_new_user_notification_true(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Mock New User
    mock_user = mocker.MagicMock()
    mock_user.first_name = "John"
    mock_user.last_name = "Smith"

    new_users = [mock_user]

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=new_users)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is listed
    assert "John Smith has joined InCollege" in concatenated_string

def test_new_user_notification_false(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=None)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "has joined InCollege" not in concatenated_string

def test_job_applications_notification_true(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Mock applications
    mock_applications = ['1', '2', '3']

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=mock_applications)
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "You have currently applied for 3 jobs" in concatenated_string

def test_job_applications_notification_false(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mocker.patch('classes.User.User.new_jobs_since_login', return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=[])
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "You have currently applied for 3 jobs" not in concatenated_string

def test_new_job_notification_true(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Mock New Job
    mock_job = mocker.MagicMock()
    mock_job.job_title = "Software Engineer"

    jobs = [mock_job]

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mock_user.new_jobs_since_login = MagicMock(return_value=jobs)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=[])
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "A new job Software Engineer has been posted." in concatenated_string

def test_new_job_notification_false(mocker):
    # Create mock user
    mock_user = mocker.MagicMock()
    mock_user.created_a_profile = True

    # Patching other user functions
    mock_user.been_week_since_last_app = MagicMock(return_value=False)
    mock_user.new_users_since_login = MagicMock(return_value=False)
    mock_user.new_jobs_since_login = MagicMock(return_value=False)
    mocker.patch('classes.Message.Message.fetch_all', return_value=False)
    mocker.patch('classes.Application.Application.get_apps_from', return_value=[])
    mocker.patch('classes.Notification.Notification.create', return_value=False)

    # Test Function
    value = classes.User.User.create_all_notifications(mock_user)

    # Make return value a string
    keys_list = list(value.keys())
    concatenated_string = ''.join(keys_list)

    # Test that notification is not listed
    assert "A new job has been posted." not in concatenated_string

def test_delete_job_notification(mocker):
    # Create mock job
    mock_job = mocker.MagicMock()
    mock_job.username = "TestUser"
    mock_job.job_id = -1
    mock_job.notify_users_about_deletion = MagicMock(return_value=True)

    # Mock Obj
    mock_obj = mocker.MagicMock()
    mock_obj.execute = MagicMock(return_value=True)
    mock_obj.commit = MagicMock(return_value=True)


    # Patching other user functions
    mocker.patch('data_.connect_to_database', return_value=(mock_obj, mock_obj))

    # Test Function
    value = classes.JobPost.JobPost.delete(mock_job, "TestUser")

    # Assert notification function is called
    mock_job.notify_users_about_deletion.assert_called_once()

