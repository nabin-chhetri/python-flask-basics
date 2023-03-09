from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect a DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



# WebServerHandler class inherits from BaseHTTPRequestHandler
class WebServerHandler(BaseHTTPRequestHandler):
    
    # Handle GET requests
    def do_GET(self, menu_id=None):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(bytes(output, "utf8"))
                return
            
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output  =   "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                output +=   "</body></html>"
                self.wfile.write(bytes(output, "utf8"))
                return
            
            
            if self.path.endswith("/menuitems"):
                menuitems = session.query(MenuItem).all()
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output += "<html><body>"
                for menuitem in menuitems:
                    output += menuitem.name
                    output += "</br>"
                output += "</body></html>"
                self.wfile.write(bytes(output, "utf8"))
                return
            
            if self.path.endswith("/menuitem/<int:menu_id>"):
                if menu_id is not None:
                    menuitem = session.query(MenuItem).filter_by(id=menu_id)
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output += "<html><body>"
                output += "menuitem"
                output += "</body></html>"
                self.wfile.write(bytes(output, "utf8"))
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
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
            
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

