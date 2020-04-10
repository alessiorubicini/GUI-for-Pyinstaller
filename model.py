# MODEL

from view import View
from controller import Controller


v = View()

c = Controller(v)

print("Apro la finestra..")
v.window(c)