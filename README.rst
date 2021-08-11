---------------------------
Demo para biblioteca Python
---------------------------
procesa informes específicos de salida de una aplicaicón específica :/
----------------------------------------------------------------------
 


**Requerimentos python**

  ``logging``
  
  ``simplejson``

  ``sqlite3``

  ``ipdb``  `(opcional)`

|

**Empezando con la demo**:

En una carpeta ejecutar:

        ``$ wget`` `https://github.com/infoprimo/demo_spazos/archive/refs/heads/main.zip <https://github.com/infoprimo/demo_spazos/archive/refs/heads/main.zip>`_

        ``$ unzip main.zip``

        ``$ cd demo_spazos``

        ``$ ipython -i demo.py``
        
En el prompt del intérprete python quedará disponible un diccionario `informes` con dos llaves de acceso. Cada una de éstas da acceso a colecciones de objetos similares.


        >>> informes.keys()
        ['jornadas', 'lote'] 
        
        
A través de la llave 'jornadas' se accede a un diccionario. Las llaves de acceso en éste se corresponden a las jornadas de operaciones de los informes leídos. 
Vemos los elementos de `jornadas`:

        >>> informes['jornadas'].keys()
        [2021-07-10,
         2021-07-08,
         2021-07-09,
         2021-07-04,
         2021-07-05,
         2021-07-06,
         2021-07-07,
         2021-07-01,
         2021-07-02,
         2021-07-03]
         
La colección de tickts de una jornada específica:

        >>> informes['jornadas']['2021-07-01']
        [Ticket1,
         Ticket2,
         ... 
         TicketN]

          
Donde "Ticket1", Ticket2, etc son los tickets del informe correspondiente al día 2021-07-01.
Esta es la sintaxis para acceder al primer elemento de la list:

        >>> informes['jornadas']['2021-07-01'][0]

A efectos de simplificar se puede cargar el objeto en una variable:

        >>> tck1 = informes['jornadas']['2021-07-01'][0]
        
`tck1` es el objeto python correspondiente un ticket.
 
Los atributos de tck1 ``cabezal`` y ``lineas`` son objetos directamente accesibles. A su vez 
dan acceso respectivamente al las lineas de cabezal y a las líneas de detalle según la 
**Especificación de la Salida de Pazos**.

Se accede al número de tícket de cabezal.

        >>> tck1.cabezal.numero_tck
        00123456

o a todos en un único diccionario en el atributo especial ``zip``
        
        >>> tck1.cabezal.zip       
        cantidadarticulos: '25',
        cantidadlineas: '30',
        codigocaja: '001',
        codigocajera: '10',
        date: '20210701',
        descripcion: 'Ticket Venta/Ingreso',
        estadoticket: 'F',
        fecha: '2021-07-01',
        numeroticket: '292197',
        sucursal: '1',
        timestamp_tck: '2021-07-01 11:46:23',
        timestampticket: '20210701114623',
        tipocabezal: '1',
        tipocliente: '20',
        totalapagar: '1593.04'
        
Es posible acceder directamente a cada uno de los atributos de cabezal::

              tck1.cabezal.cantidadarticulos        
              tck1.cabezal.cantidadlineas           
              tck1.cabezal.codigocaja               
              tck1.cabezal.codigocajera             
              tck1.cabezal.date                     
              tck1.cabezal.descripcion              
              tck1.cabezal.estadoticket             
              tck1.cabezal.fecha                    
              tck1.cabezal.numeroticket             
              tck1.cabezal.sucursal                 
              tck1.cabezal.timestamp_tck            
              tck1.cabezal.timestampticket          
              tck1.cabezal.sucursal                 
              tck1.cabezal.tipocabezal              
              tck1.cabezal.totalapagar              
                            
Por su parte ``lineas`` es un diccionario de objetos. Cada una de sus llaves de acceso 
es su número de línea de detalle en el ticket.

        >>> tck1 = informes['jornadas']['2021-07-01'][0]  #  *secuencial*
        >>> lin1 = tck1.lineas[1]												  #  *número de línea*

        >>> lin1.tipolinea
        '5'
        
        >>> lin1.descripcion
        'Cabezal de CFE'
        
        >>> lin1.datos																		# análogo a ``zip`` en el cabezal
        ciudadreceptor': ''
        descripcioncfe': 'e-Ticket'
        direccionreceptor': ''
        documentoreceptor': ''
        name': '2021070111462300100292197-5-1'
        nombrereceptor': ''
        numerocfe': '0685310'
        seriecfe': 'B'
        tipocfe': '101'
        tipodocumentoreceptor': '0'
        
Un método especial disponible en lineas de cabezal o de detalle:

				>>> tck1.cabezal.rlinea
				'C#1#1#292197#10#20210701114623#F#25#1593.04#20#30'
				
				>>> lin1.rlinea
        'L#1#5#114623#101#e-Ticket#B#0685310#0####'				

La demo contiene una función pre definida.::

        »»» repazos_csv(dia)

donde `dia` es una string de la forma: *'yyyy-MM-dd'*.
 
Haciendo uso de los métodos `rlinea`, la función reconstruye el informe original completo 
correspondiente a esa fecha o cualquier parte del mismo, sea un cabezal, una línea, 
como se vió más arriba, uno o varios tickets en particular, etc.

::

	for t in tcks_del_dia:                                         
      info_csv += ''.join(t.cabezal.rlinea + '\n')               
      for l in t.lineas:                                         
          info_csv += ''.join(t.lineas[l].rlinea + '\n')         
	

 info_csv contiene una string con un informe compelo Salidapazosnuevo*


En esta demo la función recontruye el informe completo, pudiéndo optar por mostrarlo en pantalla o escribir 
su contenido en un archivo. Esta facilidad es básicamente de uso en debug. 
        
        
----


|


``Errores, ideas, dudas`` ver_

.. _ver: https://github.com/infoprimo/demo_spazos/issues/new/choose
