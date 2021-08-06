#!/usr/bin/env python
# -*- coding: utf-8 -*-


CABEZAL = {
    '1': 'Ticket Venta/Ingreso',
    '2': 'Pedido',                                      # NO se procesa
    '3': 'Devolución',
    '4': 'Estado de cuenta',
    '5': 'Tck. Exento IVA',                             # NO se procesa
    '6': 'Canje',
    '7': 'Inventario',
    '8': 'Ticket de Cajera',
    '9': 'Gift',                                        # NO se procesa
    '10': 'Pago de caja',
    '11': 'Factura',
    '12': 'No generado (No existe en informe pazos)',   # NO se procesa
    '13': 'No generado (No existe en informe pazos)',   # NO se procesa
    '14': 'Consulta',                                   # NO se procesa
    '15': 'Apertura de Gaveta',                         # NO se procesa
    '16': 'N.Credito Devolucion',
    '17': 'Fondeo',                                     # NO se procesa
    '18': 'Retiro',                                     # NO se procesa
    '19': 'Prestamo efectivo',                          # NO se procesa
    '20': 'Retiro de Productos',                        # NO se procesa
    '21': 'Cab. Z de Caja',                             # NO se procesa
    '999': '-Cabezal DESCONOCIDO'
    }

LINEA = {
    '1': 'Venta de ítem',
    '4': 'Total del ticket',
    '5': 'Cabezal de CFE',
    '6': 'Pié de CFE',
    '7': 'Identificación de la cajera',
    '9': 'M.Pago de ticket en efectivo',
    '10': 'Cabezal de un combo',                       # NO se procesa
    '11': 'Detalle de combo',                          # NO se procesa
    '12': 'Cancelación de ítem',
    '13': 'Descuento a un ítem',                       # NO se procesa
    '15': 'Puntos generados de fidel. ítem',           # NO se procesa
    '16': 'Puntos totales de fidel. generados',        # NO se procesa
    '18': 'Regalo de artículos',                       # NO se procesa
    '19': 'Cupón',                                     # NO se procesa
    '20': 'Devolución de un ítem',
    '21': 'Entrada de cajera',                         # NO se procesa
    '22': 'Salida de cajera',                          # NO se procesa
    '23': 'Pausa de cajera',                           # NO se procesa
    '24': 'Cancelacion ticket',
    '26': 'Cabezal de beneficio al total',             # NO se procesa
    '27': 'Detalle de un beneficio al total',          # NO se procesa
    '28': 'Descuento al total',                        # NO se procesa
    '29': 'Devolución de envases',
    '30': 'Venta a la subfamilia',
    '32': 'Inventario',                                # NO se procesa
    '33': 'Canje de ítem',                             # NO se procesa
    '34': 'Información de cliente de fidel.',          # NO se procesa
    '35': 'Cancelación de un canje de ítem',           # NO se procesa
    '36': 'Total de canje',                            # NO se procesa
    '37': 'M.Pago con tarjeta',
    '38': 'M.Pago con cheque',
    '40': 'M.Pago luncheon ticket',
    '43': 'Voucher de la tarjeta',
    '44': 'Datos adicionales garantía articulo',       # NO se procesa
    '47': 'Pago de servicio',
    '49': 'Detalle beneficios med.pago-moneda',        # NO se procesa
    '52': 'M.Pago de caja',
    '53': 'Tipo de ticket',
    '55': 'Intervención de la supervisora',
    '56': 'Cancelacion de un pago de servicio',
    '57': 'Tipo de cliente',
    '58': 'Ticket de cancelación de pago',
    '60': 'Cupón',                                     # NO se procesa
    '61': 'Pedidos',
    '62': 'Fin de pausa de cajera',                    # NO se procesa
    '63': 'Redondeo importe total del ticket',
    '65': 'Puntos de fidelización',                    # NO se procesa
    '67': 'M.Pago de cupón corporativo',               # NO se procesa
    '68': 'Id. Cliente ',
    '71': 'Puntos no generadas',                       # NO se procesa
    '72': 'Descuento para parking',                    # NO se procesa
    '73': 'Ticket Z',                                  # NO se procesa
    '76': 'Descuento producido por marcas',            # NO se procesa
    '77': 'Cabezal de marca',                          # NO se procesa
    '78': 'Detalle de la marca',                       # NO se procesa
    '81': 'Devolución de pago de servicio',
    '82': 'Consulta e.de cuenta de la cobranza.',      # NO se procesa
    '83': 'Voucher de la cobranza',
    '84': 'Apertura de gaveta',                        # NO se procesa
    '85': 'M.Pago de tarjeta offline',
    '86': 'Recargo',                                   # NO se procesa
    '87': 'Descuento a los med.pago-moneda.',          # NO se procesa
    '88': 'Venta cómputos celular',                    # NO se procesa
    '89': 'Devolución venta cómputos celular',         # NO se procesa
    '90': 'M.Pago ticket TAlimentos',
    '91': 'M.Pago ticket Total',
    '92': 'Linea de factura',
    '94': 'Pago con cheque cobranza',
    '95': 'Ticket de fondeo',                          # NO se procesa
    '97': 'Ticket de retiro',
    '99': 'Cupones Numeros',                           # NO se procesa
    '100': 'Ticket de cobranza',
    '101': 'Ticket de devolución de cobranza',
    '102': 'Ticket cancelacion de cobranza',
    '103': 'Cancelación de salida de cajera',          # NO se procesa
    '104': 'Seteo monto de prestamo en efectivo',      # NO se procesa
    '105': 'Prestamo en efectivo',                     # NO se procesa
    '106': 'Ticket del cliente de facturación ',       # NO se procesa
    '107': 'Ticket de información del cliente',        # NO se procesa
    '108': 'Ticket gift card',                         # NO se procesa
    '109': 'Ticket devolución gift card',              # NO se procesa
    '115': 'Pago descuento iva Asig Fliares',          # NO se procesa
    '117': 'Preventa',                                 # NO se procesa
    '118': 'Ticket vale almuerzo',                     # NO se procesa
    '119': 'Ticket pago vale almuerzo',                # NO se procesa
    '120': 'Venta Mides',
    '121': 'Voucher retiro leche tarjeta Mides',       # NO se procesa
    '122': 'Ticket info importe',
    '123': 'M.Pago TCRE',
    '124': 'Voucher de la tarjeta TCRE',
    '125': 'Total puntos PROMO',                       # NO se procesa
    '126': 'Ticket cliente de cuenta corriente',
    '127': 'M.Pago cuenta corriente',
    '900': 'Declaración de cajera',                    # NO se procesa
}




