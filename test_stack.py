import unittest

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

class TestStack(unittest.TestCase):
    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_push_and_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_push_and_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_pop_empty(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_empty(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_push_pop_push(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

if __name__ == '__main__':
    unittest.main()
