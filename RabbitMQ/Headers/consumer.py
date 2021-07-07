import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='headers_msgs',
    exchange_type='headers'
)

result = channel.queue_declare(
    queue='',
    exclusive=True
)

queue_name = result.method.queue

match = sys.argv[1]

headers = {
    "key1" : "True",
    "key2" : "True",
    "x-match" : match
}

channel.queue_bind(
    exchange='headers_msgs',
    queue=queue_name,
    arguments=headers
)

def callback(ch, method, properties, body):
    print(f" [x] : {body}")

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Interrupted')