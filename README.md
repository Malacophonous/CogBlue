# CogBlue
A hobbyist level GUI for use with Pyglet (python based graphics package)


Reason for existance:
I wanted a gui that I could use within Pyglet for some game ideas I've had. Other solutions didn't seem to make sense to me. This is a learning project as much as a usable one.


Overview:
* The App class is to facilitate the Pyglet plumbing stuff and the ability to save/load GUI configurations from a file.
* The Window class is subclassed from Pyglet's window class. Users may want to mess with this too to get the functionality they want.
* The Widget class is the base class for all of the traditional GUI widgets that I've implemented so far. Each type will define slightly different methods and behaviours.
* The buildingblocks.py file contains basic graphic data objects and wrappers for some base Pyglet objects like text Labels.
* The Style class is used for defining colors for widgets and text. The base widget class though uses random colors at the moment.
* The Window and Widgets maintain parent/child links to allow stuff like translation motion of widgets and state changes that affect child widgets.
  
I group all the draw calls for GUI widgets to a single batch. Child widgets get drawn after their parents with pyglet's OrderedGroup. (lower means drawn under higher numbers). I have yet to implement logic to prevent widgets of a similar layer from overlaying each other. It should be trivial for rectangles but I'd like to be able to support other shapes too.



Current objective:
* An app-builder allowing a user to place widgets of different kinds and save their configuration to a file for loading later.

Other planned features:
* right click context menu
* widget highlighting
* support for arbitrary convex polygons
* texture image loading
* dynamic resizing of widgets
* saving and loading of widget configurations to a easy to read text file
