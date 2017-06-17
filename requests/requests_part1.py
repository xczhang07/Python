# requests is a Python module you can use to send all kinds of HTTP requests.
# It is an easy to use library with a lot of features ranging from passing parameters in URLs to sending
# custom headers and SSL verification.


import requests   # the requests module needs to be imported first of all
from requests.auth import HTTPBasicAuth

def simple_get_request_101(url):
    """
    make an easy get request to the url with requests library.
    and go through some information of the response
    :param url: string, the url which is going to make request
    """
    print "make GET request to url(%s)" % url
    resp = requests.get(url, stream=True)

    # encoding response in 'utf-8' format
    resp.encoding

    # get the status code
    status_code = resp.status_code
    print "status code is: %d" % status_code

    # access headers of response, the returned header is a case insensitive dictionary
    # In this case, it means all of resp.headers['Server'], resp.headers['server'], and resp.headers['HEADERS']
    # will return GitHub.com
    print "response headers is: \n"
    for key in resp.headers:
        print key, ":", resp.headers[key]

    # access text of response, we could use resp.text(if the webpage is based text),resp.content(binary form)
    # resp.json()(if the content encoded through json)

def download_large_files(url):
    """
    this function demos how to download large file with requests library.
    In this case, the function downloading a picture from the input url
    :param url: string, the url of the large file, eg, a picture
    """
    # It is not wise to load the whole response or the file
    # in the memory at once if you download the file has a huge size
    # In this case, we bring a function iter_content(chunk_size=1, decode_unicode=False) in concept
    # this function can download a huge resource in pieces or chunks, it will iterate over the response data
    # in chunk_size number of bytes at once. When stream=True has been set on the request, this method
    # will avoid reading the whole file into memory at once for large response.

    # the chunk_size parameter can be either integer or None, the relationship between chunk_size and stream
    # as following:
    # chunk_size    stream
    #    None        True        data will be read as it arrives in whatever size of chunks are received
    #    None        False       all the data will be returned in a single chunk
    #    Integer     True        chunk_size determines the number of bytes that should be read into memory
    #    Integer     False       all the data will be returned in a single chunk
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open("Night_Moon.jpg", "wb") as fd:
        for chunk in resp.iter_content(chunk_size=50000):
            print ('received a chunk\n')
            fd.write(chunk)

def simple_post_request_101(url, search_contents):
    """
    this function demos how to make a simple post request to the input url.
    :param url: string, the url of the input webpage which is going to be searched contents
    :param search_contents: string, searched contents
    """
    resp = requests.post(url, data={'search': search_contents})
    resp.raise_for_status()
    with open("search_result.html", "wb") as fd:
        for chunk in resp.iter_content(chunk_size=50000):
            fd.write(chunk)

if __name__ == "__main__":
    simple_get_request_101("https://github.com/xczhang07")
    download_large_files("http://images5.fanpop.com/image/photos/26600000/Beautiful-World-Art-sesshyswind-26642810-1280-1024.jpg")
    simple_post_request_101("https://en.wikipedia.org/w/index.php", "Hello World")

