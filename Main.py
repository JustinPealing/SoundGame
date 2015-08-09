import pygame
import random
import pyHook

# http://code.activestate.com/recipes/553270-using-pyhook-to-block-windows-keys/
def OnKeyboardEvent(event):
	if event.Key.lower() in ['lwin', 'rwin']:
		return False
	else:
		return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

pygame.init()
screen = pygame.display.set_mode((640, 480))

effects = []
effects.append(pygame.mixer.Sound('Sounds\low-intesity-a3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-a3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-a4.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-b3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-c3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-c4.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-d3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-d4.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-e3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-e4.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-f3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-f4.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-g3.wav'))
effects.append(pygame.mixer.Sound('Sounds\low-intesity-g4.wav'))

running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	if event.type == pygame.KEYDOWN:
		r = random.randint(0, len(effects) - 1)
		effects[r].play()

	screen.fill((0, 0, 0))
	pygame.display.flip()
