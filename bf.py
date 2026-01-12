import math
from os import path


C_TYPE_TO_REPLACE = ['char', 'short', 'long']  # TODO others?
PREFIX = 'bitfieldised_'


def bitfieldise(filename_in: str, bitarr: str, dim1: int , dim2: int) -> None:
    split_infile_path = path.split(filename_in)
    bare_filename = split_infile_path[1]
    prefixed_filename = PREFIX + bare_filename
    filename_out = path.join(split_infile_path[0], prefixed_filename)
    nn1 = dim1 / 8
    n1 = int(nn1)
    if n1 == nn1:
        n1 += 1
    c_type = C_TYPE_TO_REPLACE[int(math.log(n1, 2))]
    n2 = 2 ** (n1 * 8) - 1
    n1 = n1 * 8 - 1
