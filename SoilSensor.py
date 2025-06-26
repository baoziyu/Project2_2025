import RPi.GPIO as GPIO
import time

SENSOR_PIN = 4
POLL_INTERVAL = 2
DRY_THRESHOLD = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def get_moisture_status():
  return GPIO.input(SENSOR_PIN)

def main():
  dry_count = 0
  last_status = None

  try:
    print("Start...")
    print("press Ctrl+C to exit")

    while True:
      current_status = get_moisture_status()
      if current_status != last_status:
        if current_status:
          print("No Water Detected!")
        else:
          print("Water Detected")
        last_status = current_status

      if current_status:
        dry_count += 1
        if dry_count >= DRY_THRESHOLD:
          print("Warning!Need Watering")
      else:
        dry_count = 0

      time.sleep(POLL_INTERVAL)

  except KeyboardInterrupt:
    print("\nEnd")
  finally:
    GPIO.cleanup()

if __name__ == "__main__":
  main()
