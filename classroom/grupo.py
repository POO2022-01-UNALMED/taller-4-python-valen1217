

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas is None:
            self._asignaturas = dict()
        for k, v in kwargs.items():
            self._asignaturas[k] = Asignatura(v)

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            lista = [alumno]
            if self.listadoAlumnos is None:
                self.listadoAlumnos = lista
            else:
                self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista

    def getAsignaturas(self):
        return self._asignaturas

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return "Grupo de estudiantes: " + str(self._grupo)
