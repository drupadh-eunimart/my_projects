import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='topic_msgs',
    exchange_type='topic'
)

route = sys.argv[1]
message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(
    exchange='topic_msgs',
    routing_key=route,
    body=message)

print(f" [x] Sent {route}: {route}")
connection.close()