import argparse
from bf import bitfieldise


if __name__ == '__main__':
    args = argparse.ArgumentParser('bitfieldiser',
                                   usage='TODO',
                                   description='TODO',
                                   epilog='TODO',
                                   add_help=True, allow_abbrev=True, exit_on_error=True)  # should be default anyway
    args.add_argument('input_file', type=str, required=True,
                      help='TODO')
    args.add_argument('array', type=str, required=True,
                      help='TODO')
    args.add_argument('dim1', type=int, required=True,
                      help='TODO')
    args.add_argument('dim2', type=int, required=True,
                      help='TODO')
    parsed_args = args.parse_args()
    input_file = parsed_args.input_file
    array = parsed_args.array
    dim1 = parsed_args.dim1
    dim2 = parsed_args.dim2
    bitfieldise(input_file, array, dim1, dim2)
