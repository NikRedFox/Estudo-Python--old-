import time

import pyautogui

print("mova o cursor")
time.sleep(5)

x_clicar, y_clicar = pyautogui.position()

print(f'As coordenadas são x = {x_clicar} e y = {y_clicar}')