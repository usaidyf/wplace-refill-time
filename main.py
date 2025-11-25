from datetime import datetime, timedelta

while True:
    charges = int(input("Enter charges remaining: "))

    # Remaining time = charges/2 minutes; each charge equals 30 seconds.
    # Display remaining time with days (if any), hours, minutes, and seconds.
    # Second line displays when the charges will refill in absolute time.

    remaining_seconds = int(charges * 30)
    refill_time = datetime.now() + timedelta(seconds=remaining_seconds)

    days, rem = divmod(remaining_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)

    print(
        f"Remaining time is {days} days {hours} hours {minutes} minutes {seconds} seconds"
    )

    print(
        "Charges will refill completely at", refill_time.strftime("%Y-%m-%d %H:%M:%S")
    )

    if input("Type 'y' and enter to rerun: ").lower() != "y":
        break
