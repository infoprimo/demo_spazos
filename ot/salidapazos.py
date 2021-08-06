#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ipt.lib_ipt import IPTicket
from jsonsqlite import SpazosTckJson, Salidapazos2Py

import sys
import os
import logging

__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2015-2017"

ns = os.path.basename(__file__).split('.')[0]

logger = logging.getLogger(__name__)
logging.info("%s" % (ns,))

needs = (3, 9)
pvi = sys.version_info.major, sys.version_info.minor


def parate():
    """
    Debuging: 
                Detien la ejecucuíón del script,
                pasa el control al debug interactivo `ipdb`
    """
    import ipdb
    return ipdb.set_trace


# parate()()


verbose = 0  # 0/1/2


def msgout(msg_=None):
    """
        Escribe l valor de `_msg` a la slaida estabdar
    """
    msg_ = msg_ or "\n\tAlgo salio mal... FIN\n"
    sys.stdout.write(msg_, )


def cargar_informe(informe, suf, suc, info_file=None, serializa=0):
    """
    Covierte la salida del csv a objetos python
    procesa un único informe  (una única jornada, los tickets del día completo)

    :param informe:  str:    es la salida del csv2py (diccionario python)
    :param suc: str          sucursal
    :param suf: str          Sujifo del archivo salidapazos .1234
    :param info_file:  str:  Nombre y path absoluto de un informe salidapazos4 (SM)
    :param serializa:  int   1 -> Serializar a json, 0 -> No serializar (default 0)

    :return:    el contenido del este informe convertido a objetos python

    import ipdb; ipdb.set_trace()
    """
    cabs = informe.keys()
    res = []
    for cabezal in cabs:

        if verbose == 1:
            print("--- comienza {} ".format(cabezal[2], )),
        if verbose == 2:
            print("\t\tcabezal tipo:{} caja:{} tck:{}  {}/{}".format(cabezal[0], cabezal[1], cabezal[2],
                                                                     cabezal[4][6:8], cabezal[4][4:6])),
        lineas = []

        for linea in informe[cabezal]:
            if verbose == 2:
                print("\n\t\tlin {}    tipo {}".format(linea[0], linea[1]))
            lineas.append(linea)

        if verbose == 1:
            print("  Instncia IPTicket..."),
            print("    %s --- ".format(suf, ))
        if verbose == 2:
            print("\t\t{}\n\t\t\t".format(lineas[-1:]))

        ticket_pazos = IPTicket(cabezal, lineas)
        res.append(ticket_pazos)
    if serializa:
        serial_spazos(res, suf, suc, info_file)  # TODO: verificar type(ticket_pazos.cabezal.cab) == <type dict>
    return res


