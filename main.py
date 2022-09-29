import math

print("\nCourse Score Calculator\n")
print("Hello dear student!\nThis program calculates your course scores easily. Please follow next instructions. ")
name = input("\nPlease enter your name: ")

print("Welcome" + " " + name + "." + " " "Firstly, In this step we need your 4 assignments scores. ")
cont = input("If you want to continue, press 'Y' or press a button to quit ").lower()

while True:

    if cont != "y":
        print("Exiting the program")
        break

    assignment1 = input("Enter your 1. assignment score: ")
    assignment2 = input("Enter your 2. assignment score: ")
    assignment3 = input("Enter your 3. assignment score: ")
    assignment4 = input("Enter your 4. assignment score: ")

    cal1 = int((float(assignment1) + float(assignment2) + float(assignment3) + float(assignment4)) / 4)

    print("Secondly, In this step we need your 2 test scores ")
    cont1 = input("If you want to continue, press 'Y' or press a button to quit ").lower()

    if cont1 != "y":
        print("Exiting the program")
        break

    test_score1 = input("Enter your 1. test score: ")
    test_score2 = input("Enter your 2. test score: ")

    cal2 = int((float(test_score1) + float(test_score2)) / 2)

    print("Finally, In this step we need your 2 lab-works scores ")
    cont2 = input("If you want to continue, press 'Y' or press a button to quit ").lower()

    if cont2 != "y":
        print("Exiting the program")
        break

    lab_score1 = input("Enter your 1. lab-score: ")
    lab_score2 = input("Enter your 2. lab-score: ")

    cal3 = int((float(lab_score1) + float(lab_score2)) / 2)

    score = ((cal1 / 100 * 10) + (cal2 / 100 * 70) + (cal3 / 100 * 20))
    print(math.ceil(score))

    calculate_result = input("To see your result in letter press 'Y' ").lower()

    while calculate_result == "y":
        if score >= 0 and score <= 100:
            if score >= 90:
                print("You got 'A' ")
            elif score >= 80:
                print("You got 'B' ")
            elif score >= 70:
                print("You got 'C' ")
            elif score >= 60:
                print("You got 'D' ")
            else:
                print("You failed..")
        calculate_result = input("If you want to recalculate press 'Y', "
                  "if you do not want, press 'Q' ").lower()
        if calculate_result != "q" and calculate_result != "y":
            print("You entered wrong value. Press 'Y' / 'Q' or it will turn off")
            calculate_result = input("'Y' or 'N' ").lower()
    else:
        print("Exiting...")
