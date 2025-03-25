import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(event):
    """Erase objects in contact with the eraser"""
    x, y = event.x, event.y
    overlapping_items = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)

    for item in overlapping_items:
        canvas.itemconfig(item, fill="white")  # Color change to white

def main():
    global canvas
    root = tk.Tk()
    root.title("Eraser Grid")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            x1, y1 = col * CELL_SIZE, row * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")

    canvas.bind("<B1-Motion>", erase_objects)  # Left mouse button hold to erase

    root.mainloop()

if __name__ == '__main__':
    main()
