# Object-Oriented Programming (OOP) for CustomTkinter Projects

## Learning Objectives

By the end of this session, you should be able to:

- Understand what Object-Oriented Programming (OOP) is.
- Explain why OOP is useful when building GUI applications.
- Create classes for windows, pages and reusable components.
- Separate your interface from your application logic.
- Structure a medium-sized CustomTkinter project using multiple files.
- Write code that is easier to read, debug and extend.

---

# What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a way of organising your code into **objects**.

An object combines:

- **Data (Attributes)** – information about the object.
- **Behaviour (Methods)** – things the object can do.

Think about a real-world object.

## Example: A Student

A student has:

**Attributes**

- Name
- Age
- Course

**Methods**

- Study
- Submit work
- View grades

In Python we represent this using a **class**.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}.")
```

Creating a student:

```python
student1 = Student("Emily", 17)
student1.introduce()
```

The class is the blueprint.

The object is the thing created from the blueprint.

---

# Why Do We Need OOP?

Small programs don't usually need much structure.

For example:

```python
print("Hello World")
```

is perfectly fine.

But imagine your coursework project has:

- 25 buttons
- 15 labels
- Login system
- Database
- Settings page
- Multiple windows
- File saving

Trying to keep all of this in one file quickly becomes difficult.

Without OOP you often end up with:

- Hundreds of variables
- Huge functions
- Global variables
- Repeated code
- Difficult debugging

Instead, OOP allows us to organise our program into manageable pieces.

---

# Why OOP Works Well with GUI Applications

GUI applications naturally contain objects.

Think about a simple application:

```
Application
│
├── Window
│
├── Button
│
├── Label
│
├── Entry Box
│
└── Menu
```

Each of these can become a Python object.

CustomTkinter is already designed around OOP.

Instead of creating everything manually:

```python
app = ctk.CTk()

label = ctk.CTkLabel(app)
button = ctk.CTkButton(app)
```

We normally create our own application class.

```python
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Student App")
```

Now the whole application becomes one object.

---

# The Four Main OOP Ideas

You don't need to memorise these names, but understanding them will help you design better programs.

## 1. Encapsulation

Keep related data and functions together.

Instead of:

```python
score = 10

def increase_score():
    ...
```

Use:

```python
class Player:

    def __init__(self):
        self.score = 10

    def increase_score(self):
        self.score += 1
```

Everything related to the player stays together.

---

## 2. Abstraction

Hide unnecessary complexity.

Instead of worrying how something works internally, you just use it.

```python
button.pack()
```

You don't need to know how `pack()` works internally.

You simply use it.

---

## 3. Inheritance

Create new classes from existing ones.

```python
class LoginPage(ctk.CTkFrame):
    ...
```

`LoginPage` automatically gains all the functionality of a `CTkFrame`.

You only add what makes it unique.

---

## 4. Polymorphism

Different objects can respond to the same action in different ways.

For now, just remember that many widgets can have methods with the same name but behave differently.

---

# Building Your Main Window

A common structure is:

```python
class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("My App")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        ...
```

Notice that the constructor stays short.

Instead of writing 100 lines inside `__init__`, we move code into methods.

---

# Organising Your Code

As projects grow, split work into smaller methods.

Instead of:

```python
class App:

    def __init__(self):

        # 150 lines of widgets...
```

Use:

```python
class App:

    def __init__(self):

        self.create_menu()
        self.create_main_page()
        self.create_footer()
```

This makes code much easier to read.

---

# Separating the GUI from the Logic

One of the biggest beginner mistakes is putting all of the application's logic inside button commands.

## Poor Design

```python
def calculate():

    # Read input

    # Validate data

    # Calculate result

    # Save file

    # Update labels

    # Display message

    # Reset boxes
```

One function doing everything is difficult to understand and maintain.

## Better Design

```python
class ScoreCalculator:

    def calculate_score(self, score):
        return score * 10
```

Then your GUI simply asks the calculator to do the work.

```python
result = self.calculator.calculate_score(5)
```

### A useful rule

> **The GUI should ask for work, not do the work.**

---

# Creating Reusable Components

Suppose your project displays several users.

Instead of repeatedly creating labels and frames:

```python
label1 = ...
label2 = ...
label3 = ...
```

Create a reusable widget.

```python
class UserCard(ctk.CTkFrame):

    def __init__(self, parent, name):

        super().__init__(parent)

        self.label = ctk.CTkLabel(
            self,
            text=name
        )

        self.label.pack()
