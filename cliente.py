
import re
from entidad import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.__nombre = None
        self.__correo = None
        self.__telefono = None

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener mínimo 3 caracteres.")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        patron = r"^[\w.-]+@[\w.-]+\.\w+$"

        if not isinstance(valor, str) or not re.match(patron, valor):
            raise DatosInvalidosError("El correo electrónico no es válido.")

        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        telefono = str(valor).strip()

        if not telefono.isdigit() or len(telefono) != 10:
            raise DatosInvalidosError("El teléfono debe tener 10 dígitos.")

        self.__telefono = telefono

    def descripcion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )
