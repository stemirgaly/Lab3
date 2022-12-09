import hashlib
from enum import Enum
from typing import List


class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'


class Wallet:
    cash_amount: int = 0
    wallet_type: WalletType

    def __init__(self, wallet_type: WalletType):
        self.wallet_type = wallet_type

    def add_to_BankAccount(self, n: int):
        self.cash_amount += n

    def substract_from_BankAccount(self, n: int):
        self.cash_amount -= n

    def __repr__(self):
        return f'Текущий счет {self.cash_amount}'


class User:
    Surname: str
    Name: str
    username: str
    __password: str
    account: List[Wallet]

    def __init__(self, username: str):
        self.username = username

    def filter_wallets(self, wallet_type: WalletType):
        return [w for w in self.wallets if w.wallet_type == wallet_type]

    def set_password(self, password: str):
        self.__password = self._hash_password(password)

    def check_password(self, password: str) -> bool:
        return self.__password == self._hash_password(password)

    @staticmethod
    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return f'{self.username} {self.__password}'
