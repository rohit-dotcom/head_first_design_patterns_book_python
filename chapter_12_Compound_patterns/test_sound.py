import pygame

beats_path="./assets/freesound_community-drum-beat-01-37136.wav"

pygame.mixer.init()

def play_beat(beats_path):

    beat=pygame.mixer.Sound(beats_path)
    beat.play(loops=-1)
    try:
        input("Playing beat. press enter to stop \n")
    finally:
        beat.stop()
        pygame.mixer.quit()

if __name__=="__main__":
    play_beat(beats_path)


