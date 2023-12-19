# Streaming Data to Hbase with Apache Flume

> Big ISSUE : Zookeeper port permission denied 50700

This repository provides guidance and commands for setting up Apache Flume to stream data to HDFS in real-time. The focus of this lecture is to configure a Flume Agent to monitor a specified directory and stream data to a corresponding directory in HDFS. The example uses SpoolDir as a source.

## Prerequisites

Before you begin, ensure that you have the following components installed:

- [Apache Flume](https://flume.apache.org/)
- python 3.9
- Java 8
- Apache Hbase
- Apache Hadoop
- Grafana

## Installation and Configuration


1. First try to install docker deamon 



2. Pull the docker image of hadoop and create a docker network to communicate between the containers

```bash
  docker pull liliasfaxi/spark-hadoop:hv-2.7.2
```

```bash
  docker network create --driver=bridge hadoop
```

3. Create Three Container 1 master 2 slaves 

```bash
  docker run -itd --net=hadoop -p 50070:50070 -p 8088:8088 -p 7077:7077 -p 16010:16010 \
            --name hadoop-master --hostname hadoop-master \
            liliasfaxi/spark-hadoop:hv-2.7.2

  docker run -itd -p 8040:8042 --net=hadoop \
        --name hadoop-slave1 --hostname hadoop-slave1 \
              liliasfaxi/spark-hadoop:hv-2.7.2

  docker run -itd -p 8041:8042 --net=hadoop \
        --name hadoop-slave2 --hostname hadoop-slave2 \
              liliasfaxi/spark-hadoop:hv-2.7.2
```


4. Use VS code docker extension to attach with the docker container for the hadoop-master container or use this alternative commands


```bash
    docker exec -it hadoop-master bash
```

5. Install Java in the container and modify  `~/.bashrc`  for JAVA_HOME 

6. You will see that hadoop and hbase is already installed 

 - if you want to check hadoop is working go into this workshop link below :

7. Install Flume

```bash
cd ~/usr/local

# Download Apache Flume
wget https://www.apache.org/dyn/closer.lua/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz

# Extract the downloaded tar.gz file
tar -zxvf apache-flume-1.9.0-bin.tar.gz

# Rename the extracted directory to "flume"
mv apache-flume-1.9.0-bin flume
```

8. Configure Flume and FLUME_HOME

You can change in `~.bashrc` for the exportation FLUME_HOME , if the configuration is not refresed try to export in the terminal

```bash
export FLUME_HOME=$HOME/usr/local/flume
export PATH=$PATH:$FLUME_HOME/bin
export CLASSPATH=$CLASSPATH:$FLUME_HOME/lib/*
```

see other available video youtube until this command work in any path from the user

```bash
flume-ng version
```

9. Start Hadoop deamon and Hbase thrift server

```bash
cd
./start-hadoop.sh
start-hbase.sh
```

You can check the ports to see how datanodes are working

start the Hbase Thrift server

```bash
hbase thrift start
```

10. Creat a table in hbase

```hbase
CREATE 'logs' , 'cf'
```

11. Configure Flume conf and add file logs in spool directory

```bash
flume-ng agent --conf conf --conf-file ./conf/flumelogs.conf --name a1 -Dflume.root.logger=INFO,console
```

12. Check if hbase table data is added

```bash
scan 'logs'
```

13. Install python 3.9

```bash

wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz

tar -zxvf Python-3.9.7.tgz

cd Python-3.9.7

./configure

make
make install

```

14. Create and Activate python virtual environement

```bash
python3 -m venv venv_1

source venv_1/bin/activate
```


## Project Directory Structure

- **log.txt**: Sample log file to be streamed.
- **flumelogs.conf**: Configuration file for the Flume Agent.
- **spool**: Directory to monitor for incoming data.
- **etl .py**: Extract data logs from hbase and load it into influxdb for Grafana
- **main.py**:  Generator
- **api**: a folder wich contains a web application


## Project Architecture

