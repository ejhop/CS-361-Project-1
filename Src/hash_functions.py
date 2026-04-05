# Implements Double Hashing with murmur
# Author: Harvey Ramoso

"""
MurmurHash3-based hashing for Bloom filters.
"""


class HashFunctions:
    """
    Pure Python MurmurHash3 (32-bit).
    """

    def __init__(self):
        pass

    def murmur3_32(self: str, seed: int = 0) -> int:
        data = bytearray(self.encode())
        length = len(data)
        nblocks = length // 4

        h = seed

        c1 = 0xcc9e2d51
        c2 = 0x1b873593

        # body
        for block_start in range(0, nblocks * 4, 4):
            k = (data[block_start + 3] << 24) | \
                (data[block_start + 2] << 16) | \
                (data[block_start + 1] << 8) | \
                (data[block_start + 0])

            k = (k * c1) & 0xffffffff
            k = ((k << 15) | (k >> 17)) & 0xffffffff
            k = (k * c2) & 0xffffffff

            h ^= k
            h = ((h << 13) | (h >> 19)) & 0xffffffff
            h = (h * 5 + 0xe6546b64) & 0xffffffff

        # tail
        tail = data[nblocks * 4:]
        k1 = 0

        if len(tail) == 3:
            k1 ^= tail[2] << 16
        if len(tail) >= 2:
            k1 ^= tail[1] << 8
        if len(tail) >= 1:
            k1 ^= tail[0]
            k1 = (k1 * c1) & 0xffffffff
            k1 = ((k1 << 15) | (k1 >> 17)) & 0xffffffff
            k1 = (k1 * c2) & 0xffffffff
            h ^= k1

        # finalization
        h ^= length
        h ^= (h >> 16)
        h = (h * 0x85ebca6b) & 0xffffffff
        h ^= (h >> 13)
        h = (h * 0xc2b2ae35) & 0xffffffff
        h ^= (h >> 16)

        return h

    """
    First hash function using a seed of 0
    """
    def hash1(self: str) -> int:
        return HashFunctions.murmur3_32(self, seed=0)

    """
    Second hash function using a seed of 1
    """
    def hash2(self: str) -> int:
        return HashFunctions.murmur3_32(self, seed=1)

    """
    Generate a bloom hash by double hashing using the 2 hash functions. k is
    the number of hash functions and m is the number of bits in array.
    """
    def bloom_hashes(self: str, k: int, m: int):
        h1 = HashFunctions.hash1(self)
        h2 = HashFunctions.hash2(self)
        return [(h1 + i * h2) % m for i in range(k)]


#     """
#     Tests hash functions
#     """
#     @staticmethod
#     def test_hash_functions():
#         print("Running hash function tests...\n")
#
#         k = 7
#         m = 1_000_000
#
#         x1 = "Happy"
#         x2 = "Easter"
#
#         # 1. Exactly k indices
#         idx1 = HashFunctions.bloom_hashes(x1, k, m)
#         print("1. Returned k indices:", len(idx1) == k, f"(got {len(idx1)})")
#
#         # 2. All indices in range
#         in_range = all(0 <= i < m for i in idx1)
#         print("2. All indices within [0, m):", in_range)
#
#         # 3. Deterministic
#         idx1_again = HashFunctions.bloom_hashes(x1, k, m)
#         deterministic = (idx1 == idx1_again)
#         print("3. Deterministic output:", deterministic)
#
#         # 4. Different inputs → different indices
#         idx2 = HashFunctions.bloom_hashes(x2, k, m)
#         different = (idx1 != idx2)
#         print("4. Different inputs give different indices:", different)
#
#         print("\nHash function tests complete.")
#
#
# HashFunctions.test_hash_functions()
