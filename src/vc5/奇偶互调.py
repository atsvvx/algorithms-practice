# 奇偶互调
if __name__ == '__main__':
    a = 9  # 1001

    b = 10  # 1010 >>
    c = 5   # 0101 <<

    d = a & b  #
    e = a & c  #

    res = (e << 1) ^ (d >> 1)

    pass
