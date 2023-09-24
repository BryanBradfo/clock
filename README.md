<!---
# Clock

Elaboration of a clock similar to the one that we can see on Pinterest, named "Fliqlo", when your screen is unactive for a while.
--->

# Python Clock

This project creates a digital clock similar to the Fliqlo clock. The clock is updated every second.

##  Prerequisites

- Python 3
- The tkinter module

## Installation

To install the tkinter module, run the following command in a terminal:
```
  pip install tkinter
```
## Usage

To run the clock, run the clock.py script in a terminal:

```
  python clock.py
```

## Code

The clock code is available in the clock.py file. The code is explained in detail below:

```python
import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Clock")

# Create the clock
clock = tk.Label(window, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=tk.BOTH, expand=1)

# Function to update the clock every second
def tick():
    current_time = time.strftime("%I:%M:%S %p")
    clock.config(text=current_time)
    clock.after(200, tick)

# Update the clock for the first time
tick()

# Start the Tkinter main loop
window.mainloop()

```

## Create the main window

The first step is to create the main window for the clock. The window is created using the tk.Tk() function. The function takes one argument, title, which defines the title of the window.

````python
window = tk.Tk()
window.title("Clock")
````

## Create the clock

The clock is created using the tk.Label() function. The function takes two arguments, window and text. The window argument defines the window in which the label will be created. The text argument defines the text that will be displayed on the label.
````python
clock = tk.Label(window, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=tk.BOTH, expand=1)
````

## Function to update the clock every second

The tick() function is used to update the clock every second. The function takes one argument, current_time, which contains the current time.

````python
def tick():
    current_time = time.strftime("%I:%M:%S %p")
    clock.config(text=current_time)
    clock.after(200, tick)
````

## Update the clock for the first time

The tick() function is called once to update the clock immediately.

````python
tick()
````

## Start the Tkinter main loop

The Tkinter main loop is started using the window.mainloop() function. The main loop keeps the clock open and updated automatically.

````python
window.mainloop()
````

## Possible improvements
The project can be improved in a number of ways, including:

- Adding the ability to change the font, size, and color of the clock.
- Adding the ability to display the date in addition to the time.
- Adding the ability to set the clock to 24-hour mode.
- Adding the ability to customize the background of the clock.

## Conclusion

This project is a great starting point for learning how to create Python applications using Tkinter.
