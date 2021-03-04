class Client:
    def __init__(self, name, balance=0):
        self.name = name

        self.balance = balance

    def get_first(self):
        return self.name

    def get_balance(self):
        return self.balance

    def clients(self):
        return f'Клиент "{self.name}". ' \
               f'Баланс: {self.balance} '


class Guest(Client):
    def __init__(self, town, status, name):
        super().__init__(name)
        self.town = town
        self.status = status

    def get_town(self):
        return self.town

    def get_status(self):
        return self.status


db = [dict(name='Иван Петров', balance=50, town='Москва', status='Наставник'),
      dict(name='Ольга Иванова', balance=100, town='Растов-на-Дону', status='Менеджер'),
      dict(name='Мистер Х', balance='Unknown', town='Белград', status='Случайный гость')]

clients = []
for item in db:
    clients.append(Guest(item['town'], item['status'], item['name']))
for client in clients:
    print(f'«{client.get_first()}, г. {client.get_town()}, статус \"{client.get_status()}\"»')
