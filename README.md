# Big Data Analytics
# The Digital Librarian – Distributed Reverse Index (Hadoop MapReduce)

## Team Members
- Rihana Nasr (202201092)
- Bosy Ayman (202202076)

---

## Project Overview
This project implements a Distributed Reverse Index using Hadoop MapReduce.  
The system processes a collection of books and builds an index mapping each word to the documents it appears in, along with its frequency.

### Example Output
abide --> Alice.txt:1, Dracula.txt:1, Great_Expectations.txt:3

---

## Technologies Used
- Hadoop (HDFS + MapReduce)
- Java
- Docker (for cluster setup)

---

## Project Structure
├── src/
│ ├── Mapper.java
│ ├── Reducer.java
│ ├── Driver.java
│
├── resources/
│ ├── stopwords.txt
│
├── input/
│ ├── *.txt (books)
│
├── output/
│
└── README.md 

---

### Setup Instructions

## 1. Start Hadoop Cluster (Docker)
```bash
docker-compose up -d 
```
## 2. Create HDFS Directory
```bash
hdfs dfs -mkdir -p /user/hduser/library
```
## 3. Upload Dataset
```bash
hdfs dfs -put input/*.txt /user/hduser/library/
```
## 4. Compile Java Code
```bash
javac -classpath `hadoop classpath` -d . *.java
jar -cvf ReverseIndex.jar *
```
## 5. Run MapReduce Job
```bash
hadoop jar ReverseIndex.jar Driver \
/user/hduser/library \
/user/hduser/output
```
## 6. View Output
```bash
hdfs dfs -cat /user/hduser/output/part-*
```
### Data Preprocessing

The following steps are applied in the Mapper:
- Convert text to lowercase
- Remove punctuation
- Remove stop words (using stopwords.txt)
- Tokenize text

### Optimization Techniques
- Stop-word removal (reduced data by approximately 80%)
- Combiner (reduced shuffle size significantly)

### Performance Evaluation
The system was tested on:
- 1 Node (Pseudo-distributed)
- 2 Nodes
- 3 Nodes
### Results
| Nodes | Time (sec) | Speedup |
| ----- | ---------- | ------- |
| 1     | 42         | 1.0x    |
| 2     | 28         | 1.50x   |
| 3     | 23         | 1.82x   |

### Notes
- Dataset size: approximately 9.3 MB (10 books)
- Due to resource limitations, the dataset size is smaller than real-world Big Data scenarios

### Conclusion
This project demonstrates how distributed processing using Hadoop MapReduce improves search efficiency and scalability for large text datasets.
