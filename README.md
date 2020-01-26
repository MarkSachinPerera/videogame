The video game based on the ai project.

## Frames and Bottons

```buildoutcfg
# Add a frame inside the main frame
# This will be the bottom frame
bottomframe = Frame(mywindow)
bottomframe.pack(side=BOTTOM)

# add a button
bottombutton = Button(mymainframe, text="bottom button", fg="red")
bottombutton.pack(side=BOTTOM)

# add a button
topbutton = Button(bottomframe, text="top button", fg="blue")
topbutton.pack(side=TOP)

# add a button
rightbutton = Button(bottomframe, text="right button", fg="blue")
rightbutton.pack(side=RIGHT)

# add a button
leftbutton = Button(bottomframe, text="left button", fg="blue")
leftbutton.pack(side=LEFT)
```


## the main loop

```
mywindow = Tk()  # main window that i will be editing

mymainframe = Frame(mywindow)

'''
The Frame widget is very important for the process of grouping and organizing other widgets in a somehow friendly way.
It works like a container, which is responsible for arranging the position of other widgets.

It uses rectangular areas in the screen to organize the layout and to provide padding of these widgets. A
frame can also be used as a foundation class to implement complex widgets.
 '''

mymainframe.pack()  # pack() arrange geometry

mywindow.mainloop()  # launch the program / window
```