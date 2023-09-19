import math

# Square—The area is the length of a side squared.
#  Square = sideValue * sideValue

squareArea = input("What is the length of a side of the square?: ")
parsedSquareArea = float(squareArea) * float(squareArea)
print(f"The area of the square is: {parsedSquareArea}")

# Rectangle—The area is the length multiplied by the width.
# Rectangle = lengthValue * widthValue

rectangleLength = input("What is the length of a side of the Rectangle?: ")
rectangleWidth = input("What is the width of a side of the Rectangle?: ")
parsedRectangleArea = float(rectangleLength) * float(rectangleWidth)
print(f"The area of the Rectangle is: {parsedRectangleArea}")

# Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
# Circle = Pi 3.14 * radiusSquaredValue

# No. 1 ::: INSTRUCTIONS :::
# Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value
# of Pi included in the python "math" module. Hint, you might try searching on the internet
#  for something like, "python how to get the value of pi."

circleArea = input("What is the radius of the circle?: ")
# I will use the math.pi function from the math Library I have already imported above
parsedCircleArea = math.pi * (float(circleArea) ** 2)
print(f"The area of the circle is: {parsedCircleArea:.4f}")

# No. 2 ::: INSTRUCTIONS :::
# Prompt the user for a single length value, then compute and display the areas
# of a square with that length of side, a circle with that radius, and then the volumes
# of a cube with that side and a sphere with that radius, all from the same value from the user.


print("I will now calcullate the length of the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value you are required to enter below")
allLength = input("Enter a length value: ")

# Calculating the area of a Square
allSquareArea = float(allLength) * float(allLength)
print(f"The area of a Square is: {allSquareArea:.2f}.")

# Calculating the area of a Circle
allCircleArea = math.pi * (float(allLength) ** 2)
print(f"The area of a Circle is: {allCircleArea:.3f}.")

# Calculating the area of a Cube
allCubeArea = float(allLength) ** 3
print(f"The volume of a Cube is: {allCubeArea:.4f}.")

# Calculating the volume of a Sphere with the same value as the radius
allSphereArea = 4/3 * math.pi * (float(allLength) ** 3)
print(f"The Volume of a Sphere is: {allSphereArea:.4f}.")
