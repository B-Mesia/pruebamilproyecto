class Estadio():
    def __init__(self,nombre, ubicacion,capacidad,restaurante):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.restaurante = restaurante


    def get_nombre(self):
        return self.nombre
    def set_nombre(self,new_nombre):
     self.nombre = new_nombre
    def get_ubicacion(self):
        return self.ubicacion
    def get_restaurante(self):
      return self.restaurante
    def set_ubicacion(self,new_ubicacion):
     self.ubicacion= new_ubicacion
    def get_capacidad(self):
      return self.capacidad
    def set_capacidad(self,new_capacidad):
      self.capacidad = new_capacidad
    def set_restaurante(self,new_restaurante):
      self.restaurante = new_restaurante

    def show_estadio(self):
        return f'Nombre:{self.nombre}\nUbicacion:{self.ubicacion}\n'