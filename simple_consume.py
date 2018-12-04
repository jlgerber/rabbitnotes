#!/usr/bin/env python

import rabbitpy
import time

url = 'amqp://guest:guest@localhost:5672/%2F'

connection = rabbitpy.Connection(url)
channel = connection.channel()
exchange = rabbitpy.Exchange(channel, 'chapter2-example')
exchange.declare()
queue = rabbitpy.Queue(channel, "example")
while len(queue) > 0:
    message = queue.get()
    print "message id: {} message timestamp: {} body: {}"\
    .format(message.properties['message_id'], \
    message.properties['timestamp'].isoformat(),
    message.body)
    print ""
    message.ack()
