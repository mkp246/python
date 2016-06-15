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
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}",format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid row {}".format(row))
        if row not in rows:
            raise ValueError("Invalid seat " + row)
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger


    def aircraft_model(self):
        return self._aircraft.model()  # can't interroget aircraft object directly


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


