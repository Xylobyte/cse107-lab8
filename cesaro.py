import turtle


def draw(w, depth=0):
    """
    Draws a cesaro fractal at given length and depth recursively.

    w: width to draw the fractal
    depth: depth to draw the fractal. Used fo iterations. 
    """
    if depth == 0:
        turtle.forward(w)
    else:
        draw(w / 3, depth - 1)
        turtle.right(80)
        draw(w / 3, depth - 1)
        turtle.left(160)
        draw(w / 3, depth - 1)
        turtle.right(80)
        draw(w / 3, depth - 1)


def main():
    turtle.speed("fastest")
    turtle.penup()
    turtle.setpos(-400, 0)
    turtle.pendown()
    draw(500, 4)
    turtle.mainloop()


if __name__ == "__main__":
    main()
