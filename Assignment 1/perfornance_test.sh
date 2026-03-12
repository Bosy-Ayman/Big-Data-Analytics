#!/bin/bash

RESULTS_DIR="performance_results"
mkdir -p $RESULTS_DIR

run_test() {
    NODES=$1
    echo "Testing with $NODES node(s)..."
    
    TOTAL=0
    for i in 1 2 3; do
        echo "Run $i/3"
        
        # Clear output
        hdfs dfs -rm -r -f /user/student/reverse_index_output
        
        START=$(date +%s)
        
        hadoop jar $(find /usr/lib/hadoop* -name "hadoop-streaming*.jar" | head -1) \
            -D mapreduce.job.reduces=4 \
            -files mapper.py,reducer.py,combiner.py,stopwords.txt \
            -mapper "python3 mapper.py" \
            -combiner "python3 combiner.py" \
            -reducer "python3 reducer.py" \
            -input /user/student/library \
            -output /user/student/reverse_index_output
        
        END=$(date +%s)
        RUNTIME=$((END - START))
        TOTAL=$((TOTAL + RUNTIME))
        echo "$RUNTIME" >> ${RESULTS_DIR}/nodes_${NODES}_run_${i}.txt
    done
    
    AVG=$((TOTAL / 3))
    echo "$NODES $AVG" >> ${RESULTS_DIR}/times.txt
    echo "Average: $AVG seconds"
}

# Run tests
run_test 1
run_test 2
run_test 3

# Calculate speedup
echo -e "\nSpeedup Analysis:"
echo "Nodes | Time | Speedup"
echo "------|------|--------"

T1=$(grep "^1 " ${RESULTS_DIR}/times.txt | cut -d' ' -f2)

while read line; do
    N=$(echo $line | cut -d' ' -f1)
    T=$(echo $line | cut -d' ' -f2)
    S=$(echo "scale=2; $T1 / $T" | bc)
    echo "$N     | $T    | ${S}x"
done < ${RESULTS_DIR}/times.txt