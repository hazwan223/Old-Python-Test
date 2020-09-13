def arranger(problems):
    if len(problems) > 5:
        print("Error: Too many problems.")

    rows = {
        "theFirst": [],
        "theSecond": [],
        "theThird": [],
    }
    output = ""

    for problem in problems:
        first, operator, second = problem.split()

        if len(first) > 4 or len(second) > 4:
            print("Error: Numbers cannot be more than four digits.")

        if operator == "*" or operator == "/":
            print("Error: Operator must be '+' or '-'.")

        try:
            num1 = int(first)
            num2 = int(second)

        except ValueError:
            print("Error: Numbers must only contain digits.")

        else:
            length = max(len(first), len(second))
            width = length + 2
            row1 = first.rjust(width)
            row2 = f"{operator} {second.rjust(length)}"
            row3 = "-" * width

            rows["theFirst"].append(row1)
            rows["theSecond"].append(row2)
            rows["theThird"].append(row3)

            if "theFourth" not in rows:
                rows["theFourth"] = []

            total = num1
            if operator == "+":
                total += num2
            elif operator == "-":
                total -= num2

            row4 = str(total).rjust(width)
            rows["theFourth"].append(row4)

    space = 4
    spaces = " " * space
    rows_values = rows.values()
    for i in rows_values:
        output = output + spaces.join(i)
        output = output + "\n"

    print(output)


arranger(["320 + 98", "3801 - 2", "45 + 43", "123 + 49"])
