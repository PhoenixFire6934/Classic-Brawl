import logging
import socket
import time
import os
from threading import *

from Logic.Device import Device
from Logic.Player import Players
from Packets.Factory import packets
from Utils.Config import Config

logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")


def _(*args):
	print('[INFO]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()


class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		if not os.path.exists('./data.db'):
			open('data.db', 'w').close()
		if not os.path.exists('./config.json'):
			print("Creating config.json...")
			Config.create_config(self)



		self.server.bind((self.ip, self.port))
		_(f'Server started! Ip: {self.ip}, Port: {self.port}')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			_(f'New connection! Ip: {address[0]}')
			ClientThread(client, address).start()


class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)

					if packet_id in packets:
						_(f'Received packet! Id: {packet_id}')
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()
					else:
						_(f'Packet not handled! Id: {packet_id}')

				if time.time() - last_packet > 10:
					print(f"[INFO] Ip: {self.address[0]} disconnected!")
					self.client.close()
					break
		except ConnectionAbortedError:
			print(f"[INFO] Ip: {self.address[0]} disconnected!")
			self.client.close()
		except ConnectionResetError:
			print(f"[INFO] Ip: {self.address[0]} disconnected!")
			self.client.close()
		except TimeoutError:
			print(f"[INFO] Ip: {self.address[0]} disconnected!")
			self.client.close()


if __name__ == '__main__':
	server = Server('0.0.0.0', 9339)
	server.start()