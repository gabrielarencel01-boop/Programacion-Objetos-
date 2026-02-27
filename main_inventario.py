from inventario import *

prod1 = Producto("Magnum", 25, 30)
prod2 = Producto("Parringas", 20, 28)
prod3 = Producto("Twister", 15, 22)
prod4 = Producto("Calippo", 18, 24)
prod5 = Producto("Solero", 22, 29)
prod6 = Producto("Feast", 30, 40)
prod7 = Producto("Mini Milk", 10, 15)
prod8 = Producto("Ben & Jerry's", 45, 60)
prod9 = Producto("Carte D'Or", 35, 50)
prod10 = Producto("Viennetta", 32, 45)
prod11 = Producto("Nogger", 27, 35)
prod12 = Producto("Split", 12, 18)
prod13 = Producto("Cornetto Mini", 14, 20)
prod14 = Producto("Magnum Almond", 28, 38)
prod15 = Producto("Magnum White", 28, 38)
prod16 = Producto("Twister Mini", 10, 16)
prod17 = Producto("Calippo Cola", 17, 23)
prod18 = Producto("Solero Exotic", 24, 32)
prod19 = Producto("Feast Chocolate", 33, 42)
prod20 = Producto("Mini Magnum", 18, 26)
prod21 = Producto("Cornetto Chocolate", 21, 30)
prod22 = Producto("Cornetto Strawberry", 21, 30)
prod23 = Producto("Magnum Double", 35, 48)
prod24 = Producto("Ben & Jerry's Cookie Dough", 48, 65)
prod25 = Producto("Carte D'Or Vanilla", 36, 52)

prod1.aplicar_descuento(0.10)
prod1.actualizar_stock(20)
prod1.actualizar_stock(-60)
prod1.actualizar_stock(-40)
prod2.aplicar_descuento(0.15)

cat1=Categoria("Chatarra")
cat1.agregar_producto(prod1)
cat1.agregar_producto(prod20)
cat1.agregar_producto(prod21)
print(cat1.lista)

cat1.valor_total_categoria()



