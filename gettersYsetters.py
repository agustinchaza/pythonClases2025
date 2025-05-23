class trabajador:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        if edad>=18:
            self.__edad = edad
        else:
            raise ValueError("la edad no puede ser menor a 18")
        
    def __str__ (self):
        return f"el Trabajador se llama {self.__nombre} y tiene {self.__edad} años"
    
    def setNombre(self, nombre):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre
        
    
        


trabajador1=trabajador("Matias", 18)
trabajador1.setNombre("marcos")
nombre=trabajador1.getNombre()
print(nombre)
    