class mail:
    def __init__(self, nombreCuenta, contraseña):
        self.nombreCuenta=nombreCuenta
        self.__contraseña=contraseña
        
    def setContraseña(self, nuevaContraseña):
        self.__contraseña=nuevaContraseña
        
    def comprobarDatos(self, email, contraseña):
        if email==self.nombreCuenta and contraseña==self.__contraseña:
            print("acceso permitido")
            return True
        else:
            print("reintenta")
            return False
            
        


mailDePueba=mail(nombreCuenta="fulanito123@gmail.com", contraseña= "1234567")
mailDePueba.setContraseña("password")

ingreso=False
while not ingreso:
    mail=input("ingrese su email ")
    contraseña=input("ingrese su contraseña ")
    
    ingreso=mailDePueba.comprobarDatos(email=mail, contraseña=contraseña)
    
    
print("bienvenido al sistema")
    





        