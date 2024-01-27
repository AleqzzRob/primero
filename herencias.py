class Persona:
    def __init__(self): #init es el constructor de la clase de persona
        self.nombre=input("escriba su nombre") #se define como ingreso de caracteres abc
        self.edad=int(input("escriba su edad")) #se define con la variable int como valores numericos

    def mostrar(self):
        print("este es el nombre ",self.nombre) #se deja espacio al final para incluir un espacio
        print("esta es la edad ",self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=int(input("escriba su sueldo "))
        print("sueldo ",self.sueldo) #construco para llamar a la clase de persona
    def mostrar(self):
        super().mostrar()
        print("este es el sueldo ",self.sueldo)
    def impuesto(self):
        if self.sueldo>3000:
            print("el emplado debe pagar impuestos ")
        else:
            print("el empleado no debe pagar impuestos ")

Alejandro=Persona()
Alejandro.mostrar()
Manuel=Empleado()
Manuel.mostrar()
Manuel.impuesto()
              


            



                      