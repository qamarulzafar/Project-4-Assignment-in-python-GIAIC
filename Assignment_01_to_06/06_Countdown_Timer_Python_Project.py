import time
def countdown_timer(seconds):
    while seconds:
        min, sec = divmod(seconds, 60)
        timer = f"{min:02d}:{sec:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time up!")



try:
    total_time = int(input("Enter the time in second: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter a valid number.")