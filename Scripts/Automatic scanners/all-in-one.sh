echo "Data for 23 to 30 March 2020:"
ssh $1@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2020/03/202003{23..30}:*.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i text' | python3 emoji2.py || true
echo "Data for 23 to 30 March 2019:"
ssh $1@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2019/03/201903{23..30}:*.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i text' | python3 emoji2.py || true
echo "Data for 21 to 28 January 2021:"
ssh $1@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2021/01/202101{21..28}:*.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i text' | python3 emoji2.py || true
echo "Data for 21 to 28 January 2019:"
ssh $1@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2019/01/201901{21..28}:*.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i text' | python3 emoji2.py || true