# Question 130

*UGC NET CS · 2018 Dec Paper 1 And 2 · Big Data Systems · Hadoop Clusters and YARN Workloads*

Which statements are true? (i) Facebook has the world's largest Hadoop cluster. (ii) Hadoop 2.0 allows live-stream processing of real-time data.

- **1.** (i) only
- **2.** (ii) only
- **3.** Both (i) and (ii)
- **4.** Neither (i) nor (ii)

> [!TIP]
> **Correct answer: 3. Both (i) and (ii)**

## Solution

In the historical context of this 2018 question, statement (i) was treated as true: Facebook documented extremely large Hadoop/HDFS warehouse clusters, including what it described as the largest single HDFS cluster known. Statement (ii) is also true in the intended architectural sense. Hadoop 2 introduced YARN, which separates resource management from a single MapReduce engine and allows other long-running or stream-processing frameworks to run on the cluster, enabling real-time data processing workloads. Therefore both statements are true, option 3.

## Key Points

- Hadoop 2/YARN turns the cluster into a general application resource platform, not only a batch MapReduce runtime; the Facebook claim is historical, not a timeless ranking.

## Why the other options are incorrect

Options 1 and 2 omit one true statement, while option 4 rejects both. Do not confuse Hadoop Streaming—the utility for writing MapReduce mappers/reducers with arbitrary executables—with real-time stream processing; statement (ii) refers to YARN's ability to host suitable processing frameworks.

## References

- [Meta Engineering — Large Scale Hadoop Data Migration at Facebook](https://engineering.fb.com/2011/07/27/core-infra/moving-an-elephant-large-scale-hadoop-data-migration-at-facebook/)
- [Apache Hadoop 2.7.2 — YARN Architecture](https://hadoop.apache.org/docs/r2.7.2/hadoop-yarn/hadoop-yarn-site/)
