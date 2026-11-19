
from abc import abstractmethod
from entidad import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad):

    def __init__(self, identificador, nombre, tarifa):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool) or tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa = float(tarifa)
        self.disponible = True

    def _calcular_costo_base(self, argumentos):
        if len(argumentos) not in (1, 2, 3):
            raise TypeError(
                "Use: calcular_costo(duracion), "
                "calcular_costo(duracion, descuento) o "
                "calcular_costo(duracion, descuento, impuesto)."
            )

        duracion = argumentos[0]
        descuento = argumentos[1] if len(argumentos) >= 2 else 0
        impuesto = argumentos[2] if len(argumentos) == 3 else 0

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        if not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        if not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        subtotal = self.tarifa * duracion
        subtotal -= subtotal * descuento / 100
        total = subtotal + (subtotal * impuesto / 100)

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, *argumentos):
        pass

    @abstractmethod
    def validar_parametros(self, duracion, **parametros):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, tarifa, capacidad):
        super().__init__(identificador, nombre, tarifa)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un entero positivo.")

        self.capacidad = capacidad

    def calcular_costo(self, *argumentos):
        return self._calcular_costo_base(argumentos)

    def validar_parametros(self, duracion, **parametros):
        asistentes = parametros.get("asistentes", 1)

        if not isinstance(asistentes, int) or isinstance(asistentes, bool):
            raise DatosInvalidosError("El número de asistentes debe ser entero.")

        if asistentes <= 0 or asistentes > self.capacidad:
            raise DatosInvalidosError("La cantidad de asistentes supera la capacidad de la sala.")

        if duracion <= 0:
            raise DatosInvalidosError("La duración debe ser positiva.")

    def descripcion(self):
        return (
            f"Sala: {self.nombre} | Tarifa por hora: "
            f"${self.tarifa:,.2f} | Capacidad: {self.capacidad}"
        )


class AlquilerEquipo(Servicio):

    def __init__(self, identificador, nombre, tarifa, cantidad_disponible):
        super().__init__(identificador, nombre, tarifa)

        if not isinstance(cantidad_disponible, int) or isinstance(cantidad_disponible, bool) or cantidad_disponible < 0:
            raise DatosInvalidosError("La cantidad disponible no es válida.")

        self.cantidad_disponible = cantidad_disponible

    def calcular_costo(self, *argumentos):
        return self._calcular_costo_base(argumentos)

    def validar_parametros(self, duracion, **parametros):
        cantidad = parametros.get("cantidad", 1)

        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise DatosInvalidosError("La cantidad debe ser un número entero.")

        if cantidad <= 0 or cantidad > self.cantidad_disponible:
            raise DatosInvalidosError("No hay suficientes equipos disponibles.")

        if duracion <= 0:
            raise DatosInvalidosError("La duración debe ser positiva.")

    def descripcion(self):
        return (
            f"Equipo: {self.nombre} | Tarifa por hora: "
            f"${self.tarifa:,.2f} | Disponibles: {self.cantidad_disponible}"
        )


class AsesoriaEspecializada(Servicio):

    def __init__(self, identificador, nombre, tarifa, especialidad):
        super().__init__(identificador, nombre, tarifa)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Debe indicar la especialidad.")

        self.especialidad = especialidad.strip()

    def calcular_costo(self, *argumentos):
        return self._calcular_costo_base(argumentos)

    def validar_parametros(self, duracion, **parametros):
        if duracion < 1:
            raise DatosInvalidosError("La asesoría debe durar al menos una hora.")

        if duracion > 8:
            raise DatosInvalidosError("La asesoría no puede superar 8 horas.")

    def descripcion(self):
        return (
            f"Asesoría: {self.nombre} | Especialidad: "
            f"{self.especialidad} | Tarifa por hora: ${self.tarifa:,.2f}"
        )
