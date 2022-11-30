import requests
import pickle
import os
from random import randint
from Partido import Partido
from Estadio import Estadio
from Equipo import Equipo
from Bebida import Bebida
from Alimento import Alimento
from Boleto import Boleto
import operator

def endpoint_json():

  url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'

  response = requests.request('GET',url) 

  return response.json()

def endpoint_e_json():
  url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json'
  
  response = requests.request('GET',url) 

  return response.json()

def endpoint_p_json():
  url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json'
  
  response = requests.request('GET',url) 

  return response.json()

def dict_equipos(endpoint,db):

  for equipos in endpoint:

      
      pais = equipos['name']
      codigo = equipos['fifa_code']
      grupo = equipos['group']
      cod2= equipos['id']

      equipo = Equipo(pais,codigo,grupo)

      db["equipos"][cod2] = equipo

      db['pais'].append(pais)

  return db 

def dict_estadios(endpoint,db):

  for estadios in endpoint:
    id = estadios["id"]
    name = estadios["name"]
    ubicacion = estadios["location"]
    capacidad = estadios["capacity"]
    restaurantes = estadios["restaurants"]

    for restaurante in restaurantes:
      nombre_r = restaurante['name']
    

    estadio = Estadio(name,ubicacion,capacidad,nombre_r)

    db["estadios"][id] = estadio

    db['restaurante_nombre'].append(nombre_r) 

    db['nombre_estadio'].append(name)

  return db

def dict_partidos(endpointb,endpoint,db):

  for partidos in endpoint:
    home_team = partidos["home_team"]
    away_team = partidos["away_team"]
    date = partidos["date"]
    stadium = partidos["stadium_id"]
    id = partidos["id"]

    for estadios in endpointb:
      if stadium == estadios['id']:
        disponibilidad = estadios['capacity']
        break
    
    partido = Partido(date,home_team,away_team,stadium,disponibilidad)

    db["partidos"][id] = partido

    db['fechas'].append(date)
    
  return db
    
def dict_restaurants(endpoint,db):
  for estadios in endpoint:
    for restaurants in estadios['restaurants']:
      name = restaurants['name']
      products = []
      for productos in restaurants['products']:
        if productos['type'] == "beverages":
          nameb = productos['name']
          cantidad = productos['quantity']
          price = productos['price'] + productos['price']*16/100
          if productos['adicional'] == "alcoholic":
            alcoholic = True
          else:
            alcoholic = False
    
          bebida = Bebida(nameb,cantidad,price,alcoholic)
    
          if nameb.lower() not in db['platillo']:
            db['platillo'].append(nameb.lower())
          
          products.append(bebida)
        else:
          nameb = productos['name']
          cantidad = productos['quantity']
          price = productos['price'] + productos['price']*16/100
          adicional = productos['adicional']
    
          alimento = Alimento(nameb,cantidad,price,adicional)
    
          products.append(alimento)

          if nameb.lower() not in db['platillo']:
            db['platillo'].append(nameb.lower())
      
      db["restaurantes"][name] = products

  return db
      
def menu_partidos(db):
  while True:
    while True:
      try:
        option = int(input('Ingrese la busqueda que desea realizar:\n1.-Buscar todos los partidos de un pais\n2.-Buscar todos los partidos de un estadio especifico\n3.-Buscar todos los partidos segun una fecha determinada\n4.-Regresar\n==> '))
        if option not in range(1,5):
          raise Exception
        break
      except:
        print("Ingreso invalido")

    if option == 1:
      print('\n')
      search_pais(db)
      print("\n")
    elif option == 2:
      print('\n')
      search_estadio(db)
      print('\n')
    elif option == 3:
      print("\n")
      search_date(db)
      print("\n")
    else:
      break

def recive_data_text(name_txt,db):
  """
  Parametro: La funcion recibe por parametro el diccionario db(dict) y un archivo.txt.
  Return: La funcion retorna el diccionario con los datos serializados en el archivo.txt.
  """

  binary_read = open(name_txt,'rb') # Se abre el archivo 

  if os.stat(name_txt).st_size != 0: # Se comprueba que no este vacio
    db = pickle.load(binary_read) # Si no esta vacio se extraen los datos en el diccionario

  binary_read.close() # Se cierra el archivo

  return db

