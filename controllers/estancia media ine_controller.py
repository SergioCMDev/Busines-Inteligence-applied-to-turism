from ..DB.Repositorio_Estancia_Media_INE import RepositoryEstanciaMediaINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor

def obtener_cantidad_dias_estancia_media_estimados_en_ciudad_en_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene los dias de estancia media estimados en dicha ciudad en ese año
    Dado una ciudad y un año obtiene los dias de estancia media estimados en dicha ciudad en ese año
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnio(Ciudad, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_dias_estancia_media_estimados_en_ciudad_en_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene los dias de estancia media estimados en dicha ciudad en ese año dividido por meses
    Dado una ciudad y un año obtiene los dias de estancia media estimados en dicha ciudad en ese año dividido por meses
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_dias_estancia_media_estimados_en_ciudad_en_rango_anios_mensualmente(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un año obtiene los dias de estancia media estimados en dicha ciudad en ese rango de años dividido por meses
    Dado una ciudad y un año obtiene los dias de estancia media estimados en dicha ciudad en ese rango de años dividido por meses
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosMensualmente(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_dias_estancia_media_estimados_en_ciudad_en_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene los dias de estancia media estimados en dicha ciudad en esos años
    Dado una ciudad y un rango de años obtiene los dias de estancia media estimados en dicha ciudad en esos años
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_dias_estancia_media_estimados_en_ciudad_en_rango_anios_en_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un mes y un rango de años obtiene los dias de estancia media estimados en dicha ciudad en esos años en ese mes
    Dado una ciudad, un mes y un rango de años obtiene los dias de estancia media estimados en dicha ciudad en esos años en ese mes
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval
