# coding=utf-8
from os.path import dirname, abspath, isdir
from os import mkdir



# path absoluto desde el cual éste módulo es cargado
try:
    WorkPath = dirname(dirname(abspath(__file__)))
except:
    # si se carga desde el prompt del intérptrete python
    WorkPath = '/tmp/'

# definiciones para el log
ldir = ''.join(WorkPath + '/log/')

# si existe en "WorkPath", lo crea
isdir(ldir) or mkdir(ldir)

# fromatos para el log
log_format = '%(asctime)s, %(levelname)s %(message)s'
datefmt = '%H:%M:%S'
filemode = 'a'



# contantes para los informes salidapazos
TIPOS_LINEAS_CABEZAL = {                   # Tipo   Descripción        | NO SE USAN
         '1': ('Ticket Venta/Ingreso',),   #  1   |  Venta(SM).        |  2  | Pedido
         '3': ('Devolución',),             #  3   |  Devolución        |  5  | Tck. Exento IVA
         '4': ('Estado de cuenta',),       #  4   |  Estado de cuenta. |  9  | Gift
         '6': ('Canje',),                  #  6   |  Canje             | 12  | No generado (No existeen)
         '7': ('Inventario',),             #  7   |  Inventario        | 13  | No generado (el informe)
         '8': ('Ticket de Cajera',),       #  8   |  Cajera
        '10': ('Pago de caja',),           #  10  |  Pago Caja
        '11': ('Factura',),                #  11  |  Factura
        '14': ('Consulta',),               #  14  |  Consulta.
        '15': ('Apertura de Gaveta',),     #  15  |  Apertura De Gaveta
        '16': ('N.Credito Devolucion',),   #  16  |  Nota De Credito
        '17': ('Fondeo',),                 #  17  |  Fondeo
        '18': ('Retiro',),                 #  18  |  Retiro
        '19': ('Prestamo efectivo',),      #  19  |  De Prestamo Efectivo (SM)
        '20': ('Retiro de Productos',),    #  20  |  Retiro De Productos (SM)
        '21': ('Cab. Z de Caja',),         #  21  |  Z (SM)
       '999': ('-Cabezal NO definido-',)   # 999  |  No Definido
                   }
CABEZAL = {
        '1': 'Ticket Venta/Ingreso',
        '3': 'Devolución',
        '4': 'Estado de cuenta',
        '6': 'Canje',
        '7': 'Inventario',
        '8': 'Ticket de Cajera',
        '10': 'Pago de caja',
        '11': 'Factura',
        '14': 'Consulta',
        '15': 'Apertura de Gaveta',
        '16': 'N.Credito Devolucion',
        '17': 'Fondeo',
        '18': 'Retiro',
        '19': 'Prestamo efectivo',
        '20': 'Retiro de Productos',
        '21': 'Cab. Z de Caja',
        '999': '-Cabezal NO definido-'
                   }

