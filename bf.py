from math import log2
from os import path
import json
# TODO: mono gia th main, h gia sygkekrimenh synarthsh


C_TYPE_USED = ['char', 'short', 'long']
PREFIX = 'bitfieldised_'


def get_preamble(my_json:json) -> list[str]:
    preamble_lines = ['']  # TODO: get preamble from json
    return preamble_lines


def replace_array(my_json: json, my_type: str, a: int, b: int, c: int, d: int) -> list[str]:
    # periptwseis:
    # den ksekina arrayname[...][...] apo edw
    # typos mplampla,arrayname[x][y],mplamplampla;->union my_union arrayname[x];typos mplampla,mplamplampla;
    # typos mplampla,arrayname[x][y];->typos mplampla;union my_union arrayname[x];
    # typos arrayname[x][y],mplampla;->typos mplampla;union my_union arrayname[x];
    # typos arrayname[x][y];->union my_union arrayname[x];
    # initialisation
    # arrayname[a][b]=mplampla;->set(arrayname,a,b,mplampla);
    # mplamplampla(arrayname[a][b]=mplampla)mplamplamplampla->set(arrayname,a,b,mplampla);mplamplampla(mplampla)mplamplamplampla
    # arrayname[a][b]&=mplampla;->set(arrayname,a,b,get(arrayname,a,b)&mplampla);
    # arrayname[a][b]|=mplampla;->set(arrayname,a,b,get(arrayname,a,b)|mplampla);
    # arrayname[a][b]^=mplampla;->set(arrayname,a,b,get(arrayname,a,b)^mplampla);
    # arrayname[a][b]&&=mplampla;->set(arrayname,a,b,get(arrayname,a,b)&&mplampla);
    # arrayname[a][b]||=mplampla;->set(arrayname,a,b,get(arrayname,a,b)||mplampla);
    # an to entopise alla den einai tipota apo ta parapanw tote exagwgh timhs: arrayname[a][b]->get(arrayname,a,b)
    return ['']  # TODO


def make_json(filename: str) -> json:
    ep_out = ''  # TODO: run external parser
    return json.loads(ep_out)


def bitfieldise(filename_in: str, bitarr: str, dim1: int , dim2: int) -> None:
    json_in = make_json(filename_in)
    preamble = get_preamble(json_in)
    split_infile_path = path.split(filename_in)
    bare_filename = split_infile_path[1]
    prefixed_filename = PREFIX + bare_filename
    filename_out = path.join(split_infile_path[0], prefixed_filename)
    nn1 = dim1 / 8
    n1 = int(nn1)
    if n1 == nn1:
        n1 += 1
    c_type = C_TYPE_USED[int(log2(n1))]
    n2 = 2 ** (n1 * 8) - 1
    n1 = n1 * 8 - 1
    altered_program = replace_array(json_in, c_type, n1, n2, dim1, dim2)
    lines_to_write: list[str] = [
        '#define BITFIELDISED_SIZE1 ' + str(dim1) + '\n',
        '#define BITFIELDISED_SIZE2 ' + str(dim2) + '\n',
        '#define NUMBER1 ' + str(n1) + '\n',
        '#define NUMBER2 ' + str(n2) + '\n',
    ] + preamble + [
        'struct my_bitfield{\n',
    ] + ['char bit'+str(i)+':1\n' for i in range(dim1)] + [
        '};\n',
        '\n',
        '\n',
        'union my_union{\n',
        '	struct my_bitfield bit_data;\n',
        '	unsigned '+c_type+' int_data;\n',
        '};\n',
        '\n',
        'void set(union my_union pm[BITFIELDISED_SIZE2],int a,int b,char k);\n',
        'void print(union my_union pm[BITFIELDISED_SIZE2]);\n',
        'char get(union my_union pm[BITFIELDISED_SIZE2],int a,int b);\n',
        '\n',
    ] + altered_program + [
        'void set(union my_union pm[BITFIELDISED_SIZE2],int a,int b,char k){\n',
        '	if(k==1)pm[a].int_data|=(unsigned)1<<(NUMBER1-b);' + \
        'else if(!k)pm[a].int_data&=(unsigned)NUMBER2<<(NUMBER1-b);else printf(\"wrong input\\n\");\n',
        '}\n',
        '\n',
        'void print(union my_union pm[BITFIELDISED_SIZE2]){\n',
        '	int i,j;\n',
        '\n',
        '	printf(\"\\n\");\n',
        '	for(j=0;j<BITFIELDISED_SIZE2;j++){\n',
        '		for(i=0;i<BITFIELDISED_SIZE1;i++){\n',
        '			printf(\"\%d \", get(pm,i,j));\n',
        '		}\n',
        '		printf(\"\\n\");\n',
        '	}\n',
        '}\n',
        '\n',
        'char get(union my_union pm[BITFIELDISED_SIZE2],int a,int b){\n',
        '	return((pm[b].int_data & (unsigned) 1<<(NUMBER1-a)) >> (NUMBER1-a));\n',
        '}\n',
    ]

    with open(filename_out, 'w', encoding='UTF-8') as f_out:
        f_out.writelines(lines_to_write)
