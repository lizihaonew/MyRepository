# -*- coding: utf-8 -*-

import pika
import time

'''
################ sample 1 ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

# 绑定用户登陆信息,定义用户的身份证书
credentials = pika.PlainCredentials(username, password)
# 建立一个connection实例
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)   # 默认端口5672，可不写
)

# 声明信道
channel = connection.channel()

# 声明消息队列，消息将在这个队列中进行传递，如果队列不存在，则创建
# 生产者和消费者都要声明一个相同的队列，用来防止某一方挂了，另外一方能正常运行
channel.queue_declare(queue='queue_test')


def callback(ch, method, properties, body): # 定义callback()函数来处理body参数中的消息
    # 四个参数为标准格式
    print(" [x] Recevied %r" % body)    # 我们定义该函数处理消息的方式是打印出该消息体

channel.basic_consume(  # 消费消息
    callback,   # 如果收到消息，就调用callback函数来处理消息
    queue='queue_test',     # 你要从哪个消息队列收消息
    no_ack=True     # 自动应答，若为True，则生产者成功发送一条就继续发送下一条，不管mq以及生产者的状态
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()   # 开始消费消息

'''
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
    time.sleep(1)
    print("Recevied %s" % body)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    callback,
    queue='queue_test',
    no_ack=True
)

print("[*] Waiting for message. To exit press CTRL+C")

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
    time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 给mq发送确认反馈，收到该反馈mq再发消息

channel.basic_qos(prefetch_count=1)     # 每次最多处理1条消息，处理时不再接受消息
channel.basic_consume(
    callback,
    queue='queue_test2',
    no_ack=False    # 关闭自动应答，如果定义了主动反馈，这边还为True，会报错
)

print("[*] Waiting for message. To exit press CTRL+C")
channel.start_consuming()

'''
'''
################ Durable ###################

username = 'user_test'
password = '123456'
server_host = 'localhost'
virtual_host = 'vhost_test'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(server_host, 5672, virtual_host, credentials)
)
channel = connection.channel()
channel.queue_declare(queue='queue_test3', durable=True)


def callback(ch, method, properties, body):
    time.sleep(1)
    print("Recevied %s" % body)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    callback,
    queue='queue_test3',
    no_ack=True
)

print("[*] Waiting for message. To exit press CTRL+C")
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
severities = 'info'

# 将随机队列与routing_key关键字以及exchange进行绑定
channel.queue_bind(
    exchange='direct_test',
    queue=queue_name,
    routing_key=severities  # 定义绑定随机队列与exchange的routing_key是info
)

print("[*] Waiting for message. To exit press CTRL+C")


def callback(ch, method, properties, body):
    time.sleep(3)
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
severities = '#.info'

# 将随机队列与routing_key关键字以及exchange进行绑定
channel.queue_bind(
    exchange='topic_test',
    queue=queue_name,
    routing_key=severities  # 定义绑定随机队列与exchange的routing_key是info
)

print("[*] Waiting for message. To exit press CTRL+C")


def callback(ch, method, properties, body):
    time.sleep(3)
    print("Recevied routing_key: %s | message: %s" % (method.routing_key, body))

channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

channel.start_consuming()

'''




