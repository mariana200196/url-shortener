import unittest

from url_shortener_app import config, schemas, keygen

class TestConfig(unittest.TestCase):

    def test_get_settings(self):
        settings = config.get_settings()
        self.assertEqual(settings.env_name, "Local")
        self.assertEqual(settings.base_url, "http://localhost:8000")
        pass

class TestSchemas(unittest.TestCase):

    def test_url_short(self):
        url="https://www.something.com/12345"
        url_short = schemas.URLShort(url=url)
        self.assertEqual(url_short.url, url)
        pass

    def test_url_target(self):
        url="https://www.google.com"
        url_target = schemas.URLTarget(url=url)
        self.assertEqual(url_target.url, url)
        pass

class TestKeyGen(unittest.TestCase):

    def test_create_key(self):
        key = keygen.create_key()
        self.assertTrue(len(key), 5)
        self.assertTrue(type(key), str)
        pass

    def test_create_unique_key(self):
        key = keygen.create_key()
        url_dic = {key: "www.example.com"}
        while key in url_dic:
            key = keygen.create_key()
        key_in_dic = list(url_dic.keys())[0]
        self.assertNotEqual(key_in_dic, key)
        pass

    def test_add_key(self):
        url_target = schemas.URLTarget(url="https://www.google.com")
        key = "Test1"
        keygen.add_key(url_target, key)
        self.assertEqual(keygen.url_dic, {key: url_target.url})
        pass

    def test_lookup_key(self):
        key = "Test1"
        value = "www.example.com"
        keygen.url_dic = {key: value}
        lookup = keygen.lookup_key(key)
        self.assertEqual(lookup, value)
        pass

    def test_lookup_error(self):
        key = "Test1"
        keygen.url_dic = {"Other": "www.something.com"}
        lookup = keygen.lookup_key(key)
        self.assertEqual(lookup, None)
        pass

if __name__ == '__main__':
    unittest.main()
