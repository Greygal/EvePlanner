import unittest
from eveapi.cache_handler import CacheHandler

__author__ = 'apodoprigora'

class TestCacheHandler(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.cache_handler = CacheHandler()

    def test_initialized(self):
        self.assertIsNotNone(self.cache_handler)

    def test_store(self):
        self.cache_handler.store("host","path",[1,"test"],"a doc here", "obj")

if __name__ == '__main__':
    unittest.main()
