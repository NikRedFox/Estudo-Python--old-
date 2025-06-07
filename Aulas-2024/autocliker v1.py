import time
import keyboard
import pydirectinput
import pygetwindow as gw
import ctypes

parte_constante_titulo = 'Cookie Clicker'


def encontrar_janela_cookie_clicker():
    janelas_abertas = gw.getWindowsWithTitle('')
    for janela in janelas_abertas:
        if parte_constante_titulo in janela.title:
            return janela
    return None


x_clicar, y_clicar = 285, 431


def autoclicker():
    janela_cookie_clicker = encontrar_janela_cookie_clicker()

    if janela_cookie_clicker:
        pydirectinput.click(x_clicar, y_clicar)
        time.sleep(0.017)
        janela_cookie_clicker.minimize()  # Minimiza a janela após o clique
    else:
        print('Janela do Cookie Clicker não encontrada.')


input_press = input('Pressione qualquer tecla para iniciar, pressione "x" para encerrar: ')

while True:
    autoclicker()

    if keyboard.is_pressed('x'):
        break

print('Autoclicker encerrado')