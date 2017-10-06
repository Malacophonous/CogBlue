####################
#   Gui V3 16 Sept. 2017 Malacophonous
#####################

'''
API for Gui v3
guiAPP

guiWIN

guiWID

'''


#   This class is a drop-in unit that is designed to handle most of the display things for any heavily Gui-based
#       apps. Not games. I have the feeling this will be too slow for most games, which need alot of access to
#       the pyglet internals.

from collections import OrderedDict

import pyglet
from pyglet.window import key
from texturehelpers import TextureEnableGroup, TextureBindGroup

import guiWIN
import guiWID


class APP():
    def __init__(self):
        pass

    def start(self):
        pyglet.clock.schedule_interval(self.window.update, 1/60)
        pyglet.app.run()

    def stop(self):
        pyglet.app.exit()


def main():
    #----------------------
    # Pyglet Setup
    #----------------------
    res = (512,512)
    window = guiWIN.WIN(width=res[0], height = res[1])

    keys = key.KeyStateHandler()
    window.push_handlers(keys)

    #texture_enable_group = TextureEnableGroup(parent = window.background)

    foo = guiWID.Widget(20,250,256,256)
    window.addWidget(foo)
    foo.setVisibleTo(True)
    bar = guiWID.Widget(10,10,64,64)
    window.addWidget(bar)
    bar.setVisibleTo(True)

    pyglet.clock.schedule_interval(window.update, 1/60)
    pyglet.app.run()


if __name__ == '__main__':
    main()
