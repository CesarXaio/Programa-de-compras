class Cart:
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        # Obtener el total de la compra
        total_purchase_amount = self.total_amount()

        # Verificar si el propietario del carrito tiene suficiente saldo
        if self.owner.wallet.balance < total_purchase_amount:
            print("No tienes suficiente saldo en tu monedero para completar la compra.")
            return

        # Transferir el precio de compra de los artículos a los propietarios respectivos
        for item in self.items:
            item_owner = item.owner
            self.owner.wallet.withdraw(item.price)
            item_owner.wallet.deposit(item.price)

            # Transferir la propiedad del artículo al propietario del carrito
            item.owner = self.owner

        # Vaciar el carrito
        self.items = []
        print("Compra completada con éxito. ¡Gracias por tu compra!")
# Asumiendo que tienes definidas las clases Wallet y Item con sus respectivos atributos
class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

class Item:
    def __init__(self, name, price, owner):
        self.name = name
        self.price = price
        self.owner = owner

# Ejemplo de uso
class Owner:
    def __init__(self, wallet_balance):
        self.wallet = Wallet(wallet_balance)

owner1 = Owner(1000)
owner2 = Owner(500)

item1 = Item("Item 1", 200, owner2)
item2 = Item("Item 2", 150, owner2)

cart = Cart(owner1)
cart.add(item1)
cart.add(item2)

cart.check_out()
print("Owner 1 balance:", owner1.wallet.balance)
print("Owner 2 balance:", owner2.wallet.balance)
