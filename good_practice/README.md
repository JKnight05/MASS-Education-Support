# Good Coding Practices

## Python Style (PEP 8)

[PEP 8 Guidance](https://peps.python.org/pep-0008/)

[Further PEP 8 Guidance](https://realpython.com/python-pep8/)

- *snake_case* for varaibles and functions

- *PascalCase* for classes

- *UPPER_CASE* for consants (e.g paths)


        AVOID:
        x = 12
        y = 45

        z = x * y

        BETTER:
        width = 12
        height = 45 

        area = width * height


## Proper Functions

- Keep functions small 
- One responsibility per function 
- Avoiding duplicated code
- Using parameters instead of hard-coding values
- Returning values rather than printing everything

        AVOID:

        def calculate():
            subtotal = 100
            tax = 20
            print(subtotal + tax)

        BETTER: 
        
        def calculate_total(subtotal, tax):
            return subtotal + tax

[Helpful Link](https://realpython.com/ref/best-practices/functions/)

## When to Use Classes

Use functions by default. Use classes when you eed to represent objects with both data and behaviour.

e.g:

- User
- A GUI
- A vehcile

Bad examples:

    class MathUtils:
        def add(a,b):
            return a + b

[Helpful Link](https://realpython.com/python-classes/)

## Project Structure

Do NOT put your projects in a single file. 

- Split files by responsibility
- Avoid 1000+ line scripts

## Commenting and docstrings

[Helpful Link](https://medium.com/@shubhanshusharma2193/doctring-v-s-comments-in-py-f36fe0d25986)

## Error Handling

Low maintenance, high importance skill.

- Catch specific exceptions 
- Avoid bare except:
- Fail gracefully

    AVOID:

    value = int(user_input)

    BETTER:

    try:
        value = int(user_input)
    except ValueError:
        print("Please enter a number, twat")

[Helpful Link](https://docs.python.org/3/tutorial/errors.html)

## Type hints

    def calculate_area(width: float, height: float) -> float:
        return width * height

- Better intellisense
- Easier debugging
- Better self-documentation


## Logging

Basic users will:

    print("Loading file")

Professionals use:

    import logging 

    logging.info("Loading file")

[Helpful Link](https://docs.python.org/3/library/logging.html)

## Configuration Management

    AVOID:
    
    database = "server123"
    api_key = "mf8se9rfh3w78fnw78fnw738h"


- [Config files](https://medium.com/the-pythonworld/how-to-write-and-use-configuration-files-in-python-like-a-pro-717d540bc063)
- [Secret management basics](https://medium.com/@michael.hannecke/secure-python-secret-management-cloud-local-e80cfa986d4c)


# The checklist

✅ Good variable names

✅ Functions are small

✅ No duplicated code

✅ Type hints added

✅ Errors handled

✅ PEP8 compliant

✅ Comments explain why, code explains how

✅ No hard-coded secrets and configuration settings

✅ Code is understandable by someone else
        


