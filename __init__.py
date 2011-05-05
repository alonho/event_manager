import time
import osax
import lightblue

wtf = osax.OSAX()

def set_low(LOW_VOL=1): # lowest = 0
    wtf.set_volume(LOW_VOL)
def set_high(HIGH_VOL=4): # highest = 8
    wtf.set_volume(HIGH_VOL)

def get_device_names(timeout=5):
    return [name for (address, name, number) in lightblue.finddevices(length=timeout)]

def device_exists(name=u"Nexus S"):
    return name in get_device_names()

def main(poll_time=1):
    action_map = { True : set_low,
                   False : set_high }
    # we don't know what the initial level is
    # so set on first iteration
    current_state = "NOT_TRUE_AND_NOT_FALSE"

    while 1:
        new_state = device_exists()
        print "device found: {0}".format(new_state)
        if new_state != current_state:
            action = action_map[new_state]
            print "running action {0}".format(action.__name__)
            action()
            current_state = new_state
        time.sleep(poll_time)
            
if __name__ == '__main__':
    main()
