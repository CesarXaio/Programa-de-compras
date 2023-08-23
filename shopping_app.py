from customer import Customer
from item import Item
from seller import Seller
from ownable import Ownable  # Importa el módulo Ownable
# Crear un vendedor
vendedor = Seller("TiendaDIC")
for i in range(10):
    Item("CPU", 40830, vendedor)
    Item("Memoria", 13880, vendedor)
    Item("Placa madre", 28980, vendedor)
    Item("Unidad de fuente de alimentación", 8980, vendedor)
    Item("Caja de PC", 8727, vendedor)
    Item("HDD de 3.5 pulgadas", 10980, vendedor)
    Item("SSD de 2.5 pulgadas", 13370, vendedor)
    Item("SSD M.2", 12980, vendedor)
    Item("Refrigerador de CPU", 13400, vendedor)
    Item("Tarjeta gráfica", 23800, vendedor)

print("🤖 Por favor, dime tu nombre")
cliente = Customer(input())

print("🏧 Ingresa la cantidad que deseas cargar a tu monedero")
cliente.wallet.deposit(int(input()))

print("🛍️ Comenzaremos a hacer compras")
fin_compras = False
while not fin_compras:
    print("📜 Lista de productos")
    vendedor.show_items()

    print("️️⛏ Ingresa el número del producto que deseas")
    numero = int(input())

    print("⛏ Ingresa la cantidad de productos que deseas")
    cantidad = int(input())

    productos = vendedor.pick_items(numero, cantidad)
    for producto in productos:
        cliente.cart.add(producto)
    print("🛒 Contenido del carrito")
    cliente.cart.show_items()
    print(f"🤑 Total a pagar: {cliente.cart.total_amount()}")

    print("😭 ¿Deseas finalizar tus compras? (si/no)")
    fin_compras = input() == "si"

print("💸 ¿Deseas confirmar la compra? (si/no)")
if input() == "si":
    cliente.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Propiedades de {cliente.name}")
cliente.show_items()
print(f"😱👛 Saldo en tu monedero: {cliente.wallet.balance}")

print(f"📦 Inventario de {vendedor.name}")
vendedor.show_items()
print(f"😻👛 Saldo en el monedero de {vendedor.name}: {vendedor.wallet.balance}")

print("🛒 Contenido del carrito")
cliente.cart.show_items()
print(f"🌚 Total a pagar: {cliente.cart.total_amount()}")

print("🎉 Fin del proceso")