def load_data_txt(name_txt,db):
  """
  Parametro: La funcion recibe por parametro el archivo de texto y el diccionario db(dict).
  Return: La funcion no retorna ningun valor, se encarga de serializar los datos contenidos en el diccionario en el archivo de texto.
  """
  # Se abre el archivo para hacer la escritura binaria
  binary_write = open(name_txt,'wb')

  db = pickle.dump(db,binary_write) #Se extraen los daos del diccionarioy se guardan en el txt

  binary_write.close() # Se cierra el archivo

def search_pais(db):
  while True:
    try:
      pais = input("Ingresa el nombre del pais que desea ver los partidos:\n==> ").title()
      if pais not in db['pais']:
        raise 
      break
    except:
      print('Ingrese un pais que participe en el mundial de Qatar 2022')
    
  for key,partido in db['partidos'].items():
    if (partido.get_equipolocal() == pais) or (partido.get_equipovisitante() == pais):
      print(db['estadios'][partido.get_estadio()].get_nombre())
      print(partido.show_partido())

def search_estadio(db):
  while True:
    try:
      nombre = input("Ingresa el nombre del estadio del que desea ver los partidos:\n==> ").title()
      if nombre not in db['nombre_estadio']:
        raise Exception
      break
    except:
      print('Ingrese un estadio valido para los partido de Qatar 2022')

  for key, estadio in db['estadios'].items():
    if estadio.get_nombre() == nombre:
      for key2,partido in db['partidos'].items():
        if key == partido.get_estadio():
          print(estadio.get_nombre())
          print(partido.show_partido())

def search_date(db):
  while True:
    try:
      fecha = input("Ingrese la fecha y hora de los partidos que desea ver (ejemplo 07/19/2022):\n==> ")
      for date in db['fechas']:
        if fecha in date:
          break
        raise Exception
      break
    except:
      print("Ingresa una fecha donde alla un partido del mundial")

  for key,partido in db['partidos'].items():
    if fecha in partido.get_date():
      print(db['estadios'][partido.get_estadio()].get_nombre())
      print(partido.show_partido())

def menu_restaurantes(db):
  while True:
    while True:
      try:
        option = int(input('Ingrese la busqueda de productos que desee realizar:\n1.-Buscar por nombre\n2.-Buscar por tipo\n3.-Buscar por rango de precio\n4.-Regresar\n==> '))
        if option not in range(1,5):
          raise Exception
        break
      except:
        print("Ingreso invalido")

    if option == 1:
      print("\n")
      search_nombre(db)
      print("\n")
    elif option == 2:
      print("\n")
      search_tipo(db)
      print("\n")
    elif option == 3:
      search_price(db)
    else:
      break

def search_nombre(db):
  while True:
    try:
      nombre = input("Ingrese el nombre de la bebida o alimento que desea ver:\n==> ").lower()
      if nombre not in db['platillo']:
        raise Exception
      break
    except:
      print("Ingrese un nombre valido")

  for key,menu in db['restaurantes'].items():
    for platillo in menu:
      if platillo.get_name().lower() == nombre:
        print(key)
        if platillo.get_alimento():
          print(platillo.show_alimento())
        else:
          print(platillo.show_bebida())
          if platillo.get_alcoholic():
            print("Tipo:Alcoholica")
          else:
            print("Tipo:No alcoholica")
        print('\n')

def search_tipo(db):
  while True:
    try:  
      option = input("Ingrese el tipo de platillo que desea ver (alimento o bebida):\n==> ").lower()
      if (option == "bebida") or (option == "alimento"):
        break
      raise Exception
    except:
      print('Ingreso invalido')

  for key,menu in db['restaurantes'].items():
    for platillo in menu:
      if option == 'alimento':
        if platillo.get_alimento():
          print(key)
          print(platillo.show_alimento())
          print('\n')
      else:
        if not platillo.get_alimento():
          print(key)
          print(platillo.show_bebida())
          print('\n')

