import json
from http.server import HTTPServer, BaseHTTPRequestHandler

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])
        return json.loads(self.rfile.read(content_length).decode('utf-8'))

    def do_GET(self):
        if self.path == "/reset":
            USERS_LIST.clear()
            USERS_LIST.append({
                "id": 1,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345",
            })
            self._set_response(200)
        elif self.path == "/users":
            self._set_response(200, USERS_LIST)
        elif self.path.startswith("/user/"):
            username = self.path.split("/")[-1]
            user = next((u for u in USERS_LIST if u["username"] == username), None)
            if user:
                self._set_response(200, user)
            else:
                self._set_response(400, {"error": "User not found"})
        else:
            self._set_response(404)

    def do_POST(self):
        if self.path == "/user":
            try:
                data = self._pars_body()
                if isinstance(data, dict):
                    USERS_LIST.append(data)
                    self._set_response(201, data)
                elif isinstance(data, list):
                    USERS_LIST.extend(data)
                    self._set_response(201, data)
                else:
                    self._set_response(400)
            except json.JSONDecodeError:
                self._set_response(400)
        elif self.path == "/user/createWithList":
            try:
                data = self._pars_body()
                if isinstance(data, list):
                    USERS_LIST.extend(data)
                    self._set_response(201, data)
                else:
                    self._set_response(400)
            except json.JSONDecodeError:
                self._set_response(400)
        else:
            self._set_response(404)

    def do_POST(self):
        if self.path == "/user":
            try:
                data = self._pars_body()
                if isinstance(data, dict):
                    if "id" not in data or all(u["id"] != data["id"] for u in USERS_LIST):
                        USERS_LIST.append(data)
                        self._set_response(201, data)
                    else:
                        self._set_response(400)
                elif isinstance(data, list):
                    if all("id" not in user or all(u["id"] != user["id"] for u in USERS_LIST) for user in data):
                        USERS_LIST.extend(data)
                        self._set_response(201, data)
                    else:
                        self._set_response(400)
                else:
                    self._set_response(400)
            except json.JSONDecodeError:
                self._set_response(400)
        elif self.path == "/user/createWithList":
            try:
                data = self._pars_body()
                if isinstance(data, list):
                    if all("id" not in user or all(u["id"] != user["id"] for u in USERS_LIST) for user in data):
                        USERS_LIST.extend(data)
                        self._set_response(201, data)
                    else:
                        self._set_response(400)
                else:
                    self._set_response(400)
            except json.JSONDecodeError:
                self._set_response(400)
        else:
            self._set_response(404)

    def do_DELETE(self):
        if self.path.startswith("/user/"):
            user_id = int(self.path.split("/")[-1])
            user = next((u for u in USERS_LIST if u["id"] == user_id), None)
            if user:
                USERS_LIST.remove(user)
                self._set_response(200)
            else:
                self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(404)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
