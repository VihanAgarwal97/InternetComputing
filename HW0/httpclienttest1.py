import unittest
import httpclient

class TestHttpClient(unittest.TestCase):
    
    def setUp(self):
        pass

    def testGetMethod(self):
        client = httpclient.HttpClient('www.npr.org', 80);
                
        response = client.doGet('/nonExistentPage')
        self.assertEquals(response.statusCode, 404)
        self.assertEquals(response.statusMessage.lower(), 'not found')

        response = client.doGet('/index.html')
        self.assertEquals(response.statusCode, 200)
        self.assertEquals(response.statusMessage, 'OK')
        self.assertEquals(response.headers['Content-Type'], 'text/html')
        self.assertTrue(response.body.find('National Public Radio') > 0)
    
if __name__ == '__main__':
    unittest.main()
