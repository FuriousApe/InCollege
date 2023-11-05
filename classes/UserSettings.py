import sqlite3
import config
from data_ import connect_to_database

class UserSettings:

    def __init__(self, username, language, email_on, sms_on, ads_on):

        self.username = username
        self.language = language
        self.email_on = email_on
        self.sms_on = sms_on
        self.ads_on = ads_on

    @classmethod
    def fetch(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return None

        try:
            cursor.execute('SELECT language, email_on, sms_on, ads_on FROM settings WHERE username = ?', (username,))
            data = cursor.fetchone()
            if data:
                return cls(username, *data)

        except sqlite3.Error as err:
            print(f"There was an error fetching settings for user '{username}': ", err)

        finally:
            if connection: connection.close()

        return None

    @classmethod
    def save(cls, username, **settings):

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            # Assuming you validate settings keys and values beforehand
            cursor.execute('''
                UPDATE settings
                SET language = ?, email_on = ?, sms_on = ?, ads_on = ?
                WHERE username = ?
            ''', (settings['language'], settings['email_on'], settings['sms_on'], settings['ads_on'], username))
            connection.commit()

        except sqlite3.Error as err:
            print(f"There was an error updating settings for '{username}': ", err)
            return False

        finally:
            if connection: connection.close()

        return True

    @classmethod
    def initialize_settings_for(cls, username):

        default_language = "English"
        default_email_on = True
        default_sms_on = True
        default_ads_on = True

        connection, cursor = connect_to_database()
        if connection is None: return False

        try:
            cursor.execute('''
                INSERT INTO settings (username, language, email_on, sms_on, ads_on)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, default_language, default_email_on, default_sms_on, default_ads_on))
            connection.commit()

        except sqlite3.Error as err:
            print(f"There was an error creating default settings for '{username}': ", err)
            return False

        finally:
            if connection: connection.close()

        return True

    @classmethod
    def toggle_setting_for(cls, username, setting):

        connection, cursor = connect_to_database()
        if connection is None: return False

        new_value = None

        try:
            # Get current setting value
            cursor.execute(f'SELECT {setting} FROM settings WHERE username = ?', (username,))
            current_value = cursor.fetchone()
            if current_value is None:
                raise ValueError(f"No settings found for user {username}")

            # Toggle the value
            new_value = not current_value[0]
            cursor.execute(f'UPDATE settings SET {setting} = ? WHERE username = ?', (new_value, username))
            connection.commit()

        except sqlite3.Error as err:
            print(f"There was an error toggling '{setting}' for '{username}': ", err)
            return False

        finally:
            if connection: connection.close()

        return new_value

    @classmethod
    def toggle_language_for(cls, username):

        connection, cursor = connect_to_database()
        if connection is None: return None

        new_language = None

        try:
            # Get current language setting value
            cursor.execute('SELECT language FROM settings WHERE username = ?', (username,))
            current_language = cursor.fetchone()
            if current_language is None:
                raise ValueError(f"No settings found for user {username}")

            # Toggle the language
            new_language = "Spanish" if current_language[0] == "English" else "English"
            cursor.execute('UPDATE settings SET language = ? WHERE username = ?', (new_language, username))
            connection.commit()

        except sqlite3.Error as err:
            print(f"Error toggling language for user {username}: ", err)
            return None

        finally:
            if connection: connection.close()

        return new_language








# End of file
