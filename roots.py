import sys


def sqrt(x):
    """square root by Alexandria.

    Args:
        x: number to be rooted

    Returns:
        The square root of x
    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError('can\'t find root of -ve number {}'.format(x))
    guess = x
    i = 0
    while guess ** 2 != x and i < 20 :
        guess = (guess + x / guess) * 0.5
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e :
        # print("can't find root of -ve number")
        print(e, file=sys.stderr)
    print('normal execution')


if __name__ == '__main__':
    main()
