import vlc
import RPi.GPIO as GPIO
btn_pin = 25

#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)


#remember the current and previous button states

current_state = False
prev_state = False

doTrashCode = False
player = vlc.MediaPlayer("xxx.wav file")
def start():
    em = player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    player.play()
    print("Audio start")

def onEnd(event):
    global doTrashCode
    if event.type == vlc.EventType.MediaPlayerEndReached:
        doTrashCode = True
        print('Audio clip end')


def back():
    player.set_media(player.get_media())
    player.play()
    print('Audio play loop')


start()

while True:
    if doTrashCode:
        back()
        doTrashCode = False
