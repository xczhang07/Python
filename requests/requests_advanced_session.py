# all requests made from session instance, and will use urllib3's connection pooling. so if you are making several
# requests to the same host, the underlying TCP connection will be reused, which can result in a significant performance
# increase.

# A Session object has all the methods of the main Requests API.

import requests
def session_persists_cookie(cookie):
    """
    demos the cookies can be persisted across requests
    :param cookie: string, a cookie set in the requests 
    :return: None
    """
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/%s' % cookie)
    resp = s.get('http://httpbin.org/cookies')
    print resp.text
    


if __name__ == "__main__":

    session_persists_cookie("Python")

# the output as following:
{
  "cookies": {
    "sessioncookie": "Python"
  }
}


def session_provides_default_data():
    """
    demo the session object can be used to set default data of the request.
    this has been set to the properties on a Session object
    Any dictionaries that you pass to a request method will be merged with the session-level values that are set. 
    The method-level parameters override session parameters.
    :return: 
    """
    s = requests.Session()
    s.auth = ("user", "pass")
    s.headers.update({'x-test':'true'})
    resp = s.get('http://httpbin.org/headers', headers={'x-test2':'true'})
    print resp.text

if __name__ == "__main__":

    session_provides_default_data()
    
# output as following:
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Authorization": "Basic dXNlcjpwYXNz", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.9.1", 
    "X-Test": "true", 
    "X-Test2": "true"
  }
}

def data_not_persist_across_requests_on_method_level():
    """
    Note, however, that method-level parameters will not be persisted across requests, even if using a session. 
    This example will only send the cookies with the first request, but not the second
    :return: 
    """
    s = requests.Session()
    resp = s.get('http://httpbin.org/cookies', cookies={'from-my':'browser'})
    print resp.text
    resp = s.get('http://httpbin.org/cookies')
    print resp.text

if __name__ == "__main__":
    data_not_persist_across_requests_on_method_level()
    
# output as following:
{
  "cookies": {
    "from-my": "browser"
  }
}

{
  "cookies": {}
}



