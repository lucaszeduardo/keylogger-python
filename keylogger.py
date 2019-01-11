from pynput import keyboard
import sys
from tim import TIME

def on_press(key):
	if str(key) == 'Key.esc': # Se o usuario aperta o ESC, o programa ira parar.... se n quer isso.. so remover as linhas 6,7,8 e deixar apenas o print...
	    sys.exit()
	else:
	    print(TIME().Years() + ' | ' + TIME().Hors() +  f': {key}')

with keyboard.Listener(
	on_press = on_press) as listener:
	listener.join()
