for blk in 125550 125551 125552 125553  ; do
    wget https://blockchain.info/rawblock/$blk -O $blk.raw.json
done

