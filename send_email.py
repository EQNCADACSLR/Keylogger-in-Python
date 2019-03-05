# Import all modules necesaries.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# Function that sends an email.
def send_mail(sender, addressee, message, password):
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(sender, password)
	server.sendmail(sender, addressee, message)
	server.quit()
	print("Email send!")


# Function that send an file.
def send_file(sender, addressee, file, password):
	multi = MIMEMultipart()
	document = MIMEBase('application', "octet-stream")
	document.set_payload(open(file, "rb").read())
	encoders.encode_base64(document)
	document.add_header('Content-Disposition', "attachment; filename=file.tar.gz")
	multi.attach(document)

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(sender, password)
	server.sendmail(sender, addressee, multi.as_string())
	server.quit()
	print("File send!")
