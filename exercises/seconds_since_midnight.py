def seconds_since_midnight(input_hour, input_minutes, input_seconds):
    """Returns the number of seconds since midnight.
    
    Parameters:
    input_hour (int) - current hour of the day.
    input_minutes (int) - current minutes of the day.
    input_seconds (int) - current seconds of the day.
    """

    # convert input hours to seconds
    hour_in_seconds = input_hour * 60 * 60
    # convert input minutes to seconds
    minute_in_seconds = input_minutes * 60

    # Sum up all seconds value and return it because midnight in 24 hour system clock
    # is actually 00:00:00 so the difference it self is the current time in seconds
    return hour_in_seconds + minute_in_seconds + input_seconds

print(seconds_since_midnight(13, 30, 45)) # 48645
