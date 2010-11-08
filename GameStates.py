from PyQt4.QtCore import (QStateMachine, QState, pyqtSignal, pyqtProperty,
    QPropertyAnimation, QObject)
from PyQt4.QtGui import *

class ItemFader(QObject):
    @pyqtProperty(float)
    def opacity(self): return self.item.opacity()
    @opacity.setter
    def opacity(self, x): self.item.setOpacity(x)
    
    def __init__(self, item):
        super(ItemFader, self).__init__()
        self.item = item

        ani = self.fade_in_ani = QPropertyAnimation(self, "opacity")
        def fade_in_finished():
            pass
        ani.finished.connect(fade_in_finished)

        ani = self.fade_out_ani = QPropertyAnimation(self, "opacity")
        def fade_out_finished():
            self.item.setVisibile(False)
        ani.finished.connect(fade_out_finished)

    def fade_in(self, opacity = 1.0, duration = 1.0):
        self.item.setVisible(True)
        self.fade(opacity, duration)

    def fade_out(self, opacity = 0.0, duration = 1.0):
        self.fade(opacity, duration)

    def fade(self, opacity, duration):
        ani = self.fade_in_ani
        ani.setEndValue(opacity)
        ani.setDuration(duration * 1000)
        ani.start()

class State(QState):
    def __init__(self, scene, state):
        super(QState, self).__init__(state)
        self.scene = scene
        self.naubino = scene.naubino

class HighscoreState(State):
    def __init__(self, scene, state):
        super(HighscoreState, self).__init__(scene, state)
        #self.highscore = Highscore()
    
    def onEntry(self, event):
        #self.highscore.load()
        pass

    def onExit(self, event):
        print("exit highscore")

class StartState(State):
    def __init__(self, scene, state):
        super(StartState, self).__init__(scene, state)
        self.splash = splash = QGraphicsPixmapItem()
        self.fader = fader = ItemFader(splash)

        pixmap = QPixmap("splash.png")
        splash.setVisible(False)
        splash.setPixmap(pixmap)
        splash.setOpacity(0)
        splash.setPos(-300, -200)
        self.scene.add_item(self.splash)
    
    def onEntry(self, event):
        self.fader.fade_in()

    def onExit(self, event):
        self.fader.fade_out()

class PlayState(State):
    def onEntry(self, event):
        self.naubino.play()

    def onExit(self, event):
        self.naubino.stop()

class TutorialState(State):
    def onEntry(self, event):
        print("enter tutorial")

    def onExit(self, event):
        print("exit tutorial")

class FailState(State):
    def onEntry(self, event):
        print("enter fail")

    def onExit(self, event):
        print("exit fail")

class GameStateMachine(QStateMachine):
    play = pyqtSignal()
    tutorial = pyqtSignal()
    highscore = pyqtSignal()
    
    def __init__(self, scene):
        super(GameStateMachine, self).__init__()
        self.scene = scene

        state_machine = self
        
        no_play = QState(state_machine)
        play    = PlayState(scene, state_machine)

        sf    = QState(no_play)
        start = StartState(scene, sf)
        fail  = FailState(scene, sf)

        tutorial  = TutorialState(scene, no_play)
        highscore = HighscoreState(scene, no_play)

        no_play.addTransition(self.play, play)
        play.addTransition(self.highscore, fail)
        sf.addTransition(self.tutorial, tutorial)
        sf.addTransition(self.highscore, highscore)
        tutorial.addTransition(self.highscore, highscore)
        highscore.addTransition(self.tutorial, tutorial)

        no_play.setInitialState(sf)
        sf.setInitialState(start)
        state_machine.setInitialState(no_play)
        