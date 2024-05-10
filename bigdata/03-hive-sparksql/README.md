# Universidad EAFIT
# Curso ST0263 Tópicos Especiales en Telemática, 2024-1

# HIVE y SparkSQL, GESTIÓN DE DATOS VIA SQL:

# 1. Infraestructura para el lab4:

## Conexión al cluster Hadoop via HUE en Amazon EMR

Hue Web (cada uno tiene su propio cluster EMR)

    http://ec2.compute-1.amazonaws.com:8888
    

Usuarios: (entrar como hadoop/********* y crear cada uno su usuario)

    username: hadoop
    password: ********
  
### Los archivos de trabajo hdi-data.csv y export-data.csv
# si va a trabajar con hdfs, recuerde que estos datos hay que copiarlos temporalmente al cluster AWS EMR, porque no son persistentes.

```
/user/hadoop/datasets/onu/hdi
```

## 2. Gestión (DDL) y Consultas (DQL)

### Crear la tabla HDI en HDFS/beeline:

    # tabla manejada por hive: /user/hive/warehouse
    $ beeline 
    use usernamedb;
    CREATE TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    STORED AS TEXTFILE

    # OPCIONES PARA cargar datos a la tabla asi:
    # OPCIÓN 1:
    # copiando datos directamente hacia hdfs:///user/hive/warehouse/usernamedb.db/hdi/

    $ hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi-data.csv hdfs:///user/hive/warehouse/usernamedb.db/hdi

    # OPCIÓN 2:
    # cargardo datos desde hive:

    ## darle primero permisos completos al directorio:
    $ hdfs dfs -chmod -R 777 /user/hadoop/datasets/onu/
    $ beeline
    0: jdbc:hive2://sandbox-hdp.hortonworks.com:2> LOAD DATA INPATH '/user/hadoop/datasets/onu/hdi-data.csv' INTO TABLE HDI

    # tabla externa en hdfs: 
    use usernamedb;
    CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION '/user/hadoop/datasets/onu/hdi/'

### Crear la tabla HDI en EMR/S3/Hue/Hive:

    # tabla externa en S3: 
    use usernamedb;
    CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION 's3://st0263datasets/onu/hdi/'


### hacer consultas y cálculos sobre la tabla HDI:

    use usernamedb;
    show tables;
    describe hdi;

    select * from hdi;

    select country, gni from hdi where gni > 2000;    


    ### EJECUTAR UN JOIN CON HIVE:

    ### Obtener los datos base: export-data.csv

    usar los datos en 'datasets' de este repositorio.

    ### Iniciar hive y crear la tabla EXPO:

    use usernamedb;
    CREATE EXTERNAL TABLE EXPO (country STRING, expct FLOAT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION 's3://st0263datasets/onu/export/'

    ### EJECUTAR EL JOIN DE 2 TABLAS:

    SELECT h.country, gni, expct FROM HDI h JOIN EXPO e ON (h.country = e.country) WHERE gni > 2000;

## . WORDCOUNT EN HIVE:

    --- alternativa1:
    use usernamedb;
    CREATE EXTERNAL TABLE docs (line STRING) 
    STORED AS TEXTFILE 
    LOCATION 'hdfs://localhost/user/hadoop/datasets/gutenberg-small/';

    --- alternativa2:
    CREATE EXTERNAL TABLE docs (line STRING) 
    STORED AS TEXTFILE 
    LOCATION 's3://st0263datasets/gutenberg-small/';


    // ordenado por palabra

    SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
    GROUP BY word 
    ORDER BY word DESC LIMIT 10;

    // ordenado por frecuencia de menor a mayor

    SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
    GROUP BY word 
    ORDER BY count DESC LIMIT 10;

    ### RETO:

    ¿cómo llenar una tabla con los resultados de un Query? por ejemplo, como almacenar en una tabla el diccionario de frecuencia de palabras en el wordcount?
