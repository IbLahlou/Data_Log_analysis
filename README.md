# Streaming Data to Hbase with Apache Flume

> Actually we steam just to HDFS | no Hbase | no Grafana 

This repository provides guidance and commands for setting up Apache Flume to stream data to HDFS in real-time. The focus of this lecture is to configure a Flume Agent to monitor a specified directory and stream data to a corresponding directory in HDFS. The example uses SpoolDir as a source.

## Prerequisites

Before you begin, ensure that you have the following components installed:

- [Apache Flume](https://flume.apache.org/)
- Java 8
- Apache Hbase
- Apache Hadoop
- Grafana

## Commands for the Lecture

1. Download the necessary configuration file:

    ```bash
    wget https://raw.githubusercontent.com/ashaypatil11/hadoop/main/flume_logs.conf
    ```

    Credits to **ashaypatil11**

2. Navigate to the Flume directory:

    ```bash
    cd /root/big-data/flume/directory
    ```

3. Start the Flume Agent:

    ```bash
    flume-ng agent --conf conf --conf-file /root/big-data/flume_logs.conf --name a1 -Dflume.root.logger=INFO,console
    ```

4. Create a directory for SpoolDir:

    ```bash
    mkdir spool
    ```

5. Copy the sample log file to the spool directory:

    ```bash
    cp access_log.txt spool/logs.txt
    ```

6. Observe the real-time streaming of data from the specified directory to HDFS.

## Project Directory Structure

- **access_log.txt**: Sample log file to be streamed.
- **flume_logs.conf**: Configuration file for the Flume Agent.
- **spool**: Directory to monitor for incoming data.
- **[Other project files]**

Feel free to explore and adapt the provided commands and files for your specific use case. For any issues or questions, refer to the official documentation for [Apache Flume](https://flume.apache.org/).

***

