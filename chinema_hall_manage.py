class Star_cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    @classmethod
    def view_hall(clas):
        return clas.hall_list


class Hall(Star_cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self._show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().entry_hall(self)

    def __repr__(self):
        return f"Hall No: {self.__hall_no}, Total Rows: {self.rows}, Total Columns: {self.__cols}"

    def entry_show(self, id, movie_name, time):
        movie = (id, movie_name, time)
        matrix = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        self.seats[id] = matrix
        self._show_list.append(movie)

    def book_seats(self):
        print("Which film are you hoping to enjoy?")
        New = True
        while True:
            id1 = int(input("Tell me the ID, please: "))
            if id1 in self.seats:
                print("Where do you want to book a seat? Tell me row and column.")
                while True:
                    r = int(input("Row: "))
                    c = int(input("colum: "))
                    if 0 <= r < self.__rows and 0 <= c < self.__cols:
                        if self.seats[id1][r][c] == 0:
                            self.seats[id1][r][c] = 1
                            print(
                                f"Seat ({r}, {c}) booked successfully for show ID {id1}."
                            )
                            print("Do you want to book another one?")
                            num = int(input("If yes! press 1, otherwise press 0 :"))
                            if num == 0:
                                New = False
                                break
                        else:
                            print(f"Seat ({r}, {c}) is already booked!")
                            print("Please enter another seat number!")
                    else:
                        print("Invalid row or column number!")
                        print("Please enter a valid seat number!")
                break
            else:
                print("Show ID not found! Please enter a valid ID. ")

    def view_show_list(self):
        print("")
        print(f"Shows in Hall No: {self.__hall_no}")
        for show in self._show_list:
            print(f"Movie: {show[1]}, Show ID: {show[0]},  Time: {show[2]}")

    def view_available_seats(self):
        print("Which film are you hoping to enjoy?")
        while True:
            id1 = int(input("Tell me the ID, please: "))
            if id1 in self.seats:
                print(
                    f"\nAvailable seats for Show ID: {id1} in Hall No {self.__hall_no}:"
                )
                for row in self.seats[id1]:
                    print(row)
                break

            else:
                print("Show ID not found! Please enter a valid ID. ")


hall1 = Hall(5, 5, 1)
hall2 = Hall(5, 8, 2)

hall1.entry_show(111, "Jhaka Naka", "11 am")
hall1.entry_show(221, "Matha Nosto", "2 pm")

hall2.entry_show(222, "Jhaka Naka 2", "11 am")
hall2.entry_show(333, "Matha Nosto 2", "2 pm")

text = """
    Welcome to Star Cinema Hall...
    where every ticket is a passport to unforgettable stories, laughter
    and adventure under the dazzling lights of the silver screen!"""

print(text)

while True:
    press = int(
        input(
            "\n Tell me what you'd like."
            "\n   To view all show Today, press 1.\n"
            "   To view all available seats, press 2.\n"
            "   To book a seat, press 3.\n"
            "   To exit, press 0.\n \n"
        )
    )
    if press == 1:
        for hall in Star_cinema.view_hall():
            hall.view_show_list()

    elif press == 2:
        print("Which hall is your preference? Tell me the number: ")
        while True:
            no = int(input())
            if 0 <= no - 1 < len(Star_cinema.view_hall()):
                hall = Star_cinema.view_hall()[no - 1]
                hall.view_available_seats()
                break
            else:
                print(
                    "This hall isn't currently available write now!\n"
                    "Please enter a valid hall number:"
                )

    elif press == 3:
        print("Which hall is your preference? Tell me the number: ")
        while True:
            no = int(input())
            if 0 <= no - 1 < len(Star_cinema.view_hall()):
                hall = Star_cinema.view_hall()[no - 1]
                hall.book_seats()
                break
            else:
                print(
                    "This hall isn't currently available write now!\n"
                    "Please enter a valid hall number:"
                )

    elif press == 0:
        print("     Thank you for visiting Star Cinema Hall!\n"
            "       We look forward to welcoming you back for more amazing movie moments. See you soon!")
        break
