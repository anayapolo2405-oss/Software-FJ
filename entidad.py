
from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Entidad(ABC):

    def __init__(self, identificador):
        if identificador is None or isinstance(identificador, bool) or not str(identificador).strip():
            raise DatosInvalidosError("El identificador de la entidad es obligatorio.")

        self._identificador = str(identificador).strip()
    
    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def descripcion(self):
        pass
