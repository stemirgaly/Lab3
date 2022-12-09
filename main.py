import sys

from users.handlers import UserHandlers
from users.repositories import UserRepositories
from users.services import UserServices
from users.repositories import BankRepositories
from users.services import BankServices
from users.handlers import BankAccountHandlers


def main():
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
            if user_handlers.sign_in(username=username, password=password) == 'User not found' :
                print(user_handlers.sign_in(username=username, password=password))
                sys.exit(0)

            else:
                terminal()


        else:
            print('invalid command, try again')


def terminal():
    bank_repositories = BankRepositories()
    bank_services = BankServices(repositories=bank_repositories)
    bank_handlers = BankAccountHandlers(services=bank_services)

    while True:
        print(f'1. Текущий счет')
        print(f'2. Снять деньги')
        print(f'3. Пополнить баланс')
        print(f'4. Назад')
        print(f'0. Выйти')
        print(f'0')

        command = input('Enter command: ')

        if command == '0':
            sys.exit(0)

        if command == '4':
            main()

        if command == '1':
            print(BankAccountHandlers)

        elif command == '2':
            n = input('Введите сумму: ')
            bank_handlers.add_to_BankAccount(n=n)

        elif command == '3':
            n = input('Введите сумму: ')
            bank_handlers.substract_from_BankAccount(n=n)


        else:
            print('invalid command, try again')
            terminal()

if __name__ == '__main__':
    main()
