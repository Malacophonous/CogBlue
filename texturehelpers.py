import pyglet
from pyglet.gl import *
#----------------
#texture defining classes
#somewhat borrowed from the examples in the pyglet examples directory. All credit to them.
#----------------
class TextureEnableGroup(pyglet.graphics.Group):
    def set_state(self):
        glEnable(GL_TEXTURE_2D)

    def unset_state(self):
        glDisable(GL_TEXTURE_2D)

class TextureBindGroup(pyglet.graphics.Group):
    def __init__(self, texture, textenable):
        super(TextureBindGroup, self).__init__(parent = textenable)
        assert texture.target == GL_TEXTURE_2D
        self.texture = texture

    def set_state(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)

    # No unset_state method required.

    def __eq__(self, other):
        return (self.__class__ is other.__class__ and
                self.texture.id == other.texture.id and
                self.texture.target == other.texture.target and
                self.parent == other.parent)

    def __hash__(self):
        return hash((self.texture.id, self.texture.target))
