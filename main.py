from funciones import *



def main():
  db = {
    'equipos':{
    },
    'partidos':{
    },
    'estadios':{
    },
    'restaurantes':{   
    },
    'boletos':{
    },
    'boletos_vip':{
    },
    'boletos_totales':{
    },
    'pais':[
    ],
    'nombre_estadio':[
    ],
    'fechas':[
    ],
    'platillo':[
    ],
    'code':[
    ],
    'validado':[
    ],
    'restaurante_nombre':[
    ]
    }

  equipos = endpoint_json()

  estadios = endpoint_e_json()

  partidos = endpoint_p_json()

  db = dict_equipos(equipos, db)

  db = dict_estadios(estadios,db)

  db = dict_restaurants(estadios,db)

  db = dict_partidos(estadios,partidos,db)
  
  #db = recive_data_text('base_txt',db)

  while True:
   
    print('Bienvenidos a al mundial de quatar 2022')

    print("\n")
    
    while True:
      try:
        option = int(input("Ingrese la seccion a la que desea avanzar:\n1.-Gestion de partidos y estadios\n2.-Gestion de venta de entradas\n3.-Gestion de asistencia\n4.-Gestion de restaurantes\n5.-Gestion de venta de restaurantes\n6.-Estadisticas\n7.-Salir\n==> "))
  
        if option not in range(1,8):
          raise Exception
        break
      except:
        print("Ingreso invalido")  

    if option == 1:
      print('\n')
      menu_partidos(db)
      load_data_txt('base_txt',db)
      print('\n')
    elif option == 2:
      print('\n')
      registrar_cliente(db)
      load_data_txt('base_txt',db)
      print("\n")
    elif option == 3:
      print('\n')
      registrar_asistencia(db)
      load_data_txt('base_txt',db)
      print("\n")
    elif option == 4:
      print('\n')
      menu_restaurantes(db)
      load_data_txt('base_txt',db)
      print("\n")
    elif option == 5:
      print('\n')
      venta_restaurantes(db)
      load_data_txt('base_txt',db)
      print("\n")
    elif option == 6:
      print('\n')
      menu_estadisticas(db)
      print("\n")
    else:
      print("\n")
      print("Gracias por su visita")
      print('Vuelva pronto')
      break
  

main()
   