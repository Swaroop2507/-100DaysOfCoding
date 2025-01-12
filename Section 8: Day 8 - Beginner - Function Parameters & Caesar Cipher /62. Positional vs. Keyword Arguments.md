Here's a simplified guide based on the lesson using the **Pareto Principle**. I’ll focus on the 20% of concepts that deliver 80% of the benefits for understanding and using **functions with multiple inputs** in Python. This includes **practical examples**, **step-by-step notes**, and **actionable exercises** to apply the knowledge.  

---

### **Key Learning Points: Functions with Multiple Inputs**
1. **Creating a Function with Multiple Parameters**  
   Functions can accept multiple pieces of data (called parameters).  
   Example:  
   ```python
   def greet_with(name, location):
       print(f"Hello {name}")
       print(f"What is it like in {location}?")
   ```
   - **`name`** and **`location`** are parameters that the function uses when called.
   - **`f-string`** allows us to insert variables into a string for dynamic output.

2. **Calling a Function with Arguments**  
   When calling a function, you must provide values (called arguments) for each parameter.  
   Example:
   ```python
   greet_with("Jack Bauer", "Nowhere")
   ```
   Output:
   ```
   Hello Jack Bauer
   What is it like in Nowhere?
   ```

3. **Positional Arguments**  
   Arguments are matched by their order in the function call.
   ```python
   greet_with("Nowhere", "Jack Bauer")
   ```
   Output:
   ```
   Hello Nowhere
   What is it like in Jack Bauer?
   ```

   **Key Concept**: The **first argument** goes to the **first parameter** (`name`), and the **second argument** goes to the **second parameter** (`location`). This is why incorrect order leads to incorrect results.

4. **Keyword Arguments**  
   Use explicit **parameter names** when calling a function to avoid order issues.  
   Example:
   ```python
   greet_with(location="London", name="Angela")
   ```
   Output:
   ```
   Hello Angela
   What is it like in London?
   ```

---

### **Hands-On Notes**
#### **Step-by-Step Guide**
1. **Define a Function with Two Parameters**:
   ```python
   def greet_with(name, location):
       # Print a greeting using the inputs
       print(f"Hello {name}")
       print(f"What is it like in {location}?")
   ```
2. **Call the Function Using Positional Arguments**:
   ```python
   greet_with("Alice", "Paris")
   # Output:
   # Hello Alice
   # What is it like in Paris?
   ```

3. **Call the Function Using Keyword Arguments**:
   ```python
   greet_with(location="New York", name="Bob")
   # Output:
   # Hello Bob
   # What is it like in New York?
   ```

4. **Try Switching the Order with Keyword Arguments**:
   ```python
   greet_with(name="Sam", location="Berlin")
   # Same result regardless of order
   ```

---

### **Actionable Tips for Writing Better Functions**
1. **Use Positional Arguments for Simplicity**:  
   When inputs are obvious and easy to understand.
   Example: `greet_with("Alice", "Wonderland")`

2. **Use Keyword Arguments for Clarity and Safety**:  
   When there’s a risk of confusion about parameter order.
   Example: `greet_with(location="Venice", name="Marco")`

3. **Mix for Flexibility**:  
   It’s possible to mix **positional** and **keyword arguments**, but **positional** must always come first.  
   Example:  
   ```python
   greet_with("Charlie", location="Helsinki")
   ```

---

### **Quick Exercises**
1. **Create a Function**:  
   Write a function called `describe_person()` that takes `name` and `age` as inputs and prints a description.  
   Call it using both positional and keyword arguments.

2. **Debugging Practice**:  
   Predict the output of this function call:  
   ```python
   greet_with("Tokyo", "Alice")
   ```

3. **Modify the Function**:  
   Change `greet_with()` so it prints an additional message about the weather in `location`.

---

This approach gives you the **most essential concepts (20%)** to apply **functions with multiple inputs (80%)** effectively. Practice regularly with these examples and exercises to master the topic!