class IPTicket(object):
    """
        La clase es un ejemplo de uso de la biblioteca

    """

    def __init__(self, tupla_cabezal, lista_de_tuplas_lineas):
        """
        Los parámetros son los datos extraidos de salidapazosbuevo-1- CSV -> tuplas
        :param tupla_cabezal:           tuple :  Una tupla con todos los datos de un cabezal de ticket
        :param lista_de_tuplas_lineas:  list  :  Lista de tuplas. Cada tupla es una línea de detalle de ticket

        """
        lineas = dict()
        self.cabezal = IPCabezal(tupla_cabezal)  # instalcia el Cabezal

        for lin in lista_de_tuplas_lineas:
            linea = IPLinea(lin, self.cabezal.id_ticket)  # instalcia cada Línea de detalle
            lineas.update({linea.id_linea: linea})

        self.lineas = lineas




class IPCabezal(object):

    """
        Representa una línea de tipo cabezal Salida Pazos4
        --------------------------------------------------

        Separador de columnas: '#'
        Nombres de columnas en orden posicional:
            TipoLinea    # CodigoCaja        # NumeroTicket  #  CodigoCajera  #  TimestampTicket #  +
            EstadoTicket # CantidadArticulos # TotalaPagar   # TipoCliente    #   CantidadLineas

        Ejemplo::
            En csv salidapazos: "C#1#2#350#2#20151121105326#F#4#183.40#20#13"
            La misma línea tal cómo llega a una instancia de `IPCabezal` (se descarta el indicador de línea 'C')
                lista = ['1', '2', '350', '2', '20151121105326', 'F', '4', '183.40', '20', '13']

        La instanciación será
            `IPCabezal(una_linea_tipo_cabezal)`

        Con alguna diferencia, se usan estructuras similares para la instancia de líneas de tipo detalle de ticket.
        En ambos casos se omite el identificador de línea.

    """

    def __init__(self, linea_de_cabezal):
        """
        Ejemplo de línea de cabezal o cabezal del ticket::

            TipoLinea    # CodigoCaja        # NumeroTicket  #  CodigoCajera  #  TimestampTicket #  +
            EstadoTicket # CantidadArticulos # TotalaPagar   # TipoCliente    #   CantidadLineas

        """

        rlinea = 'C#' + '#'.join(linea_de_cabezal)  # reconstruye lína cabezal salidapazos (debug)

        tipocabezal        = linea_de_cabezal[0]
        codigocaja         = linea_de_cabezal[1]
        numeroticket       = linea_de_cabezal[2]
        codigocajera       = linea_de_cabezal[3]
        timestampticket    = linea_de_cabezal[4]     # aaaaMMddhhmmss
        estadoticket       = linea_de_cabezal[5]     
        cantidadarticulos  = linea_de_cabezal[6]
        totalapagar        = linea_de_cabezal[7]
        tipocliente        = linea_de_cabezal[8]
        cantidadlineas     = linea_de_cabezal[9]
        
        ts                 = linea_de_cabezal[4]
        fecha              = ts[0:4] + ts[4:6] + ts[6:8]
        id_ticket          = timestampticket + codigocaja + numeroticket

        self.cabezal = dict( 
                rlinea            = rlinea,
                id_ticket         = id_ticket,
                descripcion       = CABEZAL[tipocabezal],
                fecha             = fecha,
                tipocabezal       = tipocabezal,
                codigocaja        = codigocaja,
                numeroticket      = numeroticket,
                codigocajera      = codigocajera,
                timestampticket   = timestampticket,
                estadoticket      = estadoticket,
                cantidadarticulos = cantidadarticulos,
                totalapagar       = totalapagar,
                tipocliente       = tipocliente,
                cantidadlineas    = cantidadlineas,
            )

