from yaml import load, Loader
import pygame

# local import
from client.client import Client


if __name__ == "__main__":
    try:
        # load server config from server.yaml
        with open("../server.yaml", "r") as configFile:
            conf = load(configFile.read(), Loader)
        if conf:
            # initialize all imported pygame modules
            pygame.init()
            # start pygame main loop
            c = Client((conf["host"], conf["port"]))
            c.loop()
            # uninitialize all pygame modules
            pygame.quit()
    except Exception as confERR:
        print(
            f"\nserver.yaml must contain:\n\thost: 0.0.0.0\n\tport: 6400\n\n{confERR}"
        )
