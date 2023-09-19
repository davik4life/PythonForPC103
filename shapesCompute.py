# Square—The area is the length of a side squared.
#  Square = sideValue * sideValue

squareArea = input("What is the length of a side of the square?: ")
parsedSquareArea = float(squareArea) * float(squareArea)
print(f"The area of the square is: {parsedSquareArea:.2f}")

# Rectangle—The area is the length multiplied by the width.
# Rectangle = lengthValue * widthValue

rectangleLength = input("What is the length of a side of the Rectangle?: ")
rectangleWidth = input("What is the width of a side of the Rectangle?: ")
parsedRectangleArea = float(rectangleLength) * float(rectangleWidth)
print(f"The area of the Rectangle is: {parsedRectangleArea:.3f}")

# Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
# Circle = Pi 3.14 * radiusSquaredValue

circleArea = input("What is the radius of the circle?: ")
parsedCircleArea = 3.14 * (float(circleArea) ** 2)
print(f"The area of the circle is: {parsedCircleArea:.3f}")
