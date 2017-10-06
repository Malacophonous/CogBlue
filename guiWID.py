####################
#   Gui V3 16 Sept. 2017 Malacophonous
#####################

'''
API for Gui v3
guiAPP

guiWIN

guiWID

'''

from buildingblocks import guiRectangle,guiLines
import random as r

class Widget():
    def __init__(self,_x,_y,_w,_h):
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h

        self.children = []
        self.parent = None
        self.toplevel = False

        self.visible = True
        self.batch = None
        self.visual = None
        self.group = None

        self.holdsFocus = True
        self.style = None

        self.pad = 3

    def __repr__(self):
        return ('I am a {0} Widget at {1},{2} with a width {3} and height {4} in group {5}'
                .format(self.__class__,self.x,self.y,self.w,self.h,self.group))

    def setVisibleTo(self,state,recurse = True):
        self.visible = state
        if state == True:
            self.visual = [guiRectangle(self.x,self.y,self.x+self.w,self.y+self.h,
                                    self.batch,
                                    [r.randint(0,255),r.randint(0,255),r.randint(0,255)]+[255])]
        elif state == False and self.visual is not None:
            #should work unless there is a disconnect between the self.visual and the actual draw batch item
            for component in self.visual:
                component.delete()
            self.visual = None
        if recurse:
            for child in self.children:
                child.setVisibleTo(state,recurse)

    def highlight(self):
        if not self.toplevel:
            pcolor = self.parent.visual[0].vertexlist.colors
        else:
            pcolor = [0,0,0,255]
        if self.visible:

            self.visual.append(guiLines(self.x-self.pad,self.y-self.pad,self.x+self.w+self.pad,self.y+self.h+self.pad,self.batch,
                                            [255 - pcolor[0],255-pcolor[1],255-pcolor[2],255]))
    def dehighlight(self):
        if self.visible:
            self.visual[-1].delete()

    def setStyleTo(self,style):
        pass
    def setGroupTo(self,group):
        self.group = group
    def setBatchTo(self,batch,recurse = True):
        self.batch = batch
        if recurse:
            for child in self.children:
                child.setBatchto(batch,recurse)

    def setParentTo(self,newparent):
        if self not in newparent.children:
            if self.parent is not None:
                # remove from old parent's children
                self.parent.children.remove(self)
            # set new parent as parent
            self.parent = newparent
            # add self to new parent's children
            newparent.children.append(self)
        else:
            print('{0} already parented to {1}'.format(self,self.parent))

    def hitTest(self,x,y):
        for child in self.children:
            hit = child.hitTest(x,y)
            if hit is not None and hit.visible:
                return hit
        else:
            return self._hitFinal(x,y)

    def _hitFinal(self,x,y):
        if (0<x-self.x<self.w and 0<y-self.y<self.h and self.visible):
            return self

    def translate(self,dx,dy):
        right = self.x+dx+self.w
        left = self.x+dx
        top = self.y+dy+self.h
        bottom = self.y+dy
        if self.toplevel:
            px,py,pw,ph = (0,0,self.parent.width,self.parent.height)
        else:
            px,py,pw,ph = (self.parent.x,self.parent.y,self.parent.w,self.parent.h)
        if right >= px+pw:
            self.x = px+pw-self.w
            dx = 0
        elif left <= px:
            self.x = px
            dx = 0
        else:
            self.x = left
        if top >= py + ph:
            self.y = py + ph - self.h
            dy = 0
        elif bottom <= py:
            self.y = py
            dy = 0
        else:
            self.y = bottom
        if self.visible:
            self.visual[0].move(dx,dy)
            self.visual[1].move(dx,dy)
        for child in self.children:
            child._move(dx,dy)

        def _move(self,dx,dy):
            #only for use for a widget's children when that widget is being translated
            #this should cut down on conditional checks for translations of widgets with lots of children
            if self.visible:
                self.visual[0].move(dx,dy)

            for child in self.children:
                child._move(dx,dy)


    def gainedMouseOver(self,window):
        pass
    def lostMouseOver(self,window):
        pass
    def gainedFocus(self,window):
        @window.event
        def on_mouse_drag(x,y,dx,dy,buttons,modifiers):
            self.translate(dx,dy)

        self.highlight()

    def lostFocus(self,window):
        self.dehighlight()
