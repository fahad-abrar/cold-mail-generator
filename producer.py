from dotenv import load_dotenv
import pika
import json
import os
load_dotenv()

URL = os.getenv('URL')

def producer(msg):
    try:
        url = pika.URLParameters(URL)
        connection = pika.BlockingConnection(url)
        channel = connection.channel()

        exchange = 'cold_mail'
        queue = 'mail'
        routing_key = 'route-1'

        channel.exchange_declare(exchange=exchange, exchange_type="direct", durable=True)
        channel.queue_declare(queue=queue, durable=False)
        channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)

        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body = json.dumps(msg),
            properties=pika.BasicProperties(
                delivery_mode=2
                # 2 is used for make msg persistent
            )
        )
        print(f"message is send: {msg}")
        connection.close()

    except Exception as err:
        print(f" an error is occured: {err}")


