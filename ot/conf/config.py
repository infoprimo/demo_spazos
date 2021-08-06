# coding: utf-8
from os.path import dirname, abspath, isdir
from os import mkdir, getcwd

DEBUG = 0

_pwd = getcwd()

# es el path absoluto desde el cual éste módulo es cargado
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


# Informes Salidapazos-nuevo-1-AAAAmmdd.nnnn
inputPath = ''.join(WorkPath + "/inout/informes/")

# Informes Salidapazos-nuevo-1-AAAAmmdd.nnnn
iPrefijo = "Salidapazosnuevo-1-2021*"

# sqlite historico informes json creados
dbName = '.spazos_tck.db'
tableName = "spazosjson"

# informes de salida `json`
outputPath = ''.join(WorkPath + '/inout/json/')

# separadores e indenctación para formateo de los json
separadores = (',', ': ')
indenta = 3

# datos pre compilados de clientes y proveedores (openerp)
datafile = "/erpdata.json"


class Error(Exception):
    """Template claas para manejo de errores"""


dbSettings = {
    # 'hostname': 192.0.1.11,
    'hostname': '127.0.1.1',
    'port': 8069,
    'database': 'zuniuno',
    'username': 'admin',
    'password': 'fadmin',
    }


# constantes para salida pazos

AUXILIRES_CUENTAS = ('43', )

iva_map = {'1': 0.22, '2': 0.10, '3': 0}

MODODEINGRESO = [
    ('0', 'Teclado'),
    ('1', 'Scanner'),
    ('2', 'Banda Magn.')
 ]
 
# es un híbrido complementario (tipo_tarjeta ctacte cardtype)
TTAR_CTYPE_CTA = {
    '000': ('6203', 'VISA'),
    '001': ('6205', 'DINERS FIRSTDAT'),
    '002': ('6207', 'MASTER'),
    '003': ('3564', 'AMEX'),
    '004': ('6209', 'OCA'),
    '005': ('3569', 'CREDITEL'),
    '007': ('6202', 'CABAL'),
    '014': ('6211', 'ANDA'),
    '015': ('6208', 'CRED.DIRECTOS'),
    '020': ('3564', 'ITALCRED'),
    '021': ('6201', 'LIDER'),
    '022': ('6204', 'CLUB DEL ESTE'),
    '025': ('6212', 'PASSCARD'),
    '060': ('6207', 'MASTEREDC'),
    '061': ('6203', 'VISAEDC'),
    '122': ('6218', 'Maestro BPS Prest.'),
    '124': ('6203', 'VISAAFAM'),
    '126': ('6202', 'CABALAFAM'),
    '127': ('3569', 'CREDITELAFAM'),
    '128': ('6209', 'OCAAFAM'),
    '129': ('6218', 'Maestro'),
    '140': ('6203', 'VISA DEBITO ELECTRON'),
    '141': ('6203', 'VISAALFA'),
    '166': ('6201', 'LIDERAFAM'),
    '169': ('6201', 'SODEXO'),
    '170': ('6219', 'REDPAGOSTACRE'),
    '171': ('6207', 'MASTER DEBITO'),
    '172': ('6207', 'MASTER DEBITO NO PIN'),
    '179': ('6210', 'EDENRED'),
    '199': ('6221', 'MIDES'),
 }
 
 
TIPOTARJETA_CTA = {
    '000': '6203',
    '001': '6205',
    '002': '6207',
    '004': '6209',
    '005': '3569',
    '007': '6202',
    '014': '6211',
    '015': '6208',
    '021': '6201',
    '022': '6204',
    '025': '6212',
    '122': '6218',
    '129': '6218',
    '140': '6203',
    '169': '6201',
    '170': '6219',
    '171': '6207',
    '172': '6207',
    '179': '6210',
    '199': '6221',
    'GEN': '99999'
 }

