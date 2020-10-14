num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("Your picked an even number.")


    # One line solution

    print("odd") if int(input("insert a number: ")) % 2 else print("even")