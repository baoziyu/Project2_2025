import smtplib
from email.message import EmailMessage
import ssl

FROM_EMAIL = "15862640154@163.com"
APP_PASSWORD = "SF5JrbRwpe8w3fHb"
TO_EMAIL = "2643375817@qq.com"

def send_plant_email(status, plant_name="666"):

  try:
    msg = EmailMessage()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL


    if status == "dry":
      msg['Subject'] = f' {666}needs watering!'
      content = f"Your{666}soil is dry，please water it！\n\n"
    else:
      msg['Subject'] = f'✅ {666}is good'
      content = f"Your{666}soil is moist，not needing water.\n"


    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg.set_content(content + f"Detection Time: {timestamp}")

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.163.com', 465, context=context) as server:
      server.login(FROM_EMAIL, APP_PASSWORD)
      server.send_message(msg)

    print(f"Sent Successfully: {msg['Subject']}")
    return True

  except Exception as e:
    print(f"Fall in send: {e}")
    return False

if __name__ == "__main__":

  send_plant_email("dry", "Test plant")
