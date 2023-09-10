
# ssh-rsa
def display_title():
    print("Welcome to Grade Calculator")


def get_totalPoints():
    while True:
        try:
            total_points = float(input("Enter the total score(0-1000):"))
            if 0 <= total_points <= 1000:
                return total_points
            else:
                print("You must enter an integer value >=0 and <=1000. Try Again")
        except ValueError:
            print("You must enter an integer value >=0 and <=1000. Try Again")


def get_letterGrade(averageEarned):
    if 92 <= averageEarned <= 100:
        return 'A'
    elif 88 <= averageEarned <= 91.99:
        return 'B+'
    elif 82 <= averageEarned <= 87.99:
        return 'B'
    elif 78 <= averageEarned <= 81.99:
        return 'C+'
    elif 70 <= averageEarned <= 77.99:
        return 'C'
    elif 60 <= averageEarned <= 69.99:
        return 'D'
    else:
        return 'F'


def main():
    while True:
        display_title()
        total_points = get_totalPoints()
        averageEarned = (total_points / 1000) * 100
        m = get_letterGrade(averageEarned)
        print(f"You earned an average of {averageEarned:}%. Letter grade earned: {m}")
        a = input("Would you like to enter another score (y/n)?: ")
        if a != 'y':
            print("Thank you")
            break


if __name__ == "__main__":
    main()
