"""
database.py
SQL database functions for user authentication
"""

import sqlite3
import hashlib
import os
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_name='users.db'):
        """Initialize database connection and create tables if needed"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Establish database connection"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def create_tables(self):
        """Create the users table if it doesn't exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def generate_salt(self):
        """Generate a random salt for password hashing"""
        return os.urandom(32).hex()
    
    def hash_password(self, password, salt):
        """Hash a password with a salt using SHA-256"""
        salted_password = (password + salt).encode('utf-8')
        return hashlib.sha256(salted_password).hexdigest()
    
    def register_user(self, username, password):
        """
        Register a new user with secure password storage
        
        Args:
            username: Desired username
            password: Plain text password (will be hashed)
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Validate input
            if not username or not password:
                return False, "Username and password cannot be empty"
            
            if len(username) < 3:
                return False, "Username must be at least 3 characters"
            
            if len(password) < 6:
                return False, "Password must be at least 6 characters"
            
            # Generate salt and hash password
            salt = self.generate_salt()
            password_hash = self.hash_password(password, salt)
            
            # Insert into database
            self.cursor.execute('''
                INSERT INTO users (username, password_hash, salt)
                VALUES (?, ?, ?)
            ''', (username, password_hash, salt))
            self.conn.commit()
            
            return True, f"User '{username}' registered successfully!"
            
        except sqlite3.IntegrityError:
            return False, f"Username '{username}' already exists!"
        except Exception as e:
            return False, f"Registration error: {str(e)}"
    
    def login_user(self, username, password):
        """
        Authenticate a user by verifying their password
        
        Args:
            username: Username to authenticate
            password: Plain text password to verify
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Validate input
            if not username or not password:
                return False, "Username and password cannot be empty"
            
            # Retrieve user data
            self.cursor.execute('''
                SELECT password_hash, salt FROM users WHERE username = ?
            ''', (username,))
            
            result = self.cursor.fetchone()
            
            if result is None:
                return False, f"User '{username}' not found!"
            
            stored_hash, salt = result
            
            # Hash the provided password with the stored salt
            input_hash = self.hash_password(password, salt)
            
            # Compare hashes
            if input_hash == stored_hash:
                return True, f"Welcome back, {username}!"
            else:
                return False, "Incorrect password!"
                
        except Exception as e:
            return False, f"Login error: {str(e)}"
    
    def user_exists(self, username):
        """Check if a username exists in the database"""
        self.cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone() is not None
    
    def get_all_users(self):
        """Get a list of all usernames (for admin purposes)"""
        self.cursor.execute('SELECT username, created_at FROM users')
        return self.cursor.fetchall()
    
    def change_password(self, username, old_password, new_password):
        """
        Change a user's password after verifying the old one
        
        Args:
            username: Username
            old_password: Current password for verification
            new_password: New password to set
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Verify old password first
            success, message = self.login_user(username, old_password)
            if not success:
                return False, "Current password is incorrect!"
            
            # Validate new password
            if len(new_password) < 6:
                return False, "New password must be at least 6 characters"
            
            # Generate new salt and hash
            new_salt = self.generate_salt()
            new_hash = self.hash_password(new_password, new_salt)
            
            # Update database
            self.cursor.execute('''
                UPDATE users SET password_hash = ?, salt = ?
                WHERE username = ?
            ''', (new_hash, new_salt, username))
            self.conn.commit()
            
            return True, "Password changed successfully!"
            
        except Exception as e:
            return False, f"Error changing password: {str(e)}"
    
    def delete_user(self, username):
        """Delete a user from the database"""
        try:
            self.cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            self.conn.commit()
            return True, f"User '{username}' deleted successfully!"
        except Exception as e:
            return False, f"Error deleting user: {str(e)}"
    
    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
    
    def __del__(self):
        """Ensure connection is closed when object is destroyed"""
        self.close()