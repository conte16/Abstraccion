from abc import ABC, abstractmethod

class Fernanda(ABC):
    
    @abstractmethod
    def nombre(self):
        pass
    
    @abstractmethod
    def edad(self):
        pass
    
    
#Creando clases dependientes de figura

class Estudiante(Fernanda):
    def init (self, carrera):
        self.carrera = carrera
        
    def nombre(self):
        return self.nombre
     
    
    def edad(self):
        return self.edad
       

class Hobby(Fernanda):
    def init(self, pasatiempo):
        self.pasatiempo =  pasatiempo
      
        
    def nombre(self):
        return self.nombre
    
    def edad(self):
        return self.edad
    
class Musica(Fernanda):
    def init(self, tipoMusica):
        self.tipoMusica = tipoMusica
        
    def nombre(self):
        return self.nombre
    
    
    def edad(self):
        return self.edad 
    
#Creando clases del las clases hijas de la clase abstracta 

persona = Estudiante()
print('Nombre ', persona.nombre())
print('Edad: ' , persona.edad())

pasatiempo = Hobby()
print('Nombre ', pasatiempo.nombre())
print('Edad: ' , pasatiempo.edad())

escuharMusica = Musica()
print('Nombre ', escuharMusica.nombre())
print('Edad: ' , escuharMusica.edad())