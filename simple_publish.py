#!/usr/bin/env python

import rabbitpy
import time

url = 'amqp://guest:guest@localhost:5672/%2F'

connection = rabbitpy.Connection(url)
channel = connection.channel()
exchange = rabbitpy.Exchange(channel, 'chapter2-example')
exchange.declare()
queue = rabbitpy.Queue(channel, "example")
queue.declare()
queue.bind(exchange, 'example-routing-key')

for message_cnt in range(0,10):
    message_t = "Test Message {}".format(message_cnt)
    message_txt = '{{"message":"{}"}}'.format(message_t)
    properties = {"content_type": "text/plain"} #, "app_id": "simple_publsh:1.0", "message_id":str(100+message_cnt)}
    message = rabbitpy.Message(channel,message_txt,properties,opinionated=True)
    #print "Message Text:"
    print message_txt
    #print "Properties:"
    #print properties
    #print ""
    time.sleep(1)
message.publish(exchange, 'example-routing-key')
