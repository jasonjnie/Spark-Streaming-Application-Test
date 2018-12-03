#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
 Counts words in new text files created in the given directory
 Usage: hdfs_wordcount.py <directory>
   <directory> is the directory that Spark Streaming will use to find and read new text files.

 To run this on your local machine on directory `localdir`, run this example
    $ bin/spark-submit examples/src/main/python/streaming/hdfs_wordcount.py localdir

 Then create a text file in `localdir` and the words in the file will get counted.
"""
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: hdfs_wordcount.py <directory>", file=sys.stderr)
    #     sys.exit(-1)

    sc = SparkContext(appName="FINEFOODSHelpfulness")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    lines = ssc.textFileStream(sys.argv[1])
    # lines = ssc.sparkContext.textFile("./../../../home/nie9/Spark-Streaming-Application-Test/data/finefoods.txt") \
    #         .map(lambda line: tuple(line.split(" "))).toDF()
    # lines.pprint(999999)
    # .filter(lambda line: True if line.split("\n")[0] == "review/score:" else False)
    # print(lines.take(10))

    counts = lines.map(lambda line: tuple(line.split(" "))) \
                  .reduceByKey(lambda a, b: float(a)+float(b)) \
                  .transform(lambda rdd: rdd.sortByKey(True))



    counts.pprint(999999)

    ssc.start()
    ssc.awaitTermination()
