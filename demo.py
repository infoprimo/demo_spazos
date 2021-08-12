# coding=utf-8

from ot import salidapazos
from os.path import basename
from ot.conf import config as cfg
import logging

__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2015-2021"

ns = basename(__file__).split('.')[0]
logger = logging.getLogger(ns)

Error = cfg.Error

def parate():
    """
        Debuging: usa el módulo `ipdb`, debug paso a paso, etc.

            # pip install ipdb

        Uso:

            >>> parate()()

    :return:  Detiene la ejecución y ofrece un prompt pra debug
    """
    try:
        import ipdb
        return ipdb.set_trace
    except Error as err:
        print("\n\t ERROR: Es posible el módulo `ipdb` no esté instalado\n\t".format(err,))



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

    @staticmethod
    def ok(kch):
        """
        tl:dr
            Por diseño del lenguaje, Python pasa siempre la instancia de clase a los métodos.
            El decorador @sataicmethod evita este gasto inutil en aquellos métodos que no
            utilizan la instancia de clase en su implmentación.

            Este tipo de métodos podrán usarse incluso sin siquiera haber creado una
            instancia de clase.   contador = Clase.metodo('spam_eggs')

            En el caso, el método `Res` simplemente verifica que el argumento recibido recibe esté
            dentro de un rango específico de la tabla de caracteres del sistema. No necesita ninguno
            de los métodos o valores contenidos en la instancia, por tanto no la necesita.

            En varios paises, tal vez en la mayoría, el Estado podría tomar este tip, y ahorrar sin
            ser neoliberal!

        :param kch:
        :return:
        """
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


def repazos_csv(jornadas, dia=None):
    """
        <br />
        :param   instancia:  jornadas:  instancia de jornadas leídas en a demo es `informes`
        :param   str:        dia:       texto (entre comillas) 'yyyyMMdd' fecha del informe de salida
        :return: bool:       True:      un informe `Salidapazosnuevo` o
                             False:     nada
    """

    # verificación mínimma del parámetro día
    if not dia or len(dia) != 10:
        print("\n\tuso: >>> repazos_csv('2021-07-08')\n")
        return False

    # seleccionar el día requerido
    tcks_del_dia = jornadas['lote'][dia]['tickets_pazos']

    # una string para nuestra salida
    info_csv = ''


    # `kernel` de la función
    for t in tcks_del_dia:
        info_csv += ''.join(t.cabezal.rlinea + '\n')
        for l in t.lineas:
            info_csv += ''.join(t.lineas[l].rlinea + '\n')

    # cómo la queré, Toto?
    op = raw_input("\n\t <pantalla> o <a>rchivo p/v?")
    if op in ('p', 'P'):

        print("{} \n\t -*-\n".format(info_csv))

    elif op in ('a', 'A'):

        fpath = "/tmp/ip_Salidapazonievo-1-{}.csv".format(dia,)
        with open(fpath, "w") as f:
            f.write(info_csv)

    else:
        return False

    return True

        
if __name__ == '__main__':

    print("\n\t Los informes leídos están el diccionario «informes»")
    print("\n\t Hay también una función definida: \n"
          "\n\t\t uso:  »»» repazos_csv('jornada, 2021-07-08')")
    print("\n\t que reconstruir el/los informes leídos, "
          "\n\t mostralos por pantalla o guardarlo en /tmp/..."
          "\n\t respetando la misma estructura de los originales\n\n\t\t\t\t-*-\n")
    informes = main()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
