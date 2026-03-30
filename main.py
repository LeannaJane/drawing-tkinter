import tkinter as tk

current_colour = "black"
last_x = None
last_y = None

root = tk.Tk()
root.title("Leanna Drawing APP")

canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack(expand=True, fill="both")

frame = tk.Frame(root)
frame.pack(pady=10)


size_slider = tk.Scale(
    root, 
    from_=1,
    to=30,
    orient="horizontal",
    label="Brush size"
)

size_slider.set(3)
size_slider.pack()

def set_colour(colour):
    global current_colour
    current_colour = colour 

def start_draw(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x, last_y

    if last_x is not None and last_y is not None:
        canvas.create_line(
            last_x, last_y,
            event.x, event.y,
            fill=current_colour,
            width=size_slider.get()
        )

    last_x = event.x
    last_y = event.y 


tk.Button(frame, text="Red", width=10, command=lambda: set_colour("red")).pack(side="left", padx=5)
tk.Button(frame, text="Yellow", width=10, command=lambda: set_colour("yellow")).pack(side="left", padx=5)
tk.Button(frame, text="Green", width=10, command=lambda: set_colour("green")).pack(side="left", padx=5)
tk.Button(frame, text="Blue", width=10, command=lambda: set_colour("blue")).pack(side="left", padx=5)


canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()