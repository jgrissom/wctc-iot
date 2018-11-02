import pygame

#print(pygame.version.ver)

def main():
	running = True
	while running:
		# event handling, gets all events from the queue
		for event in pygame.event.get():
			# if the event is of type QUIT or Esc key is pressed
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
			# if spacebar is pressed
			elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
				#img = pygame.image.load('123.png')
				#img = pygame.image.load('{0}.png', '123')
				#screen.blit(img, (0, 0))
				#pygame.display.update()
				load_img('123')
			elif event.type == pygame.KEYUP and event.key == pygame.K_1:
				load_img('1')
			elif event.type == pygame.KEYUP and event.key == pygame.K_2:
				load_img('2')
			elif event.type == pygame.KEYUP and event.key == pygame.K_3:
				load_img('3')
			#else:
				#print(event)
	destroy()

def load_img(n):
	img = pygame.image.load('{0}.png'.format(n))
	screen.blit(img, (0, 0))
	pygame.display.update()

def destroy():
	print("cleanup")
	pygame.quit()

if __name__ == '__main__':     # Program start from here
	pygame.init()
	pygame.display.set_caption("1-2-3")
	screen = pygame.display.set_mode((400,400))
	load_img("123")
	try:
		main()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

