import sys

from users.handlers import UserHandlers
from users.repositories import UserRepositories
from users.services import UserServices


def init():
    user_repositories = UserRepositories()
    user_services = UserServices(repositories=user_repositories)
    user_handlers = UserHandlers(services=user_services)

    while True:
        print(f'1. Создание пользователя')
        print(f'2. Выбрать пользователя')
        print(f'0. Выйти')
        print(f'0')

        command = input('Enter command: ')

        if command == '0':
            sys.exit(0)

        if command == '1':
            Surname, Name, password = input('Enter Surname, Name and password: ').split()
            username= Surname+ " " + Name
            user_handlers.sign_up(username=username, password=password)

        elif command == '2':
            Surname, Name , password = input('Please, enter your Surname, Name and password: ').split()
            username= Surname + " " + Name
            user_handlers.sign_in(username=username, password=password)

        else:
            print('invalid command, try again')


if __name__ == '__main__':
    init()
