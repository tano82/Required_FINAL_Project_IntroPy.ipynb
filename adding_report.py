"""This program calls the adding_report() function which repeatedly takes positive integer/
input until the user quits and then sums the integers and prints a "report"."""

def adding_report(report="T"):
    """"A" used as the argument to adding_report() results in printing of all of the input integers and the total
"T" used as the argument results in printing only the total."""
    total = 0
    item = 0
    item_list = ""

    print('Report Types include All Items ("A") or Total Only ("T")')
    report = input('Choose report Type ("A") or ("T") ')

    while True:
        if report.lower() == "a":
            item = input('Input an integer to add to the total or "Q" to quit: ')
            if item.isdigit():
                total += int(item)
                item_list += str(item) + '\n'
            elif item.lower().startswith("q"):
                print("\nItems\n" + item_list + "\nTotal\n" + str(total))
                break
            else:
                print(item, "is Invalid Input")
        elif report.lower() == "t":
            item = input('Input an integer to add to the total or "Q" to quit: ')
            if item.isdigit():
                total += int(item)
            elif item.lower().startswith("q"):
                print("\nTotal\n" + str(total))
                break
            else:
                print(item, "is Invalid Input")
        else:
            report = input('Choose report Type ("A") or ("T") ')

adding_report()