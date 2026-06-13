from datetime import datetime

today = datetime.now().strftime("%d-%m-%Y")
time_now = datetime.now().strftime("%H:%M:%S")

message = f"""
========================
      PULSE BOT
========================

Date : {today}
Time : {time_now}

Daily Status:
✓ Bot Started
✓ System Healthy
✓ Automation Complete

Motivation:
"Keep learning and keep building."

========================
"""

print(message)

with open("pulse_report.txt", "w") as file:
    file.write(message)