# Applications using Apache Spark as a comparison to Crane

To save terminal output as a file:

```
script output.txt
COMMAND (eg. ls)
exit
```

### Application 1
To run the application, type in the following command inside /usr/local/spark:
```
./bin/spark-submit --master spark://172.22.158.121:7077 --deploy-mode client ./../../../home/nie9/Spark-Streaming-Application-Test/finefoods_wordcount.py ./../../../home/nie9/data/test/
```
and the following command in /home/$USER/Spark-Streaming-Application-Test/data
```
cp finefoods_wordcount.txt test/
```

### Application 2
To run the application, type in the following command inside /usr/local/spark:
```
./bin/spark-submit --master spark://172.22.158.121:7077 --deploy-mode client ./../../../home/nie9/Spark-Streaming-Application-Test/finefoods_helpfulness.py ./../../../home/nie9/Spark-Streaming-Application-Test/data/test/
```
and the following command in /home/$USER/Spark-Streaming-Application-Test/data
```
cp finefoods_helpfulness.txt test/
```

### Application 3
To run the application, type in the following command inside /usr/local/spark:
```
./bin/spark-submit --master spark://172.22.158.121:7077 --deploy-mode client ./../../../home/nie9/Spark-Streaming-Application-Test/simple_join.py ./../../../home/nie9/Spark-Streaming-Application-Test/data/test/
```
and the following command in /home/$USER/Spark-Streaming-Application-Test/data
```
cp -t test/ joinTable1.txt joinTable2.txt
```
