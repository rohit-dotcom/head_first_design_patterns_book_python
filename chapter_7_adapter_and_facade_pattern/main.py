from home_theater import (HomeTheaterFacade,
                          Amplifier,
                          StreamingPlayer,
                          Screen,
                          Projector,
                          PopcornPopper,
                          TheaterLIghts,
                          Tuner,)

if __name__=="__main__":
    amp=Amplifier()
    tuner=Tuner()
    player=StreamingPlayer()
    lights=TheaterLIghts()
    projector=Projector()
    screen=Screen()
    popper=PopcornPopper()
    facade=HomeTheaterFacade(
        amp,tuner,screen,popper,lights,projector,player)

    facade.watchMovie()
    facade.endMovie()