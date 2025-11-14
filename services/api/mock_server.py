from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def _send(self, payload):
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_GET(self):
        if self.path.startswith('/v1/dashboard'):
            payload = {'xp_total':120,'level':3,'streaks':[{'habit':'Ejercicio','days':5}],'routine_today':{'id':'r1','title':'Rutina Mañana','steps_completed':1,'steps_total':4},'oracle_available':True}
            self._send(payload)
        elif self.path.startswith('/v1/routines'):
            payload = [{'id':'r1','title':'Rutina Mañana','steps':[{'id':'s1','title':'Estirar','duration_sec':60,'xp':10,'completed':False}]}]
            self._send(payload)
        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        if self.path.startswith('/v1/oracle/play'):
            payload = {'result':'win','xp_bonus':5,'coin_bonus':10,'message':'El oraculo te sonríe','cooldown_remaining':86400}
            self._send(payload)
        else:
            self.send_response(404); self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0',8000), Handler)
    print('Mock server running on http://localhost:8000')
    server.serve_forever()
