import datetime

# Get today's date and time
now = datetime.datetime.now()

# format date and time
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Create a filename using today's date
filename = "today.txt"

# Write today's date to the file
with open(filename, 'w') as file:
    file.write(f"Today's date is: {date_str}\n")

print(f"Today's date has been saved to {filename}.")