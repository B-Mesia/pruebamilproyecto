
class Partido:
  def __init__(self,date,equipolocal, equipovisitante, estadio,disponibilidad):
    self.date = date
    self.equipolocal = equipolocal
    self.equipovisitante = equipovisitante
    self.estadio = estadio
    self.asistencia = 0
    self.disponibilidad = disponibilidad
    self.vendido = 0


  def get_date(self):
    return self.date
  
  def get_equipolocal(self):
    return self.equipolocal

  def get_equipovisitante(self):
    return self.equipovisitante
  def get_estadio(self):
    return self.estadio

  def get_disponibilidad(self):
    return self.disponibilidad

  def get_asistencia(self):
    return self.asistencia

  def get_vendido(self):
    return self.vendido
  
  def set_date(self,new_date):
    self.date = new_date
  def set_equipolocal(self,new_equipolocal):
    self.equipolocal = new_equipolocal

  def set_equipovisitante(self,new_equipovisitante):
    self.equipovisitante = new_equipovisitante
  def set_estadio(self,new_estadio):
    self.estadio = new_estadio

  def set_asistencia(self,new_asistencia):
    self.asistencia = new_asistencia

  def set_disponibilidad(self,new_disponibilidad):
    self.disponibilidad = new_disponibilidad

  def set_vendido(self,new_vendido):
    self.vendido = new_vendido
  
  def show_partido(self):
    return f'Date:{self.date}\nEquipo local:{self.equipolocal}\nEquipo visitante:{self.equipovisitante}\n'