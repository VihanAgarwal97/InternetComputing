#VIHAN AGARWAL
import socket
import string
import urllib

class HttpResponse:
    """
        Holds a structured http response.
        You will be responsible for translating an http response
        string into this structure.
    """
    def __init__(self):
        self.statusCode = 200
        self.statusMessage = 'OK'
        self.headers = {}
        self.body = ''
    
    def __repr__(self):
        return (
                'status=%s headers=%s body=%s...' %
                (self.statusCode, self.headers, self.body)
            )
        
class HttpClient:
    def __init__(self, host, port=80):
        """Constructs a new http client."""
        self.host = host
        self.port = port
    
    def doGet(self, path):
        """
            Executes an HTTP GET method and returns the result
            as an HttpResponse object.
        """
        sock = self._writeRequest(self._constructGetRequest(path))
        return self._readResponse(sock)
        
    def doPost(self, path, body):
        """
            Executes an HTTP POST method and returns the result
            as an HttpResponse object.
        """
        sock = self._writeRequest(self._constructPostRequest(path, body))
        return self._readResponse(sock)
    
    def doGetWithParams(self, path, params):
        """
            Executes an HTTP GET method and returns the result
            Params should be a dictionary of unencoded query parameters
            as an HttpResponse object.
        """
        newParams=urllib.urlencode(params)

        newPath = path + "?" + newParams 
        sock = self._writeRequest(self._constructGetRequest(newPath))
        return self._readResponse(sock)
    
    def doPostWithParams(self, path, params):
        """
            Executes an HTTP POST method and returns the result
            Params should be a dictionary of unencoded query parameters
            as an HttpResponse object.
        """
        newParams = urllib.urlencode(params)
        
        newPath = path + "?" + newParams
        sock = self._writeRequest(self._constructPostRequest(newPath,newParams))
        return self._readResponse(sock)
    
    def _constructGetRequest(self, path):
        """
            Returns a string containing an HTTP 1.0 GET request
            for self.host and the requested path.
        """
        return "GET " + path + " HTTP/1.0\nHost:" + str(self.host) + "\r\n\r\n"
    
    def _constructPostRequest(self, path, body):
        """
            Returns a string containing an HTTP 1.0 GET request
            for self.host and the requested path and body.
        """
        return "POST " + path + " HTTP/1.0\nHost:" + str(self.host) + "\nContent-Type:application/x-www-form-urlencoded\nContent-Length:" + str(len(body)) + "\r\n\r\n" + body
    
    def _writeRequest(self, request):
        """
            Creates a socket connected to the host and port
            Writes the request out and returns the socket object.
        """
        s = socket.socket()
        s.connect((self.host, self.port))
        s.send(request)
        return s
    
    def _readResponse(self, sock):
        """
            Reads in a response from a socket object.
            Returns a filled-in HttpResponse object.
        """
        responseLines = self._readResponseStr(sock).split('\r\n')
        response = HttpResponse()
        
        # fill in the member variables for the http response object
        # by parsing the responseLines list of strings
        status = responseLines[0].split(" ")
        response.statusCode = int(status[1])

        if len(status) == 4:
            response.statusMessage = status[2]+" "+status[3]
        else:
            response.statusMessage = status[2]

        index = 1

        for line in responseLines:
            if line =="":
                index = responseLines.index(line)
                break
            else:
                if "HTTP" not in line:
                    head = line.split(":")
                    response.headers[head[0]] = head[1].strip()

        response.body = responseLines[index+1]

        return response 
    
    def _readResponseStr(self, sock):
        """
            Reads in a response from a socket object.
            Returns the string contents of the response.
        """
        # Reads the response.
        # Since we are using HTTP 1.0, we can read until EOF
        bytesRead = 'foo'
        response = ''        
        while len(bytesRead) > 0: 
            bytesRead = sock.recv(1024)
            response += bytesRead
        return response    
    
if __name__ == '__main__':
    client1 = HttpClient('www.npr.org')
    print client1.doGet('/index.html')
    client1 = HttpClient('webapps.macalester.edu')
    print client1.doPost('/directory/search.cfm', 'Name=kyle')
