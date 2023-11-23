
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
    ▐░▌          ▐░▌          ▐░▌
    ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌
    ▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌▐░▌
     ▀▀▀▀▀▀▀▀▀█░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌
              ▐░▌▐░▌       ▐░▌▐░▌
     ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀

# SACE-Subject-Grade-Calculator
An unofficial python script to calculate a single SACE subject's overall/end of year grade. Use instructions at the bottom.

**DISCLAIMER: The author of this script is not related to the SACE organisation. This script is furthermore not endorsed or created by them. Use understanding the output may not allign with current SACE processes. You are liable for any damages caused from the use or interpretation of the results of this script. Use your discretion.**

**WARNING: The weightings in the current version of the script may not be accurate to the future, so either check or use with caution. It should be fine for a few years though.**

## Use Cases
This can be useful for two main reasons:

1: Having done a portion of a subject, determining what scores are needed to get the final grade you desire.

2: With a rough knowledge of how you've done on, say, an exam, how well the overall grade will be.

## What it does and doesn't take into account
This script will take into account the weighting of each assesment type, and will do the averaging and conversions. However, this will not take into account moderation changes and scaling factors. Therefore, this should not be used as the final definitive source on what your final grade will be.

## Future Updates
At the time of writing this, this only has support for a few subjects. More will be needed to be added. This would be good to seperate into a different file for ease of update as SACE changes. 

Compiling this into distributals like a .exe, .app, or a linux app would be good, or at the very least adding a script for each os to allow non tech-savvy people to launch the application easily.


# Use instructions

The easy way to run the program is through the github releases section on the right of the github screen. Download and run the file designated for your operating system. Include the subjects.csv file in the same directory. Alternativly, you can download the source code, and run `python3 SACEgradeCalculator.py` in your command line in the same folder as the source code.

# Developer Info

First off, adding something from the *Future Updates* section would be very appreciated. The main thing needed though is to add more subjects. Note that if a subject has less that 3 assesment types, the two last ones can be replaced with exactly "N/A" with a weighting of 0 to remove them on the user's side.

This is built using pyinstaller through `pyinstaller -F SACEgradeCalculator.py`

<meta name="google-site-verification" content="7b9T27fqZj3q_saKZpUhspMh0V0eeFfNzRYWuZyw4OY" />
