import RPi.GPIO as GPIO
import time
import datetime
from send_email import send_plant_email

SENSOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

CHECK_TIMES = ["03:11", "03:12", "03:13", "03:14"]

PLANT_NAME = "666"

def check_moisture():
  return GPIO.input(SENSOR_PIN)

def main():
  sent_today = []

  try:
    print(f"Plant monitoring system activated - :Monitor {666}")
    print(f"Detection Time: {', '.join(CHECK_TIMES)}")
    print("Press Ctrl+C to Exit")

    while True:
      now = datetime.datetime.now()
      current_time = now.strftime("%H:%M")
      current_date = now.strftime("%Y-%m-%d")

      if not sent_today or sent_today[0].split()[0] != current_date:
        sent_today = []
        print(f"New Day: {current_date}")

      if current_time in CHECK_TIMES and current_time not in [t.split()[1] for t in sent_today]:

        is_dry = check_moisture()
        status = "dry" if is_dry else "wet"

        print(f"{current_time} detect: soil{'dry' if is_dry else 'moist'}")


        if send_plant_email(status, PLANT_NAME):

          sent_today.append(f"{current_date} {current_time}")

          with open("plant_monitor.log", "a") as log:
            log.write(f"{current_date} {current_time} - Status: {'dry' if is_dry else 'moist'}\n")

      time.sleep(30)

  except KeyboardInterrupt:
    print("\nTerminate")
  finally:
    GPIO.cleanup()

if __name__ == "__main__":
    main()

