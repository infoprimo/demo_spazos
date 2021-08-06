#!/usr/bin/env python
# -*- coding: utf-8 -*-

__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2015-2017"
__descrip__ = "Verifica si hay informes Salidapazos sin procesar. Elabora lista de candidatos y eventualmente " \
              "ejecuta el mantenimiento de históticos de archivos `tckAAAAMMDD.json` procesados " \
              "que a su vez, tomará en cuenta en la siguiente verificación de informes."

#import ipdb     # TODO: ipdb
import sys
import os.path
import subprocess
import csv
import sqlite3
import re
import simplejson as json
import datetime
from glob import glob

import os
import logging
from conf import config as cfg
logger = logging.getLogger(__name__)

verbose = 0


def end(msg=None, warn=0):
    if cfg.DEBUG:
        logger.debug("%s" % (msg,))
        msg = msg or "\t Algo salió muy mal... "
        logger.error(msg)
        return False
    else:
        if msg and len(msg):
            logger.error(msg)
            return False


def run(command):
    output = subprocess.check_output(command, shell=True)
    return output



class SpazosTckJson(object):
    """
    Expone dos métodos:

    """

    def __init__(self, sufijos=None, force=False):
        """
        :param force: True creará nueva db vacía.
        """
        self.sufijos = sufijos
        self.Ok = False
        if not cfg:
            self.config = end("Imposible leer las configuraciones")
        else:
            self.config = cfg
            self.iPrefijo = cfg.iPrefijo

        if not os.path.isdir(cfg.inputPath):
            self.iPath = end("No existe el directorio de entrada")
        else:
            self.iPath = cfg.inputPath

        if not os.path.isdir(cfg.outputPath):
            self.oPath = end("No existe el directorio de salida")
        else:
            self.oPath = cfg.outputPath

        if not len(cfg.tableName):
            self.table_name = end("Falta el nombre de la tabla para el histórico.")
        else:
            self.table_name = cfg.tableName

        if not len(cfg.dbName):
            self.db_name = end("No se puede iniciar la base de datos!! "
                               "Verificar la configuración en %s " % ("conf.dbName",))
        else:
            self.db_name = cfg.dbName
            self.db_path = cfg.outputPath + cfg.dbName

            if force:
                db_con = sqlite3.connect(self.db_path)
                db_con.close()
                self._install()

        if self.config and self.iPath and self.oPath and self.table_name and self.db_name:
            self.Ok = 1


    def _conn(self):
        """
            Conexión a la db
            :return:        una concexión sqlite3
        """
        try:
            res = sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
                                  isolation_level=None)
            if not res:
                return end("No hay conexión a la db")
        except Exception as err:
            return end("Imposible conectar a %s, %s." % (self.db_path, err))
        return res


    def _closedb(self, cr, db):

        try:
            if cr: cr.close()
            if db: db.close()
        except Exception as err:
            return end('%s No se pudo cerrar la db.' % (err,))
        return True

    def _install(self):
        """
            Crear db sqlite3 en `db_path`
            :return:
        """
        init = '''CREATE TABLE if not exists spazosjson(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        origen TEXT NOT NULL, cod_inifin TEXT NOT NULL UNIQUE, fecha_opera DATE NOT NULL, fecha_lectura DATE NOT
        NULL, destino TEXT NOT NULL); '''

        db = self._conn()
        cr = db.cursor()
        try:
            cr.execute(init)
            self._closedb(cr, db)
        except sqlite3.Error as err:
            return end("%s No se pudo crear la db." % (err,))
        return True

    def _test_table(self):
        """
            Verifica existencia db y tabla necesarias.
            :return: True o exit con aviso
        """
        res = False
        sql = """SELECT 1 FROM sqlite_master WHERE type='table' AND name='%s';""" % (self.table_name,)
        db = self._conn()
        cr = db.cursor()
        try:
            cr.execute(sql)
            test = cr.fetchone()
            cr.close()
            if not (isinstance(test, tuple) and test[0] == self.table_name):
                self._install()
            res = True
        except sqlite3.Error as e:
            self._closedb(cr, db)
            msg = '%s No existe %s. Fallo al intentar crear la tabla.\n' % (e, self.table_name)
            msg += "Error de Base de Datos: %s" % (e,)
            return end(msg)
        except Exception as e:
            self._closedb(cr, db)
            msg = '%s No existe %s. Fallo al intentar crear la tabla.\n' % (e, self.table_name)
            msg += "Error en `_test_table` '%s'" % (e,)       # FEO
            return end(msg)

        return res

    def refresh_db(self):

        db = self._conn()
        cr = db.cursor()
        try:
            cr.execute("""CREATE TABLE if not exists spazosbak(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            origen TEXT NOT NULL, cod_inifin TEXT NOT NULL UNIQUE, fecha_opera DATE NOT NULL, fecha_lectura DATE NOT
            NULL, destino TEXT NOT NULL);""")
            cr.execute("insert into spazosbak select * from spazosjson;")
            cr.execute("delete from spazosjson;")
            return True
        except sqlite3.Error as e:
            self._closedb(cr, db)
            return end("Error de Base de Datos: %s" % (e,))
        except Exception as e:
            self._closedb(cr, db)
            return end("Error en `_refresh_db` '%s'" % (e,))

    def _pick_input(self):
        """
        Lee el contenido del directorio de salidapazos
        verifica sufijo numérico del nombre de archivo/informe
        Retorna un diccionario de archivos disponibles = { sufijo0: archivo0, sifijo1, archivo1, ...}

        self.iPath              : path al directorio de informes  "[....]/informes/"
        self.conf.iPrefijo    : prefijo de nombres de archivo de los informes "Salidapazosnuevo-1-20*"

        :return: dict:      Archivos disponibles en el directorio de informes
        """
        sufijos = []
        if self.sufijos:
            sufijos = self.sufijos
        disponibles = dict()
        if not cfg.iPrefijo:
            return end("Falta el prefijo. Verivicar configuraciones")

        digitos = re.compile('[0-9]{3,4}$')  # patron 3 o 4 dígitos
        reload(cfg)   # TODO quitar (verificar si cambió la comfiguración, 
                      #              permite cambiar la configuración 
                      #              sin reiniciar el servidor)
                                        
        files = glob(self.iPath + cfg.iPrefijo)
        for f in files:
            fext = os.path.splitext(f)[1][1:]
            if digitos.match(fext) and fext not in sufijos:
                disponibles.update({fext: f})
        if not len(disponibles):
            return end(" \n\tNo hay informes en: \n\t%s." % (self.iPath,))
        return disponibles

    def spazos_candidatos(self):
        """
        Filtra la lista de informes disponibles contra el historial de informes procesados.
        retornando la lista de aquellos que no encuentra en el historial.
        Tabla `salidapazos`:

             id, origen, cod_inifin, fecha_opera, fecha_lectura, destino
                         ^^^^^^^^^^

        :return:         lista con nombre de archivos (path absoluto) candidatos a procesar.
        """
        res = historia = []
        self._test_table()
        # se lee la carpeta de informes disponibles.
        candidatos = self._pick_input()
        if not candidatos or not len(candidatos):
            return end("No hay informes salidapazos por procesar en %s" % (self.iPath,))
        db = self._conn()
        cr = db.cursor()
        try:
            # sufijos del histórico
            cr.execute('''SELECT cod_inifin FROM spazosjson ORDER BY id;''')
            historia = cr.fetchall()
            self._closedb(cr, db)
        except sqlite3.Error as e:
            self._closedb(cr, db)
            return end("Error de Base de Datos: %s" % (e,))
        except Exception as e:
            self._closedb(cr, db)
            return end("Error en `_refresh_db` '%s'" % (e,))

        # los candidatos serán filtrados según el sujifo secuencial de los informes pazos
        sufijo_historia = [int(i[0].encode('utf-8')) for i in historia]
        # for k, v in candidatos.items() if k not in sufijo_historia]
        # print("candidatos..."),
        for k, v in candidatos.items():
            if int(k) not in sufijo_historia:
                res.append(v)
            #print("."),
            #res.append(v)  # TODO: este append saltea el filtro !!!

        if not len(res):
            print("No hay informes por procesar!")
        res.sort()
        return res

    def resgister_json_history_db(self, info_name, sucursal, serializa=False, indentar=False):
        """
            Crea el registo para el historial/control en la db.
            Si el parámetro 'serializa' está presente, escribe el jsonfile en archivo en el
            path establecido en la configuración.
            El nombre del info_namerme al final del absoluto `jsonfile` deberá mantener el
            formato original "Salidapazos-S-aaaaMMdd.sufijo"

            :param info_name:       path absoluto del info_namerme pazos
            :param sucursal:        sucursal
            :param serializa:       tickets del info_namerme para escribir `jsonfile` al filesystem (opcional)
            :param indentar:        más simpático pero más grande  (opcional, solo si exite `serializa`)
            :return:
        """
        verbose = 0
        if not len(info_name):
            return end("faltan parámetros para `resgister_json_history_db`")
        base_name = os.path.basename(info_name)

        nsp, suc, fs = os.path.basename(info_name).split('-')
        fecha, sufijo = fs.split('.')
        f_opera = datetime.date(int(fecha[:4]), int(fecha[4:6]), int(fecha[6:])).isoformat()
        f_lectura = datetime.datetime.now().isoformat()
        json_file = "%stck%s-%s-%s.json" % (cfg.outputPath, fecha, sucursal, sufijo)
        jfile = os.path.basename(json_file)
        sql = "INSERT INTO spazosjson(origen,cod_inifin,fecha_opera,fecha_lectura,destino) VALUES("
        sql += "'%s','%s','%s','%s','%s');" % (info_name, sufijo, f_opera, f_lectura, json_file)
        db = self._conn()
        cr = db.cursor()
        try:
            cr.execute(sql)
            self._closedb(cr, db)
        except sqlite3.IntegrityError as e:
            self._closedb(cr, db)
            if verbose: print("\t '%s' ya estaba registrado! No se procesa." % (base_name,))
            if serializa:
                if verbose: print("\t '%s' No se escribirá." % (jfile,))
            # serializa = 0

        except Exception as err:
            self._closedb(cr, db)
            msg = " <%s>\n\t Falla al registrar histórico de procesos." % (err,)       # FEO
            msg += "\t '%s' deberá ser procesado nuevamente.\n" % (base_name,)
            if serializa:
                msg += "\t '%s' No se escribió." % (jfile,)
            return end(msg)
            # serializa = 0
        if serializa:
            try:
                with open(json_file, 'w') as fp:
                    if indentar:
                        json.dump(serializa, fp, separators=cfg.separadores, indent=cfg.indenta)
                    else:
                        json.dump(serializa, fp)
            except Exception as escritura:
                msg = (" %s Imposible escribir el informe, verificar permisos." % (escritura,))
                msg += ("\t\t '%s' No se escibió .\n" % (jfile,))           # FEO
                return end(msg)
        return True