def search_price(db):
  while True:
    try:
      inferior = int(input('Ingrese el precio minimo dispuesto a pagar:\n==> '))
      superior = int(input("Ingrese el precio maximo dispuesto a pagar:\n==> "))
      break
    except:
      print("Ingresa un valor valido")

  for key,menu in db['restaurantes'].items():
    for platillo in menu:
      if int(platillo.get_price()) in range(inferior,superior+1):
        print(key)
        if platillo.get_alimento():
          print(platillo.show_alimento())
          print('\n')
        else:
          print(platillo.show_bebida())
          print('\n')

def registrar_cliente(db):
  while True:
    try:
      nombre = input('Ingrese el nombre del cliente:\n==> ')
      if not nombre.isalpha():
        raise Exception
      cedula = int(input("Ingrese la cedula del cliente:\n==> "))
      edad = int(input("Ingrese la edad del cliente:\n==> "))
      for key, partido in db['partidos'].items():
        print(f"Id:{key}")
        print(db['estadios'][partido.get_estadio()].get_nombre())
        print(f"Asientos generales disponibles:{partido.get_disponibilidad()[0]}")
        print(f"Asientos vip disponibles:{partido.get_disponibilidad()[1]}")
        print(partido.show_partido())

      partido = int(input("Ingresa el id del partido que desea ver:\n==> "))
      if partido not in range(1,49):
        raise Exception

      tipo = input("Que tipo de entrada desea comprar (Vip o General):\n==> ").lower()
      if not tipo.isalpha():
        raise Exception
      break
    except:
      print('Ingreso invalido')
  if tipo == 'general':
    if db['partidos'][str(partido)].get_disponibilidad()[0] == 0:
      print("No hay mas asientos disponibles de este tipo")
    else:
      costo = 50 + 50*16/100
      print(f"El costo de su entrada vip es {50}")
      while True:
        code = random_code()
        if code not in db['code']:
          break
      print('\n')
      print(f'Factura N#{code}')
      print("Partido:")
      print(db['partidos'][str(partido)].show_partido())
      print("Subtotal:50")
      print("Descuento:0")
      print(f"IVA:{50*16/100}")
      print(f"Total:{costo}")

      print('\n')  
      option = input("Si esta de acuerdo con esta compra ingrese 0, sino ingrese cualquier tecla:\n==> ")
      if option != "0":
        print("No se realizo la transaccion")
        
      else:
        print("Pago exitoso")

        disponibilidad = db['partidos'][str(partido)].get_disponibilidad()[0] - 1
      
        db['partidos'][str(partido)].get_disponibilidad()[0] = disponibilidad
      
        boleto = Boleto(nombre,cedula,edad,str(partido),tipo,costo)
      
        db['partidos'][str(partido)].set_vendido(db['partidos'][str(partido)].get_vendido()+1)
        
        db['boletos'][code] = boleto

        db['boletos_totales'][code] = boleto
        
        db['code'].append(code)

        

  elif tipo == 'vip':
    if db['partidos'][str(partido)].get_disponibilidad()[1] == 0:
      print("No hay mas asientos disponibles de este tipo")
    else:
      costo = 120 + 120*16/100
      print(f'El costo de su entrada general es {120}')
      while True:
        code = random_code()
        if code not in db['code']:
          break
      print('\n')
      print(f'Factura N#{code}')
      print("Partido:")
      print(db['partidos'][str(partido)].show_partido())
      print("Subtotal:120")
      print("Descuento:0")
      print(f"IVA:{120*16/100}")
      print(f"Total:{costo}")
      
      print('\n')
      option = input("Si esta de acuerdo con esta compra ingrese 0, sino ingrese cualquier tecla:\n==> ")
      if option != "0":
        print("No se realizo la transaccion")
      else:
        print("Pago exitoso")
    
        disponibilidad = db['partidos'][str(partido)].get_disponibilidad()[1] - 1
      
        db['partidos'][str(partido)].get_disponibilidad()[1] = disponibilidad
      
        boleto = Boleto(nombre,cedula,edad,str(partido),tipo,costo)
      
        db['partidos'][str(partido)].set_vendido(db['partidos'][str(partido)].get_vendido()+1)
        
        db['boletos_vip'][code] = boleto

        db['boletos_totales'][code] = boleto

        db['code'].append(code)
  
