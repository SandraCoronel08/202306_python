class CuentaBancaria:
    def __init__(self, tasa_interes, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
    
    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return f"${self.balance:.2f}"

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}
    
    def agregar_cuenta(self, tipo_cuenta, tasa_interes=0.02, balance=0):
        self.cuentas[tipo_cuenta] = CuentaBancaria(tasa_interes, balance)
        return self
    
    def hacer_deposito(self, tipo_cuenta, amount):
        self.cuentas[tipo_cuenta].deposito(amount)
        return self
    
    def hacer_retiro(self, tipo_cuenta, amount):
        self.cuentas[tipo_cuenta].retiro(amount)
        return self
    
    def mostrar_balance_usuario(self):
        for tipo_cuenta, cuenta in self.cuentas.items():
            print(f"User: {self.nombre}, {tipo_cuenta.capitalize()} Balance: {cuenta.mostrar_info_cuenta()}")

usuario1 = Usuario("Sandra")
usuario1.agregar_cuenta("checking", 0.02, 500).agregar_cuenta("savings", 0.01, 1000)

usuario1.hacer_deposito("checking", 150).hacer_retiro("savings", 300).mostrar_balance_usuario()
