class Boleto():
  def __init__(self,nombre,cedula,edad,partido,tipo,costo):
    self.nombre = nombre
    self.cedula = cedula
    self.edad = edad
    self.partido = partido
    self.costo = costo

  def get_nombre(self):
    return self.nombre
  def get_cedula(self):
    return self.cedula
  def get_edad(self):
    return self.edad
  def get_partido(self):
    return self.partido
  def get_tipo(self):
    return self.tipo
  def get_costo(self):
    return self.costo

  def set_nombre(self,new_nombre):
    self.nombre = new_nombre

  def set_cedula(self,new_cedula):
    self.cedula = new_cedula

  def set_edad(self,new_edad):
    self.edad = new_edad

  def set_partido(self,new_partido):
    self.partido = new_partido

  def set_tipo(self,new_tipo):
    self.tipo = new_tipo

  def set_costo(self,new_costo):
    self.costo = new_costo