def random_code():
  """
  Parametro: La funcion no recibe ningun parametro
  Return: La funcion retorna un codigo(str) de 8 numeros random.
  """
  random_list = []

  for i in range(8):
    x = randint(0,9) # Se usa la libreria random para buscar numeros aleatorios 
    random_list.append(str(x)) # Se a gregan los nuumeros a una lista
  
  code = ''.join(random_list) # Se unen concantenando strings
  
  return code  # Returnmos el codigo random

def registrar_asistencia(db):
  if len(db['boletos']) == 0 and len(db['boletos_vip']) == 0:
    print('No hay ningun boleto registrado')
  else:
    while True:
      try:
        tipo = input("Ingresa el tipo de boleto que posees (vip o general):\n==> ")
        if tipo != 'vip' and tipo != 'general':
          raise Exception
        code = int(input("Ingresa el codigo de 8 digitos de tu boleto:\n==> "))
        break
      except:
        print('Ingreso invalido')

    print(code)
    
    if str(code) in db['code']:
      if str(code) not in db['validado']:
        if tipo == 'vip':
          for key,boleto in db['boletos_vip'].items():
            if key == str(code):
              print("Asistencia validada")
              partido = boleto.get_partido()
              db["partidos"][partido].set_asistencia(db['partidos'][partido].get_asistencia()+1)
              db['validado'].append(str(code))        
        else:
          for key,boleto in db['boletos'].items():
            if key == str(code):
              print("Asistencia validada")
              partido = boleto.get_partido()
              db["partidos"][partido].set_asistencia(db['partidos'][partido].get_asistencia()+1)
              db['validado'].append(str(code))
      else:
        print("El boleto ya ha sido validado anteriormente")
    else:
      print("El boleto no es autentico, el codigo presentado no se encuentra en el sistema")
    
def venta_restaurantes(db):
  if len(db['boletos_vip']) == 0:
    print("No hay boletos vip en el sistema")
  else:
    while True:
      try:
        cedula = int(input("Ingresa la cedula enlazada al boleto vip:\n==> "))
        break
      except:
        print("Ingreso invalido")
    
    for key,boleto in db['boletos_vip'].items():
      if cedula == boleto.get_cedula():
        estadio = db['partidos'][boleto.get_partido()].get_estadio()
        nombre = db['estadios'][estadio].get_restaurante()
        for key,menu in db['restaurantes'].items():
          if key == nombre:
            for platillo in menu:
              print(key)
              if platillo.get_alimento():
                print(platillo.show_alimento())
                print('\n')
              else:
                print(platillo.show_bebida())
                print('\n')

    while True:
      seleccion = input("Ingrese el nombre del producto que desee:\n==> ").lower()
      if seleccion in db['platillo']:
        break
      else:
        print('Ingreso invalido')

    if boleto.get_edad() >=18:
      for key,boleto in db['boletos_vip'].items():
        if cedula == boleto.get_cedula():
          estadio = db['partidos'][boleto.get_partido()].get_estadio()
          nombre = db['estadios'][estadio].get_restaurante()
          for key,menu in db['restaurantes'].items():
            if key == nombre:
              for platillo in menu:
                if platillo.get_name().lower() == seleccion:
                  if platillo.get_cantidad() != 0:
                    costo = platillo.get_price()
                    if NumeroPerfecto(cedula):
                      descuento = costo * 15/100
                    else:
                      descuento = 0
                    print("\n")
                    print("Factura")
                    print(f'Restaurante:{nombre}')
                    print(f"Pedido:{seleccion}")
                    print(f"Subtotal:{costo}")
                    print(f"Descuento:{descuento}")
                    print(f'Total:{costo-descuento}')
  
                    option = input("Si esta de acuerdo con esta compra ingrese 0, sino ingrese cualquier tecla:\n==> ")
                    if option != "0":
                      print("No se realizo la transaccion")
                    else:
                      print("Pago exitoso")
  
                      platillo.set_cantidad(platillo.get_cantidad()-1)

                      boleto.set_costo(boleto.get_costo() + (costo-descuento))

                  else:
                    print("No queda mas stock de este producto")
    else:
      for key,boleto in db['boletos_vip'].items():
        if cedula == boleto.get_cedula():
          estadio = db['partidos'][boleto.get_partido()].get_estadio()
          nombre = db['estadios'][estadio].get_restaurante()
          for key,menu in db['restaurantes'].items():
            if key == nombre:
              for platillo in menu:
                  if platillo.get_name().lower() == seleccion:
                    if platillo.get_cantidad() != 0:
                      if platillo.get_alimento():
                        costo = platillo.get_price()
                        if NumeroPerfecto(cedula):
                          descuento = costo * 15/100
                        else:
                          descuento = 0
                        print("\n")
                        print("Factura")
                        print(f'Restaurante:{nombre}')
                        print(f"Pedido:{seleccion}")
                        print(f"Subtotal:{costo}")
                        print(f"Descuento:{descuento}")
                        print(f'Total:{costo-descuento}')
  
                        option = input("Si esta de acuerdo con esta compra ingrese 0, sino ingrese cualquier tecla:\n==> ")
                        if option != "0":
                          print("No se realizo la transaccion")
                        else:
                          print("Pago exitoso")
  
                          platillo.set_cantidad(platillo.get_cantidad()-1)

                          boleto.set_costo(boleto.get_costo() + (costo-descuento))
                     
                      else:
                        if platillo.get_alcoholic():
                          print("Al ser menor de edad no puedes pedir bebidas alcoholicas")
                        else:
                          costo = platillo.get_price()
                          if NumeroPerfecto(cedula):
                            descuento = costo * 15/100
                          else:
                            descuento = 0
                          print("\n")
                          print("Factura")
                          print(f'Restaurante:{nombre}')
                          print(f"Pedido:{seleccion}")
                          print(f"Subtotal:{costo}")
                          print(f"Descuento:{descuento}")
                          print(f'Total:{costo-descuento}')
  
                          option = input("Si esta de acuerdo con esta compra ingrese 0, sino ingrese cualquier tecla:\n==> ")
                          if option != "0":
                            print("No se realizo la transaccion")
                          else:
                            print("Pago exitoso")
                            
                            platillo.set_cantidad(platillo.get_cantidad()-1)

                            boleto.set_costo(boleto.get_costo() + (costo-descuento))
                    else:
                        print("No hay mas stock de este producto")     
                      