TIPOTARJETA = [
    ('000', 'VISA'),
    ('001', 'DINERS'),
    ('002', 'MASTER'),
    ('004', 'OCA'),
    ('005', 'CREDITEL'),
    ('007', 'CABAL'),
    ('014', 'ANDA'),
    ('015', 'CRED.DIRECTOS'),
    ('021', 'LIDER'),
    ('022', 'CLUB DEL ESTE'),
    ('025', 'PASSCARD'),
    ('122', 'Maestro BPS Prest.'),
    ('129', 'Maestro'),
    ('140', 'VISA DEBITO'),
    ('169', 'SODEXO'),
    ('170', 'REDPAGOS ALIMENTOS'),
    ('171', 'MASTER DEBITO'),
    ('172', 'MASTER DEBITO2'),
    ('179', 'EDENRED'),
    ('199', 'MIDES'),
 ]

CARDTYPE = [
    ('000', 'VISA'),
    ('001', 'DINERSFIRSTDATA'),
    ('002', 'MASTER'),
    ('003', 'AMEX'),
    ('004', 'OCA'),
    ('005', 'CREDITEL'),
    ('007', 'CABAL'),
    ('014', 'ANDA'),
    ('015', 'CREDIR'),
    ('020', 'ITALCRED'),
    ('021', 'LIDER'),
    ('022', 'CDESTE'),
    ('025', 'PASSCARD'),
    ('060', 'MASTEREDC'),
    ('061', 'VISAEDC'),
    ('122', 'MAESTROAFAM'),
    ('124', 'VISAAFAM'),
    ('126', 'CABALAFAM'),
    ('127', 'CREDITELAFAM'),
    ('128', 'OCAAFAM'),
    ('129', 'MAESTRO'),
    ('140', 'VISAELECTRON'),
    ('141', 'VISAALFA'),
    ('166', 'LIDERAFAM'),
    ('169', 'SODEXO'),
    ('170', 'REDPAGOSTACRE'),
    ('171', 'MASTERDEBITO'),
    ('172', 'MASTERDEBITONOPIN'),
    ('179', 'EDENRED'),
    ('199', 'MIDES2'),
    ]


MEDIOPAGO = [
    ('1',  'Efectivo'),
    ('2',  'Tarjetas'),
    ('3',  'Cheque'),
    ('4',  'Cta.Corriente'),
    ('6',  'Tarjeta Cuotas'),
    ('8',  'Orden Anda'),
    ('9',  'T.Alimentos (manual)'),
    ('11', 'Mides'),
    ('14', 'Corporativo Alimentos'),
    ('15', 'Corporativo General'),
    ('16', 'Corporativo Alimentos y Servicios'),
    ('17', 'Tarjeta Manual'),
    ('18', 'Tarjeta T.Alimentos'),
    ('26', 'Dto. Ley 18910'),
    ('29', 'Dev.Envases'),
    ('63', 'Redondeo'),
    ('87', 'Dto. Obtenido (por el cliente)'),
    ('94', 'Cheque x Cobranza'),

 ]

MEDIOSDEPAGO = {
    '1' : 'Efectivo',
    '2' : 'Tarjeta Credito/Debito',
    '3' : 'Cheque',
    '4' : 'Cuenta Corriente',
    '6' : 'Tarjeta Cuotas',
    '8' : 'Orden Anda',
    '9' : 'Ticket Alimentacion',
    '11': 'Mides',
    '14': 'Corporativo Alimentos',
    '15': 'Corporativo General',
    '16': 'Corporativo Alimntos y Servicios',
    '17': 'Tarjeta Manual',
    '18': 'Ticket Aliment. Elect.',
    '26': 'Descuento Ley 18910',
    '29': 'Dev.de envases',
    '63': 'Redondeo',
    '87': 'Dto. Obtenido (por el cliente)',
    '94': 'Cheque x Cobranza',
    }

# TIPOMEDIOPAGO = [(1, 2), (3, 4)]

CODIGOMONEDA = [
    ('00', 'Pesos'),
    ('01', 'Dolares'),
    ('1', 'Pesos'),
    ('2', 'Dolares'),
    ('3', 'Pesos Arg.')
 ]

TIPODETICKET = [
    ('1', "Ticket excento de Iva"),
    ('0', "Normal")
 ]

CODIGOIVA = [
    ('1', 'Basico'),
    ('2', 'Minimo'),
    ('3', 'Exento'),
    ('4', 'Carnes'),
    ('5', 'Cobranza/No aplica'),
    ('10', 'Exportacion y asimilados'),
    ('12', 'En suspenso')
 ]

