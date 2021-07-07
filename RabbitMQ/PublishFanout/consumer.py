import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='publish',
    exchange_type='fanout'
)

result = channel.queue_declare(
    queue='',
    exclusive=True
)

queue_name = result.method.queue

channel.queue_bind(
    exchange='publish',
    queue=queue_name
)

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Interrupted')