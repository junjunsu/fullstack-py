#简单并发实例
import socketserver
class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			conn = self.request
			print(self.client_address)

			c_address,c_port = self.client_address
			while True:
				client_data = conn.recv(1024)
				print(client_data.decode())
				print('waiting')
				server_response = input('>>>').strip()
				conn.sendall(server_response.encode(encoding='utf8'))
				#conn.sendall(client_data)
			conn.close()

if __name__ == '__main__':
	server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
	server.serve_forever()