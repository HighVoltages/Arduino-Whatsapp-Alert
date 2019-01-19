# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import serial
import time
ser = serial.Serial('COM13', 9600)


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'account sid'
auth_token = 'auth token'
client = Client(account_sid, auth_token)


while True:
    while ser.inWaiting():
        temp = ser.readline().decode()
        messageTosend="Alert!!! The temp is "+str(temp)+"."
        message = client.messages.create(
                              body=messageTosend,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+92XXXXXXXXX'
                          )
        time.sleep(10)

print(message.sid)