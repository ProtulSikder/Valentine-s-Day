'''
A fun program in valentine's day
that says 'I love you!'
by: Nasir Sikder Protul.

In this program I used
gTTS module to convert text into mp3
and then used pygame.mixer.music to
read the mp3 file.

The particular reason I used gTTS
is because it's a lady voice :D :D
'''

from gtts import gTTS
from pygame import mixer

#Specify the language and put it in a variable
tts = gTTS(text = 'I love you', lang = 'en')

#Save the file as an mp3 file
tts.save('love.mp3')

mixer.init()

#Load the mp3 file
mixer.music.load('love.mp3')

#Play the file
mixer.music.play()

#Finish
