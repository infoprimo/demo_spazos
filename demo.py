# coding=utf-8

from ot import salidapazos
from os.path import basename
import logging

ns = basename(__file__).split('.')[0]
logger = logging.getLogger(ns)


def parate():
    """
        Debuging: usa el módulo `ipdb` debug paso a paso, etc.

            >>> pip install ipdb
        o
            >>> apt install python ipdb

        Uso:
            >>> parate()()

        detiene la ejecución y ofrece un prompt similar al del intérprete python

    """
    import ipdb
    return ipdb.set_trace


__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2015-2021"


class Res(object):
    """

    Generate diccionary of counters
    +++++++++++++++++++++++++++++++

    Un diccionario de contadores de propósito general
    -------------------------------------------------

     `counter` is the dict key in default instance
     Start value = 0
     k[ey] is a string from any set of `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`

     Res(k) => d[k] = 0
     Res(k,x,z, ... ) => d[k] = 0, d[x] = 0, d[z] = 0, ...

         >>> zombie = Res()              # instance
         >>> zombie.add()                # add 1 to default key `counter`
         >>> zombie.add(9)               # add 9 to `counter`
         >>> zombie.less(4)              # now substract 4 to `counter`
         >>> zombie['counter']           # prints 6 - the `counter` actual value
         >>> zombie.addkey('sheeps')     # define a brand new key `sheeps`
         >>> zombie.showkeys()           # prints ['counter', 'sheeps' ]
         >>> zombie.flush()              # will reset instance to defaults

    """

    def __init__(self, *args):
        self.result = dict()
        if not args:
            self.result = dict(counter=float(0.0))
        else:
            for key in args:
                if self._ok(key):
                    self.result[key] = float(0.0)

    def __setitem__(self, key, value):
        self.result[key] += value

    def __getitem__(self, key):
        return self.result[key]

    def add(self, key, value=float(1.0)):
        """
        @return:    If no value -> ttl['key'] +=1 otherwise ttl['key'] += value
        """
        self.__setitem__(key, value)

    def less(self, key, value=float(1.0)):
        """
        @return:    If no value -> ttl['key'] -=1 otherwise ttl['key'] += value
        """
        value *= -1
        self.__setitem__(key, float(value))

    def addkey(self, *args):
        """
        @ strings keys no digits
        """
        for key in args:
            if self._ok(key):
                self.result[key] = float(0.0)

    def _ok(self, kch):
        for ch in kch:
            if not (65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122):
                return False
        return True

    def ret(self, key):
        """
        @return:    ttl.res['key'] -> value
        """
        self.__getitem__(key)

    def showkeys(self):
        """
        @return:    ttl.showkeys() -> all availables keys
        """
        return self.result.keys()

    def show(self):
        """
        @return:    all keys, values pairs
        """
        return self.result

    def flush(self):
        for i in self:
            del i
        self.result = dict()
        self.result = dict(counter=float(0.0))


def main():
    """
        Una demo decuso de la biblioteca `salidapazos`
        ''''''''''''''''''''''''''''''''''''''''''''''

        Retorna una diccionario cuyos miembros serán, a su vez, sendos diccionarios
            >>>
            >>> lote = {}
            >>> jornadas = {}
            >>> parate()()
            >>> info = salidapazos.mainsp()
            >>> for r in info:
            >>>     lote.update({r[1]: dict(suf=r[0], suc=r[2], ptcks=r[3])})
            >>>     jornadas.update({r[1]: r[3]})
            >>> return dict(lote=lote, jornadas=jornadas)

        Como se usa:

            $ ipython
            >>> import pazos2pytck
            >>> demo = pazos2pytck.main()
            >>> demo.keys()
            >>> [lote, jornadas]

        Tanto `lote` como `jarnadas` son diccionarios. Ambos de contenido similar,
        contienen el conjunto de informes de "SalidaPazos" disponibles para lectura.
        El `path` de los archivos de inormes está definido en la configuración:

            ./demo/ot/conf/config.py

        `lote` es un diccionario de la forma:

            lote = dict( fecha = sufijo, sucursal, tickets_pazos )

        Donde  `fecha`         : dd-MM-aaaa : fecha del informe
               `sufijo`        : NNNN...    : enteros del sufijo
               `sucursal`      : NNN...     : enteros de sucursal
               `tickets_pazos` : lista de instancias de cada ticket pazos
                                 (todos los tickets de una fecha/sufijo)

        En tanto `jornadas` es un diccionario definido por simplicidad a efectos
        de ésta demo, siendo de la forma:

            jornada = dict( fecha = tickets_pazos`)

                `fecha`         : dd-MM-aaaa : fecha del informe
                `tickets_pazos` : lista de instancias de cada ticket pazos

        La biblioteca “salidapazos” también puede:

            - serializar a un archivo json,
            - mantener un histórico de informes procesados.

            >>> from ot import jsonsqlite
            >>> help(jsonsqlite)

        con suerte y viento favor algo le va a mostrar
        """

    lote = {}
    jornadas = {}

    info = salidapazos.mainsp()
    for r in info:
        lote.update({r[1]: dict(sufijo=r[0], sucursal=r[2], tickets_pazos=r[3])})
        jornadas.update({r[1]: r[3]})
    return dict(lote=lote, jornadas=jornadas)


if __name__ == '__main__':

    tck = main()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
