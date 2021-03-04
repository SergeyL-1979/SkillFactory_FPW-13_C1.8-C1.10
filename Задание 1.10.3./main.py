class Client:
    def __init__(self, name, balance=0):
        self.name = name

        self.balance = balance

    def get_first(self):
        return self.name

    def get_balance(self):
        return self.balance

    def clients(self):
        return f'Клиент "{self.name}". '\
                f'Баланс: {self.balance} '


clients = Client('Иван Петров', 50)
print(clients.clients())
