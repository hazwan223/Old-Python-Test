def add_time(start, duration, starting_day=None):
    # split the arguements
    starting_time, period_of_day = start.split(" ")
    starting_hour, starting_minutes = starting_time.split(":")
    duration_hour, duration_minute = duration.split(":")

    # add the variables
    hour = int(starting_hour) + int(duration_hour)
    minute = int(starting_minutes) + int(duration_minute)

    # excess time
    extra_hour = minute // 60
    minute %= 60
    hour += extra_hour

    # show in 12 hour format
    extra_half_day = hour // 12
    hour = hour % 12
    extra_day = extra_half_day // 2

    if period_of_day == "PM" and not extra_half_day % 2 == 0:  # if period PM and EHD is odd
        extra_day += 1
    if hour == 0:
        hour = 12

    hour_end = str(hour)
    minute_end = str(minute).rjust(2, "0")

    period = period_of_day
    if not extra_half_day % 2 == 0:  # if ehd odd
        if period == "AM":
            period = "PM"
        else:
            period = "AM"

    final = f"{hour_end}:{minute_end} {period}"

    if starting_day:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_day = starting_day.lower()
        start_index = days.index(start_day)
        end_index = (start_index + extra_day) % len(days)
        day_end = days[end_index]
        final += f", {day_end[0].upper()}{day_end[1:]}"  # To capitalize the first letter

    if extra_day == 1:
        final += f" (the following day)"
    if extra_day > 1:
        final += f", ({str(extra_day)} days in the future)"

    print(f"Time: {final}")
    print("-----------------")


add_time("11:43 PM", "2:20", "Monday")
add_time("11:43 PM", "13:20", "tuesday")
add_time("11:43 AM", "25:20", "thursday")
add_time("11:43 AM", "37:20", "Sunday")
