import db #enlace ala base de datos
from models import Producto #estructura de cada registro de la base de datos
# Modulo faker se encarga de crear los datos 
from faker import Faker
from faker.providers import DynamicProvider
from random import randint #funcion de numeros enteros aleatorios

#Diccionario con los precios de los productos
dict_price_product = {
    "Arroz":12,"Fideos":11.5,"Azucar":15.3,"Harina":35.1,"Frutos Secos":65.2
}

def crearProductos(cant_products):
    """Crea nuevos productos utilizando la libreria de faker de Python"""
    products_provider = DynamicProvider(
        provider_name="products_objects",
        elements=["Arroz","Fideos","Azucar","Harina","Frutos Secos"],
    )
    #Instancia de Faker
    fake = Faker()
    # agrego el nuevo proovedor a la instancia de faker
    fake.add_provider(products_provider)

    for _ in range(cant_products):
        nombre = fake.products_objects()#Obtengo un producto al azar
        cantidad = randint(100,300)#Una cantidad entre 100 y 300 kg
        #el precio se obtiene calculando el precio del producto por la cantidad
        total = round(dict_price_product[nombre] * cantidad,2)
        #Creo un producto con los valores
        producto = Producto(nombre,total,cantidad) 
        #ahora lo agrego ala sesion de la base de datos
        db.session.add(producto)
        #print(f"{nombre}: {cantidad} : {precio}")
    ##Guardo los cambios en la base de datos
    db.session.commit()

if __name__ == '__main__':
    #Base de datos Instancia
    db.Base.metadata.create_all(db.engine)
    #Crear almenos 4 productos nuevos
    crearProductos(4)
	#Obtengo los productos con una query simple
    productos = db.session.query(Producto).all()
    
    for producto in productos:
        print("Producto {0}:  {1}".format(producto.getId(),producto))
