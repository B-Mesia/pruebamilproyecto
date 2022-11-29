class Alimento():
  def __init__(self,name,cantidad,price,adicional):
    self.name = name
    self.cantidad = cantidad
    self.price = price
    self.adicional = adicional
    self.alimento = True

  def get_name(self):
    return self.name
  def get_cantidad(self):
    return self.cantidad
  def get_price(self):
    return self.price
  def get_adicional(self):
    return self.adicional
  def get_alimento(self):
    return self.alimento

  def set_name(self,new_name):
    self.name = new_name
  def set_cantidad(self,new_cantidad):
    self.cantidad = new_cantidad
  def set_price(self,new_price):
    self.price = new_price
  def set_adicional(self,new_adicional):
    self.adicional = new_adicional
  def set_alimento(self,new_alimento):
    self.name = new_alimento

  def show_alimento(self):
    return f'Nombre:{self.name}, Cantidad:{self.cantidad}\nPrecio:{self.price}, Adicional:{self.adicional}'