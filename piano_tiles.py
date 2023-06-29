import pyautogui
import webbrowser
import keyboard
from time import sleep
import win32api
import win32con

# Função usada para ter um click mais rápido do que com o Pyautogui:
def click(x,y): 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Abre no navegador o site do jogo:
webbrowser.open(
    'https://sandbox.gameforge.com/en-US/littlegames/magic-piano-tiles/')

# Espera o site carregar e clicar em play:
sleep(10)
pyautogui.click(2090, 501,duration=1)

# Aguarda os anúncios finalizarem, então clicar em start:
sleep(70)
pyautogui.click(2142,467,duration=1)

# Verificar se a barra preta chegou no lugar e executa o click,
# Fara isso quanto não for pressionado a tecla 'space' ou até errar o click:
while keyboard.is_pressed('space') == False:
    if pyautogui.pixelMatchesColor(2008,390,(0, 0, 0)):
        click(2008,390)

    if pyautogui.pixelMatchesColor(2095,387,(0, 0, 0)):
        click(2095,387)

    if pyautogui.pixelMatchesColor(2174,378,(0, 0, 0)):
        click(2174,378)

    if pyautogui.pixelMatchesColor(2257,379,(0, 0, 0)):
        click(2257,379)
    
    if pyautogui.pixelMatchesColor(2056, 460, (255, 255, 255)):
        break