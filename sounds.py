import os.path
import winsound


def invalidCode():
    winsound.PlaySound(os.path.abspath("Wrong-answer-sound-effect.wav"), winsound.SND_FILENAME)


def zombie():
    winsound.PlaySound(os.path.abspath("zoombie.wav"), winsound.SND_FILENAME)


def monster():
    winsound.PlaySound(os.path.abspath("monster.wav"), winsound.SND_FILENAME)

def spider():
    winsound.PlaySound(os.path.abspath("spider.wav"), winsound.SND_FILENAME)
