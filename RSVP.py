#!/usr/local/bin/python
#rapid serial visual presentation program

#imports
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from sys import stdin
from time import sleep
from kivy.core.window import Window

#settings
Window.fullscreen = True
READSPEED=.15

#organize the input for reading
##there is probably a better way to do this
TOREAD = []
for line in stdin:
    #print(line)
    for l in line.split():
        TOREAD.append(l)
TOREAD.reverse()

#kivy layout
Builder.load_string('''
<RSVP>:
    Label:
        id: firstlabel
        text: root.firstlabelstring
        font_size: '50dp'
''')

class RSVP(BoxLayout):
    firstlabelstring = StringProperty("")
    def update(self, arg):
        if TOREAD:
            self.firstlabelstring = str(TOREAD.pop())
        else:
            exit()

#main application build and refresh schedule
class MainApp(App):
    def build(self):
        self.rsvp = RSVP()
        return self.rsvp
        sleep(2)

    def on_start(self):
        Clock.schedule_interval(self.rsvp.update, READSPEED)

#run the main app if executed on it's own
if __name__ == "__main__":
    MainApp().run()
