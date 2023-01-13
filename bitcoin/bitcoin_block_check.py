# parsing a json blockchain block file coming from 
# https://blockchain.info/rawblock/
# DOC: https://www.blockchain.com/explorer/api/blockchain_api
# e.g. https://blockchain.info/rawblock/125552


# note:
# There is something weird with blockchain representation of hash values (byte order).
# Many sources mention the 'endianness' of the hash digest. Imho this is confusing.
# I checked the FIPS spec on sha256: the hash output is a concatenation of 32-bit words,
# no mentioning of a 256-bit integer, no least or most signifant byte in this 256-bit digest
# Mentioning of endianess in FIPS spec is only about 32-bit and 64-bit words:
# Throughout this specification, the “big-endian” convention is used when expressing
# both 32- and 64-bit words, so that within each word, the most significant bit is stored
# in the left-most bit position.
# So let's assume the BE notation of a hash value is as in the NIST spec (H[0] first/left),
# and the LE notation of a hash value is with all (256/8) bytes in reverse order.

# see also https://en.bitcoin.it/wiki/Block_hashing_algorithm
# although I'm not sure that I agree with the endianess meaning there

# my own semantics with respect to byte order of hash values:
# hash "normal" = byte array as returned by hashlib
# hash "reversed" = byte array in reversed byte order

import json
import hashlib
from binascii import unhexlify, hexlify
import sys

nrargs = len(sys.argv)
if nrargs != 2:
    print('Error, need file name')
    exit(66)

filename = sys.argv[1]

try:
    f = open(filename)
    jblk = json.load(f)
except Exception as e:
    print('Error: exception in opening or reading json file')
    print(e)
    exit(77)

blk = jblk

# blockchain json format: 
# hash values are hex strings in reversed byte order (e.g. "00000000841cb802ca97cf20fb9470480cae9e5daa5d06b4a18ae2d5dd7f186f")
# version, time etc. are integers
prev_hash_reversed = blk['prev_block']
mrkl_root_reversed = blk['mrkl_root']
ver = blk['ver']
time = blk['time']
bits = blk['bits']
nonce = blk['nonce']

assert( type(prev_hash_reversed) == str)
assert( type(mrkl_root_reversed) == str)
assert( type(ver) == int)
assert( type(time) == int)
assert( type(bits) == int)
assert( type(nonce) == int)

# convert all to bytes format needed for block header hashing: 
# hash bytes in normal order again, and ints in little endian byte array
prev_hash = bytes(reversed(unhexlify(prev_hash_reversed)))
mrkl_root = bytes(reversed(unhexlify(mrkl_root_reversed)))
ver_b = ver.to_bytes(4,'little')
time_b = time.to_bytes(4,'little')
bits_b = bits.to_bytes(4,'little')
nonce_b = nonce.to_bytes(4,'little')

print('version hex:', hexlify(ver_b))
print('prev hash LE:', hexlify(prev_hash))
print('mrkl root LE:', hexlify(mrkl_root))
print('time hex:', hexlify(time_b))
print('bits hex:', hexlify(bits_b))
print('nonce hex:', hexlify(nonce_b))

# concat block header for hashing:
blk_hdr_b = ver_b + prev_hash + mrkl_root + time_b + bits_b + nonce_b 
# double sha256:
blk_hash_b = hashlib.sha256( hashlib.sha256(blk_hdr_b).digest() ).digest()

print('block hash normal byte order:', hexlify(blk_hash_b))
print('block hash reversed byte order:', hexlify(bytes(reversed(blk_hash_b))))

