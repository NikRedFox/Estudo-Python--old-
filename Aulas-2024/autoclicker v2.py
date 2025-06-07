import time
import keyboard
import ctypes


x_clicar, y_clicar = 285, 431
paused = False


def autoclicker():
    while not paused:
        ctypes.windll.user32.SetCursorPos(x_clicar, y_clicar)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
        time.sleep(0.01)


def toggle_pause():
    global paused
    paused = not paused
    if paused:
        print('Autoclicker pausado')
    else:
        print('Autoclicker retomado')


keyboard.add_hotkey('z', toggle_pause)

input_press = input('Pressione "z" para pausar/retomar, pressione "x" para encerrar: ')

while True:
    autoclicker()

    if keyboard.is_pressed('x'):
        break

print('Autoclicker encerrado')

