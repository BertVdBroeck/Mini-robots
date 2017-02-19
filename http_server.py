    
import network
import socket
 
def log(msg):
    print(msg)
 
 
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        log('connecting to network...')
        sta_if.active(True)
        sta_if.connect('snamellit7', 'D6e&u^BF*Z!v')
        while not sta_if.isconnected():
            pass
    log('network config:'+str( sta_if.ifconfig()))
 
def start_myserver():
    log('start server method')
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    log('listening on'+str( addr))
    while True:
        cl, addr = s.accept()
        log('client connected from'+str(addr))
        cl_file = cl.makefile('rwb', 0)
        first_line = cl_file.readline()
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        (method, path, protocol) = first_line.split()
        print("method: %s" % method)
        print("path: %s" % path)
        print("protocol: %s" % protocol)
        cl_file.write(html)
        cl_file.close()
 
#main part
html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266</title> </head>
    <body> 
        Hello from Python web on ESP8266
    </body>
</html>
"""
 
do_connect()
start_myserver()