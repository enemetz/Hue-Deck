from phue import Bridge
import eel

# Eel using front end directory
eel.init('web')

b = Bridge('Your bridge ip')
# Have to hit button on bridge and then run b.connect only once
# b.connect()
b.get_api()


# When light x is pressed, will turn on if off, will turn off if on
@eel.expose
def lightSwitchOnePressed():
    if b.get_light(1, 'on'):
        b.set_light(1, 'on', False)
    else:
        b.set_light(1, 'on', True)


@eel.expose
def lightSwitchTwoPressed():
    if b.get_light(2, 'on'):
        b.set_light(2, 'on', False)
    else:
        b.set_light(2, 'on', True)


@eel.expose
def lightSwitchThreePressed():
    if b.get_light(3, 'on'):
        b.set_light(3, 'on', False)
    else:
        b.set_light(3, 'on', True)


@eel.expose
def lightSwitchFourPressed():
    if b.get_light(4, 'on'):
        b.set_light(4, 'on', False)
    else:
        b.set_light(4, 'on', True)

#is called to check if light is on
@eel.expose
def isLightOn(x):
    print("Made it")
    if b.get_light(x, 'on'):
        print(x)
        return True
    else:
        print("Off")
        return False


eel.start('HueDeckUI.html', size=(800, 480))
