#!/bin/bash

USER="nie9"
# USER="ruilan2"

for i in `seq -f "%02g" 10 10`;
do
    scp -r ../Spark-Streaming-Application-Test/finefoods_helpfulness.py $USER@fa18-cs425-g36-$i.cs.illinois.edu:/home/$USER/Spark-Streaming-Application-Test/
done
