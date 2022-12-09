import playsound
#import threading

from threading import Thread

def playAudio():
    playsound.playsound('audio.mp3', True)


T = Thread(target=playAudio, args=()) # create thread
T.start() # Launch created thread


#threading.Thread(target=playAudio, args=('audio.mp3'), daemon=True).start()

#playAudio('audio.mp3')