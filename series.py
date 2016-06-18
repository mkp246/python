import sys


def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf=8')
        # series = list() # file won't be closed if any error occurred
        return [int(line.strip()) for line in f]
        # for line in f:
        #     l = int(line.strip())
        #     series.append(l)
    finally: # always executed block no matter what happens to error
        print("closing file")
        f.close()
    return series


def read_series_with(filename): # no need to call close explicitly as protocol context(with) will handle it
    with open(filename, mode='rt', encoding='utf-8') as file:
        return [int(line.strip()) for line in file]


def main(filename):
    series = []
    try:
        series = read_series(filename)
    except ValueError as e:
        print(series)
    print("+++++Read with Context+++++")
    series = read_series_with(filename)
    print(series)


if __name__ == '__main__':
    main(sys.argv[1])

