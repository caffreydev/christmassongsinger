from gtts import gTTS
import vlc
import time
import songbook
import random
from mutagen.mp3 import MP3
import math


songbook = songbook.songbook
def texttospeech(phrase, title):
    tts = gTTS(phrase, lang="en")
    tts.save(title + ".mp3")
def playsong(title, playtime):
    print("Now playing", title, " Plays for", formatseconds(playtime))
    p = vlc.MediaPlayer("./" + title + ".mp3")
    p.play()
    time.sleep(playtime)
    p.stop()
def formatseconds(playtime):
    minutes = math.floor(playtime / 60)
    seconds = playtime % 60
    message = ""
    if minutes == 1:
        message += "1 minute, and "
    if minutes > 1:
        message += str(minutes) + " minutes, and "
    message += str(seconds) + " seconds."
    return message

songs = list(songbook.keys())
index = random.randint(0,len(songs) - 1)
title = songs[index]
texttospeech(songbook[title], title)
audio = MP3(title + ".mp3")

playsong(title, math.floor(audio.info.length))

