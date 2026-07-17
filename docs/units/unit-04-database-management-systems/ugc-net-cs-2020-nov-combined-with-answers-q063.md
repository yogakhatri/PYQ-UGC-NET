# Question 63

*UGC NET CS · 2020 Nov With Answers · Data Warehousing and Data Mining · HDFS NameNode and DataNode Roles*

In Hadoop HDFS, the DataNode and NameNode are, respectively:

- **1.** Worker Node and Master Node respectively
- **2.** Master Node and Worker Node respectively
- **3.** Both Worker Nodes
- **4.** Both Master Nodes

> [!TIP]
> **Correct answer: 1. Worker Node and Master Node respectively**

## Solution

In HDFS, a DataNode stores actual data blocks, serves client read/write requests, and reports block information to the NameNode; it is a worker node. The NameNode maintains filesystem metadata such as the namespace and block-to-file mapping and coordinates DataNodes; it is the master node in the classic HDFS architecture. Hence DataNode and NameNode are worker and master, respectively—option 1.

## Key Points

- HDFS: NameNode manages metadata; DataNodes store and serve blocks.

## Why the other options are incorrect

Option 2 reverses the roles. Options 3 and 4 incorrectly place both components at the same level. Storing data blocks and managing metadata are deliberately separated between workers and the master.
