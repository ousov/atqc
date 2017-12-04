import sys, getopt


number = None
message = 'Usage:\nfibo.py -n <integer>\nWhere <integer> is a positive number > 0'

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:", ["number="])
except getopt.GetoptError:
    print('Something went wrong with parameters. Try fibo.py -h')
    sys.exit(2)

# If no parameter was given or a wrong parameter was given -> exit app
if not opts:
    print('Wrong parameter was given or wasn\'t given at all. {usage}'.format(message))

# Check parameters
for opt, arg in opts:
    if opt == '-h':
        print(message)
        sys.exit()
    elif opt in ('-n', '--number'):
        try:
            number = int(arg)
            if number == 0:
                raise ValueError
        except ValueError:
            print('Number must be an postive integer and not a null')
            sys.exit()


def main(n):
    """
    Function to get specific Fibonacci number.
    
    Keyword args:
    n -- positive integer number
    returns:
    Specific integer number from Fibonacci sequence
    """
    a, b = 0, 1
    if n == 1:
        print(a)
        return
    elif 0 < n <= 3:
        print(b)
        return
    else:
        for i in xrange(n - 1):
            a, b = b, b + a
        print(b)

if __name__ == "__main__":
    main(number)

