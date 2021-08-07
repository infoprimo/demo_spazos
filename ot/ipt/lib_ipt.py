#!/usr/bin/env python
# -*- coding: utf-8 -*-


__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2015-2019"

#  debugging
try:
    from inspect import currentframe, getframeinfo
except:
    pass

import os
import sys
import logging
import config as cfg


def parate():
    import ipdb
    return ipdb.set_trace


def embed():
    from IPython import embed
    return embed

# import pydevd


ns = os.path.basename(__file__).split('.')[0]
fn = cfg.ldir + ns
filename = ''.join(fn + '.log')
logging.basicConfig(format=cfg.log_format, filename=filename,
                    filemode=cfg.filemode, level=logging.INFO, datefmt=cfg.datefmt)
logging.info("%s" % (fn,))

# valores 0/1
stdout_err = 0  # errores en stdout
verbose    = 0  # detalles del error
debug_log  = 0  # escribe detalles en el log
debug_vivo = 0  # consola debug en punto de ejecución


def rfalla(msg='\n\tAtención: algó falló.'):
    """ notificación a stdout forzada """
    print ("%s  %s" % (msg, "Vea el log!"))


def excepcion(msg="Algo salió mal... ", frame=None, id_ticket=None):
    """ logging / notificación a stdout """

    msgv = ''.join(msg + "\n\t Ticket %s " % (id_ticket,))
    if frame:
        msgv += "\n\t-> En %s  línea: %s <-" % (frame.filename, frame.lineno)
    msf  = "\n Fin ejecución..."
    msgv += msf

    if stdout_err:
        print("\t %s" % (msg + msf,))
    if verbose and frame and id_ticket:
        print("\t %s" % (msgv,))
    if debug_log:
        logging.error(msgv, )
    msg += "\n fin ejecución..."
    if debug_vivo:
        print("\n\t %s", (msgv,))
        import ipdb
        ipdb.set_trace()
    return sys.exit(1)

# básicas manejo strings


def fecha(strg):
    """
        param:     string (14 dígitos) 'yyyyMMddhhmmss'
        retorna:   string 'aaaa-MM-dd' (10 dígitos)
    """
    if len(strg) == 14:
        res = "{}-{}-{}".format(strg[:4], strg[4:6], strg[6:8])
    else:
        res = '0000-00-00'
    return res


def timestamp_tck(strg):

    if len(strg) == 14:
        res = fecha(strg)
        res = "{} {}".format(fecha(strg), hora(strg[8:]))
    else:
        res = '0000-00-00 00:00:00'
    return res


def fecha10(strg):
    """
        param:     string (14 dígitos)
        retorna:   string 'dd/mm/aaaa' día/mes/año (10 dígitos)
    """
    if len(strg) == 14:
        res = "%s/%s/%s" % (strg[6:8], strg[4:6], strg[:4])
    else:
        res = '00/00/0000'
    return res


def fecha8(strg):
    """
        param:     string (14 dígitos) 'aaaammddhhmmss'
        retorna:   string 'dd/mm/aa' día/mes/año (8 dígitos)
    """
    if len(strg) == 14:
        res = "%s/%s/%s" % (strg[6:8], strg[4:6], strg[2:4])
    else:
        res = '00/00/00'
    return res


def yyyymmdd(strg):
    """
        param:     string 'aaaaMMddhhmmdd' (14 dígitos)
        retorna:   string 'aaaaMMdd' añomesdía (8 dígitos)
    """
    if len(strg) == 14:
        res = "%s%s%s" % (strg[0:4], strg[4:6], strg[6:8])
    else:
        res = '00000000'
    return res


def yymmdd(strg):
    """
        param:     string 'aaaaMMddhhmmdd' (14 dígitos)
        retorna:   string 'aaMMdd' añomesdía (6 dígitos)
    """
    if len(strg) == 14:
        res = "%s%s%s" % (strg[2:4], strg[4:6], strg[6:8])
    else:
        res = '000000'
    return res


def dd(strg):
    """
        param:     string (14 dígitos)
        retorna:   string 'dd' día del mes (2 dígitos)
    """
    if len(strg) == 14:
        res = "%s" % (strg[6:8])
    else:
        res = '00'
    return res


def mm(strg):
    """
        param:     string (14 dígitos)
        retorna:   string 'mm' mes del año (2 dígitos)
    """
    if len(strg) == 14:
        res = "%s" % (strg[4:6])
    else:
        res = '00'
    return res


def yy(strg):
    """
        param:     string (14 dígitos)
        retorna:   string 'aa' año (2 dígitos)
    """
    if len(strg) == 14:
        res = "%s" % (strg[2:4])
    else:
        res = '0000'
    return res


def yyyy(strg):
    """
        param:     string (14 dígitos)
        retorna:   string 'aaaa' año (4 dígitos)
    """
    if len(strg) == 14:
        res = "%s" % (strg[:4])
    else:
        res = '0000'
    return res


def hora(strg):
    """
        param:     string (6 dígitos) hhmmss
        retorna:   string 'hh:mm:ss' hora:minutos:segundos
    """
    if len(strg) == 6:
        res = "%s:%s:%s" % (strg[0:2], strg[2:4], strg[4:6])
    else:
        res = '00:00:00'
    return res


def hhmmss(strg):
    """
        Evita errores de hora (estilo salomón)
    :param     string: (6 dígitos)
    :return    string 'hhmmss'
    """
    if len(strg) == 6:
        res = strg
    else:
        res = '000000'
    return res


def hh_mm_ss(strg):
    """
    :param      string aaaaMMddhhmmdd
    """
    pass


def caja3dig(nrocaja=None):
    """
    Completa con ceros `0` el nro de caja a largo 3
    :param      nrocaja: string Número de del POS
    :return:    string 'nnn' Número del POS en 3 dígitos.
    """
    if not nrocaja:
        return '000'
    else:
        return (3 - len(str(nrocaja))) * '0' + str(nrocaja)


def tck8dig(nrotck=None):
    """
    Completa con ceros `0` el nro de ticket a largo 8
    :param      nrotck: string Número del ticket
    :return:    string 'nnnnnnnn' Número del ticket en 8 dígitos.
    """
    if not nrotck:
        return '00000000'
    else:
        return (8 - len(str(nrotck))) * '0' + str(nrotck)


class IPCabezal(object):

    """
            Nota: ver más abajo: Cambios en la Estructura de Datos


        Representa una línea de tipo cabezal Salida Pazos4
        ++++++++++++++++++++++++++++++++++++++++++++++++++

        Ejemplo::
            en salidapazos "C#1#2#350#2#20151121105326#F#4#183.40#20#13"

        Separador de columnas: '#'
        Nombres de columnas en orden posicional:
            # TipoLinea    # CodigoCaja        # NumeroTicket  #  CodigoCajera  #  TimestampTicket
            # EstadoTicket # CantidadArticulos # TotalaPagar   # TipoCliente    #   CantidadLineas

        La misma línea tal cómo llega a una instancia de `IPCabezal` (se descarta el indicador de línea 'C')
                  ['1', '2', '350', '2', '20151121105326', 'F', '4', '183.40', '20', '13']
          indices   0    1     2     3          4           5    6       7       8     9

        La instanciación será
            `IPCabezal(una_linea_tipo_cabezal)`
        Se utlizarán estructuras análogas para el caso de líneas de tipo detalle de ticket
        En ambos casos se omite el identificador de línea.

        ¯¯¯¯

        Implemantación respecto a la docuemntación
        ''''''''''''''''''''''''''''''''''''''''''

        ::  Se agrega un diccionario de "tipos de línea cabezal":
                ejemplo:: `d = { '1': 'Ticket de venta(SM),
                                 '2': 'Ticket de Pedido',
                                 '3': 'Ticket de Devolución' }`
            este dicionario se define como constante de configuración y será un "miembro de clase"

        Cambios en la Estructura de Datos:
        '''''''''''''''''''''''''''''''''


        ::  Todos los nombres de identificadores pasan a minúsculas
        ::  Cambios en largo de los valores respecto a valores originales:
                CodigoCaja: se rdefine largo 3, relleno ceros a izquierda.
                NumeroTicket: se rdefine largo 8, relleno ceros a izquierda.
        ::  Agregados a la estructura original de la descripción de una línea de cabezal pazos:
                `descripcion`   string:   Etiqueta correspondiente a `TipoLinea`
                `id_ticket`     long:     Valor numérico obtenido de timestamp + caja (3 díg.) + tiket (8 díg.)



    """
    dic_cabezal = cfg.TIPOS_LINEAS_CABEZAL

    def __init__(self, linea_de_cabezal=None):
        """
        Ejemplo de línea de cabezal o cabezal del ticket::

            TipoLinea    # CodigoCaja        # NumeroTicket  #  CodigoCajera  #  TimestampTicket
            EstadoTicket # CantidadArticulos # TotalaPagar   # TipoCliente    #   CantidadLineas

        """
        if not len(linea_de_cabezal) or len(linea_de_cabezal) != 10:
            msg = 'Imposible inizializar la clase IPCabezal:'
            if not len(linea_de_cabezal):
                msg += '\nla línea recibida como cabezal Salida Pazos4 (SM) está vacía.'
            else:
                msg += "\nel largo de la línea recibida no coincide con el largo esperado" \
                       " para un cabezal Salida Pazos4 (SM)."
            logging.error(msg)
            sys.exit(1)
        else:
            self.rlinea = 'C#' + '#'.join(linea_de_cabezal)  # reconstruye lína cabezal salidapazos (debug)

            # definimos algunos sinónimos  (el 1ero. es siempre el del doc. salidapazos)
            self.llave              = linea_de_cabezal[0]
            self.tipocabezal        = linea_de_cabezal[0]

            self.codigocaja         = caja3dig(linea_de_cabezal[1])
            self.caja               = self.codigocaja

            self.numeroticket       = tck8dig(linea_de_cabezal[2])
            self.ticket             = self.numeroticket

            self.codigocajera       = linea_de_cabezal[3]
            self.nro_cajera         = linea_de_cabezal[3]

            self.timestampticket    = linea_de_cabezal[4]     # aaaaMMddhhmmss
            self.timestamp          = linea_de_cabezal[4]

            self.estadoticket       = linea_de_cabezal[5]
            self.estado             = linea_de_cabezal[5]

            self.cantidadarticulos  = linea_de_cabezal[6]
            self.cant_articulos     = linea_de_cabezal[6]

            self.totalapagar        = linea_de_cabezal[7]
            self.totalpagar         = linea_de_cabezal[7]

            self.tipocliente        = linea_de_cabezal[8]
            self.tipo_de_cliente    = linea_de_cabezal[8]

            self.cantidadlineas     = linea_de_cabezal[9]
            self.cant_lineas        = linea_de_cabezal[9]

            self.yyyymmdd      = yyyymmdd(linea_de_cabezal[4])
            self.yymmdd        = yymmdd(linea_de_cabezal[4])
            self.yyyy          = yyyy(linea_de_cabezal[4])
            self.yy            = yy(linea_de_cabezal[4])
            self.mm            = mm(linea_de_cabezal[4])
            self.dd            = dd(linea_de_cabezal[4])
            self.fecha         = fecha(linea_de_cabezal[4])
            self.timestamp_tck = timestamp_tck(linea_de_cabezal[4])
            self.descripcion   = self.dic_cabezal[linea_de_cabezal[0]][0]
            self.id_ticket     = self.timestamp + self.codigocaja + self.numeroticket
            # aaaaMMddhhmmssCCCtttttttt
            # se define un "diccionario en la instancia" por comodidad
            self.zip = dict(
                    descripcion       = self.descripcion,
                    id_ticket         = self.id_ticket,
                    date              = self.yyyymmdd,
                    fecha             = self.fecha,
                    timestamp_tck     = self.timestamp_tck,
                    tipocabezal       = self.tipocabezal,
                    codigocaja        = self.codigocaja,
                    numeroticket      = self.numeroticket,
                    codigocajera      = self.codigocajera,
                    timestampticket   = self.timestampticket,
                    estadoticket      = self.estadoticket,
                    cantidadarticulos = self.cantidadarticulos,
                    totalapagar       = self.totalapagar,
                    tipocliente       = self.tipocliente,
                    cantidadlineas    = self.cantidadlineas,
                )

            if verbose: print ("\t - fin init `IPCabezal`"),


# --- fin clase `IPCabezal`


