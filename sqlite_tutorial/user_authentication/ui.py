"""
ui.py
CustomTkinter UI components for authentication app
"""

import customtkinter as ctk
from tkinter import messagebox


class AuthApp(ctk.CTk):
    def __init__(self, db_manager):
        super().__init__()
        
        self.db = db_manager
        self.current_user = None
        
        # Configure window
        self.title("User Authentication System")
        self.geometry("500x600")
        
        # Set theme and color
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Center window on screen
        self.center_window()
        
        # Show login frame initially
        self.show_login_frame()
    
    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def clear_frame(self):
        """Clear all widgets from the window"""
        for widget in self.winfo_children():
            widget.destroy()
    
    def show_login_frame(self):
        """Display the login interface"""
        self.clear_frame()
        self.geometry("500x600")
        
        # Main container
        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Title
        title = ctk.CTkLabel(
            container,
            text="Welcome Back!",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title.pack(pady=(40, 10))
        
        subtitle = ctk.CTkLabel(
            container,
            text="Login to your account",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 40))
        
        # Username entry
        username_label = ctk.CTkLabel(
            container,
            text="Username",
            font=ctk.CTkFont(size=14)
        )
        username_label.pack(anchor="w", padx=20)
        
        self.login_username = ctk.CTkEntry(
            container,
            placeholder_text="Enter your username",
            width=300,
            height=40
        )
        self.login_username.pack(pady=(5, 20))
        
        # Password entry
        password_label = ctk.CTkLabel(
            container,
            text="Password",
            font=ctk.CTkFont(size=14)
        )
        password_label.pack(anchor="w", padx=20)
        
        self.login_password = ctk.CTkEntry(
            container,
            placeholder_text="Enter your password",
            show="*",
            width=300,
            height=40
        )
        self.login_password.pack(pady=(5, 30))
        
        # Login button
        login_btn = ctk.CTkButton(
            container,
            text="Login",
            command=self.handle_login,
            width=300,
            height=40,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        login_btn.pack(pady=(0, 15))
        
        # Register link
        register_frame = ctk.CTkFrame(container, fg_color="transparent")
        register_frame.pack(pady=20)
        
        register_label = ctk.CTkLabel(
            register_frame,
            text="Don't have an account?",
            font=ctk.CTkFont(size=12)
        )
        register_label.pack(side="left", padx=(0, 5))
        
        register_btn = ctk.CTkButton(
            register_frame,
            text="Register here",
            command=self.show_register_frame,
            width=100,
            height=25,
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            text_color=("blue", "lightblue"),
            hover_color=("gray90", "gray20")
        )
        register_btn.pack(side="left")
        
        # Bind Enter key to login
        self.login_password.bind('<Return>', lambda e: self.handle_login())
    
    def show_register_frame(self):
        """Display the registration interface"""
        self.clear_frame()
        self.geometry("500x650")
        
        # Main container
        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Title
        title = ctk.CTkLabel(
            container,
            text="Create Account",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title.pack(pady=(40, 10))
        
        subtitle = ctk.CTkLabel(
            container,
            text="Register a new account",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 40))
        
        # Username entry
        username_label = ctk.CTkLabel(
            container,
            text="Username",
            font=ctk.CTkFont(size=14)
        )
        username_label.pack(anchor="w", padx=20)
        
        self.register_username = ctk.CTkEntry(
            container,
            placeholder_text="Choose a username",
            width=300,
            height=40
        )
        self.register_username.pack(pady=(5, 20))
        
        # Password entry
        password_label = ctk.CTkLabel(
            container,
            text="Password",
            font=ctk.CTkFont(size=14)
        )
        password_label.pack(anchor="w", padx=20)
        
        self.register_password = ctk.CTkEntry(
            container,
            placeholder_text="Choose a password (min 6 characters)",
            show="*",
            width=300,
            height=40
        )
        self.register_password.pack(pady=(5, 20))
        
        # Confirm password entry
        confirm_label = ctk.CTkLabel(
            container,
            text="Confirm Password",
            font=ctk.CTkFont(size=14)
        )
        confirm_label.pack(anchor="w", padx=20)
        
        self.register_confirm = ctk.CTkEntry(
            container,
            placeholder_text="Confirm your password",
            show="*",
            width=300,
            height=40
        )
        self.register_confirm.pack(pady=(5, 30))
        
        # Register button
        register_btn = ctk.CTkButton(
            container,
            text="Create Account",
            command=self.handle_register,
            width=300,
            height=40,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        register_btn.pack(pady=(0, 15))
        
        # Back to login link
        login_frame = ctk.CTkFrame(container, fg_color="transparent")
        login_frame.pack(pady=20)
        
        login_label = ctk.CTkLabel(
            login_frame,
            text="Already have an account?",
            font=ctk.CTkFont(size=12)
        )
        login_label.pack(side="left", padx=(0, 5))
        
        login_btn = ctk.CTkButton(
            login_frame,
            text="Login here",
            command=self.show_login_frame,
            width=100,
            height=25,
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            text_color=("blue", "lightblue"),
            hover_color=("gray90", "gray20")
        )
        login_btn.pack(side="left")
        
        # Bind Enter key to register
        self.register_confirm.bind('<Return>', lambda e: self.handle_register())
    
    def show_dashboard(self, username):
        """Display the main dashboard after successful login"""
        self.clear_frame()
        self.geometry("600x500")
        self.current_user = username
        
        # Main container
        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Welcome message
        welcome = ctk.CTkLabel(
            container,
            text=f"Welcome, {username}!",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        welcome.pack(pady=(40, 10))
        
        subtitle = ctk.CTkLabel(
            container,
            text="You have successfully logged in",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 40))
        
        # Success icon/message
        success_frame = ctk.CTkFrame(container, fg_color=("green", "darkgreen"))
        success_frame.pack(pady=20, padx=50, fill="x")
        
        success_label = ctk.CTkLabel(
            success_frame,
            text="✓ Authentication Successful",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="white"
        )
        success_label.pack(pady=20)
        
        # User info
        info_frame = ctk.CTkFrame(container)
        info_frame.pack(pady=20, fill="x", padx=50)
        
        info_label = ctk.CTkLabel(
            info_frame,
            text="Account Information",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        info_label.pack(pady=(15, 10))
        
        username_info = ctk.CTkLabel(
            info_frame,
            text=f"Username: {username}",
            font=ctk.CTkFont(size=14)
        )
        username_info.pack(pady=5)
        
        status_info = ctk.CTkLabel(
            info_frame,
            text="Status: Active",
            font=ctk.CTkFont(size=14),
            text_color="green"
        )
        status_info.pack(pady=(5, 15))
        
        # Logout button
        logout_btn = ctk.CTkButton(
            container,
            text="Logout",
            command=self.handle_logout,
            width=200,
            height=40,
            font=ctk.CTkFont(size=16),
            fg_color=("gray70", "gray30"),
            hover_color=("gray60", "gray40")
        )
        logout_btn.pack(pady=30)
    
    def handle_login(self):
        """Handle login button click"""
        username = self.login_username.get().strip()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        success, message = self.db.login_user(username, password)
        
        if success:
            messagebox.showinfo("Success", message)
            self.show_dashboard(username)
        else:
            messagebox.showerror("Login Failed", message)
            self.login_password.delete(0, 'end')
    
    def handle_register(self):
        """Handle registration button click"""
        username = self.register_username.get().strip()
        password = self.register_password.get()
        confirm = self.register_confirm.get()
        
        if not username or not password or not confirm:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            self.register_confirm.delete(0, 'end')
            return
        
        success, message = self.db.register_user(username, password)
        
        if success:
            messagebox.showinfo("Success", message)
            self.show_login_frame()
        else:
            messagebox.showerror("Registration Failed", message)
    
    def handle_logout(self):
        """Handle logout button click"""
        self.current_user = None
        messagebox.showinfo("Logged Out", "You have been logged out successfully")
        self.show_login_frame()