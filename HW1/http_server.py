#Vihan Agarwal

import socket

from http_server_request import HttpServerRequest

METHOD_GET = 'GET'
METHOD_POST = 'POST'

class HttpServer:
    def __init__(self, port, dispatcher):
        """This method initializes a HttpServer and binds a socket to the port passed"""
        self.port = port
        self.dispatcher = dispatcher
        self.socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("127.0.0.1", port))
    
    def serve(self):
        """This method opens the server on the port, reads a request from
        the browser, processes a response and then writes the response back 
        to the browser"""
        self.socket.listen(5)
        print 'listening on port', self.port
        while 1:
            (browser, address) = self.socket.accept()
            request = self.readRequest(browser)
            print 'received request', request
            response = self.dispatcher.dispatch(request)
            print 'sending response', response
            self.writeResponse(browser, response)
    
    def readRequest(self, browser):
        """This method reads a request from the browser and returns a 
        http_server_request object"""
        
        headerTokens = socketReadline(browser).split()
        method = headerTokens[0].upper()  
        path = headerTokens[1]
        headers = {}
        while True:
            line = socketReadline(browser)
            if line == '\r\n':
                break
            (field, value) = line.split(':', 1)
            field = field.lower().strip()
            value = value.strip()
            headers[field] = value
        body = None
        if method == METHOD_POST:
            contentLength = int(headers['content-length'])
            body = ''
            while len(body) < contentLength:
                body += socketReadline(browser)
        return HttpServerRequest(method, path, headers, body)
    
    def writeResponse(self, browser, response):
        """This method constructs a response and sends it to the broswer"""

        # add the content-length and connection headers
        response.addHeader('Content-Length', len(response.body))
        response.addHeader('Connection', 'close')        
        browser.send('HTTP/1.0 %s %s\r\n' % (response.code, response.reason))
        for (field, value) in response.headers.items():
            browser.send('%s: %s\r\n' % (field, value))
        browser.send('\r\n')
        browser.send(response.body)
        browser.close()


            
def socketReadline(sock, maxBytes=100000000):
    """Utility method to read a line from a socket"""
    line = ''
    while True:
        c = sock.recv(1)
        if c == None:
            return line
        line += c
        if line[-1] == '\n' or len(line) >= maxBytes:
            return line

