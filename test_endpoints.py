import unittest

from url_shortener_app import main, schemas, keygen

class TestEndpoints(unittest.TestCase):

    def test_encode(self):
        target_url = schemas.URLTarget(url="https://www.google.com/")
        short_url = main.create_url(target_url) # encode
        key = short_url.url.split("/")[-1]
        self.assertNotEqual(short_url.url, target_url.url)
        self.assertTrue(len(key), 5)
        pass

    def test_decode(self):
        key = "Test1"
        value = "https://example.com"
        keygen.url_dic = {key: value}
        request = f"http://localhost:8000/decode/{key}"
        target_url = main.get_target_url(key, request) # decode
        self.assertEqual(target_url.url, value)
        pass

    def test_forwarding(self):
        key = "Test1"
        request = f"http://localhost:8000/{key}"
        keygen.url_dic = {key: "https://www.google.com/"}
        res = main.forward_to_target_url(key, request) # forwarding
        self.assertEqual(res.status_code, 307)
        self.assertEqual(res.headers.raw[1][1], b'https://www.google.com/')
        pass


    ### Uncomment to test if wrong URLs throw HTTPExceptions ###

    # def test_bad_request(self):
    #     url = schemas.URLTarget(url="www.example.com")
    #     try:
    #         main.create_url(url) # encode
    #     except Exception as e:
    #         self.assertEqual(e.__class__.__name__, "HTTPException")
    #     pass

    # def test_not_found(self):
    #     key = "Test1"
    #     request = schemas.URLShort(url=f"http://localhost:8000/{key}")
    #     keygen.url_dic = {}
    #     try:
    #         main.forward_to_target_url(key, request) # forward
    #     except Exception as e:
    #         self.assertEqual(e.__class__.__name__, "HTTPException")
    #     pass

if __name__ == '__main__':
    unittest.main()
