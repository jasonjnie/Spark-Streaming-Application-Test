#!/bin/bash

USER="nie9"
# USER="ruilan2"

for i in `seq -f "%02g" 08 10`;
do
    scp -r ../Spark-Streaming-Application-Test $USER@fa18-cs425-g36-$i.cs.illinois.edu:/home/$USER/
done
