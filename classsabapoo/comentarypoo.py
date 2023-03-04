class Curso:                                    #se nombra una clase curso
    def __init__(self,titulo):                  #se crea el constructor y se le va un parametro
        self.__titulo=titulo                    #se instancia al objecto

    def getTitulo(self):                        #se crea una funcion y se le da un parametro
        return self.__titulo                    #retorna titulo 

class Aprendiz:                                 #se crea una clase aprendiz
    def __init__(self,nombre):                  #se crea el contructor se le da un parametro 'nombre'
        self.__nombre=nombre                    #se instancia al objecto
        self.__cursos=[]                        #se referencia una lista vacia

    def agregarCurso(self,nombreCursito):       #se crea una funcion 
        cursito=Curso(nombreCursito)            #se crea un curso
        self.__cursos.append(cursito)           #es para agregar 

    def getCursos(self):                        #es un funcion para ver el nombre del curso
        return self.__cursos                    #va retornr la lista de los cursos
    
ap=Aprendiz('Sofia')                            #objecto en la clase sofia
ap.agregarCurso('Python Basico')                #esta agregando los cursos que son de las clasa llamada curso al objecto 'op' de la clase aprendiz
ap.agregarCurso('Python Intermedio')            #esta agregando los cursos que son de las clasa llamada curso al objecto 'op' de la clase aprendiz

for c in ap.getCursos():                        #recorre el getcurso en el curso
    print(c.getTitulo())                        #imprime el getitulo

del ap                                          #elimina el objecto 'ap'