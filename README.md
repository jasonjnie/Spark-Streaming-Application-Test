# Applications using Apache Spark as a comparison to Crane

To save terminal output as a file:

```
script output.txt
COMMAND (eg. ls)
exit
```

To run an application:
```
./bin/spark-submit --master spark://172.22.158.121:7077 --deploy-mode client ./../../../home/nie9/Spark-Streaming-Application-Test/finefoods_wordcount.py ./../../../home/nie9/data/test/
```
