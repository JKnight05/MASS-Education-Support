"""
app.py
Main application file - runs the authentication system
"""

from database import DatabaseManager
from ui import AuthApp


def main():
    """Initialize and run the application"""
    # Initialize database
    db = DatabaseManager('users.db')
    
    # Create and run the UI
    app = AuthApp(db)
    
    # Run the application
    app.mainloop()
    
    # Close database connection when app closes
    db.close()


if __name__ == "__main__":
    main()