import sys

text_string = 'tsst'

def string_rev(string):
    rev_string = string[::-1]
    return string[::-1]

def main():
    reverse_string=string_rev(text_string)
    if (reverse_string == text_string):
        print 'same string'
    else:
        print 'different string'




if __name__ == '__main__':
    main()
