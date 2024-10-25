import os
from gtts import gTTS

diretorio = os.path.dirname(os.path.abspath(__file__))
filename = 'audio.mp3'

def fala(texto):
    tts = gTTS(texto, lang='pt')
    tts.save(f'{diretorio}/{filename}')


fala('DNS')
