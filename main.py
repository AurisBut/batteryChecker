import psutil
from plyer import notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)

message = f"Battery is at {percent}%"
if plugged:
    message += " and charging."
else:
    message += " and not charging."

notification.notify(
    title="Battery Percentage",
    message=message,
    timeout=10
)
