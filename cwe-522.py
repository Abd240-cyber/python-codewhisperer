# CWE-522: Weak Password Requirements
import bcrypt
def register_user():
    password = request.form.get('password')
    # 522-0
    """
    Create a new user account with the provided password
    and save it to the database.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password.decode('utf-8')))
    conn.commit()
    conn.close()
    return 'User registered successfully'

def reset_password():
    new_password = request.form.get('new_password')
    # 522-1
    """
    Update the user's password with the new password
    provided in the reset form.
    """
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password.decode('utf-8'), username))
    conn.commit()
    conn.close()
    return 'Password updated successfully'

def save_credentials():
    username = request.form.get('username')
    password = request.form.get('password')
    # 522-2
    """
    Store the user's login credentials in the database
    for authentication.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return 'Credentials saved successfully'