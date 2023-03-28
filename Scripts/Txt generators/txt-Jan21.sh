ssh $1@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2021/01/202101{21..28}:*.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i text' >> 21-28Jan2021.txt || true
