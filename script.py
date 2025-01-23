import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

SMTP_SERVER = config["SMTP"]["server"]
SMTP_PORT = int(config["SMTP"]["port"])
EMAIL_ADDRESS = config["SMTP"]["email"]
EMAIL_PASSWORD = config["SMTP"]["password"]

URL_FILE_PATH = config["URL"]["file_path"]
RECIPIENT_EMAIL = config["RECIPIENT"]["email"]
SUBJECT = config["RECIPIENT"]["subject"]
BODY = config["RECIPIENT"]["body"]

def send_mail(url):
    try:
        email_msg = MIMEMultipart()
        email_msg["From"] = EMAIL_ADDRESS
        email_msg["To"] = RECIPIENT_EMAIL
        email_msg["Subject"] = SUBJECT

        email_msg.attach(MIMEText(f"{BODY}{url}", "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(email_msg)

        print(f"E-mail sent to: {RECIPIENT_EMAIL}")
    except Exception as e:
        print(f"Error while sending email: {e}")

def check_url():
    try:
        with open(URL_FILE_PATH, "r") as file:
            url = file.readline().strip()

        if not url:
            print("File is empty or not valid.")
            return
        
        response = requests.head(url)
        if response.status_code == 200:
            print(f"File is available at: {url}")
            send_mail(url)
        elif response.status_code == 404:
            print("File still unavailable")
        else:
            print(f"Unexpected status code: {response.status_code}")

    except FileNotFoundError:
        print(f"File '{URL_FILE_PATH}' not found.")

    except requests.RequestException as e:
        print(f"Error while sending requests: {e}")

check_url()
