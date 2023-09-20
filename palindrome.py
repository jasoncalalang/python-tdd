# src/palindrome.py

def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char for char in s if char.isalnum()).lower()
    return cleaned_s == cleaned_s[::-1]  # Compare the string with its reverse
