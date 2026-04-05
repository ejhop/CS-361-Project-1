from hash_functions import HashFunctions

class BloomFilter:
    #initializes the bloomfilter with m bits and k hash functions
    def __init__(self, m, k):
        self.m=m
        self.k=k
        self.bitarray=[0]*m

    #inserts a bit into the bitarray at the indicies made in bloom_hashes
    def _set_bit(self, item):
        for i in HashFunctions.bloom_hashes(item, self.k, self.m):
            self.bitarray[i]=1

    #chescks if the bits at the indicies are all zero, if so returns 
    #false, otherwise returns true
    def _check_bit(self, item):
        for i in HashFunctions.bloom_hashes(item, self.k, self.m):
            if self.bitarray[i]==0:
                return False
        return True
    
if __name__ == "__main__":
    m = 1000 
    k = 6    

    BF = BloomFilter(m, k)
    BF._set_bit("hello")
    BF._set_bit("world")
    BF._set_bit("password123")
    BF._set_bit("daffyduck")
    #print(BF.bitarray)
    print(BF._check_bit("daffyduck"))  
    print(BF._check_bit("wrong"))
