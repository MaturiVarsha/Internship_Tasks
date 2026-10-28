# Problem 7: Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    letters=string.ascii_lowercase
    width=4*size-3
    lines=[]
    for i in range(size):
        part='-'.join(letters[size-1:size-i-1:-1]+letters[size-i-1:size])
        lines.append(part.center(width,'-'))
    print('\n'.join(lines+lines[-2::-1]))

if __name__=='__main__':
    print_rangoli(int(input()))
