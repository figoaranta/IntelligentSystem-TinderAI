import wrapper
from random import random
from time import sleep

if __name__ == "__main__":
    token = "bc408baf-c1fe-4fa2-a06b-8c7858e33edf"
    api = wrapper.tinderAPI(token)
    x = 0
    while (x < 5):
        persons = api.nearby_persons()
        for peep in persons:
            print(peep.download_images(folder="./images/unclassified",sleep_max_for=random()*3))
            sleep(random()*10)
        sleep(random()*10)
        x = x + 1