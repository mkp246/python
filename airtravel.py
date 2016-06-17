"""Model for aircraft flight"""


class Flight:
    """A flight with particular passenger aircraft"""

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in ", number)
        if not number[:2].isupper():
            raise ValueError("Invalid airline code in ", number)
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number ", number)
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat) # required self always
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("Seat {} is not occupied".format(from_seat))
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("Seat {} is already occupied".format(to_seat))
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}", format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid row {}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid seat " + row)
        return row, letter

    def aircraft_model(self):
        return self._aircraft.model()  # can't interroget aircraft object directly

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self._number, self.aircraft_model())

    def _passenger_seats(self):
        row_number, seat_letters = self._aircraft.seating_plan()
        for row in row_number:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row,letter))


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registation

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1 ), "ABCDEFGHJK"[:self._num_seats_per_row]


def make_flight():
    aircraft = Aircraft("G-EUT", "Airbus A319", num_rows=22, num_seats_per_row=6)
    f = Flight("BA758", aircraft)
    f.allocate_seat('12A', "Ankita singh")
    f.allocate_seat('13A', "Ankit Pandey")
    f.allocate_seat('15A', "Andres Chao")
    f.allocate_seat('15E', "Killi Sahng")
    f.allocate_seat('21B', "Amy Lanistor")
    f.allocate_seat('1C', "Richa Sharama")
    f.allocate_seat('1D', "Ricky Bhat")
    return f

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {}" \
            "  Flight: {}" \
            "  Seat: {}" \
            "  Aircraft: {}" \
            " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) -2) +'+'
    border = '|' + ' ' * (len(output) -2) +'|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
