import click
import pyautogui
from pynput.keyboard import *

running = False

@click.command()
@click.option('-D', '--delay',type=click.FLOAT, default=1.0, help='Delay in seconds.')
@click.option('-K', '--key', default='page_up', help='Toggle key')
@click.option('-B', '--button', default='left', help='Mouse button')
def main(delay, key, button):
    toogle_key = getattr(Key, key, key)
    button = {
        'left': pyautogui.LEFT,
        'right': pyautogui.RIGHT,
    }.get(button)

    def on_press(key):
        global running, pause

        if key == toogle_key:
            running = not running
            print(f"status = {running}")

    lis = Listener(on_press=on_press)
    lis.start()

    while True:
        if running:
            pyautogui.click(pyautogui.position(), button=button)
            pyautogui.PAUSE = delay
    lis.stop()
