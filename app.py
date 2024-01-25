import subprocess
import time
import pygame

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("default_alarm.mp3")  # Replace with the path to your sound file
    pygame.mixer.music.play()
    time.sleep(2)  # Adjust this sleep time based on the duration of your sound

def chrono_chime(url, profile_directory, interval_minutes):
    try:
        while True:
            # Open the URL in a new Chrome window with a specific profile
            subprocess.run(["google-chrome", "--new-window", "--profile-directory=" + profile_directory, url])

            # Display the remaining time
            for remaining_time in range(interval_minutes * 60, 0, -1):
                minutes, seconds = divmod(remaining_time, 60)
                print(f"Next opening in {minutes:02d} minutes {seconds:02d} seconds", end="\r")
                time.sleep(1)

            # Clear the line for the next iteration
            print(" " * 50, end="\r")

            # Play the sound
            play_sound()

    except KeyboardInterrupt:
        print("ChronoChime stopped.")

if __name__ == "__main__":
    # Set the URL, Chrome profile directory, and interval in minutes
    target_url = "https://discord.com/channels/781056715726389298/1066999015830462464"
    chrome_profile_directory = "Default"  # Change this to the name of your Chrome profile
    chime_interval_minutes = 20  # Change this to the desired interval

    print(f"ChronoChime started. Opening {target_url} in a new Chrome window for profile '{chrome_profile_directory}' every {chime_interval_minutes} minutes.")
    chrono_chime(target_url, chrome_profile_directory, chime_interval_minutes)
