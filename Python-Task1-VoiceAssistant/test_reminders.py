import time

from reminders import set_reminder


def test_speak(message):
    print("ALERT:", message)


print("Setting a reminder for 5 seconds...")

set_reminder(
    5,
    "Test reminder is working.",
    test_speak
)

print("The main program is still running.")

time.sleep(7)

print("Test finished.")