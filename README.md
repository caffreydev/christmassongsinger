# Christmas Song Text to Speech Singer

This is a simple python build that will create and play an MP3 of a random song.  Songs are chosen from the dictionary in songbook.py and converted from string to mp3 with the title as file name by gTTS (google text to speech).  An instance is then created of Mutagen MP3 to get the metadata, specifically play length, which is fed into python-vlc to make sure it plays the whole song then terminates the process.

Run the main christmastexttospeech.py file in python to use.

Have fun, pull requests of additional songs accepted :)

## Terminal Commands for Dependencies:
- pip install python-vlc
- pip install mutagen
- pip install time
- sudo apt-get install vlc (For mac/linux)