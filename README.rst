Demo para biblioteca salidapasos
--------------------------------

|

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
        
 En el prompt del intérprete python quedará disponible un diccionario `tcks` de dos llaves. Cada una de éstas dará acceso a colecciones de objetos muy similares.


        >>> tcks.keys()
        ['jornadas', 'lote'] (1)
        
        
 La llave 'jornadas' da acceso a un diccionario cuyas claves de acceso se corresponden a un jornada de operaciones, allí se podrá acceder a todos los tickets de dicha jornada :

        >>> tcks['jornadas'].keys()
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
         
 Los tickts de una jornada pueden ser accedidos así:

        >>> tcks['jornadas']['2021-07-01']
        [Ticket1,
         Ticket2, 
         TicketN]

          
 Donde "Ticket1", Ticket2, etc diferentes tickets del informe correspondiente al día 2021-07-01.
 Esta es la sintaxis para acceder al primer elemento de la list:

        >>> tcks['jornadas']['2021-07-01'][0]

 A efectos de simplificar se puede cargar el objeto en una variable:

        >>> tck1 = tcks['jornadas']['2021-07-01'][0]
        
 `tck1` es el objeto python correspondiente un ticket. Sus atributos son directamente accesibles.
 
 Los atributos de tck1 ``cabezal`` y ``lineas`` son objetos directamente accesibles y dan acceso respectivamente al las lineas de cabezal y a las líneas de detalle según la **Especificación de la Salida de Pazos**.

        >>> tck1.cabezal.numero_tck
        00123456
        
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
        
Estos son algunos de los atributos de ``cabezal``

        ``tck1.cabezal.cantidadarticulos, tck1.cabezal.cantidadlineas, tck1.cabezal.cantidadlineas, tck1.cabezal.codigocaja, tck1.cabezal.codigocajera, tck1.cabezal.descripcion, tck1.cabezal.estado, tck1.cabezal.estadoticket, tck1.cabezal.fecha, tck1.cabezal.numeroticket, tck1.cabezal.sucursal, tck1.cabezal.tipocabezal``

En particular, uno de los atributos es un diccionarios que contiene todo los datos del cabezal

        >>> tck1.cabezal.zip
    
                
Por su parte ``lineas`` es un diccionario de objetos. Cada una de sus llaves de acceso es el número de línea.
        
        >>> lin1 = tck.lineas[1]
        >>> lin1.rlinea
        L#1#5#114623#101#e-Ticket#B#0685310#0####
        >>> lin.tipolinea
        '5'
        >>> lin1.descripcion
        'Cabezal de CFE'
        >>> lin1.datos
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
        
:wq
                  
        
          
        


