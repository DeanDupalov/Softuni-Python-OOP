class Library:
    def __init__(self):
        self.user_records = []  # users
        self.books_available = {}  # {author: [ books available] }
        self.rented_books = {}  # username: {book_name: days_left_return}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        if user in self.rented_books:
            del self.rented_books[user]

        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        if user_id not in map(lambda u: u.user_id, self.user_records):
            return f"There is no user with id = {user_id}!"

        current_user = [u for u in self.user_records if u.user_id == user_id][0]

        if current_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        if current_user.username in self.rented_books:
            self.rented_books[new_username] = self.rented_books.pop(current_user.username)

        current_user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
