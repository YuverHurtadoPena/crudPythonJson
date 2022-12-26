from libreria import*

bandera=True

def crearP():
    nombreP=input('Ingresa el nombre del producto-->')
    precioP= input('ingresa el precio del producto-->')

    listaInf=buscarProducto(nombreP)
    band=False
    for i in listaInf:
        if i['nombreProducto']==nombreP:
            band=True
    if band==True:
        print("El producto ya existe")
    else:
        insertarP(nombreP, precioP)

def buscarP():
    nombreP=input('Ingresa el nombre del producto a buscar-->')
    listaInf=buscarProducto(nombreP)
    for i in listaInf:
        print("Nombre-->"+i['nombreProducto'])
        print("Precio-->"+i['precio'])


def eliminarP():
    nombreP=input('Ingresa el nombre del producto a eliminar-->')
    delete(nombreP)

def actualizar():
    
    actualizarp()

def listarAll():
    data=mostrarTodo()
    cont=0
    for i in data['infoArchivo']:
        cont= cont+1
        print('---------------------------')
        print("-----"+"Numero Producto:"+str(cont)+"----")
        print("Nombre:"+i["nombreProducto"])
        print("Precio:"+i["precio"])
        print('---------------------------')
          

while bandera!=False:
    print('1.Registrar producto')
    print('2.Buscar producto')
    print('3.Eliminar producto')
    print('4.Actualizar producto')
    print('5.listar todo')
    print('6.Salir')
    opcion=input('-->')
    
    if int(opcion)==1:
        crearP()
    if int(opcion)==2:
        buscarP()

    if int(opcion)==3:
        eliminarP()
    if int(opcion)==4:
        actualizar()
    if int(opcion)==5:
        listarAll()
    if int(opcion)==6:
        print('gracias por usar la aplicacion!!')
        bandera = False
    if int(opcion)<1 or int(opcion)>6:
        print("Error de opción")

        