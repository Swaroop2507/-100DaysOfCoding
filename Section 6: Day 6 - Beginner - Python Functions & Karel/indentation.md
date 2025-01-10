**Key Concept: Indentation in Python**

**1. Why Indentation Matters**
- Indentation defines the structure and hierarchy of code.
- Python uses indentation instead of braces `{}` seen in other languages.

**Basic Example:**
```python
# Correct indentation

def my_function():
    print("Hello")  # This line is part of my_function

my_function()

# Incorrect indentation

def another_function():
print("World")  # This line will raise an IndentationError
```

In the correct example, `print("Hello")` is indented inside `my_function()`. Without proper indentation, Python will throw an error.

---

**2. Indentation and Nested Blocks**
- Nested structures like `if-else` statements and loops also use indentation.

**Example with Multiple Blocks:**
```python
def check_weather(sky):
    if sky == "clear":
        print("Blue sky!")
    elif sky == "cloudy":
        print("Gray sky!")
    else:
        print("Unknown sky condition.")

check_weather("clear")
```

**Explanation:**
- `if`, `elif`, and `else` statements are indented inside the `check_weather` function.
- Each `print` statement inside each block is indented further to maintain the correct structure.

---

**3. Indentation Levels**
- Each block within a block requires further indentation.
- Think of indentation as creating folders and subfolders:

**Example:**
```python
def folder_example():
    if True:
        print("First level")  # Indented once
        if True:
            print("Second level")  # Indented twice
folder_example()
```

---

**4. Spaces vs. Tabs**
- Python's official style guide (PEP 8) recommends using **spaces** for indentation.
- Standard: **4 spaces per indentation level**.
- Mixing tabs and spaces can cause errors in Python 3.

**Example Configuration for Code Editors:**
- Set your editor to replace tabs with 4 spaces:
  - **VSCode, PyCharm, Sublime Text, or other editors** have this setting.

---

**Quick Practical Tips**
1. Enable "show whitespace" in your editor to visualize spaces and tabs.
2. Configure the editor to automatically use 4 spaces when pressing `Tab`.
3. Use consistent indentation to avoid errors:
   - Press `Tab` only once if your editor inserts spaces automatically.

---

**Hands-on Exercises**

1. **Fix the Indentation Error**
```python
# Correct this code

def greet_user(name):
print("Hello, " + name)

# Hint: Indent the print statement.
```
**Solution:**
```python
def greet_user(name):
    print("Hello, " + name)
```

2. **Indent the Blocks Correctly**
```python
# Fix this nested loop
for i in range(3):
print("Outer loop iteration", i)
for j in range(2):
print("  Inner loop iteration", j)
```

**Solution:**
```python
for i in range(3):
    print("Outer loop iteration", i)
    for j in range(2):
        print("  Inner loop iteration", j)
```

---

**Summary**
- Indentation in Python determines the structure of your code.
- Use 4 spaces per level; avoid mixing spaces and tabs.
- Proper indentation prevents errors and makes code readable.

By mastering the basics of indentation, you gain control over Python’s structure—one of the key 20% concepts that delivers 80% of your coding clarity and success!

