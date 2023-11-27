class UserDatabase:
    def __init__(self):
        self.users = {}  # Simulates a user database

    def add_user(self, username, password):
        self.users[username] = password

    def validate_user(self, username, password):
        return self.users.get(username) == password

