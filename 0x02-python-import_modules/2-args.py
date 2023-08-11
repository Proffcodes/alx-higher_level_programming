import sys

# Get the total number of command-line arguments
total_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name itself

# Print the number of arguments
print(f"Number of argument{'s' if total_args != 1 else ''}: {total_args}", end="")

# Print ": " if there are arguments, otherwise print "."
print(": " if total_args > 0 else ".", end="\n")

# Print each argument
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"{i}: {arg}")
