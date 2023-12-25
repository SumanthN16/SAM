# Define a function to generate a triangle of given size
def generate_triangle(size):
    # Loop through the rows of the triangle, from 1 to size
    for row in range(1, size+1):
        # Print spaces before each row to create a pyramid shape
        print(" " * (size-row), end="")
        # Loop through the columns of the triangle in each row
        for col in range(1, row+1):
            # Print "*" for each column
            print("*", end="")
        # Move to next line after each row is complete
        print()

# Ask user to enter the size of the triangle
size = int(input("Enter the size of the triangle: "))
# Call the function with user input as argument
generate_triangle(size)

