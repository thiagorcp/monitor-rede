import os
from gtts import gTTS
import pygame

def assistant_speak(text):
    tts = gTTS(text, lang='pt')
    filename = "audio.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


def fala():
    assistant_speak("Mapas foram feitos para serem mapeados")

    os.remove(filename)


if __name__ == "__main__":
    fala()
