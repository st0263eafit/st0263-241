#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))

channel = connection.channel()

channel.exchange_declare(exchange='fanout_logs', exchange_type='fanout', durable=True)

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='fanout_logs', routing_key='', body=message)

print(" [x] Sent %r" % message)

connection.close()