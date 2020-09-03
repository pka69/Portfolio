def chessboard(n=8):
    out = []
    for i in range(n):
        s = ''
        for j in range(n):
            s+= "#" if (i+j) % 2 == 0 else " "
        out.append(s + '\n')
    return ''.join([outline for outline in out])

def chessboard_1(n=8):
    char= ["#", " "]
    return '\n'.join(''.join([char[(i+j)%2] for i in range(n)]) for j in range(n))

if __name__ == '__main__':

    print('-------chessboard dla 8----------------------------------------')
    print(chessboard())
    print('-------chessboard_1 dla 7---------------------------------------')
    print(chessboard_1(7))