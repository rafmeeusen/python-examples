# parsing a json blockchain block file coming from 
# https://blockchain.info/rawblock/
# or:
# https://blockchain.info/block-height/
# DOC: https://www.blockchain.com/explorer/api/blockchain_api

# e.g. https://blockchain.info/rawblock/125552

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



# rawblocks vs block-height

if 'blocks' in jblk.keys():
    # guessing this is a blocks: hash - hash ... structure 
    blk = jblk['blocks'][0]
else:
    blk = jblk


prev_hash_xbe = blk['prev_block']
mrkl_root_xbe = blk['mrkl_root']
ver = blk['ver']
time = blk['time']
bits = blk['bits']
nonce = blk['nonce']

ver_b = ver.to_bytes(4,'little')
prev_hash_ble = bytes(reversed(unhexlify(prev_hash_xbe)))
mrkl_root_ble = bytes(reversed(unhexlify(mrkl_root_xbe)))
time_b = time.to_bytes(4,'little')
bits_b = bits.to_bytes(4,'little')
nonce_b = nonce.to_bytes(4,'little')

print('version hex:', hexlify(ver_b))
print('prev hash LE:', hexlify(prev_hash_ble))
print('mrkl root LE:', hexlify(mrkl_root_ble))
print('time hex:', hexlify(time_b))
print('bits hex:', hexlify(bits_b))
print('nonce hex:', hexlify(nonce_b))

#concat block header for hashing:
blk_hdr_b = ver_b + prev_hash_ble + mrkl_root_ble + time_b + bits_b + nonce_b 


blk_hash_b = hashlib.sha256( hashlib.sha256(blk_hdr_b).digest() ).digest()
#print('block hash BE:', hexlify(blk_hash_b))
print('block hash LE:', hexlify(bytes(reversed(blk_hash_b))))

