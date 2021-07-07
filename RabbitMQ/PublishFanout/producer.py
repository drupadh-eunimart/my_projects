import pika

import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='publish',
    exchange_type='fanout'
)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange='publish',
    routing_key='',
    body=message)

print(" [x] Sent %r" % message)
connection.close()

# python producer.py first
# python producer.py second
# python producer.py third
# python producer.py fourth
# python producer.py fifth
