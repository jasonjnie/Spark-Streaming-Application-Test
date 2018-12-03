# Applications using Apache Spark as a comparison to Crane

To save terminal output as a file:

```
script output.txt
COMMAND (eg. ls)
exit
```

To run an application, type in the following command inside /usr/local/spark:
```
./bin/spark-submit --master spark://172.22.158.121:7077 --deploy-mode client ./../../../home/nie9/Spark-Streaming-Application-Test/finefoods_wordcount.py ./../../../home/nie9/data/test/
```
```
./bin/spark-submit --master spark://172.22.158.121:7077 --deploy-mode client ./../../../home/nie9/Spark-Streaming-Application-Test/finefoods_helpfulness.py ./../../../home/nie9/Spark-Streaming-Application-Test/data/test/
```
