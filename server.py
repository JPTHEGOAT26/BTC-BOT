# server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from buy_module import perform_market_buy

API_KEY = "iOxM61JCk07h50GA"
API_SECRET = "8DNiMeLfmcXAGf9b3tnT4NDHJRvKLVpO"

class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            json_data = json.loads(post_data.decode('utf-8'))

            if 'Buy BTC' in json_data and json_data['Buy BTC'] == 100:
                total_order_value = perform_market_buy(API_KEY, API_SECRET, 100)

                if total_order_value is not None:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response_data = {'message': f'Buy BTC command executed successfully. Total Order Value: {total_order_value}'}
                    self.wfile.write(json.dumps(response_data).encode('utf-8'))

            # Add other conditions for different JSON data as needed

        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'error': 'Invalid JSON data'}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

if __name__ == '__main__':
    httpd = HTTPServer(('', 8000), MyHandler)
    print("Server started on http://localhost:8000")
    httpd.serve_forever()
