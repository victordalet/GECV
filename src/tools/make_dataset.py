import sys
import random

from google_earth import GoogleEarth


class Main:
    google_earth: GoogleEarth
    zoom: int
    move: int
    path: str
    nb_screenshots: int

    def __init__(self, path: str, zoom: int, move: int, nb_screenshots: int):
        self.path = path
        self.zoom = zoom
        self.move = move
        self.nb_screenshots = nb_screenshots
        self.google_earth = GoogleEarth()
        self.google_earth.launch()
        self.google_earth.full_screen()
        self.google_earth.zoom_in(zoom)
        self.run()

    def run(self):
        for i in range(self.nb_screenshots):
            print(f'screenshot : {i}')
            self.google_earth.screenshot(f'{self.path}/screenshot_{i}.png')
            move_value = random.choice(['left', 'up', 'down', 'right'])
            match move_value:
                case 'left':
                    self.google_earth.move_left(self.move)
                case 'right':
                    self.google_earth.move_right(self.move)
                case 'up':
                    self.google_earth.move_up(self.move)
                case 'down':
                    self.google_earth.move_down(self.move)


if __name__ == '__main__':
    main = Main(path=sys.argv[1],
                zoom=int(sys.argv[2]),
                move=int(sys.argv[3]),
                nb_screenshots=int(sys.argv[4]))
