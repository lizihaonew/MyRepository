# -*- coding: utf-8 -*-

import pika
import time

'''
################ Round-robin ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)
)
channel = connection.channel()
channel.queue_declare(queue='queue_test')


def callback(ch, method, properties, body):
    time.sleep(3)   # 处理消息时，sleep 3秒，模拟耗时
    print("Recevied %s" % body)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    callback,
    queue='queue_test',
    no_ack=True
)

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

'''
'''
################ Fair dispatch ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)
)
channel = connection.channel()
channel.queue_declare(queue='queue_test2')


def callback(ch, method, properties, body):
    print("Recevied %s" % body)
    time.sleep(3)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 定义反馈机制，在处理完消息后反馈给mq

channel.basic_qos(prefetch_count=1)     # 每次最多处理1条消息，处理时不再接受消息
channel.basic_consume(
    callback,
    queue='queue_test2',
    no_ack=False    # 自动应答置为False
)

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

'''
'''
################ Fanout ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)
)
channel = connection.channel()

channel.exchange_declare(
    exchange='exchange_test',
    exchange_type='fanout'
)

# 随机创建队列
result = channel.queue_declare(exclusive=True)  # exclusive=True表示建立临时队列，consumer关闭后，该队列就会被删除
queue_name = result.method.queue

# 将queue与exchange进行绑定
channel.queue_bind(
    exchange='exchange_test',
    queue=queue_name
)


def callback(ch, method, properties, body):
    print("Recevied message %s" % body)

channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

print("[*] Waiting for message. To exit press CTRL+C")
channel.start_consuming()

'''
'''
################ Direct ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)
)
channel = connection.channel()

# 定义exchange和类型
channel.exchange_declare(
    exchange='direct_test',
    exchange_type='direct'
)

# 生成随机队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
severities = 'error'

# 将随机队列与routing_key关键字以及exchange进行绑定
channel.queue_bind(
    exchange='direct_test',
    queue=queue_name,
    routing_key=severities      # 定义绑定随机队列与exchange的routing_key是error
)

print("[*] Waiting for message. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print("Recevied routing_key: %s | message: %s" % (method.routing_key, body))

channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

channel.start_consuming()

'''
'''
################ Topic ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)
)
channel = connection.channel()

# 定义exchange和类型
channel.exchange_declare(
    exchange='topic_test',
    exchange_type='topic'
)

# 生成随机队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
severities = '*.log.*'

# 将随机队列与routing_key关键字以及exchange进行绑定
channel.queue_bind(
    exchange='topic_test',
    queue=queue_name,
    routing_key=severities      # 定义绑定随机队列与exchange的routing_key是error
)

print("[*] Waiting for message. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print("Recevied routing_key: %s | message: %s" % (method.routing_key, body))

channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

channel.start_consuming()

'''



