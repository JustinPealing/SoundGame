import pygame
import random
from os import listdir
from os.path import join

try:
	import pyHook

	# http://code.activestate.com/recipes/553270-using-pyhook-to-block-windows-keys
	def OnKeyboardEvent(event):
	       if event.Key.lower() in ['lwin', 'rwin']:
	               return False
	       else:
	               return True

	hm = pyHook.HookManager()
	hm.KeyDown = OnKeyboardEvent
	hm.HookKeyboard()
except:
	pass

pygame.init()

effects = []
for f in listdir("Sounds"):
	p = join("Sounds", f)
	effects.append(pygame.mixer.Sound(p))

screen = pygame.display.set_mode((640, 480))

running = 1
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	if event.type == pygame.KEYDOWN:
		r = random.randint(0, len(effects) - 1)
		effects[r].play()
