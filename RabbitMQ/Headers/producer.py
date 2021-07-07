import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='headers_msgs',
    exchange_type='headers'
)

key1 = sys.argv[1]
key2 = sys.argv[2]
message = ' '.join(sys.argv[3:]) or "Hello World!"

headers = {
    "key1" : key1,
    "key2" : key2
}

properties = pika.BasicProperties(
    headers=headers
)

channel.basic_publish(
    exchange='headers_msgs',
    routing_key='',
    body=message,
    properties = properties
)

print(f" [x] Sent {headers}: {message}")
connection.close()