import json
import os

def insertarP(nombreProducto, precio):
    data={}

    data['infoArchivo']=[]
    with open('data.json')as file:
        filesize=os.path.getsize('data.json')
        if filesize >0:
            dataq=json.load(file)

            dataq['infoArchivo'].append({
                'nombreProducto':nombreProducto,
                'precio':precio
            })

            with open('data.json','w')as file:
                json.dump(dataq, file, indent=4)
            
        else:
            data['infoArchivo'].append({
                 'nombreProducto':nombreProducto,
                'precio':precio
            })
            with open('data.json','w')as file:
                json.dump(data, file, indent=4)
        print('-------------------------------')
        print('producto guardado con exito')
        print('-------------------------------')

def buscarProducto(nombreP):
    
    with open('data.json')as file:
        data=json.load(file)
        inf=[]
        for i in data['infoArchivo']:
            if i["nombreProducto"]==nombreP:
                inf.append(i)
    return inf


def mostrarTodo():
    
    with open('data.json')as file:
        data=json.load(file)
        
    return data



def delete(nombreProducto):
    data={}

    data['infoArchivo']=[]
    with open('data.json')as file:
        filesize=os.path.getsize('data.json')
        if filesize >0:
            dataq=json.load(file)
            informacion={}

            informacion['infoArchivo']=[]
            band=False

            for i in dataq['infoArchivo']:
                if i["nombreProducto"]==nombreProducto:
                    band=True
                   
                else:
                    informacion['infoArchivo'].append({
                        'nombreProducto':i['nombreProducto'],
                        'precio':i['precio']
                    })
                    
          
            with open('data.json','w')as file:
                json.dump(informacion, file, indent=4)
            
            if band==True:
                print("Producto eliminado con exito")
            else:
                print("El producto no existe")

            
        else:
            print("El producto no existe")


def actualizarp():
    nombreProducto=input('Ingresa el nombre del producto a actualizar-->')
    precio=input('Ingresa el nuevo precio-->')
    print("zdd"+precio)
    data={}

    data['infoArchivo']=[]
    with open('data.json')as file:
        filesize=os.path.getsize('data.json')
        if filesize >0:
            dataq=json.load(file)
            information={}

            information['infoArchivo']=[]
            band=False

            for i in dataq['infoArchivo']:
                if i["nombreProducto"]==nombreProducto:
                    information['infoArchivo'].append({
                        'nombreProducto':i['nombreProducto'],
                        'precio':precio
                    })
                    band=True
                   
                else:
                    information['infoArchivo'].append({
                        'nombreProducto':i['nombreProducto'],
                        'precio':i['precio']
                    })
                    
          
            with open('data.json','w')as file:
                json.dump(information, file, indent=4)
            
            if band==True:
                print("Producto actualizado con exito")
            else:
                print("El producto no existe")

            
        else:
            print("El producto no existe")
       