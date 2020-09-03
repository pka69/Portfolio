def histogram(Data):
    for Number in Data:
        if type(Number) != int: return
    return('\n'.join(['#' * Number if type(Number) == int else 'None' for Number in Data]))

def histogram1(Data):
    out=[]
    for Number in Data:
        if type(Number) == int:
            out.append('#' * Number)
        else:
            return 
    return '\n'.join([outline for outline in out])

def histogram_vert(Data):
    hor = len(Data)
    try:
        vert = max(Data)
    except:
        return
    out=''
    for i in range(vert,0,-1):
        for j in range(hor):
            if Data[j]>=i: 
                out +=" #"
            else:
                out +="  "
        out +='\n'
    return out

if __name__ == '__main__':
    print('--------histogram - [2,6,5,3,1]--------------------------------')
    print(histogram([2,6,5,3,1]))
    print("--------histogram - [1, 2, 'error!']---------------------------")
    print(histogram([1, 2, 'error!']))
    print()
    print('--------histogram 1- [2,6,5,3,1]-------------------------------')
    print(histogram1([2,6,5,3,1]))
    print("--------histogram 1 - [1, 2, 'error!']-------------------------")
    print(histogram1([1, 2, 'error!']))
    print()
    print('--------histogram vert- [2,6,5,3,1]----------------------------')
    print(histogram_vert([2,6,5,3,1]))
    print("--------histogram vert - [1, 2, 'error!']----------------------")
    print(histogram_vert([1, 2, 'error!']))
    print()