def NumeroPerfecto(num):
	suma = 0
	for i in range(1,num):
		if (num % (i) == 0):
			suma += (i)
	if num == suma:
		return True
	else:
		return False

def menu_estadisticas(db):
  while True:
    while True:
      try:
        option = int(input('Ingrese las estadisticas que desea visualizar:\n1.-Promedio de gasto de un cliente VIP en un partido\n2.-Tabla de asistencia a los partidos\n3.-Partido con mayor asistencia\n4.-Partido con mayor boletos vendidos\n5.-Top 3 productos más vendidos en el restaurante\n6.-Top 3 de clientes\n7.-Regresar\n==> '))
        if option not in range(1,8):
          raise Exception
        break
      except:
        print("Ingreso invalido")
    if option == 1:
      print("\n")
      promedio_vip = promedio(db)
      print(f"El promedio de gato de un cliente VIP es {promedio_vip}")
      print("\n")
    elif option == 2:
      print("\n")
      tabla_asistencia(db)
    elif option == 3:
      print("\n")
      mayor_asistencia(db)
    elif option == 4:
      print("\n")
      mayor_vendido(db)
    elif option == 5:
      print("\n")
      productos_vendidos(db)
      print("\n")
    elif option == 6:
      print("\n")
      clientes_vendidos(db)
      print("\n")
    else:
      break

def promedio(db):
  suma = 0
  boletos = 0
  for key, boleto in db['boletos_vip'].items():
    suma += boleto.get_costo()
    boletos += 1 
	if boletos == 0:
        print("No hubo ventas de clientes vip")
    else:
     promedio = suma/boletos
     return promedio



def tabla_asistencia(db):
  asistencias = {}
  for key,partido in db['partidos'].items():
    asistencias[key] = partido.get_asistencia()

  asistencias_sort = sorted(asistencias.items(),key=operator.itemgetter(1),reverse=True)
  
  for asistencia in asistencias_sort:
    for key,partido in db['partidos'].items():
      if asistencia[0] == key:
        estadio = partido.get_estadio()
        vendido = partido.get_vendido()
        print(db['estadios'][estadio].get_nombre())
        print(f"Boletos vendidos:{vendido}")
        print(f"Asistencia:{asistencia[1]}")
        if vendido == 0:
          print(f"Relacion asistencia/venta:{0}")
        else:
          print(f"Relacion asistencia/venta:{asistencia[1]/vendido}")
        print(partido.show_partido())

