from airtravel import *
aircraft = Aircraft("G-EUT", "Airbus A319", num_rows=22, num_seats_per_row=6)
f = Flight("BA758", aircraft)
f.allocate_seat('12A', "Ankita singh")
f.allocate_seat('12A', "Ankit Pandey")
f.allocate_seat('15A', "Andres Chao")
f.allocate_seat('15E', "Killi Sahng")
f.allocate_seat('E27', "Amy Lanistor")
f.allocate_seat('1C', "Richa Sharama")
f.allocate_seat('1D', "Ricky Bhat")


