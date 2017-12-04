import sys, ast, getopt


DEFAULT_SUM = 10

def get_help():
    print("""Usage:\npython pairs.py -sum 100 "[1,2,3,4,5...]"\ndefault sum = 10""")
    sys.exit()


unix_options = "hs:"
gnu_options = ["help", "sum="]
try:
    opts, args = getopt.getopt(sys.argv[1:], unix_options, gnu_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

if opts:
    for opt, arg in opts:
        if opt in ("-s", "--sum"):
            DEFAULT_SUM = int(arg)
        if opt in ("-h", "--help"):
            get_help()

inputList = ast.literal_eval(sys.argv[-1])


if not isinstance(inputList, list):
    get_help()


for i in inputList:
    if not isinstance(i, int):
        get_help()


def get_pair(current_element, list_):
    for number in list_:
        if number + current_element == DEFAULT_SUM:
            return (min(number, current_element), max(number, current_element))
    return None


def process_list(list_of_elements):
    pairs = []
    for index, element in enumerate(list_of_elements):
        pair = get_pair(element, list_of_elements[index:])
        if pair: pairs.append(pair)
    print(pairs)


if __name__ == '__main__':
    process_list(inputList)
