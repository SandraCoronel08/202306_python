
class CuentaBancaria:
    # No olvides agregar algunos valores  predeterminados para estos parametros
    
    def __init__(self, tasa_interes, balance=0):
    # tu codigo aqui(recuerda, los atributos de instancia van aqui)
    # no te preocupes por la informacion del usuario aqui; pronto involucraremos la clase de usuario
    
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
        print(f"Balance: ${self.balance:.2f}")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

cuenta1 = CuentaBancaria(0.01, 100)
cuenta2 = CuentaBancaria(0.02, 200)

# encadenados
cuenta1.deposito(50).deposito(30).deposito(20).retiro(70).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(100).deposito(50).retiro(30).retiro(20).retiro(10).retiro(5).generar_interes().mostrar_info_cuenta()
