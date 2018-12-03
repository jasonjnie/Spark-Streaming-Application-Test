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
 Usage: ./bin/spark-submit
 --master spark://172.22.158.121:7077
 --deploy-mode client
 ./../../../home/nie9/Spark-Streaming-Application-Test/simple_join.py
 ./../../../home/nie9/Spark-Streaming-Application-Test/data/test/
"""
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: hdfs_wordcount.py <directory>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="SimpleJoin")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 1)

    lines1 = ssc.textFileStream(sys.argv[1])
    lines2 = ssc.textFileStream(sys.argv[1])

    lines1 = lines1.map(lambda x: tuple((x.split(" ")[0], x)))
    lines2 = lines2.map(lambda x: tuple((x.split(" ")[0], x)))

    joined_lines = lines1.join(lines2) \
                    .filter(lambda x: x[1][0] != x[1][1] and x[1][0].split(" ")[1] != "male" and x[1][0].split(" ")[1] != "female") \
                    .map(lambda x: tuple((int(x[0]), x[1][0] + " " + x[1][1]))) \
                    .transform(lambda rdd: rdd.sortByKey(True)) \
                    .map(lambda x: x[1])

    joined_lines.pprint(999999)

    ssc.start()
    ssc.awaitTermination()
