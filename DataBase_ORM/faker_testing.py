from unittest import main
import db
from models import Producto
from faker import Faker
from faker.providers import DynamicProvider
from random import randint

#Diccionario con los precios de los productos
dict_price_product = {
    "Arroz":12,"Fideos":11.5,"Azucar":15.3,"Harina":35.1,"Frutos Secos":65.2
}

def crearProductos(cant_products):
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
        precio = round(dict_price_product[nombre] * cantidad,2) 
        print(f"{nombre}: {cantidad} : {precio}")
        
if (__name__=='__main__'):
    crearProductos(4)