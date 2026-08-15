import threading
import time


def set_reminder(seconds, message, speak_function):
    def reminder_task():
        time.sleep(seconds)
        speak_function(f"Reminder: {message}")

    reminder_thread = threading.Thread(
        target=reminder_task,
        daemon=True
    )

    reminder_thread.start()