TIPOCABEZAL = [
    ('1', 'Venta/Ingreso'),
    ('2', 'Pedido (NO GENERADO)'),
    ('3', 'Devolución'),                           #  tipo_operación_al_mpago = 2
    ('4', 'Estado de cuenta'),
    ('5', 'Exento IVA (NO GENERADO)'),
    ('6', 'Canje'),
    ('7', 'Inventario'),
    ('8', 'Adm Cajera'),
    ('9', 'Ticket Gift (NO GENERADO)'),
    ('10', 'Pago Caja'),
    ('11', 'C.Factura'),
    ('12', '12 No generado  (NO GENERADO)'),
    ('13', '13 No generado  (NO GENERADO)'),
    ('14', 'Consulta'),
    ('15', 'Apertura de Gaveta'),
    ('16', 'Nota de credito devolucion'),          #  tipo_operación_al_mpago = 2
    ('17', 'Adm Fondeo'),
    ('18', 'Adm Retiro'),
    ('19', 'Adm Prestamo efectivo'),
    ('20', 'Adm Retiro de Productos'),
    ('21', 'Adm Ticket Z'),
    ('999', 'Ticket NO DEFINIDO')
    ]

CABEZAL = {
    '1': 'Ticket Venta/Ingreso',
    '2': 'Pedido            # NO',
    '3': 'Devolución',
    '4': 'Estado de cuenta',
    '5': 'Tck. Exento IVA   # NO',
    '6': 'Canje',
    '7': 'Inventario',
    '8': 'Ticket de Cajera',
    '9': 'Gift              # NO',
    '10': 'Pago de caja',
    '11': 'Factura',
    '12': 'No generado      # NO',
    '13': 'No generado      # NO',
    '14': 'Consulta',
    '15': 'Apertura de Gaveta',
    '16': 'N.Credito Devolucion',
    '17': 'Fondeo',
    '18': 'Retiro',
    '19': 'Prestamo efectivo',
    '20': 'Retiro de Productos',
    '21': 'Cab. Z de Caja',
    '999': '-Cabezal NO DEFINIDO'
    }
    
