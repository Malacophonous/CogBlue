####################
#   Gui V3 16 Sept. 2017 Malacophonous
#####################

'''
API for Gui v3
guiAPP

guiWIN

guiWID

'''

import pyglet

#------------------
#Building Blocks
#-------------------
#api standards:
#   All building blocks have a move(dx,dy), changecolor(R,G,B,A) and a delete() function
#
#   move(dx,dy) does not perform any collision or overlaying checking. it simply moves the polygon
#   changecolor(R,G,B,A) turns all the vertices to the new color
#   delete()    deletes the data from the batch, releasing visual memory and stuff

class guiLines():
    def __init__(self,x1,y1,x2,y2,batch,color):
        self.vertex_list = batch.add(2, pyglet.gl.GL_LINES, None,
                                     ('v2i',[x1,y1,
                                             x2,y2]),
                                     ('c4B',color * 2)
                                     )
    def move(self,dx,dy):
        self.vertex_list.vertices = [a[0]+a[1] for a in zip(self.vertex_list.vertices,(dx,dy)*2)]
    def delete(self):
        self.vertex_list.delete()

class guiWireframe():
    def __init__(self,widget,color):
        batch = widget.batch
        numvertexes = len(widget.vertex_list)
        #TODO: make this into vertexes that have a padding, then put it into the batch add thing
        widget.vertex_list.vertices
        self.vertex_list = batch.add(numvertexes,pyglet.gl.GL_LINES, None,
                                     ('v2i',),
                                     ('c4B',color*numvertexes))

class guiRectangle():
    '''Draws a rectangle into a batch. Courtesy of the pyglet examples text_input.py'''
    def __init__(self, x1, y1, x2, y2, batch, color):
        self.vertex_list = batch.add(4, pyglet.gl.GL_QUADS, None,
            ('v2i', [x1, y1,
                     x2, y1,
                     x2, y2,
                     x1, y2]),
            ('c4B', color * 4)
        )
    def move(self,dx,dy):
        self.vertex_list.vertices = [a[0]+a[1] for a in zip(self.vertex_list.vertices,(dx,dy)*4)]
    def changecolor(self,newR,newG,newB,newA):
        self.vertex_list.colors = [newR,newG,newB,newA]
    def delete(self):
        self.vertex_list.delete()

class guiTriangle():
    '''Draws a triangle into a batch.'''
    def __init__(self,x1,y1,x2,y2,x3,y3,batch,color):
        self.vertex_list = batch.add(3,pyglet.gl.GL_TRIANGLES, None,
                                     ('v2i',[x1,y1,
                                             x2,y2,
                                             x3,y3]),
                                     ('c4B',color*3)
                                     )

    def move(self,dx,dy):
        self.vertex_list.vertices = [a[0]+a[1] for a in zip(self.vertex_list.vertices,(dx,dy)*3)]
    def delete(self):
        self.vertex_list.delete()

class guiPoly():
    '''Draws a complex 2d polygon into a batch.'''
    def __init__(self):
        pass
    def delete(self):
        pass


class guiText():
    def __init__(self,text,font,x1,y1,w,h,color,multiline,batch,group):
        self.data = pyglet.text.Label(text = text, font_name = font,
                                      x = x1, y = y1, width = w, height = h,
                                      color = color, multiline = multiline,
                                      batch = batch,group = group)
    def move(self,dx,dy):
        self.data.x+=dx
        self.data.y+=dy
    def delete(self):
        self.data.delete()

class guiDocument():
    def __init__(self,text):
        self.data = pyglet.text.document.UnformattedDocument(text)
        self.data.set_style(0,len(self.data.text),
                            dict(color=(0, 0, 0, 255))
                            )
    def setStyle(self,textcolor,fontname):
        self.data.set_style(0,len(self.data.text),
                            dict(color=textcolor,font_name = fontname)
                            )

    def delete(self):
        self.data.delete()
        #dunno if this works


class guiLayout():
    #define layout stuff for interactive text boxes(view part of MVC, ie how it renders)
    #note: the 'hitbox' of the widget is larger than the layout by the padding
    #       defined in TextField.style, hence the -2*padding

    def __init__(self,document,x1,y1,w,h,padding,multiline,batch):
        self.data = pyglet.text.layout.IncrementalTextLayout(document,
                                                             w-2*padding,
                                                             h-2*padding,
                                                             multiline=multiline,
                                                             batch = batch)
        self.data.x = x1+padding
        self.data.y = y1+padding
        self.caret = pyglet.text.caret.Caret(self.data)

    def delete(self):
        self.caret.delete()
        self.data.delete()

