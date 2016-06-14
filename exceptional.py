"""A module for demonstrating exceptions"""
import sys
from math import log


def convert(s):
    """Convert to an integer"""
    # x = -1
    try:
        return int(s)
        # print('conversion success x = ',x)
    # except ValueError:
    #     print('conversion failed')
    #     x = -1
    except (TypeError, ValueError) as e:
        # print('conversion failed type error')
        # x = -1
        # pass
        print('Error : {}'.format(str(e))) # file=sys.stderr in print is optional
        raise


def string_log(s):
    return log(convert(s))



