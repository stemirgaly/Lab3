from typing import Optional

from users.models import User
from users.models import Wallet
from users.services import UserServices
from users.services import BankServices


class UserHandlers:

    services: UserServices

    def __init__(self, services: UserServices):
        self.services = services

    def sign_up(self, username: str, password: str) -> None:
        username = username.strip().lower()
        password = password.strip()

        if not self._validate_username_and_password(username, password):
            return None

        self.services.create_user(username=username, password=password)

    def sign_in(self, username: str, password: str) -> Optional[User]:
        username = username.strip().lower()
        password = password.strip()

        if not self._validate_username_and_password(username, password):
            return None

        return self.services.get_user(username=username, password=password)

    @staticmethod
    def _validate_username_and_password(username: str, password: str) -> bool:
        if username.startswith('z'):
            print('username is invalid')
            return False

        if len(password) < 8:
            print('password is too short')
            return False

        return True

class BankAccountHandlers:
    services = BankServices

    def __init__(self, services):
        self.services = services

    def add_to_BankAccount(self, n: int) -> None:
        self.add_to_BankAccount(n=n)

    def substract_from_BankAccount(self, n: int) -> None:
        self.substract_from_BankAccount(n=n)

    def __repr__(self):
        return BankServices