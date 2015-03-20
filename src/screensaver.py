#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 6, 2013

@author: J Carroll
@emaill: jrcarroll@jrcresearch.net
'''

#!/usr/bin/env python

import gtk, random, gobject

# This function will be called whenever you click on the button:
def click_handler(widget) :
    # quit the application:
    gtk.main_quit()

def clip(i, min, max) :
    if i < min :
        return min
    if i > max :
        return max
    return i

# Global variables used by the expose and idle handlers:
xgc = None
x1 = None
x2 = None
y1 = None
y2 = None
r = random.randint(0, 65535)
g = random.randint(0, 65535)
b = random.randint(0, 65535)
movesize = 20
colorjump = 2048

def idle_handler(widget) :
    global xgc, x1, x2, y1, y2, r, g, b, movesize, colorjump

    if (xgc == None) :
        xgc = widget.window.new_gc()
        w, h = widget.window.get_size()
        x1 = random.randint(0, w)
        x2 = random.randint(0, w)
        y1 = random.randint(0, h)
        y2 = random.randint(0, h)

    # Change the line boundaries a little bit:
    w, h = widget.window.get_size()
    x1 = clip(x1 + random.randint(-movesize, movesize), 0, w)
    x2 = clip(x2 + random.randint(-movesize, movesize), 0, w)
    y1 = clip(y1 + random.randint(-movesize, movesize), 0, h)
    y2 = clip(y2 + random.randint(-movesize, movesize), 0, h)

    # Change the color a little bit:
    r = clip(r + random.randint(-colorjump, colorjump), 0, 65535)
    g = clip(g + random.randint(-colorjump, colorjump), 0, 65535)
    b = clip(b + random.randint(-colorjump, colorjump), 0, 65535)
    xgc.set_rgb_fg_color(gtk.gdk.Color(r, g, b))

    # Draw the new line
    widget.window.draw_line(xgc, x1, y1, x2, y2)

    # Return True so we'll be called again:
    return True

# Create the main window:
win = gtk.Window()

# Organize widgets in a vertical box:
vbox = gtk.VBox()
win.add(vbox)

# Create an area to draw in:
drawing_area = gtk.DrawingArea()
drawing_area.set_size_request(600, 400)
vbox.pack_start(drawing_area)

# set our drawing function
idle_id = gobject.idle_add(idle_handler, drawing_area)

drawing_area.show()

# Make a pushbutton:
button = gtk.Button("Quit")

# When it's clicked, call our handler:
button.connect("clicked", click_handler)

# Add it to the window:
vbox.pack_start(button)
button.show()
# Obey the window manager quit signal:
win.connect("destroy", gtk.main_quit)

vbox.show()
win.show()

gtk.main()

