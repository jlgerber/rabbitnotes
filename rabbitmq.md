# running rabbit from docker
```
 docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 -p 5672:5672 rabbitmq:3-management
 ```

# Message
The message published into rabbit has three frames:
- Basic.Publish
- Header
- Body

# Message Properties
Message properties contained in the header frame are a predefined set of values specified by the Basic.Properties data structure.

## Useful Properties
Some properties are used to implement specific behavior in RabbitMQ; delivery-mode tells Rabbit whether it must store a message on disk or if it can simply keep it in memory. Other properties exist for the benefit of system integrators; Rabbit will not use these properties to inform its behavior.

### content-type
Use the content-type property to let consumers know how to interpret the message body by specifying the MIME type. For example, application/json or application/xml.

### content-encoding
Use content-encoding to indicate if the message body is compressed or encoded in some special way. For example, gzip encoded. This could be useful for us to handle large messages. Mime encoding types exist:
- gzip (use gzip)
- compress (use LZW)
- deflate (zlib)
- identity (no compression)
- br (brotti)


### message-id
Use to uniquely identify message. The AMQP spec defines this for consumer use as up to 255 bytes of UTF-8.

### correlation-id
Use to uniquely identify message response. Can be used to carry the id of the message to which this message is a response to. ALternatively, it can be used to cary a transaction id. The AMQP spec defines this for consumer use as up to 255 bytes of UTF-8.

### timestamp
Defne when a message was created

### expiration
Define when a message expires. RabbitMQ will discard messages that are older than the expiration if this is set. For some reason, it is defined as a short string (255 chars) in the spec, unlike timestamp, which is an int. In RabbitMQ, this must contain an integer based Unix Epoch or timestamp in string form.
Message expiry can also be set up when creatign a queue using the ```x-message-ttl``` argument (this uses Unix Epoch with millisecond precision. ie value * 1000)

### delivery-mode
Tell rabbit to write your message to disk-backed or in-memory queues. This has two potential int values:

- 1 - non-persisted message
- 2 - persisted message

This should not be confused with the ```durable``` setting in a queue, which indicates whether the queue's definition should survive restart. Only the ```delivery-mode``` defines whether a message should be persised to disk or not.
Non-persisted messages have the lowest latency.
Persistence has significant impact on performance and scalability.

### app-id
use to define the application that sent a message. A short (255 byte) string. One use is to set the API name and version.

### user-id
Use to define the user who sent a message. Rabbit uses this to authenticate the message. If the user-id doesnt match the user publishing the message, Rabbit will reject the message.

### type
Use to define a contract between publishers an consumers

### reply-to
Use to route reply messages when implementing a relevant pattern.

### headers
use the table property to define free form property definitions and routing. Key/value.
keys can be ascii or utf-8 upt to 255 bytes. Values can be any AMQP type.
Rabbit can route messages based on the values populated in the header instead of the routing key.

### priority
as of RabbitMQ 3.5.0, the priority field has been implemented per the AMQP spec. Defiend as an integer with possible values of 0-9. 0 being the highest and 9 being the lowest. Rabbit uses these rankings to reorder message consumtion in a queue.

### cluster-id
This property is was defined in AMQP 0-8-0 and renamed to reserved in AMQP 0-9-1. According to RabbitMQ, this field must be empty.