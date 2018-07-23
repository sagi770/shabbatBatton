from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
	return 'Home'

@app.route('/play')
def play():
	import pygame
	pygame.mixer.init()
	pygame.mixer.music.load("mpthreetest.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	   	return 'done'
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
