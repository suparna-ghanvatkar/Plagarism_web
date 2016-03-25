'''
Created by: Suparna    www.github.com/suparna-ghanvatkar	
Web application to check plagarism. No installations required. 
Run this program in superuser mode and use url http://localhost/upload.html in browser
'''

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
	

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
		if self.path.endswith(".html"):	#renders the html file in current dir
			f= open(curdir + sep + self.path)	#sep makes the application os independent
			self.send_response(200)	#HTML headers
			self.send_header('Content-type',	'text/html')
			self.end_headers()
			self.wfile.write(f.read())	#read the HTML file desired and write it on output that is browser
			f.close()
			return 

    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            self.end_headers()
            text1 = query.get('text1')	#text1 and text2 are lists and not strings!
            text2 = query.get('text2')
            #logic to check plagarism
            matched_lines=[]
            count=0
            perc=0
            txt=text1[0].split(".")
            txt.remove('')
            sent=""
            for sent in txt:
                if sent in text2[0]:
                    count=count+1
                    matched_lines.append(sent)
            perc=count*100/len(txt)	#percentage wrt text 1
            self.wfile.write("Matched lines are:")
            self.wfile.write(matched_lines)
            self.wfile.write("Percentge of plagaraism is:")
            self.wfile.write(perc)	
            return		
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
