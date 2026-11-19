
class ErrorSistema(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se presenta cuando los datos no cumplen las validaciones."""
    pass


class ClienteDuplicadoError(ErrorSistema):
    """Se presenta cuando un cliente ya está registrado."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se presenta cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se presenta cuando una reserva tiene datos incorrectos."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se presenta cuando una operación no está permitida."""
    pass