class IPLinea(object):

    """
        Representa a una línea de detalle de ticket de Salidapazos4 (SM).
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        Al igual que en IPCabezal, se define un diccionario de tipos de lineas de detalle de ticket.

            En el diccionario de tipos, cada `llave` será el número del tipo de línea de ticket, 
            en tanto su `valor` será una tupla de dos elementos,

            El primer elemento de la tupla es un `string` con la descripción del tipo de línea de detalle.
            El segundo elemento, es el nombre de un método que entiende los datos de éste tipo de línea. Es
            éste metodo el que retornará la linea procesada en la instancia.
            {tipo_linea_detalle: (Descripción, métodpo)}
            Ejemplo:
                        >>>    {'4': ('Total de Ticket', self._lt_4)}
        Ejemplo:
                L#10#4#153713#774.05#21.97#183.05#21.97

            Tipo de línea: Total de ticket (4) por un total de $774.05 e incluye pago de servicio por $591.00

            Se omite el identificador de línea 'L'
                ___________
               |          |----> estructura comun a todas las lineas del ticket
               10#4#153713 # 774.05#21.97#183.05#21.97
                            |________________________|----> estructura y valores epecíficos de la línea:

            Así llega la `linea_de_detalle` en la instancia:
                    ['10','4','153713','774.05','21.97','183.05','21.97']

            Número de línea: '10'
            Tipo de línea: '4'
            Timestamp: '153713'

            Atributos comunes en todas las líneas del ticket: ['10','4','153713']
            Atributos específicos de éste tipo de línea:  ['774.05','21.97','183.05','21.97']

            En el ejemplo, dada la línea_de_cabezal ['10','4','153713','774.05','21.97','183.05','21.97']
            el código python sería:

            >>> lin_obj = IPLinea(linea_de_detalle, id_ticket)
            >>> datos   = lin_obj.metodo()
            >>> for k, v in datos.items()
            >>>    print("{}: {}".format(datos,))
            >>> totalticket: 774.05
            >>> ivatotalticket: 21.97
            >>> totalticketsinpagoservicios: 183.05
            >>> ivatotalticketsinpagoservicios: 21.97

    """

    def __init__(self, linea=None, tck_id=None):
        """
            El parametro `linea` llega a la instancia sin el identificador de línea `L`

            :param linea: list  línea de detalle de ticket  (línea de ticket)
            :param tck_id: long / str  id del ticket (id del cabezal de ticket)  es el timestamp de pazos

            El diccionario de clase `tipos_linea_tck`, es análogo al diccionario de tipos de líneas de cabezal.
            En la pequeña diferencia en su estructura es presencia de un tercer elemento en las tuplas.

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
            '94': ('Pago con cheque cobranza', self._lt_94),
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
        
        self.tck_id = tck_id
        self.rlinea = 'L#' + '#'.join(linea)          # recrea linea de detalle de salidapazos original (debug)
        self.id_linea = int(linea[0])                 # N.de línea único (permite ordenar las líneas de por sí)
        self.llave = llave = linea[1]                 # Tipo de línea de ticket
        self.esta_linea = linea[3:]                   # Datos específicos de línea           
        self.cabezal_id = tck_id                      # Id del ticket (cabezal de ticket)            
        self.descripcion = tipos_linea_tck[llave][0]  # Descripción del Tipo de línea
        self.datos = tipos_linea_tck[llave][1]()      # invoca el método específico y carga los datos de la línea
                                                      # de ese tipo de línea en la instancia
        # id_ticket + tipo_linea + numero_linea
        self.datos['name'] = str(tck_id) + '-' + str(linea[1]) + '-' + str(linea[0])

    """
        Métodos "lt_nnn":
        '''''''''''''''''
                            Son métodos específicos para cada tipo de linea_de_cabezal
        cuya referencia consituye el segundo elemento de la lista de valores
        en el diccionario de tipos.
        
        En esta documentación sólo muestram dos métodos:
        
            def _lt_1() procesa una línea tipo '1'  Líneas de Venta de ítem
            def _lt_4() procesa una línea tipo '4'  Línea de total del ticket        
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
        result = dict()
        result.update(dict(codigoarticulo = lin[0],
                           cantidad = lin[1],
                           precio = lin[2],
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
                           preciounitario = lin[25])
        )

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
        result = dict(totalticket = lin[0],                     # Importe total
                      ivatotalticket = lin[1],                  # Iva del ticket
                      totalticketsinpagoservicios = lin[2],     # Total sin servicios cobrados
                      ivatotalticketsinpagoservicios = lin[3])  # Total IVA sin servicios
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
