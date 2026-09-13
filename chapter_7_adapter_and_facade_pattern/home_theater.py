from __future__ import annotations

class Amplifier():
    def __init__(self,tuner:Tuner=None,player:StreamingPlayer=None):
        self.player=player
        self.tuner=tuner

    def on(self):
        print("This Amplifier is on")

    def off(self):
        print("This Amplifier is off")

    def setStreamingPlayer(self,player:StreamingPlayer):
        self.player=player

    def setTuner(self,tuner:Tuner):
        self.tuner=tuner

    def setSurroundSound(self):
        self.player.setSurroundAudio()

    def setVolume(self):
        pass


class Tuner():
    def __init__(self,amp:Amplifier=None):
        self.amp=amp

    def on(self):
        print("this tuner is on")

    def off(self):
        print("this tuner is off")

    def setAM(self):
        print("this tuner is set to AM")

    def setFM(self):
        print("this tuner is set to FM")

    def setFrequency(self,freq):
        print(f"this tuner is set to frequency {freq}")

class StreamingPlayer():
    def __init__(self,amp:Amplilfier=None):
        self.amp=None

    def on(self,):
        print("this Streaming Player is ON")
    def off(self,):
        print("this Streaming Player is Off")
    def play(self,):
        print("this Streaming Player is playing")
    def pause(self,):
        print("this Streaming Player is paused")
    def stop(self,):
        print("this Streaming Player is stopped")
    def setSurroundAudio(self,):
        print("this Streaming Player set to surround Audio")
    def setTwoChannelAudio(self):
        print('this streaming player is set to two channel Audio')


class Screen():
    def up(self):
        print('THis screen is up')
    def down(self):
            print('THis screen is down')

class PopcornPopper():
    def on(self):
        print("this popper is on")
    def off(self):
        print("this popper is off")
    def pop(self):
        print("this popper is popping")

class TheaterLIghts():
    def on(self):
        print("this theater lights are on")
    def off(self):
            print("this theater lights are off")
    def dim(self):
            print("this theater lights are dim")

class Projector():
    def __init__(self,player:StreamingPlayer=None):
        self.player=player

    def setPlayer(self,player:StreamingPlayer):
        self.player=player
    
    def on(self):
        print("this projector is on")
        
    def off(self):
        print("this projector is off")

    def tvMode(self):
        print("this projector is in tv mode")
    
    def wideScreenMode(self):
        print("this projector is in wide screen mode")

class HomeTheaterFacade():
    def __init__(self,
                 amp:Amplifier=None,
                 tuner:Tuner=None,
                 screen:Screen=None,
                 popper:PopcornPopper=None,
                 lights:TheaterLIghts=None,
                 projector:Projector=None,
                 player:StreamingPlayer=None):

        self.amp=amp
        self.tuner=tuner
        self.screen=screen
        self.popper=popper
        self.lights=lights
        self.projector=projector
        self.player=player

    def watchMovie(self):
        print("Get ready to wathc the movie....")
        self.popper.on()
        self.popper.pop()
        self.lights.dim()
        self.screen.down()
        self.projector.on()
        self.projector.setPlayer(self.player)
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setStreamingPlayer(self.player)
        self.amp.setSurroundSound()
        self.amp.setVolume()
        self.player.on()
        self.player.play()

    def endMovie(self):
        print("Shutting the movie theater down")
        self.popper.off()
        self.lights.off()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()
    
