# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# producer.py
# This script will publish MQ message to my_exchange MQ exchange

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

channel.basic_publish(exchange='my_exchange', routing_key='test', body='Test!')

connection.close()