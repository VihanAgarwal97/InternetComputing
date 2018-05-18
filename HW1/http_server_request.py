                  
class HttpServerRequest:
    def __init__(self, method, path, headers={}, body=None):
        self.method = method
        self.path = path
        self.body = body
        self.headers = headers
    
    def getResource(self):
        return self.resource
        
    def getHeaders(self):
        return self.headers
    
    def getBody(self):
        return self.body
    
    def __repr__(self):
        return `(self.method, self.path, self.body, self.headers)`