import playsound
from gtts import gTTS

tts = gTTS('Secuencia enero terminada')
tts.save('speak.mp3')
playsound('speak.mp3')