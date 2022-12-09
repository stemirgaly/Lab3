from typing import Optional

from users.models import User
from users.models import Wallet
from users.repositories import UserRepositories
from users.repositories import BankRepositories


class UserServices:

    repositories: UserRepositories

    def __init__(self, repositories: UserRepositories):
        self.repositories = repositories

    def create_user(self, username: str, password: str) -> None:
        self.repositories.create_user(username=username, password=password)

    def get_user(self, username: str, password: str) -> Optional[User]:
        return self.repositories.get_user(username=username, password=password)

class BankServices:
    repositories: BankRepositories

    def __init__(self, repositories: BankRepositories):
        self.repositories = repositories

    def add_to_BankAccount(self, n: int) -> None:
        self.add_to_BankAccount(n=n)

    def substract_from_BankAccount(self, n: int) -> None:
        self.substract_from_BankAccount(n=n)

    def __repr__(self):
        return self.repositories