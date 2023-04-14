class Codec:

    def __init__(self):
        self.tiny_url = {}
        self.url_tiny = {}
        self.counter = 1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.url_tiny:
            s = str(self.counter)
            self.url_tiny[longUrl] = s
            self.tiny_url[s] = longUrl
            self.counter += 1
            return s
        else:
            return self.url_tiny[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.tiny_url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))