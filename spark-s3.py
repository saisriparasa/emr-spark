from pyspark import SparkContext, SparkConf
conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

file = sc.textFile("s3n://aws-sai-sriparasa/op/pig-kinesis/iteration_0/part-r-00000")
print file.top(10)
