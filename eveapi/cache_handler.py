import hashlib
import time
import tempfile
import pickle
import zlib
import os
from os.path import join, exists


class CacheHandler(object):
    #TODO should be thread-safe and handle errors properly.

    def __init__(self, debug=False, trace=False):
        self.debug = debug
        self.trace = trace
        self.count = 0
        self.cache = {}
        self._init_temp_dir()

    def _init_temp_dir(self):
        self.tempdir = join(tempfile.gettempdir(), "eveapi")
        self._trace(self.tempdir)
        if not exists(self.tempdir):
            os.makedirs(self.tempdir)

    def get_string_of(self, params):
        """
        Due the properties of dict, ensure that the keys are stored in the same order.
        """
        result = ""
        if "keyID" in params:
            result += str(params["keyID"])
        if "vCode" in params:
            result += str(params["vCode"])
        if "characterID" in params:
            result += str(params["characterID"])
        return result

    def get_hash_of(self, host, params, path):
        result = self.get_string_of(params)
        hash_sum = hashlib.sha1(pickle.dumps((host, path, result))).hexdigest()[0:32]
        return hash_sum

    def _get_cached_file_by(self, key):
        return join(self.tempdir, str(key) + ".cache")

    def _try_to_load_from_disk(self, key, path):
        cached = None
        cacheFile = self._get_cached_file_by(key)
        if exists(cacheFile):
            self._debug("%s: retrieving from disk" % path)
            f = open(cacheFile, "rb")
            cached = self.cache[key] = pickle.loads(zlib.decompress(f.read()))
            f.close()
        return cached

    def _ensure_cache_in_memory(self, key, path):
        # see if we have the requested page cached...
        cached = self.cache.get(key, None)
        if not cached:
            cached = self._try_to_load_from_disk(key, path)
        return cached

    def _purge_data_by_key(self, key):
        del self.cache[key]
        cacheFile = self._get_cached_file_by(key)
        if cacheFile:
            os.remove(cacheFile)

    def retrieve(self, host, path, params):
        key = self.get_hash_of(host, params, path)
        self._debug("Retrieving key : %s" % key)
        self.count += 1  # for logging
        cached = self._ensure_cache_in_memory(key, path)

        if cached:
            # check if the cached doc is fresh enough
            self._debug("Current time : %d, cached on %s" % (time.time(), cached[0]))
            if time.time() < cached[0]:
                self._debug("%s: returning cached document" % path)
                return cached[1]  # return the cached XML doc
            else:
                self._debug("%s - Purging cache" % path)
                self._purge_data_by_key(key)

        self._debug("%s: not cached, fetching from server..." % path)
        return None

    def store(self, host, path, params, doc, obj):
        key = self.get_hash_of(host, params, path)
        self._debug("Store key : %s" % key)

        cachedFor = obj.cachedUntil - obj.currentTime
        if cachedFor:
            self._debug("%s: cached (%d seconds)" % (path, cachedFor))
            cachedUntil = time.time() + cachedFor
            cached = self.cache[key] = (cachedUntil, doc)

            # store in cache folder
            cacheFile = join(self.tempdir, str(key) + ".cache")
            f = open(cacheFile, "wb")
            f.write(zlib.compress(pickle.dumps(cached, -1)))
            f.close()

    def purge_all_caches(self):
        keys = list(self.cache.keys())
        for key in keys:
            self._purge_data_by_key(key)
        assert len(self.cache) == 0, "All caches should be purged!"

    def _debug(self, what):
        if self.debug:
            print("[%d] %s" % (self.count, what))

    def _trace(self, message):
        if self.trace:
            print("[%d] %s" % (self.count, message))
