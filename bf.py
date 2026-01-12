

C_TYPE_TO_REPLACE = ['char', 'short', 'long']  # TODO others?


def bitfieldise(filename_in: str, bitarr: str, dim1: int , dim2: int) -> None:
    nn1 = dim1 / 8
    n1 = int(nn1)
    if n1 == nn1:
        n1 += 1
