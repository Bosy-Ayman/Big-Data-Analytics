#!/bin/bash

# Configuration
INPUT_PATH="/user/hduser/library"
OUTPUT_PATH="/user/hduser/reverse_index_output"
STOPWORDS="stopwords.txt"

# Find Hadoop streaming jar
HADOOP_STREAMING_JAR=$(find /usr/local/hadoop -name "hadoop-streaming*.jar" | head -1)

if [ -z "$HADOOP_STREAMING_JAR" ]; then
    HADOOP_STREAMING_JAR=$(find /usr/lib/hadoop* -name "hadoop-streaming*.jar" | head -1)
fi

echo "Using Hadoop Streaming JAR: $HADOOP_STREAMING_JAR"

# Remove old output
hdfs dfs -rm -r -f $OUTPUT_PATH

# Record start time
START=$(date +%s)

# Run Hadoop job
hadoop jar $HADOOP_STREAMING_JAR \
    -D mapreduce.job.reduces=4 \
    -files mapper.py,reducer.py,combiner.py,$STOPWORDS \
    -mapper "python3 mapper.py" \
    -combiner "python3 combiner.py" \
    -reducer "python3 reducer.py" \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH

# Record end time
END=$(date +%s)
DURATION=$((END - START))

echo "=================================="
echo "Job completed in $DURATION seconds"
echo "=================================="

# Show results
echo ""
echo "Sample output (first 20 lines):"
hdfs dfs -cat $OUTPUT_PATH/part-00000 2>/dev/null | head -20

echo ""
echo "Total unique words:"
hdfs dfs -cat $OUTPUT_PATH/part-* 2>/dev/null | wc -l