class IPLinea(object):

    """
           Nota: ver más abajo: Cambios en la Estructura de Datos



        Representa a una línea de detalle de ticket de Salidapazos4 (SM).
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        Al ingual que en IPCabezal, se define un diccionario de "tipos de lineas de ticket".

            Cada `llave` o clave del diccionario será el número que identifica el tipo
            de línea de ticket, en tanto su `valor` será una lista (array) de dos elementos,

            El primer elemento es una `string` con la descripción/etiqueta del tipo de línea
            de detalle de ticket.

            El segundo elemento, es el nombre de un método que entiende sobre los datos y
            operaciones de éste tipo de línea. Obviamente este segundo elemento será usado
            cada vez que se necesite invocar a dicho método.

        Ejemplo:

            Tipo de línea: Total de ticket (4) por un total de $774.05 e incluye
            pago de servicio por $591.00

                Total  774.05
                Serv. -591.00
                     --------
                       183.05

            En la línea de detalle de origen salidapazos el identificador de línea es la `L`
                   ___________
                  |          |----> estructura comun a todas las lineas del ticket
                  10#4#153713#774.05#21.97#183.05#21.97
                             |________________________|----> estructura y valores epecíficos de la línea

            `linea_de_detalle` en la instancia ['10','4','153713','774.05','21.97','183.05','21.97']
            La `llave` aquí es '4'
            Atributos (no sus valores) comunes en todas las líneas del ticket: ['10','4','153713']
            Atributos específicos de éste tipo de línea:  ['774.05','21.97','183.05','21.97']
            que son los datos que traerá la invocación del método de línea.

            En el ejemplo, dada la línea_de_cabezal ['10','4','153713','774.05','21.97','183.05','21.97']
            el código python sería:

            # >>> from ticket import IPLinea
            # >>> lin_obj = IPLinea(linea_de_detalle, cabezal.id_ticket)
            # >>> datos   = lin_obj.metodo()
            # >>> print datos

            mostraría algo así: 'totalticket': 774.05, 'ivatotalticket': 21.97, \
                                'totalticketsinpagoservicios': 183.05, 'ivatotalticketsinpagoservicios': 21.97


                Atributos comunes para todas las `Líneas de Detalle`
                ----------------------------------------------------
                     numerodelinea  ->   id_linea   : número secuencial de la línea en el ticket | único
                     tipolinea      ->   llave      : del dicc. de tipos de línea,               | puede repetirse
                     horalinea      ->   hhmss      : hora minuto y segundo de l línea,          | puede repetirse

        Ejemplo:
               Sí linea_cabezal_tck = ('10','4','153713','774.05','21.97','183.05','21.97')
               entonces toddas las lineas tendrán estos 3 elementos en común: ('10','4','153713')


            Implemantación respecto a la docuemntación
            ''''''''''''''''''''''''''''''''''''''''''

            ::  Se agrega un diccionario de "tipos_linea_tck":

            Cambios en la Estructura de Datos:
            '''''''''''''''''''''''''''''''''

            ::  Todos los nombres de identificadores pasan a minúsculas
            ::  Cambios en largo de los valores respecto a valores originales:
                    xxxxxxxxxx: se redefine largo 3, relleno ceros a izquierda.
                    xxxxxxxxxx: se redefine largo 8, relleno ceros a izquierda.
            ::  Agregados a la estructura original de la descripción de línea de detalle
                    `descripcion`   string:  Etiqueta correspondiente a `TipoLinea`
                    `id_linea`     int:      Valor numérico obtenido del número de línea
            ::  Atributos agregdos a la estructura de datos
                    `tipos de línea`     `nombre de indentificador`
                          63                'cambio'
                          63                'totalpagadomonedareferencia'

    """

    def __init__(self, linea=None, tck_id=None):
        """
            El parametro `linea` llega a la instancia sin el identificador de línea `L`

            :param linea: list  línea de detalle de ticket  (línea de ticket)
            :param tck_id: long / str  id del ticket (id del cabezal de ticket)  es el timestamp de pazos

        """
        tipos_linea_tck = {
            '1': ('Venta de ítem', self._lt_1),
            '4': ('Total del ticket', self._lt_4),
            '5': ('Cabezal de CFE', self._lt_5),
            '6': ('Pié de CFE', self._lt_6),
            '7': ('Identificación de la cajera', self._lt_7),   # 9: Efectivo. También usan el mismo método
            '9': ('M.Pago de ticket en efectivo', self._lt_9),  # 54: 115: 119: 127: y 128:
            '10': ('Cabezal de un combo', self._lt_10),
            '11': ('Detalle de combo', self._lt_11),
            '12': ('Cancelación de ítem', self._lt_12),
            '13': ('Descuento a un ítem', self._lt_13),
            '15': ('Puntos generados de fidel. ítem', self._lt_15),
            '16': ('Puntos totales de fidel. generados', self._lt_16),
            '18': ('Regalo de artículos', self._lt_18),
            '19': ('Cupón', self._lt_19),
            '20': ('Devolución de un ítem', self._lt_20),
            '21': ('Entrada de cajera', self._lt_21),
            '22': ('Salida de cajera', self._lt_22),
            '23': ('Pausa de cajera', self._lt_23),
            '24': ('Cancelacion ticket', self._lt_24),
            '26': ('Cabezal de beneficio al total', self._lt_26),
            '27': ('Detalle de un beneficio al total', self._lt_27),
            '28': ('Descuento al total', self._lt_28),
            '29': ('Devolución de envases', self._lt_29),
            '30': ('Venta a la subfamilia', self._lt_30),
            '32': ('Inventario', self._lt_32),
            '33': ('Canje de ítem', self._lt_33),
            '34': ('Información de cliente de fidel.', self._lt_34),
            '35': ('Cancelación de un canje de ítem', self._lt_35),
            '36': ('Total de canje', self._lt_36),
            '37': ('M.Pago con tarjeta', self._lt_37),
            '38': ('M.Pago con cheque', self._lt_38),
            '40': ('M.Pago luncheon ticket', self._lt_40),
            '43': ('Voucher de la tarjeta', self._lt_43),
            '44': ('Datos adicionales garantía articulo', self._lt_44),
            '47': ('Pago de servicio', self._lt_47),
            '49': ('Detalle beneficios med.pago-moneda', self._lt_49),
            '52': ('M.Pago de caja', self._lt_52),
            '53': ('Tipo de ticket', self._lt_53),
            '54': ('Pago con Puntos', self._lt_54),
            '55': ('Intervención de la supervisora', self._lt_55),
            '56': ('Cancelacion de un pago de servicio', self._lt_56),
            '57': ('Tipo de cliente', self._lt_57),
            '58': ('Ticket de cancelación de pago', self._lt_58),
            '60': ('Cupón', self._lt_60),
            '61': ('Pedidos', self._lt_61),
            '62': ('Fin de pausa de cajera', self._lt_62),
            '63': ('Redondeo importe total del ticket', self._lt_63),
            '65': ('Puntos de fidelización', self._lt_65),
            '67': ('M.Pago de cupón corporativo', self._lt_67),
            '68': ('Id. Cliente ', self._lt_68),
            '71': ('Puntos no generadas', self._lt_71),
            '72': ('Descuento para parking', self._lt_72),
            '73': ('Ticket Z', self._lt_73),
            '76': ('Descuento producido por marcas', self._lt_76),
            '77': ('Cabezal de marca', self._lt_77),
            '78': ('Detalle de la marca', self._lt_78),
            '79': ('Pago Web', self._lt_79),
            '81': ('Devolución de pago de servicio', self._lt_81),
            '82': ('Consulta e.de cuenta de la cobranza.', self._lt_82),
            '83': ('Cobranza de Tarjeta (voucher)', self._lt_83),
            '84': ('Apertura de gaveta', self._lt_84),
            '85': ('M.Pago de tarjeta offline', self._lt_85),
            '86': ('Recargo', self._lt_86),
            '87': ('Descuento a los med.pago-moneda.', self._lt_87),
            '88': ('Venta cómputos celular', self._lt_88),
            '89': ('Devolución venta cómputos celular', self._lt_89),
            '90': ('M.Pago ticket TAlimentos', self._lt_90),
            '91': ('M.Pago ticket Total', self._lt_91),
            '92': ('Linea de factura', self._lt_92),
            '94': ('M.Pago con cheque cobranza', self._lt_94),
            '95': ('Ticket de fondeo', self._lt_95),
            '97': ('Ticket de retiro', self._lt_97),
            '98': ('No existe', self._lt_98),
            '99': ('Cupones Numeros', self._lt_99),
            '100': ('Ticket de cobranza', self._lt_100),
            '101': ('Ticket de devolución de cobranza', self._lt_101),
            '102': ('Ticket cancelacion de cobranza', self._lt_102),
            '103': ('Cancelación de salida de cajera', self._lt_103),
            '104': ('Seteo monto de prestamo en efectivo', self._lt_104),
            '105': ('Prestamo en efectivo', self._lt_105),
            '106': ('Ticket del cliente de facturación ', self._lt_106),
            '107': ('Ticket de información del cliente', self._lt_107),
            '108': ('Ticket gift card', self._lt_108),
            '109': ('Ticket devolución gift card', self._lt_109),
            '115': ('Pago desc. iva Asig.Fams.', self._lt_115),
            '117': ('Preventa', self._lt_117),
            '118': ('Ticket vale almuerzo', self._lt_118),
            '119': ('Ticket pago vale almuerzo', self._lt_119),
            '120': ('Venta Mides', self._lt_120),
            '121': ('Voucher retiro leche tarjeta Mides', self._lt_121),
            '122': ('Ticket info importe', self._lt_122),
            '123': ('M.Pago TACRE', self._lt_123),
            '124': ('Voucher de la tarjeta TACRE', self._lt_124),
            '125': ('Total puntos PROMO', self._lt_125),
            '126': ('Ticket cliente de cuenta corriente', self._lt_126),
            '127': ('M.Pago cuenta corriente', self._lt_127),
            '128': ('M.Pago devolución envases', self._lt_128),
            '900': ('Declaración de cajera', self._lt_900),
            }
        if not linea or not len(linea) or not tck_id:
            msg = 'Imposible inizializar la clase IPCabezal: '
            if not len(linea):
                msg += '\nla línea recibida como detalle Salida Pazos4 (SM) está vacía.'
            elif not tck_id or len(tck_id) != 14:
                if not len(tck_id):
                    msg += "\nel largo del id del ticket/cabezal no coincide con lo esperado."
                else:
                    msg += "\nfalta el id del ticket/cabezal. "

                msg += "\nfalta la línea de detalle de ticket Salida Pazos4 (SM)."
            logging.error(msg)
            sys.exit(1)
        else:
            self.tck_id = tck_id
            self.rlinea = 'L#' + '#'.join(linea)  # recrea linea de detalle de salidapazos original (debug)
        try:
            self.id_linea = int(linea[0])                 # N.de línea único
            self.numerolinea = linea[0]                   # Idem anterior
            self.llave = llave = linea[1]                 # Tipo de línea de ticket
            self.tipolinea = linea[1]                     # Idem anterior
            self.esta_linea = linea[3:]                   # Datos específicos de línea
            self.hhmmss = hhmmss(linea[2])                # hhmmss (hora minuto segundo)
            self.cabezal_id = tck_id                      # Id del ticket (cabezal de ticket)
            self.hora = hora(linea[2])                    # hh:mm:ss
            self.descripcion = tipos_linea_tck[llave][0]  # Descripción del Tipo de línea

            self.datos = tipos_linea_tck[llave][1]()      # carga datos específicos del tipo de línea en instancia
            _name = str(tck_id) + '-' + str(linea[1]) + '-' + str(linea[0])     # id_ticket + tipo_linea + numero_linea
            self.datos['name'] = _name                    # un id + fuerte. muchas lineas serán cabezales relacionados.

            if verbose:
                print ("\t - fin init `IPLinea`"),
        except Exception as ex:
            print("Error: %s \n\tLínea: %s" % (ex, linea))
            msg = "[ERROR]: %s %s %s" % (ex, linea[1], tipos_linea_tck[linea[1]][0])
            frame = getframeinfo(currentframe())
            excepcion(msg, frame, tck_id)
            sys.exit(1)

    def _lt_method(self):
        """
            El método es un ejemplo, no tiene aplicación práctica.

        :return: dict:  llave0:valor0, llave1=valor1
        """

        lin = self.esta_linea
        result = {}
        try:
            result = {'totalticket': lin[0], 'ivatotalticket': lin[1]}
        except Exception as ex:
            msg = "[ERROR]: %s %s %s %s tck: %s" % (ex, self.llave, self.descripcion, self.id_linea,
                                                    self.cabezal_id)
        return result

    """
        Métodos "lt_nnn":
        '''''''''''''''''
                            Son métodos específicos para cada tipo de linea_de_detalle_de_ticket
        cuya referencia cunsituye el segundo elemento de la lista de valores en el diccionario 
        de tipos.

        Se han definido los métodos correspondiente a los tipos de líneas (casi todas). Algunos
        métodos solo cuentan con el encabezado/definición del método.
        
        A medida que sea necesario se irá desarrollando el resto. Por el momento son `enduído` 
        para namespaces.
    """

    def _lt_1(self):
        """
            Línea de venta de ítem (1)-SM.
            ------------------------------
            `Tipo Líneas de Detalle`        (sin atributos comunes)

            CodigoArticulo # Cantidad # Precio # Iva # PrecioDescuento # IvaDescuento #
                   0            1         2       3          4                5

            PrecioDescuentoCombo # IvaDescuentoCombo # PrecioDescuentoMarca #
                     6                    7                   8

            IvaDescuentoMarca  #   PrecioDescuentoTotal # IvaDescuentoTotal #
                    9                    10                      11

            CantDescManuales # LineaCancelada # ModoIngreso # CodigoVendedor #
                12                  13             14            15

            Talle # Color # Marca # Modelo # SiEsTandem # CodigoArticuloOriginal #
              16      17      18      19       20                  21

            CodigoIva # SiAplicaDescFidel # MontoRealDescFidel # PrecioUnitario
                  22          23                      24               25

            Descripción:
            0. codigoarticulo         Código interno del artículo.
            1. cantidad               Cantidad de artículos vendidos en esa línea. Es la cantidad que
                                            sale impresa en el ticket.
            2. precio                 Precio de la línea del articulo (cantidad x precio unitario)
                                            expresado en la moneda de referencia. Es el precio “limpio”
                                            al cual no se le efectuó ningún descuento (no incluye iva,
                                            este va separado en el siguiente campo).
            3. iva                    Iva de la línea del artículo expresado en la moneda de referencia.
            4. preciodescuento        Precio de la línea del artículo a la cual se aplicó un descuento
                                            directo. Si esta es igual a Precio la línea no fue afectada
                                            por un descuento directo.
            5. ivadescuento           Iva del descuento directo de la línea del articulo.
            6. preciodescuentocombo   Precio de la línea del articulo la cual fue afectada por un
                                            descuento de un Combo. Si el artículo pertenece a un combo y
                                            este se efectuó, se le aplicará el descuento correspondiente
                                            (excepto si el Combo otorga un descuento al total).
                                            Si el importe es igual a PrecioDescuento la línea no fue
                                            afectada por un descuento del Combo.
            7. ivadescuentocombo      Iva del descuento del combo a la línea del artículo.
            8. preciodescuentomarca   Precio de la línea del articulo la cual fue afectada por un
                                            descuento por Marcas. Si el artículo pertenece a una Marca
                                            y esta se efectuó, se le aplicará el descuento correspondiente
                                            (excepto si la Marca otorga un descuento al total). Si el
                                            importe es igual a PrecioDescuentoCombo la línea no fue
                                            afectada por un descuento de Marca.
            9. ivadescuentomarca      Iva del descuento a la Marca a la línea del artículo.
           10. preciodescuentototal   Precio de la línea del artìculo la cual fue afectada por un
                                            descuento al total. Si bien es un descuento al total, se
                                            prorratea a las líneas. Si esta es igual a PrecioDescuentoMarca
                                            la línea no fue afectada por un descuento al total. Nota: Este
                                            es el precio final de artículo una vez aplicado todos los
                                            descuentos si corresponde (sino conserva el precio original),
                                            por lo tanto si se va a procesar los importes de los artículos,
                                            se debe tomar este valor mas el iva.
           11. ivadescuentototal      Iva del descuento al total a la línea del artículo.
           12. cantdescmanuales       Cantidad de descuentos manuales que realizó la cajera.
           13. lineacancelada         Estado
                                        0-Línea no cancelada.
                                        1-Línea cancelada.
                                            Este tipo de línea no tiene valor contable. A pesar
                                            que pudo haber sido afectada por descuentos, esta no
                                            se debe tomar en cuenta.
           14. modoingreso            Modo de ingreso del artículo. Son los siguientes:
                                        0-De teclado.
                                        1-De scanner.
                                        2-Lectora de banda magnética.
           15. codigovendedor         Código de vendedor si aplica, sino va vacío.
           16. talle                  Datos del talle si aplica, sino va vacío.
           17. color                  Color si aplica, sino va vacío.
           18. marca                  Marca si aplica, sino va vacío.
           19. modelo                 Modelo si aplica, sino va vacío.
           20. siestandem             Es tandem.
                                            0 - No es artículo de tandem.
                                            1 - Es artículo de tandem.
           21. codigoarticulooriginal   Es el código original del artículo que ingresó la cajera, ya
                                            sea el código de barras entero o el código digitado manualmente.
                                            En el caso de repetir el ultimo articulo ingresado este campo
                                            no se setea, ya que la cajera no lo ingresa en forma explicita.
           22. codigoiva              Código de iva aplicado.Si no aplica IVA va 0.
           23. siaplicadescfidel      Flag que indica si a la línea se le aplico control de descuento
                                            al total por fidelización.
                                        0-No se aplico control de descuento.
                                        1-Se aplico control de descuento (ver MontoRealDescFidel).
           24. montorealdescfidel     Monto real del descuento controlado por fidelizacion.
           25. preciounitario         Precio unitario del item (precio de lista que incluye IVA).
        """
        lin = self.esta_linea or False
        documentar = {'1': 0.22, '2': 0.10, '3': 0}
        result = dict()
        try:
            result.update(dict(codigoarticulo = lin[0],
                               cantidad = lin[1],
                               precio = lin[2],  # es el IMPORTE sin iva y sin descuentos de la línea
                               iva = lin[3],
                               preciodescuento = lin[4],
                               ivadescuento = lin[5],
                               preciodescuentocombo = lin[6],
                               ivadescuentocombo = lin[7],
                               preciodescuentomarca = lin[8],
                               ivadescuentomarca = lin[9],
                               preciodescuentototal = lin[10],
                               ivadescuentototal = lin[11],
                               cantdescmanuales = lin[12],
                               lineacancelada = lin[13],
                               modoingreso = lin[14],
                               codigovendedor = lin[15],
                               talle = lin[16],
                               color = lin[17],
                               marca = lin[18],
                               modelo = lin[19],
                               siestandem = lin[20],
                               codigoarticulooriginal = lin[21],
                               codigoiva = lin[22],
                               siaplicadescfidel = lin[23],
                               montorealdescfidel = lin[24],
                               preciounitario = lin[25],  # precio unitario "de lista" con iva
                               ))

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_4(self):
        """
            Línea de total del ticket (4)
            Contiene el total del ticket:

            TotalTicket # IvaTotalTicket # TotalTicketSinPagoServicios # IvaTotalTicketSinPagoServicios
                 0              1                     2                                3
            TotalTicket     ->  Importe total del ticket (incluye el iva).

            IvaTotalTicket  ->  Iva del total de ticket (que esta sumado en TotalTicket).

            TotalTicketSinPagoServicios ->  Total del ticket excluyendo los pagos de
                servicios (incluye el iva). Si no hubo pago de servicios es igual que
                TotalTicket.

            IvaTotalTicketSinPagoServicios  ->  Iva del importe anterior (que esta sumado a
                TotalTicketSinPagoServicios).

            Ejemplo de total de ticket sin pago de servicios con un total de 261.76:
            L#13#4#181644#261.76#47.21#261.76#47.21

            Ejemplo de un total de ticket con un total de 774.05 que incluye un pago de servicio de
            774.05 -183.05=591.00 (UTE):
            L#10#4#153713#774.05#21.97#183.05#21.97
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {'totalticket': lin[0],     # Importe total
                      'ivatotalticket': lin[1],  # Iva del ticket
                      'totalticketsinpagoservicios': lin[2],    # Total sin servicios cobrados
                      'ivatotalticketsinpagoservicios': lin[3]} # Total IVA sin servicios
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_5(self):
        """
            Línea de cabezal CFE (5)

            Si el sistema utiliza el modo de Comprobante Fiscal Electronico representa los datos del
            cabezal del documento electronico:

            TipoCFE #  DescripcionCFE # SerieCFE # NumeroCFE # TipoDocumentoReceptor
               0             1             2           3                4
            DocumentoReceptor # NombreReceptor # DireccionReceptor # CiudadReceptor
                  5                   6                 7                 8

            TipoCFE     -> Tipo de comprobante, estos pueden ser:
                            101 e-Ticket
                            102 Nota de Crédito de e-Ticket
                            103 Nota de Débito de e-Ticket
                            111 e-Factura
                            112 Nota de Crédito de e-Factura
                            113 Nota de Débito de e-Factura
                            181 e-Remito
                            182 e-Resguardo
                            201 e-Ticket Contingencia
                            202 Nota de Crédito de e-Ticket Contingencia
                            203 Nota de Débito de e-Ticket Contingencia
                            211 e-Factura Contingencia
                            212 Nota de Crédito de e-Factura Contingencia
                            213 Nota de Débito de e-Factura Contingencia
                            281 e-Remito Contingencia
                            282 e-Resguardo Contingencia

            DescripcionCFE  -> Descripcion del tipo de CFE (ver arriba).

            SerieCFE        -> Serie del CFE.

            NumeroCFE       -> Número del CFE.

            TipoDocumentoReceptor -> Tipo de documento del receptor del CFE.
                este campo es opcional en eTicket y obligatorio en eFactura
                (asímismo en sus recpectivos NdeCr. y NdeDeb.)

                Los valores pueden ser:

                    0: No usado.
                    2: RUC (Uruguay)
                    3: C.I. (Uruguay)
                    4: Otros
                    5: Pasaporte (todos los países)
                    6: DNI (documento de identidad de Argentina, Brasil, Chile o Paraguay).

            DocumentoReceptor->Documento del receptor del CFE si es factura.

            NombreReceptor->Nombre del cliente receptor del CFE si es factura.

            DireccionReceptor->Direccion del cliente receptor del CFE si es factura.

            CiudadReceptor-> Ciudad del cliente receptor del CFE si es factura.

            Ejemplo de un tipo Cfe 112 (Nota de credito de una e-Factura), con serie Cfe AA y
            numero Cfe 5, tipo de documento 2 (Ruc) y numero de RUC 215303240017, a nombre
            de Objetos T &S cuya direccion es Bacigalupi 2158 en la ciudad de Montevideo.
            L#1#5#164324#112#Nota de Crédito de e-Factura# AA# 0000005# 2# 215303240017#
            Objetos T &S # Bacigalupi 2158# Montevideo

            Ejemplo de un tipo de Cfe 101 (e-Ticket) con serie AA y numero 10.
            L#1#5#181708#101#e-Ticket#AA#0000010#0####

            IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea # (no se usan)

            TipoCFE #  DescripcionCFE # SerieCFE # NumeroCFE # TipoDocumentoReceptor
               0             1             2           3                4
            DocumentoReceptor # NombreReceptor # DireccionReceptor # CiudadReceptor
                   5                  6                7                   8

        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'tipocfe': lin[0],
                'descripcioncfe': lin[1],
                'seriecfe': lin[2],
                'numerocfe': lin[3],
                'tipodocumentoreceptor': lin[4],
                'documentoreceptor': lin[5],
                'nombrereceptor': lin[6],
                'direccionreceptor': lin[7],
                'ciudadreceptor': lin[8]
            }
        except Exception as ex:
            print("\tOtro trace:n\t"),
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("%s <-- En %s %s %s\n===\n" % (ex, exc_type, fname, exc_tb.tb_lineno))

            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_6(self):

        """
            Línea de pie CFE (6) pie del documento electronico:

            Cliente # LinkDGI # TipoCFE # RucEmisor # NumeroCFE # FechaCFE # MontoNeto # Hash # CodigoCAE # SerieCFE
               0         1         2         3           4           5           6         7        8           9
            NroInicioCAE # NroFinCAE # FechaVencimientoCAE
                10            11                12

            NombreCliente       -> Nombre del cliente de fidelización (no de CFE, puede venir vacio si no aplica).
            LinkDGI             -> Link al portal DGI.
            TipoCFE             -> Tipo de CFE.
            RucEmisor           -> Ruc de quien emite el CFE.
            NumeroCFE           -> Numero de CFE.
            FechaCFE            -> Fecha de emision del CFE (AAAAMMDD).
            MontoNeto           -> Monto neto del CFE.
            Hash                -> Hash del CFE (los 6 primeros caracteres se utiliza como codigo de seguridad).
            CodigoCAE           -> Codigo de CAE.
            NroInicioCAE        -> Rango de inicio de la CAE.
            NroFinCAE           -> Rango fin de la CAE.
            FechaVencimientoCAE -> Fecha de vencimiento de la CAE(AAAAMMDDHHmmSS).

            Ejemplo de un Cfe tipo 101 cuyo Ruc Emisor es 210297450018, numero de CFE 284, con fecha de emision del CFE 2015/11/11 con un monto neto de 699.00, el hash del CFE es aeSfsWawQz4h9d1XuHnxW24eLNQ= , el codigo de CAE 90115003001,serie de Cfe AC, numero de inicio de rango de CAE 1 y fin 10000 con fecha de vencimiento 2015/12/31/ 00:00:00

            L#12#6#170634# #https://www.efactura.dgi.gub.uy/consultaQR/cfe?#101#210297450018#0000284#2015 1111#699.00#aeSfsWawQz4h9d1XuHnxW24eLNQ=#90115003001#AC#1#10000#20 151231000000

        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'cliente': lin[0],
                'linkdgi': lin[1],
                'tipocfe': lin[2],
                'rucemisor': lin[3],
                'numerocfe': lin[4],
                'fechacfe': lin[5],
                'montoneto': lin[6],
                'hash': lin[7],
                'codigocae': lin[8],
                'seriecfe': lin[9],
                'nroiniciocae': lin[10],
                'nrofincae': lin[11],
                'fechavencimientocae': lin[12]
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_7(self):
        """
            Línea de identificación de la cajera (7).
            ----------------------------------------

            CodigoCajera # Nombre
            0.Código
            1.Nombre
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {'codigocajera': lin[0], 'nombrecajera': lin[1]}

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_9(self):
        """
         Línea de pago de ticket en efectivo (9).
         ---------------------------------------

         CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
                0                1                 2
         TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                     3                               4
         TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
                     5                    6          7                8
         AutorizaSupervisora # CodigoSupervisora # LineaCancelada
                  9                    10                11
         0. Código del medio de pago.
         1. Código de la moneda.
         2. Monto total de lo que se puede pagar con el medio de pago moneda.
         3. Idem que el anterior pero expresado en la moneda de referencia.
         4. Total entregado de ese medio de pago-moneda.
         5. Total entregado expresado en la moneda de referencia.
         6. Cambio de la línea de pago (valor >= 0.00)
         7. Codigo de Operacion.
                 0 - Si corresponde a una venta (los importes van en positivo).
                 1 - Si corresponde a una devolución por parte del cliente (los
                     importes van en negativo).
         8. Ultimo pago.
                 0 - No es la línea del último pago. Esto sucede cuando el ticket
                     se paga con múltiples pagos (inclusive de distintos medios
                     de pago-monedas) cuando el importe abonado es menor al
                     total a pagar.
                 1 - Es la línea del último pago.
         9. Intervención supervisor.
                 0 - Línea de pago sin intervención de supervisor.
                 1 - Línea de pago autorizada por supervidor.
        10. Código de la supervisora.
        11. Estado de la línea de pago.
            0-Línea de pago no cancelada.
            1-Línea de pago cancelada.
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                # monto pagable en éste medio de pago expresado en la moneda usada.
                'totalmediopagomonedamonedareferencia': lin[3],
                # lo mismo pero expresado en mon.referencia (PESOS)
                'totalpagado': lin[4],  # Total recibido en la moneda usada.
                'totalpagadomonedareferencia': lin[5],  # lo mismo pero expresado en moneda de referencia (PESOS)
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'autorizasupervisora': lin[9],
                'codigosupervisora': lin[10],
                'lineacancelada': lin[11],
                }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_10(self):
        """ Cabezal de un combo """
        pass

    def _lt_11(self):
        """Detalle de combo"""
        pass

    def _lt_12(self):
        """
            Línea de cancelación de ítem (12).
            ----------------------------------

            La línea de cancelación de un artículo se produce cuando se cancela
            una línea registrada de venta de artículo.

            CodigoArtSubf # NroLineaVta # Importe # IndicadorArtSubf # NombreSupervisora # CodigoVendedor
                  0             1            2              3                 4                 5
            CodigoArtSubf-> Código del artículo o subfamilia que se cancela.
            NroLineaVta-> Número de línea de venta que se cancela.
                          Esto sirve para indicar cuando hay mas de un artículo
                          de mismo código en la venta y se cancelo uno en particular.
                          Este numero de línea de venta no corresponde a NumeroDeLinea
                          (segundo campo) que es el numero de línea de ticket,
                          sino al numero de línea de venta de tipo 1 (es decir, el numero
                          de línea de venta de tipo 1 del ticket), o sea hay que contar
                          los tipos de línea de venta 1 para llegar a la línea de venta
                          cancelada.
            Importe-> Importe cancelado. Es a nivel informativo, ya que debe coincidir con
                      el importe de la línea de venta.Incluye Iva.
            IndicadorArtSubf-> A - Cancelación de artículo.
                               S - Cancelación de Subfamilia.
                               C - Cancelación de Cobranza.
                               T - Cancelación de artículo de tandem.
            NombreSupervisora-> Nombre de la supervisora que intervino en la cancelación
                                (también a nivel informativo).
            CodigoVendedor-> Código de vendedor si la caja está configurado para utilizar vendedor.
                             Si no hay vendedor va vacío.

            Ejemplo de una línea de venta del artículo 241800, de importe 11.20 que fue cancelada (1):
            L#6#1#191524#241800#1.000#9.18#2.02#9.18#2.02#9.18#2.02#9.18#2.02#9.18#2.02#0#1#1######0
            El artículo 241800 fue cancelado, corresponde a la primera línea de venta,
            el importe cancelado es de 11,20 (que también coincide con el importe de
            la línea de venta 9.18 + 2.02).
            El código de vendedor es 12:
            L#8#12#191524#241800#1#-11.20#A#Supervisora Uno#12
            Ejemplo de cancelación de subfamilia 3 por 250 pesos, sin código de vendedor.
            L#9#12#133552#3#1#-250.00#S#Supervisora Uno#
            La línea de venta de subfamilia 3 (tipo 30) que fue cancelada es:
            L#7#30#133552#3#1.000#204.92#45.08#204.92#45.08#204.92#45.08##1#0
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigoarticulosubf': lin[0],
                'nrolineavta': lin[1],
                'importe_cancelado': lin[2],
                'indicadorartsubf': lin[3],
                'nombresupervisora': lin[4],
                'codigovendedor': lin[5],
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_13(self):
        """Descuento a un ítem"""
        pass

    def _lt_15(self):
        """Puntos generados de fidelización por el ítem"""
        pass

    def _lt_16(self):
        """Puntos totales de fidelización generados"""
        pass

    def _lt_18(self):
        """Regalo de artículos"""
        pass

    def _lt_19(self):
        """Cupón"""
        pass

    def _lt_20(self):
        """
            Línea de devolución de un ítem (20) -SM.
            Representa la línea de devolución de artículos.
            IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea #
            CodigoArticuloSubf # Cantidad # Precio # Iva # IndicadorArtSubf # CodigoSupervisora # CodigoArticuloOriginal
                    0                1         2       3          4                   5                     6
            ModoIngreso # CodigoVendedor # LineaCancelada # PrecioDescuento # IvaDescuento # CodigoIva # PrecioInicial
                 7              8               9                 10               11            12           13
            IvaPrecioInicial
                  14

            CodigoArticuloSubf          ->  Código de artículo/subfamilia.
            Cantidad                    ->  Cantidad de ítems devueltos.
            Precio                      ->  Precio del ítem (negativo). El precio no siempre coincide con
                                            el de venta (si es que se vendió, pues se puede imputar un precio
                                            distinto al de lista, generalmente cuando el artículo tuvo descuentos
                                            o fue una promoción. También puedo devolver un artículo que no es parte
                                            de la venta.
            Iva                         ->  Iva del ítem (negativo).
            IndicadorArtSubf            ->  A - Devolución de artículo.
                                            S - Devolución de subfamilia.
            CodigoSupervisora           ->  Código de la supervisora.
            CodigoArticuloOriginal      ->  Es el código original del artículo que ingresó la cajera, ya sea el
                                            código de barras entero o el código digitado manualmente.
            ModoIngreso                 ->  Modo de ingreso del artículo/subfamilia. Son los siguientes:
                                            0 - De teclado.
                                            1 - De scanner.
                                            2 - Lectora de banda magnética.
            CodigoVendedor              ->  Código de vendedor si la caja está configurado para utilizar
                                            vendedor. Si no hay vendedor va vacío.

            LineaCancelada              ->  0 - Línea no cancelada.
                                            1 - Línea cancelada. La devolución del item fue cancelada y no debe ser
                                            tomada en cuenta como valor contable.
            PrecioDescuento             ->  Precio del Articulo con sus cantidades ya con descuentos aplicados.
            IvaDescuento                ->  Contiene el IVA del articulo con sus cantidades ya con descuentos
                                            aplicados.
            CodigoIva                   ->  Codigo de iva.


            Ejemplo de la línea de venta del artículo 972197 por 235.30 pesos y 51.76 de iva.
            L#7#1#154232#972197#1.000#235.30#51.76#235.30#51.76 #235.30#51.76 #235.30#51.76#235.30#51.76 #0#0#0######0#1

            Devolución del mismo artículo, con código de vendedor 12:
            L#9#20#154232#972199#1.000#-235.30#-51.76#A#1#972199#1#12#0#-235.30#-51.76#1#-235.30#-51.76

            Línea de devolución de un ítem (20) -SM. Representa la línea de devolución de artículos.



        CodigoArticuloSubf # Cantidad # Precio # Iva # IndicadorArtSubf # CodigoSupervisora # CodigoArticuloOriginal #
                0               1          2      3           4                 5                        6
        ModoIngreso # CodigoVendedor # LineaCancelada # PrecioDescuento # IvaDescuento # CodigoIva
              7           8                   9              10                11            12

        """

        # if self.id_linea ==  '20171204001841611545328':
        #    import ipdb;ipdb.set_trace()

        lin = self.esta_linea or False
        result = {}
        try:
            result = dict(codigoarticulosubf = lin[0] or None,
                          cantidad = lin[1] or None,
                          precio = lin[2] or None,
                          iva = lin[3] or None,
                          indicadorartsubf = lin[4] or None,
                          codigosupervisora = lin[5] or None,
                          codigoarticulooriginal = lin[6] or None,
                          modoingreso = lin[7] or None,
                          codigovendedor = lin[8] or '',
                          lineacancelada = lin[9] or None,
                          preciodescuento = lin[10] or None,
                          ivadescuento = lin[11] or None,
                          codigoiva = lin[12] or None,
                          )

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_21(self):
        """Entrada de cajera
            Línea de entrada de cajera (21)

            # NombreCajera # NumeroSesion
                  0               1
            NombreCajera        ->  Nombre de la cajera.
            NumeroSesion        ->  Número de la sesión de la cajera.

            Ejemplo de entrada de cajera (21)
            L#6#21#181633#Cajera Uno#1
        """
        lin = self.esta_linea
        result = dict()
        try:
            result.update(
                dict(nombrecajera = lin[0], numerosesion = lin[1])
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_22(self):
        """
              Línea de salida de cajera (22)

              # NombreCajera # NumeroSesion
                    0               1
              NombreCajera        ->  Nombre de la cajera.
              NumeroSesion        ->  Número de la sesión de la cajera.

              Ejemplo de salida de cajera (22)
              L#6#22#154650#Cajera Uno#1
        """
        lin = self.esta_linea
        result = dict()
        try:
            result.update(
                dict(nombrecajera = lin[0], numerosesion = lin[1])
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_23(self):
        """   Línea de pausa de cajera (23)

              # NombreCajera # NumeroSesion
                    0               1
              NombreCajera        ->  Nombre de la cajera.
              NumeroSesion        ->  Número de la sesión de la cajera.

              Ejemplo de pausa de cajera (23)
              L#6#23#154942#Cajera Uno#2
        """
        lin = self.esta_linea
        result = dict()
        try:
            result.update(
                dict(nombrecajera = lin[0], numerosesion = lin[1])
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_24(self):
        """Cancelacion ticket"""
        lin = self.esta_linea or False

        result = {}
        try:
            result = {'texto': lin[0]}

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_26(self):
        """Cabezal de beneficio al total"""
        pass

    def _lt_27(self):
        """Detalle de un beneficio al total"""
        pass

    def _lt_28(self):
        """Descuento al total"""
        pass

    def _lt_29(self):
        """ Línea de devolución de envases (29).
            Representa las líneas de ticket de devolución de envases.
            IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea # Importe # Iva
            Importe->Importe de la devolución de envases.
            Iva->Iva del importe.
            Ejemplo de devolución de envases por 8.20 + 1.80 = 10.00
            L#6#29#160110#8.20#1.80
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'importe': lin[0],
                'iva': lin[1]
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_30(self):

        """
            Línea de venta a la subfamilia (30).
            -----------------------------------

            Representa las líneas de tickets de venta por imputación a una subfamilia.

            Código-> Código de la subfamilia.
            Cantidad-> Cantidad imputada a la subfamilia.
            Precio-> Precio imputado a la subfamilia.
            Iva-> Iva del precio.
            ImporteDescuento-> Importe de la línea a la cual se aplicó un descuento directo. Si esta es igual a Precio la línea no fue afectada por un descuento directo.
            IvaDescuento-> Iva del descuento.
            ImporteDescuentoTotal-> Importe de la línea la cual fue afectada por un descuento al total. Si bien es un descuento al total, se prorratea a las líneas. Si esta es igual a ImporteDescuento la línea no fue afectada por un descuento al total.
            IvaImporteDescuentoTotal-> Iva del importe del descuento al total.
            CodigoVendedor-> Código de vendedor si aplica, sino va vacío.
            LineaCancelada-> 0-Línea no cancelada.
                            1-Línea cancelada.
                                Este tipo de línea no tiene valor contable.
                                A pesar que pudo haber sido afectada por descuentos, esta no se debe tomar en cuenta.
            ModoIngreso-> Modo de ingreso del artículo. Son los siguientes:
                            0-De teclado.
                            1-De scanner.
                            2-Lectora de banda magnética.

            Código # Cantidad # Precio # Iva # ImporteDescuento # IvaDescuento # ImporteDescuentoTotal # IvaImporteDescuentoTotal # CodigoVendedor # LineaCancelada # ModoIngreso
               0         1        2       3           4                5                 6                          7                     8               9               10
            Ejemplo de una venta a la subfamilia 3 con cantidad unitaria, por in importe de 18.85 + 4.15 = 23.00, el cual no tuvo ni descuentos directos ni al total, sin vendedor, la línea no está cancelada y se ingresó por teclado.
            L#8#30#160219#3#1.000#18.85#4.15#18.85#4.15#18.85#4.15##0#0
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigo': lin[0],
                'cantidad': lin[1],
                'precio': lin[2],
                'iva': lin[3],
                'importedescuento': lin[4],
                'ivadescuento': lin[5],
                'importedescuentototal': lin[6],
                'ivaimportedescuentototal': lin[7],
                'codigovendedor': lin[8],
                'lineacancelada': lin[9],
                'modoingreso': lin[10]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_32(self):
        pass

    def _lt_33(self):
        pass

    def _lt_34(self):
        pass

    def _lt_35(self):
        pass

    def _lt_36(self):
        pass

    def _lt_37(self):
        """
        Pago con tarjeta
        ----------------


         0. Código del medio de pago.
         1. Código de la moneda.
         2. Monto total de lo que se puede pagar con el medio de pago moneda.
         3. Idem que el anterior pero expresado en la moneda de referencia.
         4. Total entregado de ese medio de pago-moneda.
         5. Total entregado expresado en la moneda de referencia.
         6. Cambio de la línea de pago (valor >= 0.00)
         7. Codigo de Operacion.
                 0 - Si corresponde a una venta (los importes van en positivo).
                 1 - Si corresponde a una devolución por parte del cliente (los
                     importes van en negativo).
         8. Ultimo pago.
                 0 - No es la línea del último pago. Esto sucede cuando el ticket
                     se paga con múltiples pagos (inclusive de distintos medios
                     de pago-monedas) cuando el importe abonado es menor al
                     total a pagar.
                 1 - Es la línea del último pago.
         9. Numero de la tarjeta.
        10. Cuotas.
        11. Nro. de autorización del emisor.
        12. Tipo de tarjeta - undocumented.
        13. Intervención supervisor.
                  0 - Línea de pago sin intervención de supervisor.
                  1 - Línea de pago autorizada por supervidor.
        15. Código de la supervisora.
        15. Estado de la línea de pago.
             0-Línea de pago no cancelada.
             1-Línea de pago cancelada.
        16. Plan utilizado por la tarjeta.
        17. Numero de comercio al que pertenece el socio titular de la tarjeta.
        18. Si aplica ley descuento iva
        19. Monto Descuento Ley Iva
        20. Texto Ley
        21. Tarjeta de Debito/Credito.
                 0 - No especificado.
                 1 - La tarjeta es de credito.
                 2 - La tarjeta es de debito.

        CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
               0              1                   2

        TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                        3                           4

        TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
               5                         6           7             8

        NumeroTarjetaCredito # CuotasTarjetaCredito #
            9                   10

        NumeroAutorizacionTarjetaCredito # TipoTarjetaCredito # AutorizaSupervisora  #
                  11                              12                  13

        CodigoSupervisora # LineaCancelada # Plan # NroComercio #
                14                  15        16       17

        SiAplicaLeyDescIva # MontoDescuentoLeyIva # # TextoLey # SiEsDebitoCredito
              18                      19                  20            21


        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'numerotarjetacredito': lin[9],
                'cuotastarjetacredito': lin[10],
                'numeroautorizaciontarjetacredito': lin[11],
                'tipotarjetacredito': lin[12],
                'autorizasupervisora': lin[13],
                'codigosupervisora': lin[14],
                'lineacancelada': lin[15],
                'plan': lin[16],
                'nrocomercio': lin[17],
                'siaplicaleydesciva': lin[18],
                'montodescuentoleyiva': lin[19],
                'textoley': lin[20],
                'siesdebitocredito': lin[21]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_38(self):
        """
            Línea de pago con cheque (38)-SM.
            --------------------------------

            Línea de ticket cuando se paga con cheque. Cuando un cliente paga
            con cheques, el mismo debe estar autorizado con un identificador
            (campo idCliente).

            0. Código del medio de pago.
            1. Código de la moneda.
            2. Monto total de lo que se puede pagar con el medio de pago moneda.
            3. Idem que el anterior pero expresado en la moneda de referencia.
            4. Total entregado de ese medio de pago-moneda.

            5. Total entregado de ese medio de pago-moneda.
            6. Total entregado expresado en la moneda de referencia.

            7. Cambio de la línea de pago
                    0 - Venta (valor >= 0.00 )
                    1 - Devolución por parte del cliente (valor < 0.00 )

            8. Lin. Ultimo Pago
                    0 - No es la línea del último pago. Esto sucede cuando el
                        ticket se paga con múltiples pagos (inclusive de
                        distintos medios de pago-monedas) cuando el importe
                        abonado es menor al total a pagar.
                    1 - Es la línea del último pago.

            9. Tipo de Cliente.
           10. Identificación cliente.
           11. Supervisora
                       0 - La línea de pago no tuvo autorización de la
                           supervisora.
                       1 - La línea de pago tuvo autorización de la supervisora.

           12. Código de la supervisora (vacío si no aplica)
           13. Linea cancelada
                       0 - Línea de pago no cancelada.
                       1 - Línea de pago cancelada.

            Indices:
            -------

            CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
                  0                 1                2

            TotalMedioPagoMonedaMonedaReferencia #  TotalPagado #
                             3                               4

            TotalPagadoMonedaReferencia # Cambio # TipoOperacion #
                        5                   6           7

            LineaUltimoPago # TipoCliente # IdCliente # AutorizaSupervisora #
                    8               9           10          11

            CodigoSupervisora # LineaCancelada
                  12                  13

        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'tipocliente': lin[9],
                'idcliente': lin[10],
                'autorizasupervisora': lin[11],
                'codigosupervisora': lin[12],
                'lineacancelada': lin[13]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_40(self):
        """

         Línea de pago luncheon ticket (40) SM.
         -------------------------------------

         0 Código del medio de pago.
         1 Código de la moneda.
         2 Monto total de lo que se puede pagar con el medio de pago moneda.
         3 Idem que el anterior pero expresado en la moneda de referencia.
         4 Total entregado de ese medio de pago-moneda.
         5 Total entregado expresado en la moneda de referencia.
         6 Cambio de la línea de pago (valor >= 0.00 5).
         7 TipoOperacion.
             0 - Venta ( importes > 0.00).
             1 - Devolución ( importes < 0.00).
         8 LineaUltimoPago.
             0 - No es la línea del último pago. Esto sucede cuando el ticket
                 se paga con múltiples pagos (inclusive de distintos medios de
                 pago-monedas) cuando el importe abonado es menor al total a pagar.
             1 - Es la línea del último pago.
         9 CodigoBarra.
             1 - código de barras del cupón.
             0 - monto total de los cupones o el codigo de barras ingresado
                 manualmente de ese cupon.
        10 ModoIngresoCupon.
             0 - Teclado.Este modo de ingreso se efectua cuando la cajera
                 ingresa el monto del total de los cupones o el codigo de
                 barras de ese cupon.
             1 - Scanner.Cuando se procesan los cupones por scanner, validando
                 los mismos.
        11 AutorizaSupervisora.
             0 - La línea de pago no tuvo autorización de la supervisora.
             1 - La línea de pago tuvo autorización de la supervisora.
        12 CodigoSupervisora.
        13 Código de la supervisora (vacío si no aplica)
        14 LineaCancelada.
             0 - activa.
             1 - cancelada.


        Indices:
        -------

        CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
             0                  1                 2

        TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                        2                           4

        TotalPagadoMonedaReferencia # Cambio # TipoOperacion #
                    5                   6           7

        LineaUltimoPago# CodigoBarra # ModoIngresoCupon # AutorizaSupervisora #
                8           9               10                  11

        CodigoSupervisora # LineaCancelada
            12                  13
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'codigobarra': lin[9],
                'modoingresocupon': lin[10],
                'autorizasupervisora': lin[11],
                'codigosupervisora': lin[12],
                'lineacancelada': lin[13]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_43(self):

        """
            Línea de voucher de la tarjeta (43)-SM.
            Muestran la información de un Voucher de Pago cuando se paga con Tarjeta de Crédito/Debito.
            La mayoría de la información aquí presentada la retorna el autorizador y Jswitch
            (Referirse al documento Especificaciones jSwitch.doc por posibles cambios).

            IdentificadorLinea* # NumeroDeLinea* # TipoLinea* # TimestampLinea* # NombreEmisorTarjeta #
            NumeroTarjeta # Vencimiento # Comprobante # Autorizacion # Plan # CantidadCuotas          #
            CodigoTerminal # CodigoComercio # TipoAutorizacion # NroLote # CodigoMoneda               #
            TipoTransaccion # TipoVoucher # ImportePago # FechaTransaccion # CodigoCaja*             #
            CodigoCajera* # NombrePropietario # TipoIngreso # DescuentaIvaRestaurante                 #
            SiEsDebitoCredito # CardType # SaldoGift # TipoTarjetaCredito2 # DescuentoAfam            #
            SiAplicaLeyDescIva # MontoDescuentoLeyIva # MontoTicket # MontoGravado                    #
            FlagImprimeFirma

            *Datos que no provienen de la autorizadora.

            NombreEmisorTarjeta         -> Nombre emisor de la tarjeta.
            NumeroTarjeta               -> Número de la tarjeta de crédito.
            Vencimiento                 -> Vencimiento de la tarjeta de crédito (aamm).
            Comprobante                 -> Número de comprobante.
            Autorizacion                -> Número de autorización.
            Plan                        -> Código de plan asociado.
            CantidadCuotas              -> Cantidad de cuotas.
            CodigoTerminal              -> Código de la terminal asociado.
            CodigoComercio              -> Código de comercio asociado.
            TipoAutorizacion            -> Tipos : 00-Online;
                                                   01-Offline;
                                                   20-Online aplica ley descuento IVA;
            NroLote                     -> Número de lote asociado.
            CodigoMoneda                -> Código de la moneda asociado.
                                                   00-Pesos
                                                   01-Dólares.
            TipoTransaccion             -> Tipo de transacción asociado (MTI).
                                                   1200 - Compra
                                                   1220 - Confirmación Compra
                                                   1240 - Notificación de Compra
                                                   1400 - Devolución (Total o parcial)
                                                   1420 - Confirmación Devolución
                                                   1440 - Notificación de Devolución
                                                   9xxx - Entrenamiento
            TipoVoucher                 -> Tipo de voucher asociado.
                                                   0-Original Cliente.
                                                   1-Vía Establecimiento.
            ImportePago                 -> Importe pagado por la tarjeta de crédito.
            FechaTransaccion           -> Fecha de transacción de la autorización.
            CodigoCaja*                 -> Código de la caja.
            CodigoCajera*               -> Código de la cajera.
            NombrePropietario           -> Nombre del propietario de la tarjeta de crédito.
            TipoIngreso                 -> Tipo de ingreso asociado.
                                                   0-Lectura magnética.
                                                   1-Entrada manual
                                                   2-Internet.
            ATENCION: Hay valores '4' para `TipoIngreso` octubre 2018
            DescuentaIvaRestaurante     -> Descuento restaurante
                                                   0 - No tiene descuento iva por ley 17934.
                                                   1 - Tiene descuento iva por ley 17934.
            SiEsDebitoCredito           -> Tipo de la tarjeta de crédito:
                                                   0-Nada.
                                                   1-Crédito.
                                                   2-Débito.
            CardType                    -> Card Type retornado por el autorizador.
            SaldoGift                   -> Saldo de la tarjeta Gift (vacio si no es tarjeta gift).
            TipoTarjetaCredito2         -> Tipo de tarjeta de credito (redundante con TipoTarjetaCredito)
                                                   1-Crédito
                                                   2-Débito.
                                                   3-Gift
            4-Afam
            DescuentoAfam               -> Importe del descuento aplicado si la tarjeta es Afam (0.00 si no aplica).
            SiAplicaLeyDescIva          -> Flag que indica si se aplica la ley 19210 de inclusión financiera de descuento de iva.
                                                   0 - No aplica ley de descuento de iva.
                                                   1 - Aplica ley de descuento de iva.
            MontoDescuentoLeyIva        -> Monto del descuento de Iva (en negativo).
            MontoTicket                 -> Monto del ticket.
            MontoGravado                -> Monto gravado sin Iva del ticket.
            FlagImprimeFirma            ->         0 - No se solicita la firma.
                                                   1 - Se solicita la firma.
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'nombreemisortarjeta': lin[0],
                'numerotarjeta': lin[1],
                'vencimiento': lin[2],
                'comprobante': lin[3],
                'autorizacion': lin[4],
                'plan': lin[5],
                'cantidadcuotas': lin[6],
                'codigoterminal': lin[7],
                'codigocomercio': lin[8],
                'tipoautorizacion': lin[9],
                'nrolote': lin[10],
                'codigomoneda': lin[11],
                'tipotransaccion': lin[12],
                'tipovoucher': lin[13],
                'importepago': lin[14],
                'fechatransaccion': lin[15],
                'codigocaja': caja3dig(lin[16]),
                'codigocajera': lin[17],
                'nombrepropietario': lin[18],
                'tipoingreso': lin[19],
                'descuentaivarestaurante': lin[20],
                'siesdebitocredito': lin[21],
                'cardtype': lin[22],
                'saldogift': lin[23],
                'tipotarjetacredito2': lin[24],
                'descuentoafam': lin[25],
                'siaplicaleydesciva': lin[26],
                'montodescuentoleyiva': lin[27],

                'montoticket': lin[28],
                'montogravado': lin[29],
                'flagimprimefirma': lin[30]
            }


        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_44(self):
        pass

    def _lt_47(self):
        """
        Línea de pago de servicio (47) - por ahora cuenta corriente-

        Representa las líneas de los pagos de servicios .
        Código         -> Código del pago de servicio
        Monto          -> Importe del pago de servicio.
        Moneda         -> Código de moneda.
        ModoIngreso    -> 0-Teclado. 1-Scanner. 2-Banda magnética.
        CodigoVendedor -> Código de vendedor si la caja está configurado para utilizar vendedor.Si no hay vendedor va vacío.
        Referencia     -> Referencia del pago de servicio.Esta se compone de dos partes,los primeros 10 dígitos corresponde al número de factura, los siguientes 10 dígitos al número de cuenta.Puede venir vacio.
        LineaCancelada -> 0 - Línea de pago no cancelada. 1 - Línea de pago cancelada. No tiene valor contable.

        C#1#4#1294#131#20151218113128#F#0#15603.00#20#12
        L#1#5#113128#
        L#3#7#113128#131#SHIRLEY BRAVO
        L#4#53#113128#TICKET DE VENTA#0
        L#5#57#113128#20##0###
        L#6#47#113128#1#15602.83#1#0###0
        L#7#68#113143#4580#ROIG ELBIO##JUAN M.GUTIERREZ 1643 -21490###1#0
        L#8#4#113229#15602.83#0.00#0.00#0.00
        L#9#63#113229#15602.83#0.17#15603.00#1#1
        L#10#9#113229#1#1#15603.00#15603.00#15603.00#15603.00#0.00#0#1#0##0

        ticket = {
            ('C', '1', '4', '1294', '131', '20151218113128', 'F', '0', '15603.00', '20', '12') :
                ['L', '1', '5', '113128', ''],
                ['L', '3', '7', '113128', '131', 'SHIRLEY BRAVO'],
                ['L', '4', '53', '113128', 'TICKET DE VENTA', '0'],
                ['L', '5', '57', '113128', '20', '', '0', '', '', ''],
            --> ['L', '6', '47', '113128', '1', '15602.83', '1', '0', '', '', '0'], <--
                ['L', '7', '68', '113143', '4580', 'ROIG ELBIO', '', 'JUAN M.GUTIERREZ 1643 -21490', '', '', '1', '0'],
                ['L', '8', '4', '113229', '15602.83', '0.00', '0.00', '0.00'],
                ['L', '9', '63', '113229', '15602.83', '0.17', '15603.00', '1', '1'],
                ['L', '10', '9', '113229', '1', '1', '15603.00', '15603.00', '15603.00', '15603.00', '0.00', '0', '1', '0', '', '0']
         }

            Código # Monto # Moneda # ModoIngreso # CodigoVendedor # Referencia # LineaCancelada
               0       1       2          3               4              5              6
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codserviciopagado': lin[0],  # '1' = cta.cte
                'importecobranza': lin[1],
                'codigomoneda': lin[2],
                'modoingreso': lin[3],
                'codigovendedor': lin[4],
                'referencia': lin[5],
                'lineacancelada': lin[6]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_49(self):
        pass

    def _lt_52(self):
        """
            Línea de pago de caja (52).
            Representa la linea_de_cabezal de pago de caja (similar a un retiro pero se
            utiliza para pagos puntuales como pago a proveedores, taxis, etc.).


            IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea # Codigo # Importe
            Codigo->Código del rubro de pago de caja.
            Importe->Importe del pago de caja.
            Ejemplo de un pago de caja con codigo 1 y monto de 150.00 pesos
        """
        lin = self.esta_linea or False

        result = dict()
        try:
            result.update(dict(codigo = lin[0], importe = lin[1]))

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_53(self):
        """
            Línea tipo de ticket (53)-SM.
            '''''''''''''''''''''''''''''

            Representa la línea del `tipo de ticket`
            y si se trata de un ticket normal o excento de iva.

            DescripcionTipoTicket -> Descripcion del tipo de ticket.
            TipoVenta             -> Flag de tipo
                                        1 - El ticket esta excento de iva.
                                        0 - Ticket normal.

            Indices:
            ''''''''

            # DescripcionTipoTicket # TipoVenta
                     0                   1

            Por ahora, este último campo sirve para los tickets de venta y
            devolución.
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'descripciontipoticket': lin[0],
                'tipoventa': lin[1]
                }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_54(self):

        # igual a la 9 efectivo

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                # monto pagable en éste medio de pago expresado en la moneda usada.
                'totalmediopagomonedamonedareferencia': lin[3],
                # lo mismo pero expresado en mon.referencia (PESOS)
                'totalpagado': lin[4],  # Total recibido en la moneda usada.
                'totalpagadomonedareferencia': lin[5],  # lo mismo pero expresado en moneda de referencia (PESOS)
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'autorizasupervisora': lin[9],
                'codigosupervisora': lin[10],
                'lineacancelada': lin[11],
                }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_55(self):

        """Intervensión Supervidora"""

        lin = self.esta_linea or False

        result = {}
        try:
            result = {'codigosuper': lin[0],
                      'nombresuper': lin[1]}

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_56(self):
        pass

    def _lt_57(self):
        """
            Línea de tipo de cliente (57)-SM
            --------------------------------

            Representa el detalle del tipo de cliente en la venta.

            0 Nombre del cliente (vacio si no aplica).
            1 Número del cliente interno (vacio si no aplica).
            2 Tipo de cliente interno.
                0-Productor
                1-Empleado
                Vacio-General.

            Indices:
            --------

            Tipo # NumeroTarjeta # ModoIngreso # Nombre # Numero #  TipoClienteInterno
              0         1               2           3       4                5

            L#4#57#221300#20##-1###

            NumeroDeLinea # TipoLinea # TimestampLinea # Tipo # NumeroTarjeta # ModoIngreso
                 4        #    57     #   221300       #   20 #    ''         #    -1
              # Nombre # Numero # TipoClienteInterno
              #   ''   #  ''    #    ''

            raw = [4, 57, 221300, 20, '', -1, '', '', '']
            self.esta_linea = raw[3:]
            self.esta_linea = [20, '', -1, '', '', '']
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'tipo': lin[0],
                'numerotarjeta': lin[1],
                'modoingreso': lin[2],
                'nombre': lin[3],
                'numero': lin[4],
                'tipoclienteinterno': lin[5]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_58(self):
        pass

    def _lt_60(self):
        pass

    def _lt_61(self):
        """
        Línea de pedidos (61)-SM.
            Representa la línea de un pedido (por lo tanto el ticket entero responde a un pedido).
            NumeroPedido

            NumeroPedido    ->  Numero de pedido (también llamada orden del pedido).
            Ejemplo de una línea de pedido con la orden de pedido 125:
            L#6#61#190956#125
            """
        lin = self.esta_linea or False
        result = {}
        try:
            result = {'numeropedido': lin[0], }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result



    def _lt_62(self):
        """
              Línea de fin de pausa de cajera (62)

              # NombreCajera # NumeroSesion
                    0               1
              NombreCajera        ->  Nombre de la cajera.
              NumeroSesion        ->  Número de la sesión de la cajera.

              Ejemplo de fin de pausa de cajera (62)
              L#6#62#152517#Cajera Dos#1
        """
        lin = self.esta_linea
        result = dict()
        try:
            result.update(
                dict(nombrecajera = lin[0], numerosesion = lin[1])
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_63(self):
        """

            Línea de redondeo del ticket.
            ----------------------------

            # ImporteTicket # ImporteRedondeo # ImporteTotalTicket # CodigoMedioPago # CodigoMoneda
                    0                1                  2                  3                 4
            ImporteTicket->Importe del total del ticket sin redondeo.

            ImporteRedondeo->Importe del redondeo aplicado.

            ImporteTotalTicket->Importe total del ticket que es ImporteTicket + ImporteRedondeo.

            CodigoMedioPago->Codigo del medio de pago. (ojo, siempre viene en '1': Efectivo)

            CodigoMoneda->Codigo de la moneda.

            Ejemplo de una línea de redondeo con un importe de ticket de 42.90, al cual se le aplicó
            un redondeo de 0.10 para obtener un importe total a abonar de 43.00 efectivo-pesos
            L#9#63#164146#42.90#0.10#43.00#1#1

            I M P O R T A N T E:
            '''''''''''''''''''    Una posibilidad es tratarlo como `medio de pago`, para eso
            se *modifica estructura*, agregando dos campos por compatibilidad con el resto de
            los medios de pago. Se agregaron 'cambio' y 'totalpagadomonedareferencia' éste último
            es copia del valor de `importeredondeo`

            En el ERP se consideran los valores ya redondeados en todos los casos, es por eso que
            el redondeo se tratará como una simple etiqueta que informa el valor pero no se tiene
            en cuenta su monto.
            """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'importeticket': lin[0],
                'importeredondeo': lin[1],
                'importetotalticket': lin[2],
                'codigomediopago': lin[3],
                'codigomoneda': lin[4],
                'cambio': 0,                            # se incorpora `cambio` y `totalpagadomonedareferencia`
                'totalpagadomonedareferencia': lin[1],  # éste último es copia del copia valor de `importeredondeo`
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_65(self):
        pass

    def _lt_67(self):
        """
             Línea de pago de cupón corporativo (67).
            Representa la línea cuando se paga con cupón corporativo.

            CodigoMedioPago
            CodigoMoneda
            TotalMedioPagoMoneda
            TotalMedioPagoMonedaMonedaReferencia
            TotalPagado
            TotalPagadoMonedaReferencia
            Cambio
            TipoOperacion
            LineaUltimoPago
            CodigoCupon
            AutorizaSupervisora
            CodigoSupervisora
            LineaCancelada

            CodigoMedioPago                         ->  Código del medio de pago.
            CodigoMoneda                            ->  Código de la moneda.
            TotalMedioPagoMoneda                    ->  Monto total de lo que se puede pagar con el medio de pago
            moneda.
            TotalMedioPagoMonedaMonedaReferencia    ->  Idem que el anterior pero expresado en
            la moneda de referencia.
            TotalEntregado                          ->  Total entregado de ese medio de pago-moneda.
            TotalEntregadoMonedaReferencia          ->  Total entregado expresado en la moneda de
            referencia.
            Cambio                                  ->  Cambio de la línea de pago (su valor puede ser 0.00
                                                             (no hay cambio) o positvo que es parte del cambio
                                                             que se le da al cliente).
            TipoOperacion                           ->  0-Si corresponde a una venta (los importes van en
            positivo).
                                                        1-Si corresponde a una devolución por parte del cliente
                                                             (los importes van en negativo).
            LineaUltimoPago                         ->  0-No es la línea del último pago. Esto sucede cuando el
                                                             ticket se paga con múltiples pagos (inclusive de
                                                             distintos medios de pago-monedas) cuando el importe
                                                             abonado es menor al total a pagar.
                                                        1-Es la línea del último pago.
            CodigoCupon                             ->  Código de barras del cupón corporativo.
            AutorizaSupervisora                     ->  0-La línea de pago no tuvo autorización de la supervisora.
                                                        1-La línea de pago tuvo autorización de la supervisora.
            CodigoSupervisora                       ->  Código de la supervisora si AutorizaSupervisora=1,
                                                            sino va vacío.
            LineaCancelada                          ->  0-Línea de pago no cancelada.
                                                        1-Línea de pago cancelada.

            Ejemplo de un pago con cupón corporativo con código 989016000000101400 de 140.00
            pesos. No es la línea de último pago.

            L#12#67#155100#15#1#347.40#347.40#140.00#140.00#0.00#0#0#9890160000001014
            00#0##0
        """
        lin = self.esta_linea or False
        result = {}
        try:
            results = dict(codigomediopago                      = lin[0],
                           codigomoneda                         = lin[1],
                           totalmediopagomoneda                 = lin[2],
                           totalmediopagomonedamonedareferencia = lin[3],
                           totalpagado                          = lin[4],
                           totalpagadomonedareferencia          = lin[5],
                           cambio                               = lin[6],
                           tipooperacion                        = lin[7],
                           lineaultimopago                      = lin[8],
                           codigocupon                          = lin[9],
                           autorizasupervisora                  = lin[10],
                           codigosupervisora                    = lin[11],
                           lineacancelada                       = lin[12])
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_68(self):
        """
        Línea de entrega a domicilio (68).
        Representa la línea de entrega a domicilio (delivery) con los datos del cliente.

        (La usamos para obtener los datos [nombre y número de cuenta] de una cobranza de cta.cte.)

        IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea # Código # Nombre # Telefono # Direccion # Esquina1 # Esquina2 # Gratis # LineaCancelada
        Código->Código del cliente.
        Nombre->Nombre del cliente.
        Telefono->Telefono del cliente.
        Direccion->Direccion del cliente.
        Esquina1->Primera esquina donde se encuentra el cliente.
        Esquina2->Segunda esquina donde se encuentra el cliente.
        Gratis-> Según el monto de venta, se cobra el delivery o no y se indica de la siguiente forma:
        1-El delivery es gratis.
        0-El delivery se cobra.
        LineaCancelada->0-Línea no cancelada.
        1-Línea cancelada. Este tipo de línea no tiene valor contable.

        C#1#4#1294#131#20151218113128#F#0#15603.00#20#12
        L#1#5#113128#
        L#3#7#113128#131#SHIRLEY BRAVO
        L#4#53#113128#TICKET DE VENTA#0
        L#5#57#113128#20##0###
        L#6#47#113128#1#15602.83#1#0###0
        L#7#68#113143#4580#ROIG ELBIO##JUAN M.GUTIERREZ 1643 -21490###1#0
        L#8#4#113229#15602.83#0.00#0.00#0.00
        L#9#63#113229#15602.83#0.17#15603.00#1#1
        L#10#9#113229#1#1#15603.00#15603.00#15603.00#15603.00#0.00#0#1#0##0

        ticket = {
            ('C', '1', '4', '1294', '131', '20151218113128', 'F', '0', '15603.00', '20', '12') :
                ['L', '1', '5', '113128', ''],
                ['L', '3', '7', '113128', '131', 'SHIRLEY BRAVO'],
                ['L', '4', '53', '113128', 'TICKET DE VENTA', '0'],
                ['L', '5', '57', '113128', '20', '', '0', '', '', ''],
                ['L', '6', '47', '113128', '1', '15602.83', '1', '0', '', '', '0'],

           --> ['L', '7', '68', '113143', '4580', 'ROIG ELBIO', '', 'JUAN M.GUTIERREZ 1643 -21490', '', '', '1', '0'], <--

                ['L', '8', '4', '113229', '15602.83', '0.00', '0.00', '0.00'],
                ['L', '9', '63', '113229', '15602.83', '0.17', '15603.00', '1', '1'],
                ['L', '10', '9', '113229', '1', '1', '15603.00', '15603.00', '15603.00', '15603.00', '0.00', '0', '1', '0', '', '0']
            }

            Código # Nombre # Telefono # Direccion # Esquina1 # Esquina2 # Gratis # LineaCancelada
               0       1          2          3           4          5         6           7
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigocliente': lin[0],
                'nombrecliente': lin[1],
                'telefonocliente': lin[2],
                'direccioncliente': lin[3],
                'Esquina1': lin[4],
                'Esquina2': lin[5],
                'enviogratis': lin[6],
                'lineacancelada': lin[7]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_71(self):
        pass

    def _lt_72(self):
        pass

    def _lt_73(self):
        """
            Línea de ticket Z (73)
            Subtipos de líneas
            Contiene informacion de cabecera de la Z (por lo tanto solamente debe haber solo un sub tipo de
            línea 1 en la línea de informe Z).
            IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea #

            SubTipo # CodigoCaja # NumeroZ # TotalVenta # TotalPagoServicios # TotalVentaGeneral # GranTotal #
               0           1          2          3                 4                    5               6
            CantidadPagoCajas # ImportePagoCajas # ImporteRedondeo
                    7                   8                 9

            Subtipos de líneas
            1) Sub tipo línea Z. (obligatoria, es el cabezal del tipo de línea de detalle Z

                SubTipo             -> Sub tipo de línea que es 1.
                CodigoCaja          -> Codigo de la caja.
                NumeroZ             -> Número emitido de la Z en la caja.
                TotalVenta          -> Total de venta de la caja de mercaderia (incluye ivas pero no los pago de servicios).
                TotalPagoServicios  -> Total de pago de servicios.
                TotalVentaGeneral   -> Total de venta de la caja mas el total de venta de los pagos de servicios (TotalVenta + TotalPagoServicios).
                GranTotal           -> Gran total de la caja en el momento de la emision de la Z.
                CantidadPagoCajas   -> Cantidad de pagos de la caja.
                ImportePagoCajas    -> Importe de pagos de la caja.
                ImporteRedondeo     -> Importe (saldo) del redondeo acumulado en la sesion de la caja.

                Ejemplo de sub tipo de línea 1 de la caja 1, con numero de Z 954, con un total de venta de
                1696.80, un total de pago de servicios de 153.00 pesos, un total de venta general de 1849.80,
                un gran total de 20125014.50 pesos, se hicieron 2 pagos de caja por un monto de 750.00 pesos
                y el acumulado de redondeo es 2.00 pesos.

                    L#1#105#185528#1#1#954#1696.80#153.00#1849.80#20125014.50 # 2 # 750.00 # 2.00


            2) Sub tipo línea Iva.

                Representa el subtipo de línea de iva del informe Z.
                Pueden existir varias líneas de este subtipo, una por cada codigo de iva aplicado en la sesion de
                venta de la caja.

                    SubTipo # CodigoCaja # NumeroZ # CodigoIva # VentaBrutaIva # VentaNetaIva # VentaIva
                       0          1           2          3             4              5           6

                SubTipo         -> Sub tipo de línea que es 2.
                CodigoCaja      -> Codigo de la caja.
                NumeroZ         -> Número emitido de la Z en la caja.
                CodigoIva       -> Codigo de Iva.
                VentaBrutaIva   -> Es el total de la venta afectado por ese codigo de iva incluyendo al propio
                                    iva (VentaNetaIva + VentaIva).
                VentaNetaIva    -> Es el total de la venta afectado por ese codigo de iva sin incluir al propio
                                    iva (VentaBrutaIva – VentaIva).
                VentaIva        -> Importe solo de iva.

                Ejemplo de subtipo de línea 2 de la caja 1, con numero de Z 954 , para el codigo de iva 1, con un
                total de venta bruta de 1696.80 pesos, 1390.82 de venta neta de iva y 305.98 de venta de iva.
                    L#2#105#185528#2#1#954#1#1696.80#1390.82#305.98
                Idem para el codigo de iva 2.
                    L#3#105#185528#2#1#954#2#2568.90#2335.36#233.54

            3) Sub tipo línea medios de pago-monedas.

                Representa el subtipo de línea de los totales de los medios de pago-monedas (para la venta, para
                el fondo de caja y retiro) del informe Z. Pueden existir varias líneas de este subtipo, una por
                cada medio de pago-moneda en la sesion de venta de la caja.

                SubTipo # CodigoCaja # NumeroZ # CodigoMedioPago # CodigoMoneda # ImporteVenta # ImporteFondo
                    0          1          2           3               4               5               6
                ImporteRetiro
                      7

                SubTipo             -> Sub tipo de línea que es 3.
                CodigoCaja          -> Codigo de la caja.
                NumeroZ             -> Número emitido de la Z en la caja.
                CodigoMedioPago     -> Código del medio de pago.
                CodigoMoneda        -> Código de la moneda
                ImporteVenta        -> Importe de la venta del medio de pago-moneda.
                ImporteFondo        -> Importe de fondeo para ese medio de pago-moneda.
                ImporteRetiro       -> Importe de retiro para ese medio de pago-moneda.

                Ejemplo del subtipo 3, de la caja 1 para el número de Z 954, del medio de pago 1 y moneda 1,
                con un total acumulado de 1249.80 en ventas, se hizo un fondeo de 98.00 y un retiro de 47.00.
                    L#5#105#185528#3#1#954#1#1#1249.80#98.00#47.00
                Igual que el anterior para el codigo medio de pago 1 moneda 2, que tiene un fondo solamente de
                12750.00.
                    L#4#105#185528#3#1#954#1#2#0.00#12750.00#0.00

            4) Sub tipo línea de pago de servicios.

                Representa el subtipo de línea de los pagos de servicio del informe Z.
                Pueden existir varias líneas de este subtipo, una por cada pago de servicio en la sesion de la caja.

                SubTipo # CodigoCaja # NumeroZ # CodigoPagoServicio # CantidadPagos # ImportePagoServicios
                   0           1          2               3                  4                  5

                SubTipo             -> Sub tipo de línea que es 4.
                CodigoCaja          -> Codigo de la caja.
                NumeroZ             -> Número emitido de la Z en la caja.
                CodigoPagoServicio  -> Código del pago de servicio.
                CantidadPagos       -> Cantidad de pagos de servicios

            dict_subtipoZ = dict(


            """
        lin = self.esta_linea or False
        result = {}
        try:
            if lin[0] == '1':
                result = dict(codigo = lin[0],
                              importe = lin[1],
                              moneda = lin[2],
                              modoingreso = lin[3],
                              codigosupervisora = lin[4],
                              codigovendedor = lin[5],
                              referencia = lin[6],
                              lineacancelada = lin[7], )
            elif lin[0] == '2':
                result = dict(subtipo = lin[0],
                              codigocaja = caja3dig(lin[1]),
                              numeroz = lin[2],
                              codigoiva = lin[3],
                              ventabrutaiva = lin[4],
                              ventanetaiva = lin[5],
                              ventaiva = lin[6], )
            elif lin[0] == '3':
                result = dict(subtipo = lin[0],
                              codigocaja = caja3dig(lin[1]),
                              numeroz = lin[2],
                              codigomediopago = lin[3],
                              codigomoneda = lin[4],
                              importeventa = lin[5],
                              importefondo = lin[6],
                              importeretiro = lin[7], )
            elif lin[0] == '4':
                result = dict(subtipo = lin[0],
                              codigocaja = caja3dig(lin[1]),
                              numeroz = lin[2],
                              codigopagoservicio = lin[3],
                              cantidadpagos = lin[4], )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        result.update(dict(tipo_linea = 'Z'))
        return result

    def _lt_76(self):
        # Línea de descuento producido por marcas (76)
        pass

    def _lt_77(self):
        # Línea de cabezal de marca (77)
        pass

    def _lt_78(self):
        # Línea de detalle de la marca (78)
        pass

    def _lt_79(self):
        """
        Línea pago Web (79)
            Representa una línea de pago Web.

          IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea # CodigoMedioPago # CodigoMoneda #
                    0               1               2           3                   4               5
          TotalMedioPagoMoneda # TotalMedioPagoMonedaMonedaReferencia # TotalPagado # TotalPagadoMonedaReferencia #
                    6                           7                            8                  9
          Cambio # TipoOperacion # LineaUltimoPago # AutorizaSupervisora # CodigoSupervisora # LineaCancelada #
             10         11              12                     13                   14              15
          NroTarjetaBandeja # BindTarjetaCredito
                 16                 17

            CodigoMedioPago -> Código del medio de pago.
            CodigoMoneda -> Código de la moneda.
            TotalMedioPagoMoneda -> Monto total de lo que se puede pagar con el medio de pago moneda.
            TotalMedioPagoMonedaMonedaReferencia  ->  Idem que el anterior pero expresado en
            la moneda de referencia.
            TotalPagado  ->  Total entregado de ese medio de pago-moneda.
            TotalPagadoMonedaReferencia  -> Total entregado expresado en la moneda de
            referencia.
            Cambio -> Cambio de la línea de pago (su valor puede ser 0.00 (no hay cambio) o
            positvo que es parte del cambio que se le da al cliente).
            TipoOperacion -> 0-Si corresponde a una venta (los importes van en positivo).
            1-Si corresponde a una devolución por parte del cliente (los importes
            van en negativo).
            LineaUltimoPago ->  0-No es la línea del último pago. Esto sucede cuando el ticket se
            paga con múltiples pagos (inclusive de distintos medios de pago-
            monedas) cuando el importe abonado es menor al total a pagar.
                            1-Es la línea del último pago.
            AutorizaSupervisora ->  0-La línea de pago no tuvo autorización de la supervisora.
                            1-La línea de pago tuvo autorización de la supervisora.
            CodigoSupervisora -> Código de la supervisora si AutorizaSupervisora=1, sino va vacío.
            LineaCancelada -> 0-Línea de pago no cancelada.
                            1-Línea de pago cancelada.
            NroTarjetaBandeja -> Numero de tarjeta de la bandeja.
            BindTarjetaCredito -> Bind de la tarjeta de credito utilizada.

            Ejemplo de línea de pago Web, medio de pago web (38) ,moneda pesos (1) en la cual se
            pagó la totalidad de 6005.23 ,no tuvo cambio (0.00), pertenece a una venta (0), es la
            linea del último pago (1), el numero de la tarjeta de bandeja es 1234567890 y el bind de
            la tarjeta utilizada es 553456

            L#12#79#202350#38#1#6005.23#6005.23#6005.23#6005.23#0.00#0#1#0##0#1234567890#553456


        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = dict(
                        identificadorlinea                   = lin[0],
                        numerodelinea                        = lin[1],
                        tipolinea                            = lin[2],
                        timestamplinea                       = lin[3],
                        codigomediopago                      = lin[4],
                        codigomoneda                         = lin[5],
                        totalmediopagomoneda                 = lin[6],
                        totalmediopagomonedamonedareferencia = lin[7],
                        totalpagado                          = lin[8],
                        totalpagadomonedareferencia          = lin[9],
                        cambio                               = lin[10],
                        tipooperacion                        = lin[11],
                        lineaultimopago                      = lin[12],
                        autorizasupervisora                  = lin[13],
                        codigosupervisora                    = lin[14],
                        lineacancelada                       = lin[15],
                        nrotarjetabandeja                    = lin[16],
                        bindtarjetacredito                   = lin[17]
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_81(self):
        # Línea de devolución de pago de servicio (81)
        """
        Línea de devolución de pago de servicio (81).
        Representa la línea de devolución de un pago de servicio.
        IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea #

        Código # Importe # Moneda # ModoIngreso # CodigoSupervisora # CodigoVendedor #
           0        1        2           3              4                   5
        Referencia # LineaCancelada
            6              7

        Código      ->  Código del pago de servicio
        Importe     ->  Importe de la devolución del pago de servicio (en negativo).
        Moneda      ->  Código de moneda.
        ModoIngreso ->  0-Teclado
                        1-Scanner.
                        2-Banda magnética.
        CodigoSupervisora   ->  Código de la supervisora si intervino, sino va vacío.
        CodigoVendedor      ->  Código de vendedor si la caja está configurado para utilizar
                                vendedor. Si no hay vendedor va vacío.
        Referencia          ->  Referencia del pago de servicio.
        LineaCancelada      ->  0-Línea de devolucion de pago de servicio no cancelada.
                                1-Línea de devolucion de pago de servicio cancelada.
                                No se deberia tomar en cuenta como valor contable.

        Ejemplo de la devolucion del servicio 513 por -250.00 de la moneda 1, ingresado por
        teclado (0) e intervino la supervisora 1, sin vendedor ni referencia y la línea no esta
        canclada (0).
        L#7#81#122220#513#-250.00#1#0#1###0
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigo': lin[0],
                'importe': lin[1],
                'moneda': lin[2],
                'modoingreso': lin[3],
                'codigosupervisora': lin[4],
                'codigovendedor': lin[5],
                'referencia': lin[6],
                'lineacancelada': lin[7],
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_82(self):
        # Línea de consulta de estado de cuenta de la cobranza (82).
        pass

    def _lt_83(self):
        """
            Línea de voucher de la cobranza (83).  cobranza de tarjeta de crédito
            Representa el vocucher de un pago/devolución de tarjeta de crédito.
            La mayoría de la información aquí presentada la retorna el autorizador y Jswitch
            (referirse al documento Especificaciones jSwitch.doc por posibles cambios).

            Descripcion # NumeroTarjeta # NumeroCuenta # Vencimiento # Autorizacion #
                 0              1               2             3             4
            TipoAutorizacion # CodigoMoneda # Importe # TipoVoucher # TipoCobranza #
                    5                6           7           8             9
            IndicadorPagoDev
                    10

            NumeroCuenta->Numero de cuenta del cliente (cuando la cobranza se hace offline, si es
            online puede venir vacio).
            *Datos que no provienen de la autorizadora.

            Ejemplo del voucher de cobranza VISA con numero de tarjeta 5898920239862737 sin
            numero de cuenta con vencimineto 0705 , autorizacion 000000 que se hizo online (00)
            con importe de 250.00 pesos (00), es la via del cliente (0) , se selecciono online (1) y
            es un pago (0).
            L#11#83#183404#VISA#5898920239862737##0705#000000#00#00#250.00#0#1#0

            Idem para el establecimiento (1):
            L#12#83#183404#VISA#5898920239862737##0705#000000#00#00#250.00#1#1#0

        """
        lin = self.esta_linea or False
        result = {}
        try:
            result = {
                'descripcion': lin[0],
                'numerotarjeta': lin[1],
                'numerocuenta': lin[2],
                'vencimiento': lin[3],
                'autorizacion': lin[4],
                'tipoautorizacion': lin[5],
                'codigomoneda': lin[6],
                'importe': lin[7],
                'tipovoucher': lin[8],
                'tipocobranza': lin[9],
                'indicadorpagodev': lin[10],
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_84(self):
        # Línea de apertura de gaveta.                           84
        """
            Línea de apertura de gaveta (84).
            Representa la línea de apertura de gaveta que hace la cajera de forma expresa con la
            tecla de función correspondiente (en este momento esta en el menú de cierre de caja).En
            si el dato relevante es el tipo de línea para contabilizar cuantas aperturas de gaveta hizo
            la cajera.
            Descripcion
            Descripcion->Contiene el texto “Apertura de gaveta manual”.
            Ejemplo de apertura de gaveta:
            L#6#84#143820#Apertura de gaveta manual
        """
        lin = self.esta_linea or False
        result = {}
        try:
            result = {
                'descripcion': lin[0],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_85(self):
        # Línea de pago de tarjeta offline (SM).                 85
        """
            Línea de pago de tarjeta offline (85) - SM.
            ===========================================

            Línea de ticket de cuando se paga con tarjeta de crédito pero de modo offline en SM.


             0 CodigoMedioPago                         ->  Código del medio de pago.

             1 CodigoMoneda                            ->  Código de la moneda.

             2 TotalMedioPagoMoneda                    ->  Monto total de lo que se puede pagar con
                                                                el medio de pago moneda.

             3 TotalMedioPagoMonedaMonedaReferencia    ->  Idem que el anterior pero expresado en la
                                                                moneda de referencia.

             4 TotalEntregado                          ->  Total entregado de ese medio de pago-moneda.

             5 TotalEntregadoMonedaReferencia          ->  Total entregado expresado en la moneda de referencia.

             6 Cambio                                  ->  Cambio de la línea de pago.
                                                                Su valor puede ser 0.00 (no hay cambio) o
                                                                positvo que es parte del cambio que se le da
                                                                al cliente.

             7 TipoOperacion                           ->  0-Si corresponde a una venta
                                                                los importes van en positivo.
                                                           1-Si corresponde a una devolución por parte del cliente
                                                                los importes van en negativo.

             8 LineaUltimoPago                         ->  0-No es la línea del último pago.
                                                                Esto sucede cuando el ticket se paga con
                                                                múltiples pagos, inclusive distintos medios de
                                                                pago-monedas, cuando el importe abonado es menor
                                                                al total a pagar.
                                                           1-Es la línea del último pago.

             9 NumeroTarjetaCredito                    ->  Número de la tarjeta de crédito. Se graba solamente si
                                                                es cliente de fidelización.

            10 AutorizaSupervisora                     ->  0-La línea de pago no tuvo autorización de la supervisora.
                                                           1-La línea de pago tuvo autorización de la supervisora.

            11 LineaCancelada                          ->  0-Línea de pago no cancelada.
                                                           1-Línea de pago cancelada.

            CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda # TotalMedioPagoMonedaMonedaReferencia #
                   0                1                 2                             3
            TotalPagado # TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
                  4                   5                    6            7               8
            NumeroTarjetaCredito # AutorizaSupervisora # CodigoSupervisora # LineaCancelada
                      9                     10                  11                 12
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'numerotarjetacredito': lin[9],
                'autorizasupervisora': lin[10],
                'codigosupervisora': lin[11],
                'lineacancelada': lin[12]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_86(self):
        # Línea de recargo. 86
        pass

    def _lt_87(self):

        """
            Línea descuento a los medios de pago-moneda (87)

            Representa a las líneas de Ticket para descuentos a los Medios de Pago Moneda.
            Esta condición se presenta en promociones al total de la venta por medio de pago-
            moneda y a la promoción de categorías por medio de pago moneda.

            CodigoMedioPago # CodigoMoneda # CodigoDescuento # ImporteTotalSinDesc #
                   0                1               2                  3
            ImporteDesc # LineaCancelada # TipoDescuento # PorcentajeDescuento #
                  4              5               6                 7
            CodigoPromocion
                   8

            CodigoMedioPago     ->     Código del medio de pago.
            CodigoMoneda        ->     Código de la moneda
            CodigoDescuento     ->     Código del descuento.
            ImporteTotalSinDesc ->     Total sin descuento.
                                       Si el TipoDescuento = 1 (ver TipoDescuento) este campo respresentará
                                       el suma del importe de articulos de la categoria, sin el descuento aplicado.
            ImporteDesc         ->     Importe del descuento (su valor es en negativo).
            LineaCancelada      ->     0-Línea no cancelada.
                                       1-Línea cancelada. Este tipo de línea no tiene valor contable.
            TipoDescuento       ->     1-Descuento por categoria.
                                       2-Descuento al total.
            PorcentajeDescuento ->     Porcentaje del descuento aplicado en formato importe con valor
                                       negativo. Por ejemplo, si se aplicó un descuento de 5 % aparecerá -0.05
            CodigoPromocion     ->     Código de la promoción que disparo el descuento al medio de
                                       pago-moneda, ya sea al total o categorizado.
        """
        lin = self.esta_linea or False
        result = {}
        try:
            result = dict(
                codigomediopago      = lin[0],
                codigomoneda         = lin[1],
                codigodescuento      = lin[2],
                importetotalsindesc  = lin[3],
                importedesc          = lin[4],
                lineacancelada       = lin[5],
                tipodescuento        = lin[6],
                porcentajedescuento  = lin[7],
                codigopromocion      = lin[8],
                cambio               = 0,               # se incorpora cambio y totalpagadomonedareferencia dado qué
                totalpagadomonedareferencia = lin[4]    # en el erp esto se tratará igual que un medio de pago.
            )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result
        pass

    def _lt_88(self):
        # Línea venta cómputos celular                           88
        pass

    def _lt_89(self):
        # Devolución línea venta cómputos celular.               89
        pass

    def _lt_90(self):
        """
        Línea de pago ticket TAlimentos (90) SM.
        ---------------------------------------

         0 Código del medio de pago.
         1 Código de la moneda.
         2 Monto total de lo que se puede pagar con el medio de pago moneda.
         3 Idem que el anterior pero expresado en la moneda de referencia.
         4 Total entregado de ese medio de pago-moneda.
         5 Total entregado expresado en la moneda de referencia.
         6 Cambio de la línea de pago (valor >= 0.00 5).
         7 TipoOperacion.
             0 - Venta ( importes > 0.00).
             1 - Devolución ( importes < 0.00).
         8 LineaUltimoPago.
             0 - No es la línea del último pago. Esto sucede cuando el ticket
                 se paga con múltiples pagos (inclusive de distintos medios de
                 pago-monedas) cuando el importe abonado es menor al total a pagar.
             1 - Es la línea del último pago.
         9 CodigoBarra.
             1 - código de barras del cupón.
             0 - monto total de los cupones o el codigo de barras ingresado
                 manualmente de ese cupon.
        10 ModoIngresoCupon.
             0 - Teclado.Este modo de ingreso se efectua cuando la cajera
                 ingresa el monto del total de los cupones o el codigo de
                 barras de ese cupon.
             1 - Scanner.Cuando se procesan los cupones por scanner, validando
                 los mismos.
        11 AutorizaSupervisora.
             0 - La línea de pago no tuvo autorización de la supervisora.
             1 - La línea de pago tuvo autorización de la supervisora.
        12 CodigoSupervisora.
        13 Código de la supervisora (vacío si no aplica)
        14 LineaCancelada.
             0 - activa.
             1 - cancelada.


        Indices:
        -------

        CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
             0                  1                 2

        TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                        2                           4

        TotalPagadoMonedaReferencia # Cambio # TipoOperacion #
                    5                   6           7

        LineaUltimoPago# CodigoBarra # ModoIngresoCupon # AutorizaSupervisora #
                8           9               10                  11

        CodigoSupervisora # LineaCancelada
            12                  13
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {

                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'codigobarra': lin[9],
                'modoingresocupon': lin[10],
                'autorizasupervisora': lin[11],
                'codigosupervisora': lin[12],
                'lineacancelada': lin[13]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_91(self):
        """
        Línea de pago ticket Total (91) SM.
        ----------------------------------

         0 Código del medio de pago.
         1 Código de la moneda.
         2 Monto total de lo que se puede pagar con el medio de pago moneda.
         3 Idem que el anterior pero expresado en la moneda de referencia.
         4 Total entregado de ese medio de pago-moneda.
         5 Total entregado expresado en la moneda de referencia.
         6 Cambio de la línea de pago (valor >= 0.00 5).
         7 TipoOperacion.
             0 - Venta ( importes > 0.00).
             1 - Devolución ( importes < 0.00).
         8 LineaUltimoPago.
             0 - No es la línea del último pago. Esto sucede cuando el ticket
                 se paga con múltiples pagos (inclusive de distintos medios de
                 pago-monedas) cuando el importe abonado es menor al total a pagar.
             1 - Es la línea del último pago.
         9 CodigoBarra.
             1 - código de barras del cupón.
             0 - monto total de los cupones o el codigo de barras ingresado
                 manualmente de ese cupon.
        10 ModoIngresoCupon.
             0 - Teclado.Este modo de ingreso se efectua cuando la cajera
                 ingresa el monto del total de los cupones o el codigo de
                 barras de ese cupon.
             1 - Scanner.Cuando se procesan los cupones por scanner, validando
                 los mismos.
        11 AutorizaSupervisora.
             0 - La línea de pago no tuvo autorización de la supervisora.
             1 - La línea de pago tuvo autorización de la supervisora.
        12 CodigoSupervisora.
        13 Código de la supervisora (vacío si no aplica)
        14 LineaCancelada.
             0 - activa.
             1 - cancelada.


        Indices:
        -------

        CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
             0                  1                 2

        TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                        2                           4

        TotalPagadoMonedaReferencia # Cambio # TipoOperacion #
                    5                   6           7

        LineaUltimoPago# CodigoBarra # ModoIngresoCupon # AutorizaSupervisora #
                8           9               10                  11

        CodigoSupervisora # LineaCancelada
            12                  13
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'codigobarra': lin[9],
                'modoingresocupon': lin[10],
                'autorizasupervisora': lin[11],
                'codigosupervisora': lin[12],
                'lineacancelada': lin[13]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_92(self):
        # Línea de Factura 2.                                    92
        pass

    def _lt_94(self):
        # Línea de M.pago con cheque cobranza.                     94
        """

            Línea de pago con cheque cobranza (94).
        Línea de ticket cuando se paga con cheque pero para la cobranza (pago de servicios).
        IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea #

        CodigoMedioPago  # CodigoMoneda  # TotalMedioPagoMoneda  # TotalMedioPagoMonedaMonedaReferencia
               0                1                   2                           3
        TotalPagado  # TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago
             4                      5                   6           7               8
        TipoCliente # IdCliente # AutorizaSupervisora # CodigoSupervisora # LineaCancelada
            9            10             11                      12              13

        CodigoMedioPago                        ->  Código del medio de pago.
        CodigoMoneda                           ->  Código de la moneda.
        TotalMedioPagoMoneda                   ->  Monto total de lo que se puede pagar con el medio de pago
                                                    moneda.
        TotalMedioPagoMonedaMonedaReferencia   ->  Idem que el anterior pero expresado en la moneda de referencia.
        TotalEntregado                         ->  Total entregado de ese medio de pago-moneda.
        TotalEntregadoMonedaReferencia         ->  Total entregado expresado en la moneda de
        referencia.
        Cambio                                 ->  Cambio de la línea de pago. Su valor puede ser 0.00 o positvo
                                                     y es parte del cambio que se le da al cliente.
        TipoOperacion                          ->  0-Si corresponde a una venta (los importes van en positivo).
                                                   1-Si corresponde a una devolución por parte del cliente
                                                     los importes van en negativo.
        LineaUltimoPago                        ->  0-No es la línea del último pago.
                                                     Esto sucede cuando el ticket se paga con múltiples pagos,
                                                     inclusive de distintos medios de pago-monedas, cuando el
                                                     importe abonado es menor al total a pagar.
                                                   1-Es la línea del último pago.
        TipoCliente                            ->  Tipo de cliente
        IdCliente                              ->  Identificación cliente.
        AutorizaSupervisora                    ->  0-La línea de pago no tuvo autorización de la supervisora.
                                                   1-La línea de pago tuvo autorización de la supervisora.
        CodigoSupervisora                      ->  Código de la supervisora si AutorizaSupervisora=1, sino vacío.
        LineaCancelada                         ->  0-Línea de pago no cancelada. 1-Línea de pago cancelada.

        Ejemplos:
        Pago con cheque cobranza pesos (medio de pago 6, moneda 1) por un importe de 250.00 pesos,
        para el tipo de cliente general (20) (por lo tanto no lleva id de cliente).
        L#8#94#174421#6#1#250.00#250.00#250.00#250.00#0.00#0#1#20##0##0

        Idem que el anterior, por un monto de 400.00 pesos, para el tipo de cliente 0 cuyo
        id es 9990003046413.
        L#8#94#174544#6#1#400.00#400.00#400.00#400.00#0.00#0#1#0#9990003046413#0##0  """
        lin = self.esta_linea or False

        result = {}
        try:
            result = dict(
                    codigomediopago                      = lin[0],
                    codigomoneda                         = lin[1],
                    totalmediopagomoneda                 = lin[2],
                    totalmediopagomonedamonedareferencia = lin[3],
                    totalpagado                          = lin[4],
                    totalpagadomonedareferencia          = lin[5],
                    cambio                               = lin[6],
                    tipooperacion                        = lin[7],
                    lineaultimopago                      = lin[8],
                    tipocliente                          = lin[9],
                    idcliente                            = lin[10],
                    autorizasupervisora                  = lin[11],
                    codigosupervisora                    = lin[12],
                    lineacancelada                       = lin[13]
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_95(self):
        # Línea de ticket de fondeo.                             95
        pass

    def _lt_97(self):
        # Línea de ticket de retiro                              97

        """
            Línea de ticket de retiro (97).

            Este tipo de línea se presenta cuando la cajera realiza un retiro de caja.

                CodigoMedioPago # CodigoMoneda # MontoRetiro
                       0               1             2

                0. CodigoMedioPago ->  Código del medio de pago.
                1. CodigoMoneda    ->  Código de la moneda.
                2. MontoRetiro     ->  Monto del retiro realizado.

            Ejemplo de un retiro del codigo de medio de pago 1 y codigo de moneda 1 por 300.00 ,
            del codigo de medio de pago 1 y codigo de moneda 2 por 500.00 y del codigo de medio
            de pago 1 y codigo de moneda 4 por 300.00

                L#8#97#201128#1#1#300.00
                L#9#97#201128#1#2#500.00
                L#10#97#201128#1#4#300.00
        """

        lin = self.esta_linea or False

        result = dict()
        try:
            result.update(dict(codigomediopago = lin[0], codigomoneda = lin[1], montoretiro = lin[2]))
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_98(self):
        # no existe
        pass


    def _lt_99(self):
        # Línea de ticket Cupones Numeros (SM)                   99
        pass

    def _lt_100(self):
        # Línea de ticket de cobranza (SM).               100
        """
            Línea de ticket de cobranza (100)-SM / (119)-P4
            Especificacion de la línea de cobranza.
            Los campos con * son retornados por el autorizador de la tarjeta.

            # Codigo # Importe # Moneda # ModoIngreso # Tipo # CodigoVendedor # NumeroTarjeta
                 0        1         2         3           4         5               6
            # NumeroContrato *  # FormaPagoContrato *  # ProductoContrato *  # NumeroOperacion *
                   7                    8                       9                   10
            # CantPagosRealizados *  # NumeroCuenta # FechaVencimiento # NumeroAutorizacion *
                    11                      12              13                  14
            # TipoAutorizacion *  # LineaCancelada # FlagSantander # CardType
                    15                      16              17          18
            Código         ->    Código del pago de servicio (cobranza).
            Importe        ->    Importe de la cobranza.
            Moneda         ->    Código de moneda.
            ModoIngreso    ->     0-Teclado
                                  1-Scanner.
                                  2-Banda magnética.
            Tipo            ->    0-Offline.
                                  1-Online.

            CodigoVendedor  ->    Código de vendedor si la caja está configurado para utilizar vendedor.
                                  Si no hay vendedor va campo vacío.
            NumeroTarjeta         ->    Número de la tarjeta de credito.
            NumeroContrato *      ->     Número del contrato de la tarjeta.
            FormaPagoContrato *   ->    Forma de pago del contrato.
            ProductoContrato *    ->    Producto/subproducto del contrato.
            NumeroOperacion *     ->    Número de operación realizada.
            CantPagosRealizados * ->    Cantidad de pagos realizado de la tarjeta.
            NumeroCuenta          ->    Numero de cuenta de la tarjeta.
            FechaVencimiento      ->    Fecha de vencimiento de la tarjeta (aamm).
            NumeroAutorizacion*   ->    Numero de autorizacion.
            TipoAutorizacion*     ->    01- Offline
                                        00-Online.
            LineaCancelada        ->    0-Línea de cobranza no cancelada.
                                        1-Línea de cobranza cancelada.No tiene valor contable.
            FlagSantander         ->    Se utiliza para las cobranzas Visa-Master offline de Santander para
                                        diferenciar si es una cobranza de Santander o ex ABN.
                                        Los posibles valores son:
                                        X - Es el valor que viene por defecto, indicando que no es
                                            una cobranza Visa-Master offline de Santander.
                                        S - Santander.
                                        A - ex ABN.
            CardType*             ->    Card Type (identificador de la tarjeta) retornado por el autorizador.Si es
                                        offline viene vacio.

            Ejemplo de la cobranza 522 con importe de 300.00 de la moneda 1, que se ingreso por
            banda magnética (2) que se hizo online (1), sin vendedor, numero de tarjeta 002130744,
            numero de contrato 12345678901111122222, forma de pago de contrato 00, producto
            de contrato 11111111111, numero de operación 22222222222, cantidad de pagos
            realizados 11, sin numero de cuenta, fecha de vencimiento 9802, numero de
            autorizacion 123456, se hizo online (00) , no esta cancelada (0) y tiene un card type de 128.
            L#6#100#183430#522#300.00#1#2#1##002130744#12345678901111122222#00#11111111111#222222
            22222#11##9802#123456#00#0#X#128
            Ejemplo de una cobranza offline (0) con el numero de cuenta 0001986720 que es de
            Santander (S)
            L#6#100#204626#520#2318.67#1#1#0########0001986720####0#S#
            Idem para la cuenta 090137974408 que es ex ABN (A)
            L#6#100#211938#520#10527.38#1#0#0########090137974408####0#A#

        :return:
        """
        lin = self.esta_linea or False
        result = dict()
        try:
            result.update(dict(
                                codigo               = lin[0],
                                importe              = lin[1],
                                moneda               = lin[2],
                                modoingreso          = lin[3],
                                tipo                 = lin[4],
                                codigovendedor       = lin[5],
                                numerotarjeta        = lin[6],
                                numerocontrato       = lin[7],
                                formapagocontrato    = lin[8],
                                productocontrato     = lin[9],
                                numerooperacion      = lin[10],
                                cantpagosrealizados  = lin[11],
                                numerocuenta         = lin[12],
                                fechavencimiento     = lin[13],
                                numeroautorizacion   = lin[14],
                                tipoautorizacion     = lin[15],
                                lineacancelada       = lin[16],
                                flagsantander        = lin[17],
                                cardtype             = lin[18],
                                ))

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_101(self):
        # Línea de ticket de devolucion de cobranza (SM). 101
        """
            Línea de ticket de devolución de cobranza (101)-SM
            Especificacion de la línea de devolución de una cobranza para (SM).
            Es igual a la línea de cobranza (100)-SM solo que el importe es negativo y puede
            intervenir la supervisora.

        :return:
        """
        lin = self.esta_linea or False
        result = dict()
        try:
            result.update(dict(
                            codigo               = lin[0],
                            importe              = lin[1],
                            moneda               = lin[2],
                            modoingreso          = lin[3],
                            tipo                 = lin[4],
                            codigosupervisora    = lin[5],
                            codigovendedor       = lin[6],
                            numerotarjeta        = lin[7],
                            numerocontrato       = lin[8],
                            formapagocontrato    = lin[9],
                            productocontrato     = lin[10],
                            numerooperacion      = lin[11],
                            cantpagosrealizados  = lin[12],
                            numerocuenta         = lin[13],
                            fechavencimiento     = lin[14],
                            numeroautorizacion   = lin[15],
                            tipoautorizacion     = lin[16],
                            lineacancelada       = lin[17],
                            flagsantander        = lin[18],
                            cardtype             = lin[19]
                        ))

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_102(self):
        # Línea de ticket de cancelacion de cobranza(SM). 102
        """Línea de ticket cancelacion de cobranza (102)-SM / (121)-P4
            Representa la línea de cancelacion de la cobranza.
            No tiene valor contable.

            # Codigo #  LineaTicket
            Código      ->  Código del pago de servicio (cobranza).
            LineaTicket ->  Línea del ticket a la cual cancela.

        """
        lin = self.esta_linea
        result = dict()
        try:
            result.update(
                dict(codigo = lin[0], lineaticket = lin[1])
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_103(self):

        """
        Cancelación de salida de cajera (SM)            103
              # NombreCajera # NumeroSesion
                    0               1

              NombreCajera        ->  Nombre de la cajera.
              NumeroSesion        ->  Número de la sesión de la cajera.

              Ejemplo para la cancelación de salida de cajera para (103)
              L#6#103#140928#Cajera Do
        """
        lin = self.esta_linea
        result = dict()
        try:
            result.update(
                dict(nombrecajera = lin[0], numerosesion = lin[1])
                )
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_104(self):
        # Seteo de monto de prestamo en efectivo (SM).    104
        pass

    def _lt_105(self):
        # Prestamo en efectivo (SM).                      105
        pass

    def _lt_106(self):
        """ Ticket cliente facturacion (SM)                 106
            Representa los datos del cliente de facturación (al cual se factura).

            tipodocumento  codigopais  documento  nombre  direccion  ciudad  codigodepartamento  codigopostal  rut
                   0            1           2       3          4        5            6                 7        8

            TipoDocumento-> Corresponde al codigo de tipo de documento de la tabla
            TipoDocumentosCliente. 2-Rut, 3-CI, 4-OTR, 5-PSP, 6-DNI.

            CodigoPais  ->  Codigo de pais del cliente.
                                                        Corresponde al codigo de la tabla Paises.  UY
            Documento   ->  Documento del cliente.
            Nombre      ->  Nombre del cliente.
            Direccion   ->  Direccion del cliente.
            Ciudad      ->  Ciudad del cliente.
            CodigoDepartamento  ->  Codigo de departamento del cliente.
                                                        Corresponde al codigo de la tabla DepartamentosPais.  AR
            CodigoPostal    ->  Codigo postal del cliente (opcional, puede venir en cero).
            Rut             ->  Rut de la factura.

            Ejemplo del cliente de facturación con tipo de documento 2 (Rut), código de país UY
            (Uruguay) con documento 1234567 y nombre Juan Perez.
            Su dirección es Gaboto 1234, ciudad Montevideo, código de departamento 10
            (Montevideo),codigo postal 0 y Rut 123456789123

            L#8#106#203221#2#UY#1234567#Juan Perez#Gaboto 1234#Montevideo#10#0#123456789123

        :return:
        """
        lin = self.esta_linea or False
        result = {}
        try:
            result = dict(
                        tipodocumento = lin[0],
                        codigopais = lin[1],
                        documento = lin[2],
                        nombre = lin[3],
                        direccion = lin[4],
                        ciudad = lin[5],
                        codigodepartamento = lin[6],
                        codigopostal = lin[7],
                        rut = lin[8])

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result



    def _lt_107(self):
        # Ticket de informacion del cliente (SM)          107
        pass

    def _lt_108(self):
        # Ticket gift card (108)-SM                       108
        pass

    def _lt_109(self):
        # Devolución gift card (109)                      109
        pass

    def _lt_115(self):
        """
        Pago descuento Iva Afam (SM)                      115
        Esta línea sigue las mismas especificaciones que la línea de pago efectivo (9),
        cambiando el codigo del medio de pago al principio y el total pagado refleja el
        descuento de Iva.
        Ejemplo de un pago con tarjeta Afam (20) por un total de 377.11 y un descuento de Iva de 36.07.
        L#8#115#174844#20#1#377.11#377.11#36.07#36.07#0.00#0#0#0##0
        :return:
        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                # monto pagable en éste medio de pago expresado en la moneda usada.
                'totalmediopagomonedamonedareferencia': lin[3],
                # lo mismo pero expresado en mon.referencia (PESOS)
                'totalpagado': lin[4],  # Total recibido en la moneda usada.
                'totalpagadomonedareferencia': lin[5],  # lo mismo pero expresado en moneda de referencia (PESOS)
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'autorizasupervisora': lin[9],
                'codigosupervisora': lin[10],
                'lineacancelada': lin[11],
                }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result



    def _lt_117(self):
        # Preventa (SM)                                   117
        pass

    def _lt_118(self):

        """ Línea de ticket vale almuerzo                 118

            FlagTarjetaDocumento # TipoDocumento # NumeroDocumento # ModoIngreso #
            Track1 # Track2 # NumeroTarjeta # ModoValeAlmuerzo # AcumuladoDiasSemana

            FlagTarjetaDocumento    ->      Indicador si se trata de tarjeta o documento como dato
                                            identificatorio.
                    0-Tarjeta.
                    1-Documento
            TipoDocumento           ->     Tipo de documento si FlagTarjetaDocumento=1, sino va vacío.
                    C-Cédula de identidad.
                    O-Otro.
            NumeroDocumento         ->      Número de documento si FlagTarjetaDocumento=1, sino va vacío.
                                                El número de documento tiene concatenado el tipo de documento
                                                (primer carácter).
            ModoIngreso             ->      Modo de ingreso de la Tarjeta/Documento:
                    0-Teclado.
                    1-Scanner.
                    2-Lectora de banda magnética.
            Track1                  ->      Track 1 de la tarjeta si FlagTarjetaDocumento=0.Puede venir vacío.
            Track2                  ->      Track 2 de la tarjeta si FlagTarjetaDocumento=0.Puede venir vacío.
            NumeroTarjeta           ->      Numero de la tarjeta si FlagTarjetaDocumento=0.Puede venir vacío.
            ModoValeAlmuerzo        ->      D-Diario-El vale almuerzo se puede aplicar todos los dias de la
                                                semana (aplicando el descuento correspondiente por dia).
                    S-Semanal  El vale almuerzo se aplica en su totalidad una vez a la
                                    semana (aplicando el descuento acumulado una vez a la semana).
                                    Dicho descuento depende de AcumuladoDiasSemana.
            AcumuladoDiasSemana     ->       Acumulado de dias trabajados en la semana para aplicar el
                                            descuento si es semanal.

            Ejemplo de identificación de un vale almuerzo de tipo tarjeta (0) que se ingresó por la
            lectora de banda magnetica (2), el valor del track 2 es 1032240472=0000 ,el numero de
            tarjeta es 1032240472, el modo de vale almuerzo es semanal (S) y lo acumulado de dias
            a la semana de trabajo es 6.
            L#6#118#180726#0###2##1032240472=0000#1032240472#S#6

            Ejemplo de identificación de un vale almuerzo de tipo documento (1) con tipo de
            documento Otro (O), numero de documento O12345678 (el documento real seria
            12345678 ya que el primer carácter tambien identifica el tipo de documento) y se
            ingresó por teclado (0).
            L#6#118#170035#1#O#O12345678#0###
            """
        lin = self.esta_linea or False
        result = {}
        try:
            result = {
                'flagtarjetadocumento': lin[0],
                'tipodocumento':        lin[1],
                'numerodocumento':      lin[2] if lin[0] == '0' else lin[2][1:],
                'modoingreso':          lin[3],
                'track1':               lin[4],
                'track2':               lin[5],
                'numerotarjeta':        lin[6],
                'modovalealmuerzo':     lin[7],
                'acumuladodiassemana':  lin[8],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_119(self):
        """

        Ticket vale almuerzo (119)
        --------------------------

        CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
               0                1                 2

        TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                    3                               4


        TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
                    5                    6          7                8

        AutorizaSupervisora # CodigoSupervisora # LineaCancelada
                 9                    10                11

        0. Código del medio de pago.
        1. Código de la moneda.
        2. Monto total de lo que se puede pagar con el medio de pago moneda.
        3. Idem que el anterior pero expresado en la moneda de referencia.
        4. Total entregado de ese medio de pago-moneda.
        5. Total entregado expresado en la moneda de referencia.
        6. Cambio de la línea de pago (valor >= 0.00)
        7. Codigo de Operacion.
                0 - Si corresponde a una venta (los importes van en positivo).
                1 - Si corresponde a una devolución por parte del cliente (los
                    importes van en negativo).
        8. Ultimo pago.
                0 - No es la línea del último pago. Esto sucede cuando el ticket
                    se paga con múltiples pagos (inclusive de distintos medios
                    de pago-monedas) cuando el importe abonado es menor al
                    total a pagar.
                1 - Es la línea del último pago.
        9. Intervención supervisor.
                0 - Línea de pago sin intervención de supervisor.
                1 - Línea de pago autorizada por supervidor.
        10. Código de la supervisora.
        11. Estado de la línea de pago.
             0-Línea de pago no cancelada.
             1-Línea de pago cancelada.
        """
        lin = self.esta_linea or False
        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                # monto pagable en éste medio de pago expresado en la moneda usada.
                'totalmediopagomonedamonedareferencia': lin[3],
                # lo mismo pero expresado en mon.referencia (PESOS)
                'totalpagado': lin[4],  # Total recibido en la moneda usada.
                'totalpagadomonedareferencia': lin[5],  # lo mismo pero expresado en moneda de referencia (PESOS)
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'autorizasupervisora': lin[9],
                'codigosupervisora': lin[10],
                'lineacancelada': lin[11],
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_120(self):
        """
            Línea de venta Mides (120)-SM
            -----------------------------

            Representa la línea identificadora de una venta en un voucher o tarjeta MIDES. (sin especificar)

            VentaMides  Texto que indica venta MIDES (Venta Mides).
            CI          Cédula de identidad del cliente. Este campo es opcional,puede no venir.

            VentaMides # CI
                0         1

            Ejemplo de una línea de venta Mides:
            L#6#120#144019#Venta Mides

            Ejemplo de una línea de venta Mides con CI 19068364:
            L#8#120#190241#Venta Mides#19068364
            [] los primeros 3 campos son comuneas al tickets (salvo en numero oridinal de línea) en ambos ejemplos
            y no están
        """
        # import ipdb; ipdb.set_trace()n
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'ventamides': lin[0],  # es texto y dice "Venta Mides"
                'ci': lin[1] if len(lin) > 1 else ''
            }
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result

    def _lt_121(self):
        """
            Línea de voucher retiro leche tarjeta Mides (121)-SM:
            ====================================================
            Representa la línea de retiro de productos (en este caso leche)
            sin costo (hasta cierto tope) de la tarjeta Mides.

            NumeroTarjeta # CedulaIdentidad # UnidadesRetiradas # SaldoUnidades # TipoVoucher # Modo

            0. Numero de la tarjeta Mides.
            1. Documento de identidad del cliente.
            2. Cantidad de unidades retiradas.
            3. Saldo de unidades que puede retirar sin costo.
            4. Tipo de voucher asociado.
                    0 - Original Cliente.
                    1 - Vía Establecimiento.
            5. Modo
                    0 - Retiro de productos.
                    1 - Devolución de productos.

            NumeroTarjeta # CedulaIdentidad # UnidadesRetiradas # SaldoUnidades #

            TipoVoucher # Modo

        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'numerotarjeta': lin[0],
                'cedulaidentidad': lin[1],
                'unidadesretiradas': lin[2],
                'saldounidades': lin[3],
                'tipovoucher': lin[4],
                'modo': lin[5],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_122(self):

        """
            Línea ticket info importe (122)-SM
            Contiene la información de importes gravados de los pagos con Tarjeta de Credto/Debito, Lucheon, etc.

            ImporteTotalTicket # ImporteGravadoTicket
                    0                      1
            ImporteTotalTicket   -> Importe total del ticket.
            ImporteGravadoTicket -> Importe gravado del ticket.

            Ejemplo de un importe con un total de ticket de 287.06 con un importe gravado de 235.30
                L|10|122|191720|287.06|235.30

        """

        lin = self.esta_linea or False
        result = {}
        try:
            result = {
                'importetotalticket': lin[0],
                'importegravadoticket': lin[1],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_123(self):
        pass

        """
        Línea de pago TACRE (123)-SM / (126) P4 (no CFE).
            Representa la línea de pago por Tarjeta Ticket Alimentacion/Canasta/Restaurante de forma electrónica.

              CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
                    0                1               2
              TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                             3                           4
              TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
                           5                   6           7               8
              NumeroTarjeta # NumeroAutorizacion # AutorizaSupervisora # CodigoSupervisora #
                  9                 10                     11                   12
              LineaCancelada # SiAplicaLeyDescIva # MontoDescuentoLeyIva # TextoLey
                  13                 14                   15                  16



             0. CodigoMedioPago                         ->  Código del medio de pago.

             1. CodigoMoneda                            ->  Código de la moneda.

             2. TotalMedioPagoMoneda                    ->  Monto total de lo que se puede pagar con el medio de pago
                                                            moneda.

             3. TotalMedioPagoMonedaMonedaReferencia    ->  Idem que el anterior pero expresado en
                                                            la moneda de referencia.

             4. TotalPagado                             ->  Total entregado de ese medio de pago-moneda.

             5. TotalPagadoMonedaReferencia             ->  Total entregado expresado en la moneda de
                                                            referencia.

             6. Cambio                                  ->  Cambio de la línea de pago (su valor puede ser 0.00 (no hay cambio) o
                                                            positvo que es parte del cambio que se le da al cliente).

             7. TipoOperacion                           ->  0 - Si corresponde a una venta (los importes van en positivo).
                                                            1 - Si corresponde a una devolución por parte del cliente (los importes
                                                                van en negativo).

             8. LineaUltimoPago                         ->  0 - No es la línea del último pago. Esto sucede cuando el ticket se
                                                                paga con múltiples pagos (inclusive de distintos medios de pago-
                                                                monedas) cuando el importe abonado es menor al total a pagar.
                                                            1 - Es la línea del último pago.

             9. NumeroTarjeta                           ->  Número de la tarjeta de crédito enmascarada (excepto grupo Disco).

            10. NumeroAutorizacion                      ->  Número de autorización.

            11. AutorizaSupervisora                     ->  0 - La línea de pago no tuvo autorización de la supervisora.
                                                            1 - La línea de pago tuvo autorización de la supervisora.

            12. CodigoSupervisora                       ->  Código de la supervisora si AutorizaSupervisora=1, sino va vacío.

            13. LineaCancelada                          ->  0 - Línea no cancelada.
                                                            1 - Línea cancelada. Este tipo de línea no tiene valor contable.

            14. SiAplicaLeyDescIva                      ->  Flag que indica si se aplica la ley 19210 de inclusión financiera
                                                            de descuento de iva.
                                                            0 - No aplica ley de descuento de iva.
                                                            1 - Aplica ley de descuento de iva.

            15. MontoDescuentoLeyIva                    ->  Monto del descuento de Iva.

            16. TextoLey                                ->  Texto de la ley (numero).


            CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
                    0             1                    2
            TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                            3                           4
            TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
                        5                 6            7                8
            NumeroTarjeta # NumeroAutorizacion # AutorizaSupervisora #
                9                 10                   11
            CodigoSupervisora # LineaCancelada # SiAplicaLeyDescIva #
                12                13                   14
            MontoDescuentoLeyIva # TextoLey
                    15               16
        """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'numerotarjeta': lin[9],
                'numeroautorizacion': lin[10],
                'autorizasupervisora': lin[11],
                'codigosupervisora': lin[12],
                'lineacancelada': lin[13],
                'siaplicaleydesciva': lin[14],
                'montodescuentoleyiva': lin[15],
                'textoley': lin[16],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_124(self):

        """
            Línea de voucher de la tarjeta TACRE (124)-SM
            =============================================

            Muestran la información de un Voucher de pago por Tarjeta Ticket
            Alimentacion/Canasta/Restaurante de forma electronica.

             0. NumeroTarjeta    -> Número de la tarjeta.
             1. Vencimiento      -> Vencimiento de la tarjeta (aamm).
             2. Comprobante      -> Número de comprobante.
             3. Autorizacion     -> Número de autorización.
             4. CodigoTerminal   -> Código de la terminal asociado.
             5. CodigoComercio   -> Código de comercio asociado.
             6. TipoAutorizacion ->
                    00-Online.
                    01-Offline
                    20-Online y aplica ley descuento IVA (ley 19210).
                    21-Online, aplica ley descuento IVA (ley 19210) y no requiere firma.

             7. NroLote          -> Número de lote asociado.
             8. CodigoMoneda     -> Código de la moneda asociado.
                    00-Pesos
                    01-Dólares.

             9. TipoTransaccion  -> Tipo de transacción asociado (MTI).
                    1200-Compra
                    1220-Confirmación Compra
                    1240-Notificación de Compra
                    1400-Devolución (Total o parcial)
                    1420-Confirmación Devolución
                    1440-Notificación de Devolución
                    1900-VentaTACRE
                    1901-Devolución TACRE
                    1902-Anulación TACRE
                    4900-Reversa venta TACRE
                    4901-Reversa devolución TACRE
                    4902-Reversa anulación TACRE
                    9xxx-Entrenamiento

            10. TipoVoucher         -> Tipo de voucher asociado.
                    0-Original Cliente.
                    1-Vía Establecimiento.

            11. ImportePago         -> Importe pagado por la tarjeta.
            12. FechaTransaccion   -> Fecha de transacción de la autorización (dd/mm/aaaa hh:mm:ss).
            13. CodigoCaja          -> Código de la caja.
            14. CodigoCajera        -> Código de la cajera.
            15. NombrePropietario   -> Nombre del propietario de la tarjeta.
            16. TipoIngreso         -> Tipo de ingreso asociado.
                    0-Lectura magnética.
                    1-Entrada manual
                    2-Internet.

            17. DescuentaIva        ->
                    0-No descuenta iva (ley 17934).
                    1-Descuenta iva (ley 17934).

            18. SiAplicaLeyDescIva  -> Flag que indica si se aplica la ley 19210 de inclusión financiera
                de descuento de iva.
                    0-No aplica ley de descuento de iva.
                    1-Aplica ley de descuento de iva

            19. MontoDescuentoLeyIva    -> Monto del descuento de Iva.
            20. MontoFactura            -> Monto de la factura.
            21. MontoGravado            -> Monto gravado.
            22. NombreTarjeta           -> Nombre de la tarjeta.
            23. FlagImprimeFirma        ->
                    0-No imprime la firma.
                    1-Imprime la firma.

            Ejemplo de un voucher de la tarjeta TACRE numero 6007940999999318,con
            vencimiento de tarjeta 0116 (01/16),número de comprobante 1004002818,número de
            autorización 000001,código de terminal 00000004, código de comercio asociado
            42140140042, tipo de autorización 20,número de lote 1, moneda 00 (pesos), tipo de
            transacción 1900, tipo voucher 0 (via cliente), importe de tarjeta de 287.06, fecha de
            autorización 05/06/2015 19:17:10, caja 4,cajera 1,propietario tarjeta es PRUEBAS
            REDBANK, tipo de ingreso de la tarjeta 0,descuenta Iva (1), aplica ley de descuento de
            Iva (1) , el importe de descuento es de -10.00,monto de factura 1024.40,monto gravado
            839.68,nombre tarjeta EDENRED y no imprime la firma.

            L|13|124|191720|6007940999999318|0107|1004002818|000001|00000004|42140140042|20|1|00|1900|0|287.06|05/06/2015 19:17:10|4|1|PRUEBAS REDBANK|0|1|1|-10.00|1024.40|839.68|EDENRED|0


                0               1             2             3               4
           NumeroTarjeta # Vencimiento # Comprobante # Autorizacion # CodigoTerminal #
                5                   6             7          8                9
           CodigoComercio # TipoAutorizacion # NroLote # CodigoMoneda # TipoTransaccion #
               10            11                 12             13           14
           TipoVoucher # ImportePago # FechaTransaccion # CodigoCaja # CodigoCajera #
                15                  16             17            18
           NombrePropietario # TipoIngreso # DescuentaIva # SiAplicaLeyDescIva #
                    19                 20                21          22               23
           MontoDescuentoLeyIva # MontoFactura # MontoGravado # NombreTarjeta # FlagImprimeFirma

        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'numerotarjeta': lin[0],
                'vencimiento': lin[1],
                'comprobante': lin[2],
                'autorizacion': lin[3],
                'codigoterminal': lin[4],
                'codigocomercio': lin[5],
                'tipoautorizacion': lin[6],
                'nrolote': lin[7],
                'codigomoneda': lin[8],
                'tipotransaccion': lin[9],
                'tipovoucher': lin[10],
                'importepago': lin[11],
                'fechatransaccion': lin[12],
                'codigocaja': caja3dig(lin[13]),
                'codigocajera': lin[14],
                'nombrepropietario': lin[15],
                'tipoingreso': lin[16],
                'descuentaiva': lin[17],
                'siaplicaleydesciva': lin[18],
                'montodescuentoleyiva': lin[19],
                'montofactura': lin[20],
                'montogravado': lin[21],
                'nombretarjeta': lin[22],
                'flagimprimefirma': lin[23]
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_125(self):
        pass

    def _lt_126(self):
        """

          Línea de ticket de cliente de cuenta corriente (126)-SM.
          -------------------------------------------------------

            Especificacion de la línea de ticket de cliente de cuenta corriente (clientes especiales).

            0. CodigoCC     Código de cliente de cuenta corriente.
            1. NombreCC     Nombre del cliente de cuenta corriente.
            2. MontoPagoCC  Es el monto de pago del cliente de cuenta corriente
                            No necesariamente es igual al monto total del ticket,
                            cuando se usa medio de pago.

             CodigoCC # NombreCC # MontoPagoCC
                 0         1           2
       y moneda pesos.

          Línea de pago de ticket en efectivo (9).
          ---------------------------------------


            0. Código del medio de pago.
            1. Código de la moneda.
       """

        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigocc': lin[0],
                'nombrecc': lin[1],
                'montopagocc': lin[2],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_127(self):
        """
          Línea de pago cuenta corriente (127)-SM   Medio de pago Venta o devolución
          ---------------------------------------------------

            Especificacion de la línea de ticket del pago de clientes de
            cuenta corriente. Es igual a la línea de pago en efectivo (9),
            solo que se refiere al codigo de medio de pago cuenta corriente
            y moneda pesos.

          Línea de pago de ticket en efectivo (9).
          ---------------------------------------


            0. Código del medio de pago.
            1. Código de la moneda.
            2. Monto total de lo que se puede pagar con el medio de pago moneda.
            3. Idem que el anterior pero expresado en la moneda de referencia.
            4. Total entregado de ese medio de pago-moneda.
            5. Total entregado expresado en la moneda de referencia.
            6. Cambio de la línea de pago (valor >= 0.00)
            7. Codigo de Operacion.
                    0 - Si corresponde a una venta (los importes van en positivo).
                    1 - Si corresponde a una devolución por parte del cliente (los
                        importes van en negativo).
            8. Ultimo pago.
                    0 - No es la línea del último pago. Esto sucede cuando el ticket
                        se paga con múltiples pagos (inclusive de distintos medios
                        de pago-monedas) cuando el importe abonado es menor al
                        total a pagar.
                    1 - Es la línea del último pago.
            9. Intervención supervisor.
                    0 - Línea de pago sin intervención de supervisor.
                    1 - Línea de pago autorizada por supervidor.
            10. Código de la supervisora. o vacio
            11. Estado de la línea de pago.
                    0-Línea de pago no cancelada.
                    1-Línea de pago cancelada.

            CodigoMedioPago # CodigoMoneda # TotalMedioPagoMoneda #
                0                1                 2

            TotalMedioPagoMonedaMonedaReferencia # TotalPagado #
                        3                               4


            TotalPagadoMonedaReferencia # Cambio # TipoOperacion # LineaUltimoPago #
                        5                    6          7                8

            AutorizaSupervisora # CodigoSupervisora # LineaCancelada
                    9                    10                11

        """
        lin = self.esta_linea or False

        result = {}
        try:
            result = {
                'codigomediopago': lin[0],
                'codigomoneda': lin[1],
                'totalmediopagomoneda': lin[2],
                'totalmediopagomonedamonedareferencia': lin[3],
                'totalpagado': lin[4],
                'totalpagadomonedareferencia': lin[5],
                'cambio': lin[6],
                'tipooperacion': lin[7],
                'lineaultimopago': lin[8],
                'autorizasupervisora': lin[9],
                'codigosupervisora': lin[10],
                'lineacancelada': lin[11],
            }

        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)

        return result

    def _lt_128(self):
        # es idéntica que la 9
        pass

    def _lt_900(self):
        """
            Línea de declaración de cajera (900)
            Esta línea se da posteriormente a la línea de salida de cajera (22) siempre y cuando la
            cajera haya realizado la declaración de los valores cuando cierra su sesión.

            IdentificadorLinea # NumeroDeLinea # TipoLinea # TimestampLinea #

            CodigoCaja # CodigoCajera # NombreCajera # CodigoMedioDePago # CodigoMoneda # MontoDeclaracion # DiferenciaDeclaracion # TimeStampDeclaracion

            CodigoCaja ->Codigo de caja donde se hace la declaracion.
            CodigoCajera->Codigo de cajera quien hace la declaracion.
            NombreCajera ->Nombre de la cajera.
            CodigoMedioDePago->Codigo del medio de pago de la declaracion.
            CodigoMoneda ->Codigo de la moneda de la declaracion.
            MontoDeclaracion -> Importe de la declaracion para ese medio de pago-moneda.
            DiferenciaDeclaracion -> Diferencia encontrada entre lo declarado y lo acumulado por
            la caja en la sesion de la cajera para ese medio de pago-moneda.
            TimeStampDeclaracion-> Fecha y hora de cuando se hizo la declaracion (aaaammddhhMMss)
        """
        lin = self.esta_linea or False
        result = {}
        try:
            result = dict(
                codigocaja              = caja3dig(lin[0]),
                codigocajera            = lin[1],
                nombrecajera            = lin[2],
                codigomediopago         = lin[3],
                descrip_medio_pago      = "Declaración Cajera",
                codigomoneda            = lin[4],
                montodeclaracion        = lin[5],
                diferenciadeclaracion   = lin[6],
                timestampdeclaracion    = lin[7])
        except Exception as ex:
            msg = "[ERROR]: %s %s %s" % (ex, self.llave, self.descripcion)
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, self.tck_id)
        return result
# --- fin clase `IPLinea`


class IPTicket(object):

    def __init__(self, tupla_cabezal, lista_de_tuplas_lineas):
        """
        Los parámetros son los datos extraidos de salidapazosbuevo-1- CSV -> tuplas
        :param tupla_cabezal: tuple:    todos los datos para el cabezal de UN ticket
        :param lista_de_tuplas_lineas: list: todos los datos de cada línea de detalle UN ticket

        :return:
           # TipoLinea    # CodigoCaja        # NumeroTicket  #  CodigoCajera  #  TimestampTicket
           # EstadoTicket # CantidadArticulos # TotalaPagar   # TipoCliente    #   CantidadLineas

        """

        if not tupla_cabezal or not len(tupla_cabezal):
            print "así no!\n\t por lo menos dame un cabezal ¿no?"
            sys.exit(0)
        try:
            self.cabezal = IPCabezal(tupla_cabezal)
            lineas = dict()
            tu = 'C' + '#'.join(tupla_cabezal)
            if verbose: print("voy!\n\t%s" % (tu,))
            for lin in lista_de_tuplas_lineas:
                linea = IPLinea(lin, self.cabezal.id_ticket)
                lineas.update({linea.id_linea: linea})
                if verbose:
                    li = 'L#' + '#'.join(lin)
                    print("\t%s" % (li,))
            if verbose:
                print("\tTicket %s %s %s" % (self.cabezal.llave, self.cabezal.descripcion, tu))

            self.lineas = lineas

            # if 'L#' + '#'.join(lin) == 'L#1#5#090259#101#e-Ticket#B#0306142#0####':
            # import ipdb;ipdb.set_trace()
        except Exception as ex:
            tipo_lin = tupla_cabezal[0]
            npos = tupla_cabezal[1]
            nticket = tupla_cabezal[2]
            tst = tupla_cabezal[4]
            tck_id = tst + '.' + npos + '.' + nticket
            msg = "[ERROR]: %s %s %s %s %s %s" % (ex, '__init__ de IPTicket', tipo_lin,  npos, nticket, tst)
            logging.info("%s" % (msg,))  # TODO:
            frame = getframeinfo(currentframe()) if verbose else False
            excepcion(msg, frame, tck_id)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: