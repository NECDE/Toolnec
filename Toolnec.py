# coding=utf-8
# Toolnec v0.7
# Pequeño programa para acceder a utilidades en windows
# Algunas opciones solo están disponibles al abrir cmd como administrador
# By NECDE

import tkinter as tk
from tkinter import ttk
import os

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		# GENERAL
		self.w = tk.Label(self, text="GENERAL", fg="blue")
		self.w.grid(row=0, column=1)
		self.cinco = tk.Button(self, text="Msconfig", command=self.msconfig)
		self.cinco.grid(row=2, column=1)
		self.seis = tk.Button(self, text="Dxdiag", command=self.dxdiag)
		self.seis.grid(row=1, column=1)
		self.siete = tk.Button(self, text="Regedit", command=self.regedit)
		self.siete.grid(row=3, column=1)
		self.sep = tk.Button(self, text="----------------------------------------------", command=self.sepa)
		self.sep.grid(row=4, column=1)
		# NETWORK
		self.w = tk.Label(self, text="NETWORK", fg="blue")
		self.w.grid(row=5, column=1)
		self.uno = tk.Button(self, text="Visibles Wifi", command=self.scanwi)
		self.uno.grid(row=6, column=1)
		self.tres = tk.Button(self, text="Ipconfig", command=self.ipconfig)
		self.tres.grid(row=7, column=1)
		self.cuatro = tk.Button(self, text="Arp -a", command=self.arpa)
		self.cuatro.grid(row=8, column=1)
		self.ocho = tk.Button(self, text="Nslookup", command=self.nslookup)
		self.ocho.grid(row=9, column=1)
		self.dos = tk.Button(self, text="Ping Google.com", command=self.ping)
		self.dos.grid(row=10, column=1)
		self.nueve = tk.Button(self, text="Activar Firewall", command=self.fireon)
		self.nueve.grid(row=11, column=1)
		self.diez = tk.Button(self, text="Desactivar Firewall", command=self.fireoff)
		self.diez.grid(row=12, column=1)
		self.sep2 = tk.Button(self, text="----------------------------------------------", command=self.sepa)
		self.sep2.grid(row=13, column=1)
		# TXT
		self.w = tk.Label(self, text="SAVE TO FILE", fg="blue")
		self.w.grid(row=14, column=1)
		self.once = tk.Button(self, text="Services to txt", command=self.servicetxt)
		self.once.grid(row=15, column=1)
		self.doce = tk.Button(self, text="System Drivers to txt", command=self.sysdriverstxt)
		self.doce.grid(row=16, column=1)
		self.trece = tk.Button(self, text="Process to txt", command=self.processtxt)
		self.trece.grid(row=17, column=1)
		self.catorce = tk.Button(self, text="Computer sys to txt", command=self.computersys)
		self.catorce.grid(row=18, column=1)
		self.sep3 = tk.Button(self, text="----------------------------------------------", command=self.sepa)
		self.sep3.grid(row=19, column=1)
		# QUIT
		self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
		self.quit.grid(row=20, column=1)
		# self.cinco.pack(side="left")

		# ASDASDASD
	def sepa(self):
		print("Soy un boton que separa partes asbdlasdulfjasndask")
	def scanwi(self):
		os.system("netsh wlan show networks mode=Bssid")

	def ping(self):
		os.system("ping google.com")

	def ipconfig(self):
		os.system("ipconfig /all")

	def arpa(self):
		os.system("arp -a")

	def msconfig(self):
		os.system("msconfig")

	def dxdiag(self):
		os.system("dxdiag")

	def regedit(self):
		os.system("regedit")

	# Al terminar su consulta ingrese "quit" para salir de nslookup
	def nslookup(self):
		os.system("nslookup")

	# NECESITA PERMISOS DE ADMINISTRADOR
	def fireon(self):
		os.system("netsh advfirewall set currentprofile state on")

	# NECESITA PERMISOS DE ADMINISTRADOR
	def fireoff(self):
		os.system("netsh advfirewall set currentprofile state off")

	def servicetxt(self):
		os.system("wmic /OUTPUT:services.txt service get /all")

	def sysdriverstxt(self):
		os.system("wmic /OUTPUT:systemdrivers.txt sysdriver get /all")

	def processtxt(self):
		os.system("wmic /OUTPUT:process.txt process list full /format:table")

	def computersys(self):
		os.system("wmic /OUTPUT:computersystem.txt computersystem get /all /format:list")

print("\nPara salir de nslookup debe ingresar 'exit'\n")

root = tk.Tk()
app = Application(master=root)
app.master.title("Toolnec By NECDE")
app.master.maxsize(250, 550)
app.mainloop()
