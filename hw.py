import datetime

# Get today's date
today = datetime.date.today()

# Format the date as a string (e.g., 'YYYY-MM-DD')
date_str = today.strftime('%Y-%m-%d')

# Create a filename using today's date
filename = "today.txt"

# Write today's date to the file
with open(filename, 'w') as file:
    file.write(f"Today's date is: {date_str}\n")

print(f"Today's date has been saved to {filename}.")