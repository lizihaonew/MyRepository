# -*- coding: utf-8 -*-

import pika

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

# 声明一个信道，在信道里发送消息
channel = connection.channel()

# 在信道里声明queue
channel.queue_declare(queue='queue_test')

# rabbitmq发送消息通常需要通过exchange，只是这里的exchange默认名称为空字符串
channel.basic_publish(
    exchange='',
    routing_key='queue_test',  # queue名字
    body='Hello world!'         # 消息内容
)

# 代码是串行的，发送成功后会执行到该打印语句
print(" [x] Sent 'hello world!'")

# 缓冲区已经flush，而且消息已经确认发送到了rabbitmq中，关闭链接
connection.close()

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

for i in range(20):
    channel.basic_publish(
        exchange='',
        routing_key='queue_test',
        body='[%s] Hello World!!!' % i
    )
print(" [x] Sent the message!!")
connection.close()

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
message_body = 'Hello world!!'

for i in range(20):
    channel.basic_publish(
        exchange='',
        routing_key='queue_test2',
        body="[%s]" % i + message_body
    )
    
print('队列启动，消息已经发出！！！')
connection.close()

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

channel.queue_declare(queue='queue_test3', durable=True)    # durable置为True，将queue声明为持久化

message_body = 'Hello world!!!'

for i in range(5):
    channel.basic_publish(
        exchange='',
        routing_key='queue_test3',
        body="[%s] " % i + message_body,
        properties=pika.BasicProperties(        # 将具体消息声明为持久化
            delivery_mode=2,
        )
    )

print('队列启动，消息已经发出！！！')
connection.close()

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

# 定义交换机，exchange表示交换机名称，type表示类型
channel.exchange_declare(
    exchange='exchange_test',
    exchange_type='fanout'
)

message_body = 'Hello World!!!'

# 将消息发送到交换机，而不是发送到queue了
for i in range(10):
    channel.basic_publish(
        exchange='exchange_test',   # 指定exchange
        routing_key='',     # fanout模式为广播模式，不需要路由键，配置了也不生效
        body="[%s] " % i + message_body
    )

print('队列启动，消息已经发出！！！')
connection.close()

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

# 定义交换机名称及类型
channel.exchange_declare(
    exchange='direct_test',
    exchange_type='direct'
)

severity1 = 'info'
severity2 = 'error'
message_body = 'Hello World!!!'

# 发布消息至交换机direct_test, 且发布的消息携带的关键字routing_key是info
channel.basic_publish(
    exchange='direct_test',
    routing_key=severity1,
    body=message_body
)

print("[x] Sent routing_key: %s |message: %s" % (severity1, message_body))

# 再定义一个basic_publish发布消息至交换机direct_test, 且发布的消息携带的routing_key是error
channel.basic_publish(
    exchange='direct_test',
    routing_key=severity2,
    body=message_body
)

print("[x] Sent routing_key: %s |message: %s" % (severity2, message_body))

connection.close()

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

# 定义交换机名称及类型
channel.exchange_declare(
    exchange='topic_test',
    exchange_type='topic'
)

severity1 = 'order.log.info'
severity2 = 'product.log.error'
message_body = 'Hello World!!!'

# 发布消息至交换机topic_test, 且发布的消息携带的关键字routing_key是order.log.info
channel.basic_publish(
    exchange='topic_test',
    routing_key=severity1,
    body=message_body
)

print("[x] Sent routing_key: %s |message: %s" % (severity1, message_body))

# 再定义一个basic_publish发布消息至交换机topic_test, 且发布的消息携带的routing_key是product.log.error
channel.basic_publish(
    exchange='topic_test',
    routing_key=severity2,
    body=message_body
)

print("[x] Sent routing_key: %s |message: %s" % (severity2, message_body))

connection.close()

'''





