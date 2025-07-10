import pywhatkit as kit
import datetime

# Set phone number with country code (example: +91 for India)
phone_number = '+917232001202'  # Replace with actual number
message = 'Hello! This is a test message from Python.'

# Set time 1 minute ahead of current time
now = datetime.datetime.now()
send_hour = now.hour
send_minute = now.minute + 1



# Send the message
kit.sendwhatmsg(phone_number, message, send_hour, send_minute)
