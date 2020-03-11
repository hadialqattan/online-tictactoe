import pygame

# local import
from src.client import Client


if __name__ == "__main__":
    # initialize all imported pygame modules
    pygame.init()
    # start pygame main loop
    c = Client(('127.0.0.1', 6400), 'X')
    c.loop()
    # uninitialize all pygame modules
    pygame.quit()
    