def serial_spazos(informe, sufijo, sucurs, info_file):
    """

    :param informe:   todos las las instancias de IPTicket de una jornada.
    :param sufijo:    extensión del arcchivo salidapazos
    :param sucurs     SUCURSAL
    :param info_file: nombre del informe

    :return: lista de tuplas (s_cabezal, s_lineas) serializables en estructuras json (texto)
            s_cabezal: dict: datos del cabezal s_cabezal = {k: v, k1: v1, ...} `dict python`
            s_lineas:  list: lista de `dict`s análogos al diccionario cabezal
    """
    res = list()
    quedan = len(informe)
    if verbose:
        print(" Son %s tickets".format(quedan, )),
    quedan -= 1
    if verbose:
        print("{}".format(quedan + 1))
    for ticket_pazos in informe:  # parsea tickets
        if verbose == 1:
            print("Ticket: {}   N.Lineas:\t".format(ticket_pazos.cabezal.cab['numeroticket'], )),
        # parate()()
        del ticket_pazos.cabezal.cab['id_ticket']
        # TODO: verificar type(ticket_pazos.cabezal.cab) == <type dict>
        s_cabezal = ticket_pazos.cabezal.cab
        s_lineas = dict()
        for k, v in ticket_pazos.lineas.items():  # parsea líneas
            if verbose == 1:
                print("%s" % (k,)),
            lin = dict(tipo=v.llave, descripcion=v.descripcion, tstlinea=v.hhmmss)
            try:
                lin.update(v.datos)
            except Exception as er:
                print("tipo = {}  descripcion = {} ".format(v.llave, v.descripcion))
                print("{}".format(er))
                # import ipdb; ipdb.set_trace()
            s_lineas.update({k: lin})
        if verbose == 1:
            print("\n")
        quedan -= 1
        if verbose:
            print(" Fin tck: {}, {} lineas. Quedan: {} tcks del informe {} \n\n".format(s_cabezal['numeroticket'],
                                                                                        len(ticket_pazos.lineas),
                                                                                        quedan + 1, sufijo))
        if s_cabezal and s_lineas:
            res.append((s_cabezal, s_lineas))
    if verbose == 2:
        if pvi >= needs:
            input("Todos desmepaquetados. Serializar informe {}} ...<cualquiera para continuar>".format(sufijo, ))
        else:
            raw_input("Todos desmepaquetados. Serializar informe {}} ...<cualquiera para continuar>".format(sufijo, ))
        #  resgister_json_history_db(self, info_name, serializa=False, indentar=False)
    SpazosTckJson().resgister_json_history_db(info_file, res, sucurs)
    # TODO: ticket_pazos.cabezal.cab['sucursal'] = sucurs verificar en serialización
    # Salidapazos2Py.ajson(res, fecha, sufijo)
    return 1


def mainsp(sufijos=None):
    """
    :param sufijos: list: Lista de extenciones `sifijos` de informes disponibles.

    :return: list:        List de informes procesables
        

        `mainsp`: Ejemplo de uso del script "salidapazos.py"
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        La clase `SpazosTckJson`, importada del módulo `jsonsqlite`, gestiona una db sqlite para mantenimiento 
        del histórico de informes procesados. Se inicializa con valores por defecto leídos de la configuración::

            db_path=dbpath, tablename=tablename, force=False

        La insancia de `stj = SpazosTckJson(sufijos)`, expondrá el método `spazos_candidatos`. Este extrae una 
        lista de informes no registrados desde cierto 'path'. Los nombre de informes son del tipo:

            Salidapazosnuevo-1-AAAAMMDD.sufijo -> "Salidapazosnuevo-1-20210729.9876"

        El parámetro `sufijos`, es una lista de sufijos (int) de informes ya procesados y es usada con el 
        propósito de restringir la cantidad de informes a considerar. Una lista vacía como parámetro de la 
        instancia verificará todos los informes disponibles en el 'path'.
                
            informes = SpazosTckJson(list())

            infofiles = stj.spazos_candidatos()

        Luego, cada candidato levantado del filesystem se será llevado a objetos python. Estos objetos podrán ser
        serializados a `json` o directamente pasados a otra aplicación. Como especificación de una eventual "api" 
        puede considerarse la versión 1.6.67 del documento “Salida estándar CSTVIEW para Pazos4 y Supermercado.”

    """
    res = list()

    stj = SpazosTckJson(sufijos)
    if not stj.Ok:
        return {}
    stj.refresh_db()  # TODO: eliminar!
    infofiles = stj.spazos_candidatos()

    if not infofiles:
        msg = " %s" % ('No hay informes sin procesar!\n',)
        if verbose:
            msgout(msg)
        logger.warn(msg)
        return {}

    for i in infofiles:
        if verbose:
            print("{}".format(os.path.basename(i), ))

        spazos = Salidapazos2Py(i)  # csv -> py
        if not spazos:
            return {}

        fecha, sucursal, sufijo = spazos.check()
        informe = spazos.csv2py()
        ip_tickets = cargar_informe(informe, sufijo, sucursal, i, serializa=0)  # py -> libtck

        [ipt.cabezal.zip.update(dict(sucursal=sucursal)) for ipt in ip_tickets]

        for ipt in ip_tickets:
            ipt.cabezal.sucursal = sucursal
        res.append((sufijo, fecha, sucursal, ip_tickets))

    return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
