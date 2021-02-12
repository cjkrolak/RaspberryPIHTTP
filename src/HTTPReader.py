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


def make_connection(url):
    """
    Make URL connection.

    inputs:
        url(str):  URL string
    returns:
        HTTP connection object
    """

    conn = http.client.HTTPConnection(url)
    # conn = http.client.HTTPSConnection(url)
    print("conn=" + str(conn))
    conn.connect()
    return conn


def read_lines(conn, lines):
    """
    Read <lines> lines from HTTP connection <conn>.

    inputs:
        conn(obj): HTTP connection
        lines(int): number of lines to read
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
            response_line = response.readline()
            print("line %s=%s" % (i, response_line))
    finally:
        # close the connection
        conn.close()


if __name__ == '__main__':
    url = "www.uci.edu"  # URL string
    lines = 1000  # number of lines to read
    conn = make_connection(url)
    read_lines(conn, lines)
