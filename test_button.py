from pybox.button import BUTTON

push = BUTTON()

def press():
    print("PRESS")
    
def release():
    print("RELEASE")
    print(push.press_time)
    
push.press_handler(press)
push.release_handler(release)

while True:
    push.update()