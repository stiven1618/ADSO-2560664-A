class Aprendiz:                                     #se agrega un clase aprendiz 
    def __init__(self,nombre):                      #se crea el constructor y se le dan parametros
        self.__nombre=nombre                        #se instancia al objecto
        self.__cursos=[]                            #se refencia una lista vacia
    def agregarCurso(self,nombreCurso):             #se crea una funcion para agregar en la lista vacia 'parametro'
        self.__cursos.append(nombreCurso)           #es para agregar a la lista
    def verCursos(self):                            #se crea una funcion
        return self.__cursos                        #retorna cursos 

class Curso:                                        #se agrega otra case curso
    def __init__(self,nombreCurso):                 #se crea un constructor y se le da un parametro
        self.__nombreCurso=nombreCurso              #se instancia el objecto

    def getNombreCurso(self):                       #una funcion para ver el nombre del curso
        return self.__nombreCurso                   #retona el nombrecurso
    
ob=Aprendiz('Miguel')                               #objecto de clase miguel
c1=Curso('Python Basico')                           #objecto clase python basico
c2=Curso('Python Intermedio')                       #objecto clase pyton intermedio
c3=Curso('Java Basico')                             #objecto clase java basico

ob.agregarCurso(c1)                                 #esta agregando los cursos que son de las clasa llamada curso al objecto 'ob' de la clase aprendiz
ob.agregarCurso(c2)                                 #esta agregando los cursos que son de las clasa llamada curso al objecto 'ob' de la clase aprendiz
ob.agregarCurso(c3)                                 #esta agregando los cursos que son de las clasa llamada curso al objecto 'ob' de la clase aprendiz

for curso in ob.verCursos():                        #recorre los objectos de la clase del curso
    print(curso.getNombreCurso())                   #imprime el curso con el metodo getNombreCurso

del ob                                              #elimina el objecto 'ob'
#print(ob)
print('.....',c1.getNombreCurso())                  #imprime el curso 'c1' con el metodo getNombreCurso
