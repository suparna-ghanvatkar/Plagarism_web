import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

matched_lines=""
text1=""
text2=""
perc=0

def plag():
	global text1,text2,matched_lines,perc
	

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
		if self.path.endswith(".html"):
			f= open(curdir + sep + self.path)
			self.send_response(200)
			self.send_header('Content-type',	'text/html')
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
			return 

    def do_POST(self):
        global matched_lines,perc,text1,text2
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            text1 = query.get('text1')
            text2 = query.get('text2')
            self.wfile.write(matched_lines)
            self.wfile.write(perc)			
        except :
            pass

def main():
	try:
		server = HTTPServer(('', 80), MyHandler)
		print 'started httpserver...'
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C received, shutting down server'
		server.socket.close()

if __name__ == '__main__':
	main()






