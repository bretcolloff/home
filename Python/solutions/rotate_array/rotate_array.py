
def main(argv=None):
    a = []
    size = 4
    for i in range(0,size):
        b = []
        for j in range(0, size):
            b.append(j * i)
        a.append(b)
    temp = a[0][0]
    a[0][0] = a[0][3]
    a[0][3] = a[3][3]
    a[3][3] = a[3][0]
    a[3][0] = temp

    dr = []
    for x in range(0, size):
        dr.append((x,x))

    ur = []
    for x in reversed(range(0, size)):
        ur.append((x, (size-1) - x))

    half = int(size/2)
    ul = list(reversed(dr))[0:half]
    dl = list(reversed(ur))[0:half]
    ur = ur[0:half]
    dr = dr[0:half]
    for i in range(0, half):
        tr = dl[i]

        print (tr)
        for b in a:
            print(b)
        while dr[i] != tr:
            print (dr[i], dl[i], ul[i], ur[i])
            (xa, xb) = dr[i]
            (ya, yb) = dl[i]
            (za, zb) = ul[i]
            (wa, wb) = ur[i]
            temp = a[xa][xb]
            a[xa][xb] = a[wa][wb]
            a[wa][wb] = a[za][zb]
            a[za][zb] = a[ya][yb]
            a[ya][yb] = temp
            xb += 1
            ya += 1
            zb -= 1
            wa -= 1
            dr[i] = (xa, xb)
            dl[i] = (ya, yb)
            ul[i] = (za, zb)
            ur[i] = (wa, wb)

    for b in a:
        print(b)


if __name__ == '__main__':
    main()
