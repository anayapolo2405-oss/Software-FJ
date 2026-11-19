
import logging

from cliente import Cliente
from servicios import Servicio
from reserva import Reserva
from excepciones import (
    DatosInvalidosError,
    ClienteDuplicadoError,
    ServicioNoDisponibleError
)


class SistemaFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        try:
            if not isinstance(cliente, Cliente):
                raise DatosInvalidosError("El objeto no corresponde a un cliente.")

            if any(c.identificador == cliente.identificador for c in self.clientes):
                raise ClienteDuplicadoError("El cliente ya está registrado.")

            self.clientes.append(cliente)

        except Exception:
            logging.exception("Error al registrar un cliente.")
            raise

        else:
            logging.info("Cliente registrado: %s", cliente.nombre)
            return True

    def agregar_servicio(self, servicio):
        try:
            if not isinstance(servicio, Servicio):
                raise DatosInvalidosError("El objeto no es un servicio válido.")

            if any(s.identificador == servicio.identificador for s in self.servicios):
                raise DatosInvalidosError("El servicio ya está registrado.")

            self.servicios.append(servicio)

        except Exception:
            logging.exception("Error al agregar un servicio.")
            raise

        else:
            logging.info("Servicio agregado: %s", servicio.nombre)
            return True

    def crear_reserva(self, identificador, cliente, servicio, duracion, **parametros):
        if cliente not in self.clientes:
            raise DatosInvalidosError("El cliente no está registrado.")

        if servicio not in self.servicios:
            raise ServicioNoDisponibleError("El servicio no está registrado.")

        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion,
            **parametros
        )

        self.reservas.append(reserva)

        logging.info("Reserva creada: %s", identificador)

        return reserva

    def listar_clientes(self):
        return [cliente.descripcion() for cliente in self.clientes]

    def listar_servicios(self):
        return [servicio.descripcion() for servicio in self.servicios]

    def listar_reservas(self):
        return [reserva.descripcion() for reserva in self.reservas]
