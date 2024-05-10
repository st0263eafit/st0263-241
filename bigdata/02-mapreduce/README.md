# Universidad EAFIT
# Curso ST0263 Tópicos Especiales en Telemática, 2024-1

# Demo MapReduce en Python con MRJOB

# WordCount en python

* correr la versión serial / secuencial asumimiendo todos los datos locales:

    $ cd 02-mapreduce
    $ python wordcount-local.py /datasets/gutenberg-small/*.txt > salida-serial.txt
    $ more salida-serial.txt

* Hay varias librerias de python para acceder a servicios MapReduce en Hadoop

* Se usará MRJOB (https://mrjob.readthedocs.io/en/latest/)

* Se puede emplear una version de python 2.x o 3.x, del sistema (como root) o con un manejador de versiones de node (pyenv o virtualenv).

* Como parte del sistema, se instalará mrjob así:

>		user@master$ sudo yum install python3-pip
>		user@master$ sudo pip3 install mrjob

* Probar mrjob python local:

>		user@master$ cd 02-mapreduce
>		user@master$ python wordcount-mr.py ./datasets/gutenberg-small/*.txt

* Ejecutar mrjob python en Hadoop con datos en hdfs o s3:

Se deberá consultar en la documentación de mrjob para ejecutar en clusters AWS EMR (se deja como parte del lab5-3)

Se ejecutará algo similar a esto:

>		user@master$ python wordcount-mr.py hdfs:///datasets/gutenberg-small/*.txt -r hadoop --output-dir hdfs:///user/<login>/result3 --hadoop-streaming-jar $HADOOP_STREAMING_HOME/hadoop-streaming.jar

* el directorio 'result*' no puede existir)

## "-D mapred.reduce.tasks=10" para especificar el nro de reducers en MRJOB