def mayor_asistencia(db):
  asistencias = {}
  for key,partido in db['partidos'].items():
    asistencias[key] = partido.get_asistencia()

  asistencias_sort = sorted(asistencias.items(),key=operator.itemgetter(1),reverse=True)

  for key,partido in db['partidos'].items():
    if key == asistencias_sort[0][0]:
      estadio = partido.get_estadio()
      vendido = partido.get_vendido()
      print(db['estadios'][estadio].get_nombre())
      print(f"Boletos vendidos:{vendido}")
      print(f"Asistencia:{asistencias_sort[0][1]}")
      if vendido == 0:
        print(f"Relacion asistencia/venta:{0}")
      else:
        print(f"Relacion asistencia/venta:{asistencias_sort[0][1]/vendido}")
      print(partido.show_partido())

def mayor_vendido(db):
  vendidos = {}
  for key,partido in db['partidos'].items():
    vendidos[key] = partido.get_vendido()

  vendidos_sort = sorted(vendidos.items(),key=operator.itemgetter(1),reverse=True)

  for key,partido in db['partidos'].items():
    if key == vendidos_sort[0][0]:
      estadio = partido.get_estadio()
      asistencia = partido.get_asistencia()
      print(db['estadios'][estadio].get_nombre())
      print(f"Boletos vendidos:{vendidos_sort[0][1]}")
      print(f"Asistencia:{asistencia}")
      if vendidos_sort[0][1] == 0:
        print(f"Relacion asistencia/venta:{0}")
      else:
        print(f"Relacion asistencia/venta:{asistencia/vendidos_sort[0][1]}")
      print(partido.show_partido())

def productos_vendidos(db):
  while True:
    try:
      for nombre in db['restaurante_nombre']:
        print(nombre)
      option = input('Ingresa el nombre del restaurante que deseas revisar:\n==> ').title()
      if option not in db['restaurante_nombre']:
        raise Exception
      break
    except:
      print("Ingreso invalido")

  platillos = {}
  
  for key,menu in db['restaurantes'].items():
    if key == option:
      for platillo in menu:
        platillos[platillo.get_name()] = platillo.get_cantidad()
      
  platillos_sort = sorted(platillos.items(),key=operator.itemgetter(1),reverse=False)

  n = 0
  while n != 3:
    for key,menu in db['restaurantes'].items():
      if key == option:
        for platillo in menu:
          if platillos_sort[n][0] == platillo.get_name():
            if platillo.get_alimento():
              print("\n")
              print(option)
              print(platillo.show_alimento())
            else:
              print("\n")
              print(option)
              print(platillo.show_bebida())
    n +=1

def clientes_vendidos(db):
  clientes = []

  for key,boleto in db['boletos_vip'].items():
    cedula = boleto.get_cedula()
    clientes.append(cedula)

  for key,boleto in db['boletos'].items():
    cedula = boleto.get_cedula()
    clientes.append(cedula)
  clientes.append('a')
  boletos = {}


  if len(clientes) != 0:
    while True:
      count = 0
      x = clientes[0]
      for cliente in clientes:
        if clientes[0] == cliente:
          count +=1
  
      boletos[x] = count
  
      for cliente in clientes:
        clientes.remove(x)
          
          
      if len(clientes) == 1:
        break
  
    boletos_sort = sorted(boletos.items(),key=operator.itemgetter(1),reverse=True)
  
    n = 0
    while n!=3:
      if len(boletos_sort) > n:
        for key,boleto in db['boletos_totales'].items():
          if boleto.get_cedula() == boletos_sort[n][0]:
            print(f'Nombre:{boleto.get_nombre()}')
            print(f"Edad:{boleto.get_edad()}")
            print(f"Cedula:{boleto.get_cedula()}")
            print(f"Cantidad de boletos:{boletos_sort[n][1]}")
            print("\n")
            break
        n +=1
      else:
        break
  else:
    print("No hay clientes registrados en el sistema")
    
