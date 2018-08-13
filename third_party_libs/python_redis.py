"""
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. 
It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. 
Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, 
and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.
https://redis.io/topics/introduction

install redis on mac os:
brew install redis

start redis server on your local mac device:
brew services start redis

install python redis client:
sudo pip install redis
"""

$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0)
>>> r.set('foo','bar')
True
>>> r.get('foo')
'bar'
>>> r.set('num',10)
True
>>> r.get('num')
'10'
>>> r.incr('num')
11
>>> r.get('num')
'11'
>>> r.incrby('num',5)
16

at the mean time, we use command: "telnet localhost 6379" to connect with the redis server to verify the data we insert into redis server
Xiaochongs-MacBook-Pro:~ xiaochongzhang$ telnet localhost 6379
Trying ::1...
Connected to localhost.
Escape character is '^]'.
get foo
$3
bar
clear
-ERR unknown command `clear`, with args beginning with: 
get bar
$-1
get kkk
$-1
get foo
$3
bar
get num
$2
11
get num
$2
16

mget and mset
>>> r.mset(first_num=1, second_num=2, third_num=3)
True
>>> r.get(first_num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'first_num' is not defined
>>> r.get('first_num')
'1'
>>> r.mget('second_num','third_num')
['2', '3']
>>> r.mget('second_num','third_num','first_num')
['2', '3', '1']

exist
>>> r.exists('foo')
True
>>> r.exists('bar')
False

delete
>>> r.delete('foo')
1
>>> r.get('foo')

expire
>>> r.expire('first_num',10)
True
>>> r.get('first_num')
'1'
>>> r.get('first_num')
>>> r.get('first_num')

redis list
>>> r.lpush('list1',1)
1L
>>> r.lpush('list1',2,5,4)
4L
>>> r.lrange('list1',0,-1)
['4', '5', '2', '1']

get the list1 in redis console as following:
lrange list1 0 -1
*4
$1
4
$1
5
$1
2
$1
1

redis hashes
>>> r.hmset('adminstrator',{'name':'Bob','age':45})
True
>>> r.hgetall('adminstrator')
{'age': '45', 'name': 'Bob'}
>>> r.hget('adminstrator','name')
'Bob'
>>> r.hget('adminstrator','age')
'45'

