#!/bin/bash

INPUT_PATH="/user/student/library"
OUTPUT_PATH="/user/student/reverse_index_output"
STOPWORDS_FILE="stopwords.txt"

# Find Hadoop streaming jar
HADOOP_STREAMING_JAR=$(find /usr/lib/hadoop* -name "hadoop-streaming*.jar" | head -1)

if [ -z "$HADOOP_STREAMING_JAR" ]; then
    echo "Error: Hadoop streaming jar not found!"
    exit 1
fi

echo "Using: $HADOOP_STREAMING_JAR"

# Remove old output
hdfs dfs -rm -r -f $OUTPUT_PATH

# Record start time
START=$(date +%s)

# Run job
hadoop jar $HADOOP_STREAMING_JAR \
    -D mapreduce.job.reduces=4 \
    -files mapper.py,reducer.py,combiner.py,$STOPWORDS_FILE \
    -mapper "python3 mapper.py" \
    -combiner "python3 combiner.py" \
    -reducer "python3 reducer.py" \
    -input $INPUT_PATH \
    -output $OUTPUT_PATH

END=$(date +%s)
DURATION=$((END - START))

echo "Job completed in $DURATION seconds"
echo "$DURATION" > execution_time.txt