from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
import time
personas: Persona = []
productos: Producto = []
factutas: Factura = []


def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            persona.nombres = str(input("Ingrese nuevo nombre: "))
            Persona.convertir_a_string(persona)


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)

def producto():
    print("¿Desea ver nuestro catálogo?, escribir SI, sí así lo desea")
    ver=input()

    if ver=="SI":
        print("Aquí esta nuestros productos")
        print("     CELULARES:       ")
        print("     |CODIGO: 6049702568465|CELULAR:Galaxy A03 Core 6.5'' 2GB 3rm|PRECIO: S/ 379.00|MARCA:SAMSUNG|                                                                     |")                                                                                      
        print("     |CODIGO: 6049704587895|CELULAR:Galaxy A13 6.59'' 4GB 64GB 50+5+2+2MP Negro|PRECIO: S/ 699.00|MARCA:SAMSUNG|                                                       |")
        print("     LAPTOPS:         ")
        print("     |CODIGO: 6049702875345|Laptop ASUS FX506LH-HN100T 15.6'' Intel Core i7 10ma generación 16GB 512GB SSD|PRECIO: S/ 4,599.00|MARCA:ASUS|                             |")
        print("     |CODIGO: 6049702146205|Laptop Gamer Acer Predator Helios 300 17.3 Intel Core i7 11800H 16GB RAM 512GB SSD RTX 3060 6GB Video Negro|PRECIO: S/ 9,299.00|MARCA:ACER |")  
        print("     TABLETS           ")
        print("     |CODIGO: 6049703457675|TABLET:SAMSUNG Galaxy A8 10.5'' 32gb Gris|PRECIO: S/ 1,049.00|MARCA:SAMSUNG|                                                               |")
        print("     |CODIGO: 6049703767305|TABLET:LENOVO TB-X606F 10.4'' 4GB 64GB HDD Negro|PRECIO: S/ 899.00|MARCA:LENOVO|                                                           |")
        print("     TELEVISORES:      ")
        print("     |CODIGO: 6049702943825|TELEVISOR:Neo QLED 65'' UHD 4K Smart Tv|PRECIO: S/5,799.00|MARCA:SAMSUNG|                                                                  |")
        print("     |CODIGO: 6049703025035|TELEVISOR:NanoCell UHD 4K ThinQ AI|PRECIO: S/4,799.00|MARCA:LG|                                                                            |")
        print("     EQUIPOS DE SONIDO:")
        print("     |CODIGO: 6049703487245|MINICOMPONENTE: PANASONIC 2000W SC-AKX730PUK Negro|PRECIO: S/ 1,499.00|MARCA:PANASONIC|                                                    |")
        print("     |CODIGO: 6049703497565|MINICOMPONENTE: PANASONIC SC-TMAX50PUK Negro|PRECIO: S/ 1,999.00|MARCA:PANASONIC|                                                          |")
        print("     SMARTWATCH:       ")
        print("     |CODIGO: 6049702645175|SMARTWATCH: HUAWEI Fit New Negro|PRECIO: S/ 439.00|MARCA:HUAWEI|                                                                           |")
        print("     |CODIGO: 6049702789285|SMARTWATCH: SLIDE SLEDGE multideporte Ip65 Negro: S/ 159.90|MARCA:SLIDE SLEDGE|                                                            |")
        print("     VIEDOJUEGOS:      ")
        print("     |CODIGO: 6049703427795|CONSOLA: Ps5 Con Lector De Discos+Audifono Pulse 3D Negro + Mando Negro|PRECIO: S/ 6,199.00|MARCA:SONY|                                    |")
        print("     |CODIGO: 6049703567045|CONSOLA: Ps5 con Lector de Discos + Dirt 5 + Rainbowsix + Control|PRECIO: S/ 5,856.00|MARCA:SONY|                                          |")
    print("¿Que producto desea comprar?")
    print("Tenemos: celulares, laptops, tablets, televisores, equipos de sonido, smartwatch, videojuegos")
    desea_comprar=input()

    if desea_comprar=="celulares":
        print("Aquí tenemos los celulares")
        print("     |CODIGO: 6049702568465|CELULAR:Galaxy A03 Core 6.5'' 2GB 3rm|PRECIO: S/ 379.00|MARCA:SAMSUNG")                                                                                      
        print("     |CODIGO: 6049704587895|CELULAR:Galaxy A13 6.59'' 4GB 64GB 50+5+2+2MP Negro|PRECIO: S/ 699.00|MARCA:SAMSUNG|")
    else:
        if desea_comprar=="laptops":
            print("Aquí tenemos las laptops")
            print("     |CODIGO: 6049702875345|Laptop ASUS FX506LH-HN100T 15.6'' Intel Core i7 10ma generación 16GB 512GB SSD|PRECIO: S/ 4,599.00|MARCA:ASUS|")
            print("     |CODIGO: 6049702146205|Laptop Gamer Acer Predator Helios 300 17.3 Intel Core i7 11800H 16GB RAM 512GB SSD RTX 3060 6GB Video Negro|PRECIO: S/ 9,299.00|MARCA:ACER|") 
        else:
            if desea_comprar=="tablets":
                print("Aquí tenemos las tablets")
                print("|CODIGO: 6049703457675|TABLET:SAMSUNG Galaxy A8 10.5'' 32gb Gris|PRECIO: S/ 1,049.00|MARCA:SAMSUNG|")
                print("|CODIGO: 6049703767305|TABLET:LENOVO TB-X606F 10.4'' 4GB 64GB HDD Negro|PRECIO: S/ 899.00|MARCA:LENOVO|")
            else:
                if desea_comprar=="televisores":
                    print("Aquí tenemos las televisores")
                    print("CODIGO: 6049702943825|TELEVISOR:Neo QLED 65'' UHD 4K Smart Tv|PRECIO: S/5,799.00|MARCA:SAMSUNG|")
                    print("CODIGO: 6049703025035|TELEVISOR:NanoCell UHD 4K ThinQ AI|PRECIO: S/4,799.00|MARCA:LG|")
                else:
                    if desea_comprar=="equipos de sonido":
                        print("Aquí tenemos equipos de sonido")
                        print("CODIGO: 6049703487245|MINICOMPONENTE: PANASONIC 2000W SC-AKX730PUK Negro|PRECIO: S/ 1,499.00|MARCA:PANASONIC|")
                        print("CODIGO: 6049703497565|MINICOMPONENTE: PANASONIC SC-TMAX50PUK Negro|PRECIO: S/ 1,999.00|MARCA:PANASONIC|")
                    else:
                        if desea_comprar=="smartwatch":
                            print("Aquí tenemos los smartwatch")
                            print("CODIGO: 6049702645175|SMARTWATCH: HUAWEI Fit New Negro|PRECIO: S/ 439.00|MARCA:HUAWEI|")
                            print("CODIGO: 6049702789285|SMARTWATCH: SLIDE SLEDGE multideporte Ip65 Negro: S/ 159.90|MARCA:SLIDE SLEDGE|")
                        else:
                            if desea_comprar=="videojuegos":
                                print("Aquí tenemos los videojuegos")
                                print("CODIGO: 6049703427795|CONSOLA: Ps5 Con Lector De Discos+Audifono Pulse 3D Negro + Mando Negro|PRECIO: S/ 6,199.00|MARCA:SONY|")
                                print("CODIGO: 6049703567045|CONSOLA: Ps5 con Lector de Discos + Dirt 5 + Rainbowsix + Control|PRECIO: S/ 5,856.00|MARCA:SONY|")
    print("Llene los datos para agregar al carrito de compras")
    print("Más adelante ya se les pedirá los datos para ya comprarlos")

    codigo: str = str(input("Ingrese código del producto: "))
    nombre: str = str(input("Ingrese nombre del producto: "))
    precio: float = float(input("Ingrese precio del producto: "))
    marca: str = str(input("Ingrese marca del producto: "))
    producto: Producto = Producto(codigo, nombre, precio, marca)
    productos.append(producto)


