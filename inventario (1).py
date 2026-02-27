class Producto():
    def __init__(self,nom,prec,stok):
        self.nombre=nom
        self.precio=prec
        self.stock=stok

    def aplicar_descuento(self,porcentaje):
        self.precio*=(1-porcentaje)
        print(f"el nuevo precio del producto {self.nombre} es {self.precio}")

    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("no puedes tener stock negativo")
        else:
            self.stock+=cantidad
            print(f"la nueva cantidad es {self.stock}")

class Categoria():
    def __init__(self,nomb):
        self.nombre_cat=nomb
        self.lista=[]

    def agregar_producto(self,producto):
        self.lista.append(producto)
        print(f"el producto {producto.nombre} se agrego a la lista")

    def valor_total_categorias(self):
        suma=0
        for m in self.lista:
            suma+=m.precio*m.stock
        print(f"El precio total de la categoria {self.nombre_cat} es {suma} pesos")
        

class Pedido():
    def __init__(self,cliente):
        self.cliente=cliente
        self.lista_comprados=[]
        self.estado="Pendiente" 
    
    def agregar_producto(self,product):       
        self.lista_comprados.append(product)
        print(f"Agregaste el producto {product.nombre}al carrito")
        
    def calcula_total(self):
        total=0
        for x in self.lista_comprados:
            total+=x.precio
        print(f" El total de productos comprados rd:${total}, el iva es ${0.16*total} y dando sumanso ${1.16*total:0.2f}")
        
    def finalizar_pedido(self,listab):
        self.estado="Completado"
        for x in  self.lista_comprados:
            for y in listab:
               if x.nombre==y.nombre:
                  y.stock-=1
                  print(f"El producto {y.nombre} se le quito un elemento")
                    