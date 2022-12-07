class BankAccount:
    name: str = None
    surname: str = None
    account = None
def main_page():
    print(f'1. Создание пользователя')
    print(f'2. Выбор ползователя')
    print(f'0. Выйти')
    print(0)
    a=int(input())
    return a
a=main_page()
if a==0:
    print(f'Сеанс окончен')