#Function to initialize the seats
def initializeSeats():
    seats = []
    for i in range(13):
        row = []
        for j in range(6):
            row.append('*')
        seats.append(row)
    return seats

#Function to display the menu and handle the seat reservation process
def showMenu(seats):
    while True:
        print("This program assigns seats for a commercial airplane.")
        print("The current seat assignments is as follows.")
        showSeatAssignments(seats)
        print("* -- available seat\nX -- occupied seat\n")
        print("Rows 1 and 2 are for first class passengers.")
        print("Rows 3 through 7 are for business class passengers.")
        print("Rows 8 through 13 are for economy class passengers.")
        reserve = input("To reserve a seat enter Y/y(Yes), N/n(No): \n").lower()
        if reserve == 'n':
            print("Exiting the program.")
            break
        elif reserve == 'y':
            ticketType = input("Enter ticket type: F/f (first class); B/b (business class); E/e (economy class): ")
            assignSeat(seats, ticketType)
        else:
            print("Invalid input. Please try again.")
            continue

#Function to show the current seat assignments
def showSeatAssignments(seats):
    print("\tA B C D E F")
    i = 1  # Initialize the row counter
    for row in seats:
        row_str = ""
        for seat in row:
            row_str += seat + " "
        row_str = row_str.strip()
        print(f"Row {i:<2}  {row_str}")
        i += 1 

#Function to handle seat assignment
def assignSeat(seats, ticketType):
    if ticketType.lower() == 'f':
        rowRange = range(1, 3)  # First class rows
    elif ticketType.lower() == 'b':
        rowRange = range(3, 8)  # Business class rows
    elif ticketType.lower() == 'e':
        rowRange = range(8, 14)  # Economy class rows
    else:
        print("Invalid ticket type.")
        return
    
    while True:
        rowInput = input(f"Enter Row number {rowRange.start} - {rowRange.stop - 1}: ")
        if rowInput.isdigit() and int(rowInput) in rowRange:
            row = int(rowInput)
        else:
            print(f"Invalid row number. Enter Row number {rowRange.start} - {rowRange.stop - 1}.")
            continue

        while True:
            seat = input("Enter seat number (A - F): ").upper()
            seat_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
            seat_index = seat_map.get(seat, -1)
            if seat_index == -1:
                print("Invalid seat number. Enter seat number (A - F).")
                continue
            
            if seats[row - 1][seat_index] == '*':  #Check if the seat is available
                seats[row - 1][seat_index] = 'X'  #Reserve the seat
                print("This seat is reserved for you")
                showSeatAssignments(seats)
                print("* -- available seat\nX -- occupied seat\n")
                return
            else:
                print("\n*#*#*#*# This seat is occupied *#*#*#*#")
                print("Make another selection")
                showSeatAssignments(seats)
                print("* -- available seat\nX -- occupied seat\n")
                print("Rows 1 and 2 are for first class passengers.")
                print("Rows 3 through 7 are for business class passengers.")
                print("Rows 8 through 13 are for economy class passengers.")
                break

def main():
    seats = initializeSeats()  #Initialize seats
    showMenu(seats)  #Display menu and handle seat reservations

main()
