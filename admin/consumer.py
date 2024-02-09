import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.setttings")
django.setup()

from product.models import Product


params = pika.URLParameters('')

connection =  pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.Objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Products like increased!')



channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()