TIPOLINEA = [
    ('1', u'Venta de item'                        ),    #
    ('4', u'Total del ticket'                     ),    #
    ('5', u'Cabezal de CFE'                       ),    #
    ('6', u'Pie de CFE'                           ),    #
    ('7', u'Identificacion de la cajera'          ),    #
    ('9', u'M.Pago de ticket en efectivo'         ),    #                            #  tipo_operación = 1
    ('10', u'Cabezal de un combo'                 ),    #
    ('11', u'Detalle de combo'                    ),    #
    ('12', u'Cancelacion de item'                 ),    #
    ('13', u'Descuento a un item'                 ),    #
    ('15', u'Puntos generados de fidel. item'     ),    #
    ('16', u'Puntos totales de fidel. generados'  ),    #
    ('18', u'Regalo de articulos'                 ),    #
    ('19', u'Cupon'                               ),    #
    ('20', u'Devolucion de un item'               ),    #
    ('21', u'Entrada de cajera'                   ),    #
    ('22', u'Salida de cajera'                    ),    #
    ('23', u'Pausa de cajera'                     ),    #
    ('24', u'Cancelacion ticket'                  ),    # verificar si cancela cuenta o tarjeta  etc.
    ('26', u'Cabezal de beneficio al total'       ),    #
    ('27', u'Detalle de un beneficio al total'    ),    #
    ('28', u'Descuento al total'                  ),    #
    ('29', u'Devolucion de envases'               ),    #
    ('30', u'Venta a la subfamilia'               ),    #
    ('32', u'Inventario'                          ),    #
    ('33', u'Canje de item'                       ),    #
    ('34', u'Informacion de cliente de fidel.'    ),    #
    ('35', u'Cancelacion de un canje de item'     ),    #
    ('36', u'Total de canje'                      ),    #    generan auxiliar == ga
    ('37', u'M.Pago con tarjeta'                  ),    # 37 'M.Pago con tarjeta'          ga      tipo_operacion = 1
    ('38', u'M.Pago con cheque'                   ),    # 38 'M.Pago con cheque'                   tipo_operacion = 1
    ('40', u'M.Pago luncheon ticket'              ),    # 40 'M.Pago luncheon ticket'      ga      tipo_operacion = 1
    ('43', u'Voucher de la tarjeta'               ),    # 43 'Voucher de la tarjeta'       ga
    ('44', u'Datos adicionales garantia articulo' ),    #
    ('47', u'Pago de servicio/cobranzas'          ),    #  esta es la cobranza de cuenta corriente
    ('49', u'Detalle beneficios med.pago-moneda'  ),    #
    ('52', u'M.Pago de caja'                      ),    #
    ('53', u'Tipo de ticket'                      ),    #
    ('54', u'Pago de ticket en puntos'            ),    # 'Pago de ticket en puntos'
    ('55', u'Intervencion de la supervisora'      ),    #
    ('56', u'Cancelacion de un pago de servicio'  ),    #
    ('57', u'Tipo de cliente'                     ),    #
    ('58', u'Ticket de cancelacion de pago'       ),    #
    ('60', u'Cupon'                               ),    #
    ('61', u'Pedidos'                             ),    #
    ('62', u'Fin de pausa de cajera'              ),    #
    ('63', u'Redondeo'                            ),    # Redondeo al importe total del ticket
    ('65', u'Puntos de fidelizacion'              ),    #
    ('67', u'M.Pago de cupon corporativo'         ),    #
    ('68', u'Id. domicilio/Cliente'               ),    #
    ('71', u'Puntos no generadas'                 ),    #
    ('72', u'Descuento para parking'              ),    #
    ('73', u'Ticket Z'                            ),    # 37 'M.Pago con tarjeta'
    ('76', u'Descuento producido por marcas'      ),    #
    ('77', u'Cabezal de marca'                    ),    # 40 'M.Pago luncheon ticket'
    ('78', u'Detalle de la marca'                 ),    # 43 'Voucher de la tarjeta'
    ('81', u'Devolucion de pago de servicio'      ),    # 85 'M.Pago de tarjeta offline'
    ('82', u'Consulta e.de cuenta de la cobranza.'),    # 90 'M.Pago ticket TAlimentos'
    ('83', u'Voucher de la cobranza'              ),    # 91 'M.Pago ticket Total'
    ('84', u'Apertura de gaveta'                  ),    #
    ('85', u'M.Pago de tarjeta offline'           ),    # 'M.Pago de tarjeta offline'     tipo_operación = 1
    ('86', u'Recargo'                             ),    #
    ('87', u'Descuento a los med.pago-moneda.'    ),    #
    ('88', u'Venta computos celular'              ),    #
    ('89', u'Devolucion venta cómputos celular'   ),    #
    ('90', u'M.Pago ticket TAlimentos'            ),    # 90 'M.Pago ticket TAlimentos'     tipo_operación = 1
    ('91', u'M.Pago ticket Total'                 ),    # 91 'M.Pago ticket Total'          tipo_operación = 1
    ('92', u'Linea de factura'                    ),    #
    ('93', u'A marzo 2020 no hay linea 93'        ),    #
    ('94', u'Pago con cheque cobranza'            ),    #
    ('95', u'Ticket de fondeo'                    ),    #
    ('97', u'Ticket de retiro'                    ),    #
    ('99', u'Cupones Numeros'                     ),    #
    ('100', u'Ticket de cobranza'                  ),    #
    ('101', u'Ticket de devolucion de cobranza'    ),    #
    ('102', u'Ticket cancelacion de cobranza'      ),    #
    ('103', u'Cancelacion de salida de cajera'     ),    #
    ('104', u'Seteo monto de prestamo en efectivo' ),    #
    ('105', u'Prestamo en efectivo'                ),    #
    ('106', u'Ticket del cliente de facturacion '  ),    #
    ('107', u'Ticket de informacion del cliente'   ),    #
    ('108', u'Ticket gift card'                    ),    #
    ('109', u'Ticket devolucion gift card'         ),    #
    ('115', u'M.Pago descto. iva Asig Fliares'     ),    #
    ('117', u'Preventa'                            ),    #
    ('118', u'Ticket vale almuerzo - Emision'      ),    #
    ('119', u'Tick. pago vale almuerzo - Modo Pago'),    #
    ('120', u'Venta Mides'                         ),    #
    ('121', u'Voucher retiro leche tarjeta Mides'  ),    #
    ('122', u'Ticket info importe'                 ),    #
    ('123', u'M.Pa T.Alim/Canasta/Restauran elec.' ),    #                              tipo_operación = 1
    ('124', u'Voucher de la tarjeta TCRE'          ),    #
    ('125', u'Total puntos PROMO'                  ),    #
    ('126', u'Ticket cliente de cuenta corriente'  ),    #
    ('127', u'M.Pago cuenta corriente'             ),    #                              tipo_operación = 1
    ('128', u'M.Pago Devolución envases'           ),    #                              tipo_operación = 2

    ('900', u'Declaracion de cajera'               )
 ]


