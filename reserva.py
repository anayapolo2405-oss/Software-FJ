
import logging
from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError
)


class Reserva:

    def __init__(self, identificador, cliente, servicio, duracion, **parametros):
        if not identificador or not str(identificador).strip():
            raise ReservaInvalidaError("El identificador de la reserva es obligatorio.")

        self.identificador = str(identificador)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.parametros = parametros
        self.estado = "Pendiente"
        self.total = 0

    def confirmar(self):
        if self.estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        if not self.servicio.disponible:
            raise ServicioNoDisponibleError("El servicio no está disponible.")

        self.servicio.validar_parametros(
            self.duracion, **self.parametros
        )

        self.total = self.servicio.calcular_costo(self.duracion)
        self.estado = "Confirmada"

        logging.info("Reserva %s confirmada.", self.identificador)
        return self.total

    def cancelar(self):
        if self.estado != "Confirmada" and self.estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "La reserva no se puede cancelar."
            )

        self.estado = "Cancelada"
        logging.info("Reserva %s cancelada.", self.identificador)

    def procesar(self):
        try:
            resultado = self.confirmar()

        except Exception as error:
            logging.exception(
                "Error al procesar la reserva %s.",
                self.identificador
            )

            self.estado = "Fallida"

            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            logging.info("Procesamiento finalizado correctamente.")
            return resultado

        finally:
            logging.info(
                "Finalizó el intento de procesamiento de la reserva %s.",
                self.identificador
            )

    def descripcion(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado} | "
            f"Total: ${self.total:,.2f}"
        )
