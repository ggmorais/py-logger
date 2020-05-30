import schedule
import time
import email_controller
import input_controller

input_controller.listen()

schedule.every(1).day.at('12:00').do(email_controller.send)

while True:
  schedule.run_pending()
  time.sleep(1)
