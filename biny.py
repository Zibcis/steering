def DecimalToBinary(test_num):
    return  [int(i) for i in list('{0:0b}'.format(test_num))]

def binaryToDecimal(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def combine(buff1,buff):
    for i in buff1:
        buff.append(i)


def raw_angle(l):
    L1 = []
    L2 = []
    buff = []
    buff1 = []
    buff2 = []
    i=0
    L1.append(l[1])
    L1.append(l[2])
    L2.append(4)
    L2.append(154)
    buff1 = DecimalToBinary(L1[0])
    buff2 = DecimalToBinary(L1[1])
    print((360/4096)*binaryToDecimal(buff))