```

Now you can simply write:

```python
user1 = UserCard(app, "Jacob")
user2 = UserCard(app, "Sarah")
```

One class can be reused many times.

---

# Multi-Page Applications

Many projects eventually grow beyond one screen.

Typical pages include:

- Login
- Dashboard
- Settings
- Help
- Reports

Each page can become its own class.

```python
class LoginPage(ctk.CTkFrame):
    ...

class DashboardPage(ctk.CTkFrame):
    ...

class SettingsPage(ctk.CTkFrame):
    ...
```

Each page is responsible for itself.

This makes your project much easier to extend.

---

# Good Project Structure

As your project grows, split your code into multiple files.

```
project/
│
├── main.py
├── app.py
│
├── pages/
│   ├── login.py
│   ├── dashboard.py
│   └── settings.py
│
├── models/
│   └── user.py
│
├── services/
│   ├── calculator.py
│   └── database.py
│
└── assets/
```

Don't wait until your file reaches 1,000 lines before organising it!

---

# Tips & Tricks

## 1. Use Instance Variables

Instead of:

```python
entry = ctk.CTkEntry(self)
```

Use:

```python
self.entry = ctk.CTkEntry(self)
```

You'll probably need access to it later.

---

## 2. Avoid Global Variables

Instead of:

```python
global score
```

Store data inside the object.

```python
self.score
```

Objects manage their own data.

---

## 3. Give Classes One Responsibility

Avoid:

```text
App
├── GUI
├── Database
├── File Saving
├── Calculations
├── Settings
├── Login
└── Reports
```

Better:

```
App
DatabaseManager
FileManager
ScoreCalculator
User
Settings
```

Each class should have one clear job.

---

## 4. Keep Methods Small

Instead of one giant function:

```python
def update_everything():
```

Use smaller methods:

```python
update_score()
update_timer()
update_labels()
save_game()
```

Smaller methods are easier to test and debug.

---

## 5. Use Meaningful Names

Avoid:

```python
button1
button2
entry3
```

Instead:

```python
submit_button
username_entry
score_label
```

Your future self will thank you!

---

## 6. Store Data in Objects

Instead of:

```python
username = ""
age = 0
score = 0
```

Create a class.

```python
class User:

    def __init__(self, username, age):
        self.username = username
        self.age = age
```

This keeps related information together.

---

## 7. Use `__repr__()` for Easier Debugging

```python
class User:

    def __repr__(self):
        return f"User({self.username})"
```

Printing a `User` object now gives useful information rather than a memory address.

---

# Common Beginner Mistakes

 Everything in one file

 Very long functions

 Global variables

 Repeated code

 One class that does everything

 Unclear variable names

---

# A Good Workflow

When building your project:

1. Make it work.
2. Make it readable.
3. Refactor into classes.
4. Split into multiple files.
5. Test everything.

Don't worry about making the perfect design straight away—it's normal to improve your code as your project grows.

---

# Mini Challenge

## Refactor a Simple Application

Imagine you've been given the following program:

```python
import customtkinter as ctk

app = ctk.CTk()

label = ctk.CTkLabel(app, text="Counter: 0")
label.pack()

count = 0

def increase():

    global count

    count += 1

    label.configure(text=f"Counter: {count}")

button = ctk.CTkButton(
    app,
    text="Increase",
    command=increase
)

button.pack()

app.mainloop()
```

### Task 1

Identify **at least three** things you would improve.

---

### Task 2

Sketch how you would redesign it using OOP.

For example:

```
App
│
├── Counter
│
└── CounterFrame
```

What responsibility would each class have?

---

### Task 3 (Stretch)

If your coursework project had:

- Login page
- Dashboard
- User accounts
- High scores
- Database

Draw a class diagram showing:

- The classes you would create.
- What each class is responsible for.
- Which classes need to communicate with each other.

You don't need to write any code—focus on the design.

---

# Key Takeaways

- OOP helps organise larger projects into manageable pieces.
- GUI applications naturally fit the OOP model.
- Keep your GUI separate from your application logic.
- Give each class one responsibility.
- Split projects into multiple files early.
- Small, organised code is much easier to debug, maintain and extend.
- Good code isn't just about making it work—it's about making it easy to understand and improve.