# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# BaseHTTPServer for Python 2 and http.server for Python 3
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# WebServerHandler class inherits from BaseHTTPRequestHandler
class WebServerHandler(BaseHTTPRequestHandler):
    
    # Handle GET requests
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output = ""
                output += "<html><body>Hello!</body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
                <h2>What would you like me to say?</h2><input name='message' \
                type='text'><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                # self.wfile.write(output) # TypeError: a bytes-like object is required, not 'str'
                self.wfile.write(bytes(output, "utf8")) # Convert the string to bytes and use utf8 encoding
                print(output)
                return
            
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                message = ""
                message += "<html><body>!Hola!</body></html>"
                message += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
                <h2>What would you like me to say?</h2><input name='message' \
                type='text'><input type='submit' value='Submit'> </form>"
                message += "</body></html>"
                self.wfile.write(bytes(message, "utf8"))
                print(message)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
    
    #   HAndle POST requests
    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ctype, pdict = cgi.parse_header(
                self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            
            output = ""
            output += "<html><body>"
            output += "<h2> Okay how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            # output += f"<h1> {messagecontent[0]}</h1>"
            output += "<form method='POST' enctype='multipart/form-data' action='/hello'> \
                <h2>What would you like me to say?</h2><input name='message' \
                type='text'><input type='submit' value='Submit'> </form>"
            output += "</body></html>"
            self.wfile.write(bytes(output, "utf8"))
            print(output)
            # return
            
        except:
            pass
            
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        # server = HTTPServer(('', port), BaseHTTPRequestHandler)
        print(f"Web Server running on port {port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == "__main__":
    main()


