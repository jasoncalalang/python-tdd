## TDD Exercise

This README file describes a TDD exercise using Python.

**Goal:** Write a function called `add_numbers()` that takes two numbers as input and returns their sum.

**Steps:**

1. Create a new Python file called `exercise.py`.
1. Add the following code to the file:
```python
def add_numbers(a, b):
    return a + b
```
1. Create a new file called test_exercise.py.
1. Add the following code to the file:
```python
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```
1. Run the tests by executing the following command:
```
python test_exercise.py
```
1. The tests should fail, because the `add_numbers()` function is not yet implemented.
1. Implement the add_`numbers()` function so that the tests pass.
1. Run the tests again to verify that they pass.