class Usuario:		
    def __init__(self, name="N/A", email="N/A"):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_depósito(self, amount):	
        self.balance_cuenta += amount

    def hacer_retiro(self, cantidad):
        self.balance_cuenta -= cantidad

    def mostrar_balance_usuario(self):
        print("Usuario: {}, Balance: ${}".format(self.name,self.balance_cuenta))

    def transferir_dinero(self, other_user, valor):
        self.balance_cuenta-=valor
        other_user.balance_cuenta+=valor