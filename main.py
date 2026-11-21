import logging

from sistema import SistemaFJ
from cliente import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)


# Configuración del archivo de eventos y errores
logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


def ejecutar_operacion(numero, nombre, funcion):
    print(f"\nOPERACION {numero}: {nombre}")

    try:
        resultado = funcion()

    except Exception as error:
        logging.exception("Operacion %s fallida.", nombre)
        print(f"Error controlado: {error}")

    else:
        print("Operacion realizada correctamente.")
        if resultado is not None:
            print(resultado)

    finally:
        print("Fin de la operacion.")


def iniciar_sistema():
    sistema = SistemaFJ()

    print("=" * 55)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print(" Clientes, servicios y reservas")
    print("=" * 55)

    # OPERACION 1: Registro correcto de cliente
    cliente1 = Cliente(
        "C001",
        "Carlos Rodriguez",
        "carlos@gmail.com",
        "3001234567"
    )

    ejecutar_operacion(
        1,
        "Registrar cliente valido",
        lambda: sistema.registrar_cliente(cliente1)
    )

    # OPERACION 2: Registro de cliente con correo invalido
    ejecutar_operacion(
        2,
        "Registrar cliente con correo incorrecto",
        lambda: Cliente(
            "C002",
            "Maria Lopez",
            "correo_invalido",
            "3011234567"
        )
    )

    # OPERACION 3: Intentar registrar cliente duplicado
    ejecutar_operacion(
        3,
        "Registrar cliente duplicado",
        lambda: sistema.registrar_cliente(cliente1)
    )

    # OPERACION 4: Crear y registrar sala
    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        50000,
        20
    )

    ejecutar_operacion(
        4,
        "Crear servicio de reserva de sala",
        lambda: sistema.agregar_servicio(sala)
    )

    # OPERACION 5: Crear y registrar equipos
    equipo = AlquilerEquipo(
        "E001",
        "Video Beam",
        30000,
        5
    )

    ejecutar_operacion(
        5,
        "Crear servicio de alquiler de equipos",
        lambda: sistema.agregar_servicio(equipo)
    )

    # OPERACION 6: Crear y registrar asesoria
    asesoria = AsesoriaEspecializada(
        "A001",
        "Asesoria informatica",
        80000,
        "Ingenieria de sistemas"
    )

    ejecutar_operacion(
        6,
        "Crear servicio de asesoria especializada",
        lambda: sistema.agregar_servicio(asesoria)
    )

    # OPERACION 7: Intentar crear servicio incorrecto
    ejecutar_operacion(
        7,
        "Crear servicio con tarifa negativa",
        lambda: ReservaSala(
            "S002",
            "Sala incorrecta",
            -50000,
            10
        )
    )

    # OPERACION 8: Crear reserva valida de sala
    reserva1 = sistema.crear_reserva(
        "R001",
        cliente1,
        sala,
        2,
        asistentes=10
    )

    ejecutar_operacion(
        8,
        "Procesar reserva correcta de sala",
        reserva1.procesar
    )

    # OPERACION 9: Crear reserva con capacidad excedida
    reserva2 = sistema.crear_reserva(
        "R002",
        cliente1,
        sala,
        2,
        asistentes=30
    )

    ejecutar_operacion(
        9,
        "Procesar reserva con asistentes incorrectos",
        reserva2.procesar
    )

    # OPERACION 10: Crear reserva de equipos (multiplica tarifa * horas * cantidad)
    reserva3 = sistema.crear_reserva(
        "R003",
        cliente1,
        equipo,
        3,
        cantidad=2
    )

    ejecutar_operacion(
        10,
        "Procesar reserva de equipos",
        reserva3.procesar
    )

    # OPERACION 11: Crear reserva de asesoria con descuento e impuesto
    reserva4 = sistema.crear_reserva(
        "R004",
        cliente1,
        asesoria,
        2,
        descuento=10,
        impuesto=19
    )

    ejecutar_operacion(
        11,
        "Procesar reserva de asesoria con descuento e IVA",
        reserva4.procesar
    )

    # OPERACION 12: Cancelar una reserva confirmada
    ejecutar_operacion(
        12,
        "Cancelar reserva confirmada",
        reserva1.cancelar
    )

    # OPERACION 13: Intentar cancelar una reserva dos veces
    ejecutar_operacion(
        13,
        "Intentar cancelar una reserva ya cancelada",
        reserva1.cancelar
    )

    # OPERACION 14: Calcular costo normal (sobrecarga 1 parametro)
    ejecutar_operacion(
        14,
        "Calcular costo normal",
        lambda: sala.calcular_costo(2)
    )

    # OPERACION 15: Calcular costo con descuento (sobrecarga 2 parametros)
    ejecutar_operacion(
        15,
        "Calcular costo con descuento",
        lambda: sala.calcular_costo(2, 10)
    )

    # OPERACION 16: Calcular costo con descuento e impuesto (sobrecarga 3 parametros)
    ejecutar_operacion(
        16,
        "Calcular costo con descuento e impuesto",
        lambda: sala.calcular_costo(2, 10, 19)
    )

    # OPERACION 17: Procesar reserva con parametros faltantes (sin 'asistentes')
    reserva5 = sistema.crear_reserva(
        "R005",
        cliente1,
        sala,
        2
    )

    ejecutar_operacion(
        17,
        "Procesar reserva con parametros faltantes",
        reserva5.procesar
    )

    # OPERACION 18: Procesar reserva cuando el servicio no esta disponible
    asesoria.disponible = False
    reserva6 = sistema.crear_reserva(
        "R006",
        cliente1,
        asesoria,
        2
    )

    ejecutar_operacion(
        18,
        "Procesar reserva con servicio no disponible",
        reserva6.procesar
    )

    # Mostrar informacion final
    print("\n" + "=" * 55)
    print("           INFORMACION FINAL DEL SISTEMA")
    print("=" * 55)

    print("\nCLIENTES REGISTRADOS:")
    for cliente in sistema.listar_clientes():
        print(cliente)

    print("\nSERVICIOS REGISTRADOS:")
    for servicio in sistema.listar_servicios():
        print(servicio)

    print("\nRESERVAS REGISTRADAS:")
    for reserva in sistema.listar_reservas():
        print(reserva)

    print("\nEl sistema finalizo sin detenerse por los errores.")
    print("Los eventos y errores fueron registrados en software_fj.log.")

    logging.info("Finalizacion del sistema Software FJ.")


if __name__ == "__main__":
    iniciar_sistema()
