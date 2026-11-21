from abc import abstractmethod
from entidad import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad):
    """Clase abstracta base para los servicios ofrecidos por Software FJ."""

    def __init__(self, identificador, nombre, tarifa):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool) or tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa = float(tarifa)
        self.disponible = True

    def _calcular_costo_base(self, argumentos, multiplicador=1):
        if len(argumentos) not in (1, 2, 3):
            raise DatosInvalidosError(
                "Use: calcular_costo(duracion), "
                "calcular_costo(duracion, descuento) o "
                "calcular_costo(duracion, descuento, impuesto)."
            )

        duracion = argumentos[0]
        descuento = argumentos[1] if len(argumentos) >= 2 else 0
        impuesto = argumentos[2] if len(argumentos) == 3 else 0

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        subtotal = self.tarifa * duracion * multiplicador
        subtotal -= subtotal * descuento / 100
        total = subtotal + (subtotal * impuesto / 100)

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, *argumentos, **parametros):
        pass

    @abstractmethod
    def validar_parametros(self, duracion, **parametros):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):
    """Servicio especializado para reserva de salas por horas."""

    def __init__(self, identificador, nombre, tarifa, capacidad):
        super().__init__(identificador, nombre, tarifa)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un entero positivo.")

        self.capacidad = capacidad

    def calcular_costo(self, *argumentos, **parametros):
        return self._calcular_costo_base(argumentos)

    def validar_parametros(self, duracion, **parametros):
        if "asistentes" not in parametros:
            raise DatosInvalidosError("Falta el parámetro obligatorio: asistentes.")

        asistentes = parametros["asistentes"]

        if not isinstance(asistentes, int) or isinstance(asistentes, bool):
            raise DatosInvalidosError("El número de asistentes debe ser entero.")

        if asistentes <= 0 or asistentes > self.capacidad:
            raise DatosInvalidosError("La cantidad de asistentes supera la capacidad de la sala.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser positiva.")

    def descripcion(self):
        return (
            f"Sala: {self.nombre} | Tarifa por hora: "
            f"${self.tarifa:,.2f} | Capacidad: {self.capacidad}"
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado para alquiler de equipos tecnológicos."""

    def __init__(self, identificador, nombre, tarifa, cantidad_disponible):
        super().__init__(identificador, nombre, tarifa)

        if not isinstance(cantidad_disponible, int) or isinstance(cantidad_disponible, bool) or cantidad_disponible < 0:
            raise DatosInvalidosError("La cantidad disponible no es válida.")

        self.cantidad_disponible = cantidad_disponible

    def calcular_costo(self, *argumentos, **parametros):
        cantidad = parametros.get("cantidad", 1)

        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise DatosInvalidosError("La cantidad de equipos debe ser un entero positivo.")

        return self._calcular_costo_base(argumentos, multiplicador=cantidad)

    def validar_parametros(self, duracion, **parametros):
        if "cantidad" not in parametros:
            raise DatosInvalidosError("Falta el parámetro obligatorio: cantidad.")

        cantidad = parametros["cantidad"]

        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise DatosInvalidosError("La cantidad debe ser un número entero.")

        if cantidad <= 0 or cantidad > self.cantidad_disponible:
            raise DatosInvalidosError("No hay suficientes equipos disponibles.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser positiva.")

    def descripcion(self):
        return (
            f"Equipo: {self.nombre} | Tarifa por hora: "
            f"${self.tarifa:,.2f} | Disponibles: {self.cantidad_disponible}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado para consultoría y asesoría técnica."""

    def __init__(self, identificador, nombre, tarifa, especialidad):
        super().__init__(identificador, nombre, tarifa)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Debe indicar la especialidad.")

        self.especialidad = especialidad.strip()

    def calcular_costo(self, *argumentos, **parametros):
        return self._calcular_costo_base(argumentos)

    def validar_parametros(self, duracion, **parametros):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise DatosInvalidosError("La duración debe ser numérica.")

        if duracion < 1:
            raise DatosInvalidosError("La asesoría debe durar al menos una hora.")

        if duracion > 8:
            raise DatosInvalidosError("La asesoría no puede superar 8 horas.")

    def descripcion(self):
        return (
            f"Asesoría: {self.nombre} | Especialidad: "
            f"{self.especialidad} | Tarifa por hora: ${self.tarifa:,.2f}"
        )
