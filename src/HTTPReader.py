"""
Created on Feb 12, 2021

@author: cjkro

Use the http.client package to read the contents of the www.uci.edu top level
web page and print out the first 3 lines. You will need to use
http.client.HTTPSConnection() to make the connection to the
www.uci.eduweb page.

Then you will need to use conn.request("GET", "/") to send the get request.
Then use conn.getresponse() to extract the response and use the
read() method of the response to return the contents of the webpage.


"""
import http.client
import sys


def make_connection(url):
    """
    Make URL connection.

    inputs:
        url(str):  URL string
    returns:
        HTTP connection object
    """
    c = http.client.HTTPSConnection(url)
    c.connect()
    return c


def read_lines(conn, lines, mode):
    """
    Read <lines> lines from HTTP connection <conn>.

    inputs:
        conn(obj): HTTP connection
        lines(int): number of lines to read
        mode(int): 0 for read, 1 for readlines
    returns:
        None
    """
    try:
        print("sending GET")
        conn.request("GET", "/")
        print("requesting response")
        response = conn.getresponse()
        print("parsing response")
        for i in range(lines):
            # using readline here instead of read() so that newline
            # characters are recognized
            if mode == 0:
                response_line = response.read()
            else:
                response_line = response.readline()
            print("line %s=%s" % (i, response_line))
    finally:
        # close the connection
        conn.close()


if __name__ == '__main__':
    url = "www.uci.edu"  # URL string
    lines = 20  # number of lines to read

    # runtime mode
    if len(sys.argv) > 1 and sys.argv[1] in ['0', '1']:
        mode = int(sys.argv[1])  # mode, 0 for read(), 1 for readlines()
    else:
        mode = 0  # default is read()

    print("reading HTTP data from web site %s "
          "(%sparsing on newline characters)..." %
          (url, ["NOT ", ""][mode]))
    conn = make_connection(url)
    read_lines(conn, lines, mode)
