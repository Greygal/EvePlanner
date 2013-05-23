from datetime import timedelta
import unittest
import time
from eveapi.cache_handler import CacheHandler

__author__ = 'apodoprigora'
debug = True
hash_code = "dfab227d20f3abffad5d5473337064b8"


class Obj(object):
    def __init__(self, currentTime, cachedUntil):
        self.cachedUntil = cachedUntil
        self.currentTime = currentTime


class TestCacheHandler(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.host = "host"
        self.path = "/path/path"
        self.params = {"keyID": "keyABC", "vCode": "1YvdXjzmgDz3NFcEkbad5d5tk70wSYRmbQGnAVyreOePcE2ErNY2XIgs2MkA",
                       "characterID": "character1"}
        self.doc = "a doc here"
        self.obj = Obj(time.time(), time.time() + 3)

    def test_hash_key(self):
        for i in range(1000):
            dictionary = dict(self.params)
            result = CacheHandler(debug=debug).get_hash_of(self.host, dictionary, self.path)
            self.assertEqual(hash_code, result)

    def test_store_retrieve(self):
        CacheHandler(debug=debug).store(self.host, self.path, self.params, self.doc, self.obj)
        time.sleep(2)
        result = CacheHandler(debug=debug).retrieve(self.host, self.path, self.params)
        self.assertIsNotNone(result)
        self.assertEqual(self.doc, result)

    def test_retrieve_expire(self):
        result = CacheHandler(debug=debug).retrieve(self.host, self.path, self.params)
        self.assertIsNone(result)
        CacheHandler(debug=debug).store(self.host, self.path, self.params, self.doc, self.obj)
        time.sleep(3)
        result = CacheHandler(debug=debug).retrieve(self.host, self.path, self.params)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
