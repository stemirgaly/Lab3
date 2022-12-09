from typing import List, Optional

from users.models import User
from users.models import Wallet


class UserRepositories:
    users: List[User] = []

    def create_user(self, username: str, password: str) -> None:
        user = User(username=username)
        user.set_password(password=password)

        self.users.append(user)

    def get_user(self, username: str, password: str) -> Optional[User]:
        user = next(
            (u for u in self.users if username == u.username and u.check_password(password)),
            None
        )

        if not user:
            return 'User not found'


        return user
class BankRepositories:


    def add_to_BankAccount(self, n: int) -> None:
        self.add_to_BankAccount(n=n)

    def substract_from_BankAccount(self, n: int) -> None:
        self.substract_from_BankAccount(n=n)

    def __repr__(self):
        return Wallet