def listar_producto():
    for producto in productos:
        Producto.convertir_a_string(producto)


def buscar_producto():
    codigo: str = str(input("Ingrese Código para buscar el producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            return producto


def nueva_factura():
    print("Para seguir con la compra llene estos datos")
    print("Para generar una factura busca un cliente")
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(factutas)+1, cliente)
    continuar: bool = True

    while continuar:

        producto: Producto = buscar_producto()
        cantidad: int = int(input("Ingrese la cantidad: "))
        factura.detalle.append(FacturaDetalle(
            producto.codigo, producto.nombre, cantidad, producto.precio,))

        condicion: str = str(input("SI para agregar productos: "))

        if condicion == "SI":
            continuar = True
        else:
            continuar = False
            factura.calcular_igv()
            factutas.append(factura)


def listar_factura():
    for factura in factutas:
        Factura.convertir_a_string(factura)


def buscar_factura():
    numero: int = int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero == numero:
            Factura.convertir_a_string(factura)
            print("===========================")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)


def main():
    continuar: bool = True

    while continuar:
        print("********************************************")
        print("***********💲SISTEMA DE VENTAS💲************ ")
        print("--------------------------------------------")
        print("                QUE SOMOS 🗯                ")
        print("______________________________________________________________________________________")
        print("Somos una empresa de tecnología dedicada a complacer las necesidades de comunicación,|")
        print("postura e incrementación de nuestros clientes. A través de servicios altamente       |")
        print("competitivos, productos de la más alta tecnología y estándares de calidad. Todo es   |")
        print("gracias a la sinergia del equipo profesional que trabaja en conjunto y aplica sus    |")
        print("habilidades para brindar un servicio que deleita a los clientes.                     |")
        print("--------------------------------------------------------------------------------------")
        print("=====================MENÚ===================")
        print("****************INGRESE OPCIONES************")
        print("    PARA AGREGAR   PERSONA   ESCRIBA 1")
        print("    PARA LISTAR    PERSONAS  ESCRIBA 2")
        print("    PARA BUSCAR    PERSONA   ESCRIBA 3")
        print("    PARA EDITAR    PERSONA   ESCRIBA 4")
        print("    PARA ELIMINAR  PERSONA   ESCRIBA 5")
        print("    PARA AGREGAR   PRODUCTO  ESCRIBA 6")
        print("    PARA LISTAR    PRODUCTO  ESCRIBA 7")
        print("    PARA CREAR     FACTURA   ESCRIBA 8")
        print("    PARA LISTAR    FACTURA   ESCRIBA 9")
        print("    PARA BUSCAR    FACTURA   ESCRIBA 10")
        print("    PARA SALIR ESCRIBA 20")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                producto()
            case "7":
                listar_producto()
            case "8":
                nueva_factura()
            case "9":
                print(
                    "____________________________________________________________________________")
                print(
                    "                                      |    HIGHLAND TECHNOLOGY             |")
                print(
                    "                                      |    RUC: 20100070970                |")
                print(
                    "                                      |    HIGHLAND TECHNOLOGY S.A.C.      |")
                print(
                    "                                      |    Jr. San Martin, Juliaca 21103   |")
                print(
                    " _____________________________________|____FECHA Y HORA____________________|")
                fecha_hora=time.ctime()
                print(fecha_hora)
                print(
                    "______________________________________________________________________________________")
                listar_factura()
                print(" ")
                print("¿Cuanto es el monto que va a pagar?")
                monto_pagar=int(input())
                print(
                    "❗❗SI REALIZA UN RECLAMO SOBRE EL PRODUCTO, TIENE '48 HRS' PARA EFECTUARLO❗❗ ")
                print("Que tenga un buen día 😄")
                print(" ")
            case "10":
                buscar_factura()
            case "20":
                print("¿Desea finalizar? si o no")
                finalizar=input()
                if finalizar=="si":
                    print("¡Hasta la próxima!🖐️")
                    continuar = False
                else:
                    print("Continue 👍")
                    continuar = True

if __name__ == '__main__':
    main()
