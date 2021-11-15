class Codec:
    def __init__(self):
        self.URLS = defaultdict(str)
        self.key = ""
        self.count = 0
        self.char = 'a'
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if not self.key:
            self.key = '0'
        if self.key[-1]=='9':
            self.key += self.char 
            self.char+= chr(self.char + 1)
            self.count = 0
        elif self.key[-1] == 'z':
            self.key += self.count
            self.count += 1
        elif self.key[-1] in '0123456789':
            self.key = self.key[:-1] + str(self.count)
            self.count += 1
        else:
            self.key = self.key[:-1] + self.char
            self.char += chr(self.char+1)
        self.URLS[self.key] = longUrl
        return self.key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.URLS[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))