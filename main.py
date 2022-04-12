import kivy
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


MyLiberalUncle = [
    '../kivy/assets/COWS_AT_THE_GRASS.mp4',
    "../kivy/assets/everycodeingtutorial.mp4",
    "../kivy/assets/Y2Mate.is - Rick Astley - Never Gonna Give You Up (Official Music Video)-dQw4w9WgXcQ-144p-1635693724816.mp4",
    ""
]

PotatoPancakes = MyLiberalUncle[2]


class myApp(App):
    def build(self):
        video = VideoPlayer(source = PotatoPancakes)
        video.state = 'play'
        video.options = {'eos': 'loop' }
        video.allow_stretch = True
        return video


if __name__ == "__main__":
    myApp().run()