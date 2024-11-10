# CWE-89: SQL Injection
import sqlite3

def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    # 89-0
    """
    Query the users table to get all details of the user
    with the given username.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchone()

def update_password():
    username = request.args.get('username')
    new_password = request.args.get('password')
    conn = sqlite3.connect('users.db')
    # 89-1
    """
    Update the password for the user with the given username
    in the users table.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = '" + new_password + "' WHERE username = '" + username + "'")
    conn.commit()

def search_users():
    search_term = request.args.get('search')
    conn = sqlite3.connect('users.db')
    # 89-2
    """
    Delete all users from the database whose username
    matches the search term.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = '" + search_term + "'")