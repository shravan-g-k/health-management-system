from pygame import mixer as song
from datetime import datetime 
now = datetime.now()
time = int(now.strftime("%H%M"))


def song_play():

    song.init()
    song.music.load("Chill.mp3")
    song.music.play()
    while True:
        a = input('Enter "done " to stop the music - ')
        if a == "done":
            song.music.stop()
            break
        else :
            song_play()
        

def water():
    global time
    if int(datetime.now().strftime('%H%M'))-time == 1 :
        time = int(datetime.now().strftime('%H%M'))
        a = (datetime.now().strftime('%H:%M')) 
        song_play()
        with open('data.txt','a') as file :
            file.write(f'\nYou drank water at {a} ')

            
def eye():
    global time
    if int(datetime.now().strftime('%H%M'))-time == 20 :
        time = int(datetime.now().strftime('%H%M'))
        a = (datetime.now().strftime('%H:%M'))
        song_play()
        with open('data.txt','a') as file :
            file.write(f'\nYou excercised your eye at {a} ')


def exercise():
    global time
    if int(datetime.now().strftime('%H%M'))-time == 100 :
        time = int(datetime.now().strftime('%H%M'))
        a = (datetime.now().strftime('%H:%M'))
        song_play()
        with open('data.txt','a') as file :
            file.write(f'\nYou excercised at {a} ')

while True:
    water()
    exercise()
    eye()
