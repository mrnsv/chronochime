
# ChronoChime

ChronoChime is a Python script designed to infuse your browsing routine with a dash of whimsy and functionality. By combining the power of Python, subprocesses, and Pygame, ChronoChime ensures that you never lose track of time while browsing. Whether you're engrossed in work, leisure, or a bit of both, ChronoChime keeps you punctual and entertained.

### Features:

-   **Customizable URL Opening:** Specify the URL you want to open at regular intervals, allowing you to seamlessly integrate ChronoChime with your workflow or leisure activities.
-   **Chrome Profile Support:** Choose the Chrome profile in which you want the URL to open, providing flexibility for different browsing contexts.
-   **Interval-Based Reminder:** Set the interval in minutes for ChronoChime to open the URL, ensuring you stay on schedule without being overwhelmed by constant alerts.
-   **Auditory Cue:** Enjoy a delightful chime every time the URL opens, adding a touch of charm and whimsy to your browsing experience.

### Requirements:

-   Python 3.x
-   Pygame library
-   Google Chrome browser

### Installation:

1.  Clone this repository to your local machine.

    `git clone https://github.com/mrnsv/chronochime.git` 

2.  Navigate to the project directory.

    `cd ChronoChime` 

3.  Install the required dependencies using pip:

    `pip install -r requirements.txt` 

4.  Ensure you have Google Chrome installed on your system.

### Usage:

1.  Open `app.py` in a text editor.
2.  Modify the `target_url`, `chrome_profile_directory`, and `chime_interval_minutes` variables according to your preferences.
3.  Run the script using the command:
       
    `python app.py` 
    

### Example:

`target_url = "https://example.com"
chrome_profile_directory = "Profile 1"
chime_interval_minutes = 30

chrono_chime(target_url, chrome_profile_directory, chime_interval_minutes)` 

### Contributions:

Contributions are welcome! Feel free to submit issues or pull requests if you have suggestions for improvements or encounter any bugs.

----------

With ChronoChime, time management becomes an enchanting journey. Stay punctual, stay entertained, and let ChronoChime be your trusty companion in the digital realm. Happy browsing! 🕰️🎵
