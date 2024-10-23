import os
from gtts import gTTS
import pygame

diretorio = os.path.dirname(os.path.abspath(__file__))
filename = 'audio.mp3'

def assistant_speak(text):
    tts = gTTS(text, lang='pt')
    tts.save(f'{diretorio}/{filename}')

    pygame.mixer.init()
    pygame.mixer.music.load(f'{diretorio}/{filename}')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.quit()


def fala():
    assistant_speak('DNS')

    os.remove(f'{diretorio}/{filename}')


fala()
