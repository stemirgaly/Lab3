from typing import Optional

from users.models import User
from users.repositories import UserRepositories


class UserServices:

    repositories: UserRepositories

    def __init__(self, repositories: UserRepositories):
        self.repositories = repositories

    def create_user(self, username: str, password: str) -> None:
        self.repositories.create_user(username=username, password=password)

    def get_user(self, username: str, password: str) -> Optional[User]:
        return self.repositories.get_user(username=username, password=password)
