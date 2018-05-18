#Vihan Agarwal
from http_server_response import HttpServerResponse
from http_server import HttpServer
import mimetypes
import string
import os

class Dispatcher:
    def __init__(self):
        pass

    def handleResources(self, request):
        """Handles a response if the user makes a request for the static page"""
        path = os.getcwd() + "/resources/" + request.path.replace("/static/","") 
        try:
            resource = open(path,'r')
        except IOError:
            response = HttpServerResponse(404, 'Not Found',  '<html><body><h1>Error!</h1><p><em>The page could not be found. Please check the URL.</em></p></body></html>')
            response.addHeader('Content-Type', 'text/html')
            return response

        response = HttpServerResponse(200, 'OK',  resource.read())

        resourceType = mimetypes.guess_type(path)
        response.addHeader('Content-Type',resourceType[0])
        return response


    def handleCGI(self,request):
        """Handles a response if the user makes a GET request to the CGI page"""
        try:
            query = request.path.split("?")
            param = query[1].split("&")
        except IndexError:
            response = HttpServerResponse(200, 'OK',  '<html><body><h2>No parameters were given.</h2></body></html>')
            response.addHeader('Content-Type', 'text/html')
            return response
        
        body = """<html><body><h2>Parameters:</h2><table border="2">"""

        for line in param:
            elem = line.split("=")
            body= body + "<tr><td>"+elem[0]+"</td><td>"+elem[1]+"</td></tr>"

        body= body + "</table></body></html>"
        response= HttpServerResponse(200,'OK',body)
        response.addHeader('Content-Type','text/html')
        return response    


    def dispatch(self, request):
        if request.path == '/ping':
            response = HttpServerResponse(200, 'OK', '<html><body>PONG!</body></html>')
            response.addHeader('Content-Type', 'text/html')
            return response

        elif request.path.startswith("/cgi"):
            return self.handleCGI(request)

        elif request.path.startswith("/static"):
            return self.handleResources(request)

        else:           
            response = HttpServerResponse(404, 'Not Found', '<html><body><h1>Error!</h1><p><em>The page could not be found. Please check the URL.</em></p></body></html>')
            response.addHeader('Content-Type', 'text/html')
            return response

            
if __name__ == '__main__':
    server = HttpServer(32342, Dispatcher())
    server.serve()