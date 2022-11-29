class Bebida():
  def __init__(self,name,cantidad,price,alcoholic):
    self.name = name
    self.cantidad = cantidad
    self.price = price
    self.alcoholic = alcoholic
    self.alimento = False

  def get_name(self):
    return self.name
  def get_cantidad(self):
    return self.cantidad
  def get_price(self):
    return self.price
  def get_alcoholic(self):
    return self.alcoholic
  def get_alimento(self):
    return self.alimento

  def set_name(self,new_name):
    self.name = new_name
  def set_cantidad(self,new_cantidad):
    self.cantidad = new_cantidad
  def set_price(self,new_price):
    self.price = new_price
  def set_alcoholic(self,new_alcoholic):
    self.aalcoholic = new_alcoholic
  def set_bebida(self,new_bebida):
    self.alimento = new_bebida

  def show_bebida(self):
    return f'Nombre:{self.name}, Cantidad:{self.cantidad}\nPrecio:{self.price}'