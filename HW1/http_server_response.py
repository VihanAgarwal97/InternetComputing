
class HttpServerResponse:
    def __init__(self, code, reason, body):
        self.code = code
        self.reason = reason
        self.body = body
        self.headers = {}
    
    def addHeader(self, field, value):
        field = str(field)
        value = str(value)
        # delete matching headers regardless of case
        for f in self.headers.keys():
            if f.lower() == field.lower():
                del(self.headers[f])
        self.headers[field.strip()] = value.strip()
    
    def __repr__(self):
        return `(self.code, self.reason, self.body, self.headers)`