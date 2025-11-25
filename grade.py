def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

def main():
    marks = float(input("Enter your marks: "))
    grade = calculate_grade(marks)
    print("Your grade is:", grade)

if __name__ == "__main__":
    main()
