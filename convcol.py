"""convcol.py: Quickly convert HEX color codes to RGB"""

__author__ = "Steve Gilissen"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Steve Gilissen"

import argparse

parser = argparse.ArgumentParser(description='Convert colors from HEX to RGB')
parser.add_argument('color', help='The color to convert')
args = parser.parse_args()


def convert_color(val):
    val = val.lstrip('#')
    lv = len(val)
    print(tuple(int(val[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))


if __name__ == "__main__":
    convert_color(args.color)