class Salidapazos2Py(object):
    """
            CSV 2 Python dict y check
    """
    def __init__(self, salidapazos, serializa=0):
        """

        :param salidapazos:
        """
        if not os.path.isfile(salidapazos):
            msg = "El informe pazos no existe o no es accesible."
            self.res = end(msg)
        self.salidapazos = salidapazos

    def check(self):
        """
            Verificar fecha de los datos de un informe
            Parsea la primera línea del informe candidato.
            si bien el nombre del archivo representa a un fecha, su contenido puede
            corresponder a una `jornada` diferente.
            Salidapazosnuevo-S-AAAAMMDD.nnnn
            S = Sucursal; AAAAMMDD = fecha; nnnn = sifijo

            Obtiene la primera línea del informe candidato.
            si bien el nombre del archivo representa a un fecha, su contenido puede
            ejemplo fecha 1era transacción del informe:
            C#8#1#87#8#20151231080308#F#0#0.00#20#8
                      |_______|
                      20151231 ->  2015-12-31
        se chequea contra la AAAAMMDD del nombre de archivo informe

        :return:   tupla: una fecha, sucursal, sufijo
        """
        head = run("head -1 %s" % self.salidapazos)
        head = head.strip('\n')
        ind = has = 0
        while has < 5:
            if head[ind] == '#':
                has += 1
            ind += 1
        _da = head[ind:ind + 8]
        fecha_transac = "%s-%s-%s" % (_da[0:4], _da[4:6], _da[6:8])
        fname, sufijo = os.path.splitext(os.path.basename(self.salidapazos))
        sufijo = sufijo[1:]
        sucursal = fname[17]
        _fe = fname[19:19+8]
        fecha = "%s-%s-%s" % (_fe[0:4], _fe[4:6], _fe[6:8])
        if fecha_transac != fecha:
            return end("La fecha del informe '%s' y la de sus transacciones no coincide." % (fname + '.' + sufijo,))
        return fecha, sucursal, sufijo

    def csv2py(self):
        """
            ::PROCESA UN UNICO INFORME::
            ============================
            retorna: diccionario:
                    { cabezal_tck0: linea_tck_pazos0, cabezal_tck1: linea_tck_pazos1, ... }
            Ejemplo:

            Dada la línea de cabezal: C#1#2#350#2#20151121105326#F#4#183.40#20#13
            Cabezal_Tck1 = ('1', '2', '350', '2', '20151121105326', 'F', '4', '183.40', '20', '13')

            Dada la línea de detalle: L#4#53#120435#TICKET DE VENTA#0
            LinTckN_2 = ('4', '53', '120435', 'TICKET DE VENTA', '0')

            En ambos casos se omite el identificador de línea,  "C" o "L"

        L#7#126#132849#3656#USTRA NORMA (Z)#162.00
        """
        salidapazos = self.salidapazos or None    #
        if not salidapazos:
            return end("\n\n\t\t   Verificar ingreso ... %s" % ('\n\n',))
        key = None
        informe = dict()
        info_line = 0

        with open(salidapazos, 'r') as f:
            reader = csv.reader(f, delimiter='#')
            for row in reader:
                info_line += 1              # sólo para sber dónde se corta, si es que se corta.
                if not len(row):
                    msg = ' %s La línea está vacía.' % (__name__,)
                    logger.warn(msg)
                    sys.stdout.write("\n\t%s\n\n" % (msg,))
                    continue
                if row[0] == 'C':
                    key = tuple(row[1:])    # llave = línea de cabezal sin el primer caracter, o sea sin la "C"
                    informe[key] = []
                elif row[0] == 'L':
                    informe[key].append(tuple(row[1:]))  # valores = líneas de detalle de ticket sin la "L"
                else:
                    msg = "\n\tEl infome salidapazos puede contener erores" \
                          "\t\tNo se generaron los informes. Verificar contenido de " \
                          "%s, linea_de_cabezal %s" % (salidapazos, info_line)
                    return end(msg)
        if not informe:
            msg = " Ocurrió un error al leer informe. "
            msg += "Verificar %s. No se generó el archivo .json" % (salidapazos,)
            return end(msg)

        return informe     # { tupla:: cabezal_tck0: lista de tuplas:: linea_tck_pazos0, ... }


    @staticmethod
    def ajson(tcks_del_dia, fecha, sucursal, sufijo):

        # #### 5.  serializa python to json y escribe el json file
        json_file = "%stck%s-%s-%s.json" % (cfg.outputPath, fecha, sucursal, sufijo)
        try:
            with open(json_file, 'w') as fp:
                json.dump(tcks_del_dia, fp, separators=(',', ': '), indent=3)

        except Exception as escritura:
            logger.error(" %s Imposible escribir el informe ln 389" % (escritura,))

    """
if '__main__' == __name__:

    import ipdb;ipdb.set_trace()

    db_obj = SpazosTckJson()
    db_obj._test_table()
    db = db_obj._conn()
    cr = db.cursor()
    cr.execute('''SELECT origen,cod_inifin,fecha_opera,destino FROM spazosjson''')
    rows = cr.fetchall()
    db_obj._closedb(cr, db)
    if rows:
        for row in rows:
            print row
    else:
        print 'no hay nada!'

    if len(rows) >= 1825:
        db_obj._refresh_db()
"""

