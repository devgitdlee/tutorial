import pika


params = pika.URLParameters('')

connection =  pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BaiscProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)


