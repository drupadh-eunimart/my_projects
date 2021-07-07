import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='direct_msgs',
    exchange_type='direct'
)

route = sys.argv[1]
message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(
    exchange='direct_msgs',
    routing_key=route,
    body=message)

print(f" [x] Sent {route}: {route}")
connection.close()