def RTIPOLINEA(linea=None):
    if not linea or not isinstance(linea, (str,)):
        raise Error(u'No es un tipo de línea válido!')
    for tipo, desc in TIPOLINEA:
        if tipo == linea:
            return desc

LINEA = {
    '1': 'Venta de ítem',
    '4': 'Total del ticket',
    '5': 'Cabezal de CFE',
    '6': 'Pié de CFE',
    '7': 'Identificación de la cajera',
    '9': 'M.Pago de ticket en efectivo',                        #
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
    '37': 'M.Pago con tarjeta',                                 # 37
    '38': 'M.Pago con cheque',
    '40': 'M.Pago luncheon ticket',                             # 40
    '43': 'Voucher de la tarjeta',
    '44': 'Datos adicionales garantía articulo',
    '47': 'Pago de servicio/cobranzas',                         #
    '49': 'Detalle beneficios med.pago-moneda',
    '52': 'M.Pago de caja',
    '53': 'Tipo de ticket',
    '54': 'Pago de ticket en puntos',
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
    '68': 'Id. domicilio/Cliente ',
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
    '90': 'M.Pago ticket TAlimentos',                  #          90
    '91': 'M.Pago ticket Total',                       #          91
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
    '115': 'M.Pago descto. iva Asig. Fliares',
    '117': 'Preventa',
    '118': 'Ticket vale almuerzo',
    '119': 'Ticket pago vale almuerzo',
    '120': 'Venta Mides',
    '121': 'Voucher retiro leche tarjeta Mides',
    '122': 'Ticket info importe',
    '123': 'M.Pago TCRE',                              #          123
    '124': 'Voucher de la tarjeta TCRE',
    '125': 'Total puntos PROMO',
    '126': 'Ticket cliente de cuenta corriente',
    '127': 'M.Pago cuenta corriente',                  #          127
    '128': 'M.Pago Devolucion envases',

    '900': 'Declaración de cajera',
}

CABEZAL_HABILITADO = {
                '1': u'Venta/Ingreso',
                '3': u'Devolución',
                '6': u'Canje',
                '16': u'Nota de credito devolucion',
}

# no pasan a `tck_create`, deberán pasar a `admin` , etc
CABEZAL_NO_HABILITADO = {
               '2': u'Pedido (NO GENERADO)',
               '4': u'Estado de cuenta',
               '5': u'Exento IVA (NO GENERADO)',
               '7': u'Inventario',
               '8': u'Adm Cajera',
               '9': u'Ticket Gift (NO GENERADO)',
               '10': u'Pago Caja',
               '11': u'C.Factura',
               '12': u'12 No generado  (NO GENERADO)',
               '13': u'13 No generado  (NO GENERADO)',
               '14': u'Consulta',
               '15': u'Apertura de Gaveta',
               '17': u'Adm Fondeo',
               '18': u'Adm Retiro',
               '19': u'Adm Prestamo efectivo',
               '20': u'Adm Retiro de Productos',
               '21': u'Adm Ticket Z',
               '999': u'Ticket NO DEFINIDO',
}

TIPO_OPERACION = [
                  ('0', u'N/A'),
                  ('1', u'Venta'),
                  ('2', u'Cobranza'),
                  ('3', u'Devolución'),
                  ('4', u'Devol.Cobrza')
]

