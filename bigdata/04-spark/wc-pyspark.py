from pyspark.sql import SparkSession

# puede no necesitar instanciar las variables spark y sc si esta ejecutando en AWS EMR:
spark = SparkSession.builder.appName("WordCount").getOrCreate()
sc = spark.sparkContext

files_rdd = sc.textFile("s3://st0263datasets/gutenberg-small/*.txt")
#files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wc = wc_unsort.sortBy(lambda a: -a[1])
wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout1")
