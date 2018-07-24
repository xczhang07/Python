# concept of memcached: high-performance, distributed memory object caching system.
# official site: https://memcached.org
# how to install: on mac os: brew install memcached
# install python library (client app) to interact with memcached server: pip install pymemcache
''' after install memcached on your device, let us check the process with command " ps ef | grep "memc"(make sure your memcached
process is running, then you can use python library to interact with memcached server.)" 
    the result as following:
     501 10343     1   0 12:03AM ??         0:00.27 /usr/local/opt/memcached/bin/memcached -l localhost  <---
     501 11249 11241   0 12:33AM ttys003    0:00.00 grep memc
     
     then we use python following python code to interactive with the memcached server
     
     after running this script, you need to launch another terminal to check the memcached server data:
     
     telnet localhost 11211
     Trying ::1...
     Connected to localhost.
     Escape character is '^]'.
     get memcached
     VALUE memcached 0 11
     hello world
     END

'''



from pymemcache.client import base

def run_query_to_db(command):
  """in this function, you are able to use python code to interact with your backend database(mysql, mongodb, etc...),
  right now, we just return an simple result
  """
  print("running query on database, getting data from db...\n")
  return 100


def hit_cache_function(client, key):
"""this function perform the logic mode of the hit or miss memcached"""
  result = client.get(key)
  if result is None:
    result = run_wuery_to_db("select someting from table1 where user id equals sth")
    client.set(key, result)
  else:
    return result
  

if __name__ == "__main__":
  client = base.Client(('localhost', 11211))  # this is the localhost testing code, we use localhost, in production code, you may need to provide real ip and password
  client.set('memcached', 'Hello World')
  hit_cache_function(client, "math_score")
  
  
