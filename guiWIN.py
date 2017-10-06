####################
#   Gui V3 16 Sept. 2017 Malacophonous
#####################

'''
API for Gui v3
guiAPP

guiWIN

guiWID

'''

#   This class is a subclassed pyglet Window allowing for tracking of widgets and maintaining focus on different areas

import pyglet
from collections import OrderedDict
"""
on_activate()
on_close()
on_context_lost()
on_context_state_lost()
on_deactivate()
on_draw()
on_expose()
on_hide()
on_key_press(symbol,modifiers)
on_key_release(symbol,modifiers)
on_mouse_drag(x,y,dx,dy,buttons,modifiers)
on_mouse_enter(x,y)
on_mouse_leave(x,y)
on_mouse_motion(x,y,dx,dy)
on_mouse_press(x,y,button,modifiers)
on_mouse_release(x,y,button,modifiers)
on_mouse_scroll(x,y,scroll_x,scroll_y)
on_move(x,y)
on_resize(width,height)
on_show()
on_text(text)
on_text_motion(motion)
on_text_motion_select(motion)
"""

class WIN(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.children = []
        self.parent = self
        self.maxGuiRecursion = 5
        self.guigroups = [pyglet.graphics.OrderedGroup(i) for i
                          in range(self.maxGuiRecursion)]
        #higher numbered groups get drawn in front of lower number groups
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        self.content = pyglet.graphics.Batch()
        self.gui = pyglet.graphics.Batch()

        self.text_cursor = self.get_system_mouse_cursor('text')

        #focus is the last thing you left pressed on
        self.focus = None
        #mouseovered is the last thing your mouse cursor is hovering over
        self.mouseovered = None

    def on_window_close(self):
        self.event_loop.exit()
        return pyglet.event.EVENT_HANDLED

    def on_draw(self):
        super().clear()
        self.content.draw()
        self.gui.draw()

    def update(self,dt):
        super().clear()
        self.content.draw()
        self.gui.draw()

    def addWidget(self, widget, parent = None):
        #set widget to gui batch
        #set groups for widget children
        #sets parent as well
        print(widget)
        widget.setBatchTo(self.gui)
        if parent is not None:
            widget.setParentTo(parent)
            widget.setGroupTo(self.guigroups[parent.group.order+1])
        else:
            #widget is child to window
            widget.setParentTo(self)
            widget.setGroupTo(self.guigroups[0])
            widget.toplevel = True

    def on_mouse_press(self,x,y,button,modifiers):
        result = None
        #Left clicks only
        #iterate through toplevel widgets, see if any return hits.
        #returns None if no widgets hit, returns widget hit if otherwise
        #Will also search through all a widget's children
        if button == pyglet.window.mouse.LEFT:
            for wid in self.children:
                hit = wid.hitTest(x,y)
                if hit is not None:
                    if result is None:
                        result = hit
                    elif result.group < hit.group:     #if hit is defined, test if it's group is drawn on top of any previous hits
                        result = hit

            if self.focus is not None:
                if self.focus.holdsFocus:
                    #focus lost due to clicking on another widget
                    #self.focus.dehighlight()
                    self.focus.lostFocus(self)
    #                print('lost held focus: '+ repr(self.focus))
            self.focus = result
            if self.focus is not None:
                self.focus.gainedFocus(self)
    #            print('gained focus: '+repr(self.focus))


    def on_mouse_release(self,x,y,button, modifiers):
        result = None
        if button == pyglet.window.mouse.LEFT:
            for wid in self.children:
                hit = wid.hitTest(x,y)
                if hit is not None:
                    if result is None:
                        result = hit
                    elif result.group<hit.group:
                        result = hit

            if self.focus is None:
                pass
            else:
                if self.focus is result:
                    if self.focus.holdsFocus is True:
    #                    print('holding focus: '+ repr(self.focus))
                        pass

                    else:
                        #button click methods here
                        #self.focus.setVisibleTo(False)

    #                    print('lost focus as a button click: ' + repr(self.focus))
                        self.focus.lostFocus(self)
                        self.focus = None
                else: #focus loss is not result of mouserelease on focused widget



                    self.focus.lostFocus(self)
    #                print('lost focus, no action: '+ repr(self.focus))
                    #no button clicks here
                    self.focus = None
    '''
    conditions for losing focus:
    mouse is unpressed

    conditions for button
    mouse is unpressed while result = focus and focus is not none

    conditions for textwidget
    mouse is unpressed while result = focus and focus is not none and instead of releasing focus, focus is held
    '''
    def on_mouse_motion(self,x,y,dx,dy):
        #checks if mouse motion goes over any widgets. Any that are moved over are given mouseover status
        #works with children of widgets properly. should also get topmost drawn group too.
        #old and new mouseover statuses are communicated to the proper widgets
        result = None
        for topWidget in self.children:
            #print(topWidget)
            hit = topWidget.hitTest(x,y)
            if hit is not None:
                if result is None:
                    result = hit
                elif result.group<hit.group:
                    result = hit

        if self.mouseovered is not result:
            if self.mouseovered is not None:
                self.mouseovered.lostMouseOver(self)
    #            print('lost mouseOver: '+repr(self.mouseovered))
            self.mouseovered = result
            if self.mouseovered is not None:
                self.mouseovered.gainedMouseOver(self)
    #            print('gained mouseOver: '+repr(self.mouseovered))


    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        result = None
        if buttons == pyglet.window.mouse.LEFT:
            for topWidget in self.children:
                hit = topWidget.hitTest(x,y)
                if hit is not None:
                    if result is None:
                        result = hit
                    elif result.group<hit.group:
                        result = hit

            if self.mouseovered is not result:
                if self.mouseovered is not None:
                    self.mouseovered.lostMouseOver(self)
    #                print('lost mouseOver: '+repr(self.mouseovered))
                self.mouseovered = result
                if self.mouseovered is not None:
                    self.mouseovered.gainedMouseOver(self)
    #                print('gained mouseOver: '+repr(self.mouseovered))

        if self.focus is self.mouseovered and self.focus is not None:
            #self.focus.translate(dx,dy)
            pass



