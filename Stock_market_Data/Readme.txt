Stock_Market_Dataset


Kafka is installed in the folder /home/dharani/BigData_src/kafka_2.12-3.3.1

Installing – Kafka commands: 

Move to folder - ~/BigData_src/kafka_2.12-3.3.1$ 

– Start zookeeper
 
bin/zookeeper-server-start.sh config/zookeeper.properties 

– Start Kafka server

nohup bin/kafka-server-start.sh config/server.properties 

use jps command to see if the zookeeper and kafka server are up and running 

--Create Kafka Topic

bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4 	

-- List Topic

 bin/kafka-topics.sh --list --bootstrap-server localhost:9092

--Kafka Producer 

bin/kafka-console-producer.sh --topic test --bootstrap-server localhost:9092

--Kafka Consumer 

bin/kafka-console-consumer.sh --topic test --bootstrap-server localhost:9092


---The data is stored into s3 buckets and then Crawlers are used to create a AWS GLue catalog. Once the catalog is created, data is queried in real time using AWS Athena
