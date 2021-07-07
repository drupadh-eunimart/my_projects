import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='topic_msgs',
    exchange_type='topic'
)

result = channel.queue_declare(
    queue='',
    exclusive=True
)

queue_name = result.method.queue

route = sys.argv[1]

channel.queue_bind(
    exchange='topic_msgs',
    queue=queue_name,
    routing_key=route
)

def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}: {body}")

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Interrupted')