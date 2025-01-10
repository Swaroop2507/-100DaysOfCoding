

### **Functions in Python: Overview**
A **function** is a reusable block of code that performs a specific task. Python provides built-in functions (e.g., `print()`, `len()`, `int()`) and allows users to define custom functions.

---

### **Creating and Using Functions**
#### **1. Defining a Function**
- Use the `def` keyword to define a function.  
- Provide a **name** followed by parentheses `()` and a colon `:`.  
- Indent the block of code that belongs to the function.

```python
def my_function():
    print("Hello")
    print("Bye")
```

#### **2. Calling a Function**
- Type the function's name followed by parentheses to execute it.

```python
my_function()  # Outputs: Hello
                #          Bye
```

---

### **Function Structure**
1. **Definition**: Starts with `def my_function():`.
2. **Indentation**: Code inside the function must be indented.
3. **Execution (Call)**: The function runs only when called using its name followed by parentheses.

---

### **Why Use Functions?**
- **Reduce Code Duplication**: Functions bundle repetitive tasks into a single block.
- **Enhance Readability**: Function names describe actions, making code easier to understand.
- **Maintainability**: Updating a function affects all its calls, simplifying code changes.

---

### **Example: Built-in `len()` and `print()`**
```python
word = "Hello"
num_char = len(word)  # Calculates length of "Hello" (5)
print(num_char)       # Prints: 5
```

---

### **Creating Custom Functions**
#### Example: Turning a Robot (Reeborg’s World)
- `turn_left()` is a built-in command, but `turn_right()` is missing. Define it using `turn_left()` three times.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

Now, instead of writing `turn_left()` three times, you can call `turn_right()` to simplify your code.

---

### **Additional Concepts**
1. **Debugging with Step-through Mode**: Executes code one step at a time to understand its flow.
2. **Reusable Recipes**: Functions save typing effort and make logic more modular.

---

### **Challenge Exercise**  
Create a `turn_around()` function using `turn_left()` twice. Then use it in a sequence of movements to minimize repetitive code.

