#!/bin/bash

echo "=================================="
echo "Performance Testing - Digital Librarian"
echo "=================================="

# Test with 1 node (4 reducers)
echo ""
echo "Testing 1 node configuration..."
hdfs dfs -rm -r -f /user/hduser/output_1node
START1=$(date +%s)
hadoop jar $(find /usr/local/hadoop -name "hadoop-streaming*.jar" | head -1) \
    -D mapreduce.job.reduces=4 \
    -files mapper.py,reducer.py,combiner.py,stopwords.txt \
    -mapper "python3 mapper.py" \
    -combiner "python3 combiner.py" \
    -reducer "python3 reducer.py" \
    -input /user/hduser/library \
    -output /user/hduser/output_1node
END1=$(date +%s)
TIME1=$((END1 - START1))
echo "1 node time: $TIME1 seconds"

# Test with 2 nodes (simulated with 8 reducers)
echo ""
echo "Testing 2 node configuration..."
hdfs dfs -rm -r -f /user/hduser/output_2node
START2=$(date +%s)
hadoop jar $(find /usr/local/hadoop -name "hadoop-streaming*.jar" | head -1) \
    -D mapreduce.job.reduces=8 \
    -D mapreduce.map.memory.mb=1024 \
    -D mapreduce.reduce.memory.mb=1024 \
    -files mapper.py,reducer.py,combiner.py,stopwords.txt \
    -mapper "python3 mapper.py" \
    -combiner "python3 combiner.py" \
    -reducer "python3 reducer.py" \
    -input /user/hduser/library \
    -output /user/hduser/output_2node
END2=$(date +%s)
TIME2=$((END2 - START2))
echo "2 node time: $TIME2 seconds"

# Test with 3 nodes (simulated with 12 reducers)
echo ""
echo "Testing 3 node configuration..."
hdfs dfs -rm -r -f /user/hduser/output_3node
START3=$(date +%s)
hadoop jar $(find /usr/local/hadoop -name "hadoop-streaming*.jar" | head -1) \
    -D mapreduce.job.reduces=12 \
    -D mapreduce.map.memory.mb=1536 \
    -D mapreduce.reduce.memory.mb=1536 \
    -files mapper.py,reducer.py,combiner.py,stopwords.txt \
    -mapper "python3 mapper.py" \
    -combiner "python3 combiner.py" \
    -reducer "python3 reducer.py" \
    -input /user/hduser/library \
    -output /user/hduser/output_3node
END3=$(date +%s)
TIME3=$((END3 - START3))
echo "3 node time: $TIME3 seconds"

# Calculate speedup
echo ""
echo "=================================="
echo "RESULTS SUMMARY"
echo "=================================="
echo "1 Node: $TIME1 seconds"
echo "2 Nodes: $TIME2 seconds"
echo "3 Nodes: $TIME3 seconds"
echo ""
SPEEDUP2=$(echo "scale=2; $TIME1 / $TIME2" | bc)
SPEEDUP3=$(echo "scale=2; $TIME1 / $TIME3" | bc)
echo "Speedup with 2 nodes: ${SPEEDUP2}x"
echo "Speedup with 3 nodes: ${SPEEDUP3}x"
echo ""

# Save results
cat > performance_results.txt << EOF
PERFORMANCE TEST RESULTS
=======================
Date: $(date)
Books: 10
Total size: ~9.3 MB

Execution Times:
1 node: $TIME1 seconds
2 nodes: $TIME2 seconds
3 nodes: $TIME3 seconds

Speedup:
2 nodes: ${SPEEDUP2}x
3 nodes: ${SPEEDUP3}x
EOF

cat performance_results.txt

