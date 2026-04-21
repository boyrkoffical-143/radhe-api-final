from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        # ✅ Route
        if parsed.path == "/api/number":
            query = parse_qs(parsed.query)
            num = query.get("num", ["No number"])[0]

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()

            response = {
                "status": "success",
                "number": num,
                "name": "Radhe Gupta",
                "city": "Mithapur"
            }

            self.wfile.write(json.dumps(response).encode())

        # ✅ Root fix
        else:
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write("API Running ✅ Use /api/number")
