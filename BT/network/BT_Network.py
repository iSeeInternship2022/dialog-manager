import socket
#import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back


#DRAFT - Not currently in use
class BT_Network:




	def __init__(self, IP, port) -> None:
		# init colors
		init()

		# set the available colors
		colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
			Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
			Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
			Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
		]

		# choose a random color for the client
		self.client_color = Fore.LIGHTBLUE_EX

		# server's IP address
		# if the server is not on this machine, 
		# put the private (network) IP address (e.g 192.168.1.2)
		self.SERVER_HOST = IP
		self.SERVER_PORT = port # server's port
		self.separator_token = "<SEP>" # we will use this to separate the client name & message

		# initialize TCP socket
		self.s = socket.socket()
		print(f"[*] Connecting to {self.SERVER_HOST}:{self.SERVER_PORT}...")
		# connect to the server
		self.s.connect((self.SERVER_HOST, self.SERVER_PORT))
		print("[+] Connected.")


		# prompt the client for a name
		self.name = "ISee bot: "


		# make a thread that listens for messages to this client & print them
		#t = Thread(target=self.listen_for_messages)
		# make the thread daemon so it ends whenever the main thread ends
		#t.daemon = True
		# start the thread
		#t.start()


	def listen_for_messages(self):
		while True:
			message = self.s.recv(1024).decode()
			print("\n" + message)


	def send_message(self, message):
		# add the datetime, name & the color of the sender
		date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
		to_send = f"{self.client_color}[{date_now}] {self.name}{self.separator_token}{message}{Fore.RESET}"
		# finally, send the message
		self.s.send(to_send.encode())

	def endConnection(self):
		# close the socket
		self.s.close()


