class personsa:
    def __init__(self, nombre, apellido, edad, mascotas):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.mascotas=mascotas
        
    def __str__(self):
        return f"Persona {self.nombre} {self.apellido}"
    
    def __len__(self):
        return self.edad
    
    def __getitem__(self, indice):
        return self.mascotas[indice]
    
    def __eq__(self, other):
        return self.nombre==other.nombre
    
    def __del__(self):
        print("el objeto se detruyo")
    
    
    



texto="esto es un texto"
numero=5

mascotas=["firulais", "dido","Bluey"]

persona1=personsa("Roberto", "Carlos", 16, mascotas)
persona2=personsa("Roberto", "Carlos", 16, mascotas)