LINEA = {
    '1': 'Venta de ítem',
    '4': 'Total del ticket',
    '5': 'Cabezal de CFE',
    '6': 'Pié de CFE',
    '7': 'Identificación de la cajera',
    '9': 'M.Pago de ticket en efectivo',
    '10': 'Cabezal de un combo',
    '11': 'Detalle de combo',
    '12': 'Cancelación de ítem',
    '13': 'Descuento a un ítem',
    '15': 'Puntos generados de fidel. ítem',
    '16': 'Puntos totales de fidel. generados',
    '18': 'Regalo de artículos',
    '19': 'Cupón',
    '20': 'Devolución de un ítem',
    '21': 'Entrada de cajera',
    '22': 'Salida de cajera',
    '23': 'Pausa de cajera',
    '24': 'Cancelacion ticket',
    '26': 'Cabezal de beneficio al total',
    '27': 'Detalle de un beneficio al total',
    '28': 'Descuento al total',
    '29': 'Devolución de envases',
    '30': 'Venta a la subfamilia',
    '32': 'Inventario',
    '33': 'Canje de ítem',
    '34': 'Información de cliente de fidel.',
    '35': 'Cancelación de un canje de ítem',
    '36': 'Total de canje',
    '37': 'M.Pago con tarjeta',
    '38': 'M.Pago con cheque',
    '40': 'M.Pago luncheon ticket',
    '43': 'Voucher de la tarjeta',
    '44': 'Datos adicionales garantía articulo',
    '47': 'Pago de servicio/cobranza',
    '49': 'Detalle beneficios med.pago-moneda',
    '52': 'M.Pago de caja',
    '53': 'Tipo de ticket',
    '55': 'Intervención de la supervisora',
    '56': 'Cancelacion de un pago de servicio',
    '57': 'Tipo de cliente',
    '58': 'Ticket de cancelación de pago',
    '60': 'Cupón',
    '61': 'Pedidos',
    '62': 'Fin de pausa de cajera',
    '63': 'Redondeo importe total del ticket',
    '65': 'Puntos de fidelización',
    '67': 'M.Pago de cupón corporativo',
    '68': 'Id. Cliente ',
    '71': 'Puntos no generadas',
    '72': 'Descuento para parking',
    '73': 'Ticket Z',
    '76': 'Descuento producido por marcas',
    '77': 'Cabezal de marca',
    '78': 'Detalle de la marca',
    '81': 'Devolución de pago de servicio',
    '82': 'Consulta e.de cuenta de la cobranza.',
    '83': 'Voucher de la cobranza',
    '84': 'Apertura de gaveta',
    '85': 'M.Pago de tarjeta offline',
    '86': 'Recargo',
    '87': 'Descuento a los med.pago-moneda.',
    '88': 'Venta cómputos celular',
    '89': 'Devolución venta cómputos celular',
    '90': 'M.Pago ticket TAlimentos',
    '91': 'M.Pago ticket Total',
    '92': 'Linea de factura',
    '94': 'Pago con cheque cobranza',
    '95': 'Ticket de fondeo',
    '97': 'Ticket de retiro',
    '99': 'Cupones Numeros',
    '100': 'Ticket de cobranza',
    '101': 'Ticket de devolución de cobranza',
    '102': 'Ticket cancelacion de cobranza',
    '103': 'Cancelación de salida de cajera',
    '104': 'Seteo monto de prestamo en efectivo',
    '105': 'Prestamo en efectivo',
    '106': 'Ticket del cliente de facturación ',
    '107': 'Ticket de información del cliente',
    '108': 'Ticket gift card',
    '109': 'Ticket devolución gift card',
    '115': 'Pago descuento iva Asig Fliares',
    '117': 'Preventa',
    '118': 'Ticket vale almuerzo',
    '119': 'Ticket pago vale almuerzo',
    '120': 'Venta Mides',
    '121': 'Voucher retiro leche tarjeta Mides',
    '122': 'Ticket info importe',
    '123': 'M.Pago TCRE',
    '124': 'Voucher de la tarjeta TCRE',
    '125': 'Total puntos PROMO',
    '126': 'Ticket cliente de cuenta corriente',
    '127': 'M.Pago cuenta corriente',
    '900': 'Declaración de cajera',
}


# TODO: exponer métodos de líneas 
'''
, self._lt_1),
, self._lt_4),
, self._lt_5),
, self._lt_6),
, self._lt_7),
, self._lt_9),
, self._lt_10),
, self._lt_11),
, self._lt_12),
, self._lt_13),
, self._lt_15),
, self._lt_16),
, self._lt_18),
, self._lt_19),
, self._lt_20),
, self._lt_21),
, self._lt_22),
, self._lt_23),
, self._lt_24),
, self._lt_26),
, self._lt_27),
, self._lt_28),
, self._lt_29),
, self._lt_30),
, self._lt_32),
, self._lt_33),
, self._lt_34),
, self._lt_35),
, self._lt_36),
, self._lt_37),
, self._lt_38),
, self._lt_40),
, self._lt_43),
, self._lt_44),
, self._lt_47),
, self._lt_49),
, self._lt_52),
, self._lt_53),
, self._lt_55),
, self._lt_56),
, self._lt_57),
, self._lt_58),
, self._lt_60),
, self._lt_61),
, self._lt_62),
, self._lt_63),
, self._lt_65),
, self._lt_67),
, self._lt_68),
, self._lt_71),
, self._lt_72),
, self._lt_73),
, self._lt_76),
, self._lt_77),
, self._lt_78),
, self._lt_81),
, self._lt_82),
, self._lt_83),
, self._lt_84),
, self._lt_85),
, self._lt_86),
, self._lt_87),
, self._lt_88),
, self._lt_89),
, self._lt_92),
, self._lt_90),
, self._lt_91),
, self._lt_94),
, self._lt_95),
, self._lt_97),
, self._lt_99),
, self._lt_100),
, self._lt_101),
, self._lt_102),
, self._lt_103),
, self._lt_104),
, self._lt_105),
, self._lt_106),
, self._lt_107),
, self._lt_108),
, self._lt_109),
, self._lt_115),
, self._lt_117),
, self._lt_118),
, self._lt_119),
, self._lt_120),
, self._lt_121),
, self._lt_122),
, self._lt_123),
, self._lt_124),
, self._lt_125),
, self._lt_126),
, self._lt_127),
, self._lt_900),
'''
