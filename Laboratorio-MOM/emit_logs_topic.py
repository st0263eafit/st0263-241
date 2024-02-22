# https://www.rabbitmq.com/tutorials/tutorial-five-python.html
#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic', durable=True)

routing_key = sys.argv[1] if (len(sys.argv) > 2) else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print(" [x] Sent %r:%r" % (routing_key, message))

connection.close()
