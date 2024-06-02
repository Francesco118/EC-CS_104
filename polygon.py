import turtle
import random

def draw_polygon(sides, side_length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(360 / sides)
    turtle.end_fill()

def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))

def main():
    turtle.speed(0)  # fastest speed

    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "gray"]

    while True:
        sides = int(input("Enter the number of sides (1-99): "))
        while sides < 1 or sides > 99:
            print("Invalid input. Please enter a number between 1 and 99.")
            sides = int(input("Enter the number of sides (1-99): "))

        side_length = int(input("Enter the length of each side (in pixels): "))

        print("Choose a color:")
        for i, color in enumerate(colors):
            print(f"{i+1}. {color}")
        print("11. Rainbow (random colors for each side)")

        choice = int(input("Enter your choice (1-11): "))
        while choice < 1 or choice > 11:
            print("Invalid input. Please enter a number between 1 and 11.")
            choice = int(input("Enter your choice (1-11): "))

        if choice == 11:
            for _ in range(sides):
                turtle.pencolor(random_color())
                turtle.fillcolor(random_color())
                turtle.begin_fill()
                turtle.forward(side_length)
                turtle.right(360 / sides)
                turtle.end_fill()
        else:
            color = colors[choice - 1]
            draw_polygon(sides, side_length, color)

        response = input("Do you want to draw another polygon? (y/n): ")
        if response.lower()!= 'y':
            break

    turtle.done()

if __name__ == "__main__":
    main()