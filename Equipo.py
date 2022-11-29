class Equipo():
     def __init__(self,pais,codigo,grupo):
        self.pais = pais
        self.codigo = codigo
        self.grupo = grupo
        self.localidad = False

    
     def get_pais(self):
        return self.pais
     def get_codigo(self):
        return self.codigo
     def get_grupo(self):
        return self.grupo

    
     def set_pais(self,new_pais):
         self.pais = new_pais

     def set_codigo(self,new_codigo):
        self.codigo = new_codigo

     def set_grupo(self, new_grupo):
        return self.grupo
        


    

     