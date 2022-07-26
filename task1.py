# Доделать реализацию функции eval со скобками



def pars(st):
    st_new = []
    data = ''
    for i in range(len(st)):
        if st[i].isdigit():
            data += st[i]
        else:
            if data.isdigit():
                st_new.append(int(data))
                st_new.append(st[i])
                data = ''
            else:
                st_new.append(st[i])
    if data.isdigit():
        st_new.append(int(data))
    if st_new[0] == '-':
        st_new[1] *= -1
        del st_new[0]
    return st_new

def calculation(lst):
    res_calc = 0
    i = 0
    while '*' in lst or '/' in lst:
        if lst[i] == '*':
            res_calc = lst[i - 1] * lst[i + 1]
            lst[i + 1] = res_calc
            del lst[i - 1:i + 1]
            i = 0
            res_calc = 0
        elif lst[i] == '/':
            res_calc = lst[i - 1] / lst[i + 1]
            lst[i + 1] = res_calc
            del lst[i - 1:i + 1]
            i = 0
            res_calc = 0
        else:
            i += 1
    while '+' in lst or '-' in lst:
        if lst[i] == '+':
            res_calc = lst[i - 1] + lst[i + 1]
            lst[i + 1] = res_calc
            del lst[i - 1:i + 1]
            i = 0
            res_calc = 0
        if lst[i] == '-':
            res_calc = lst[i - 1] - lst[i + 1]
            lst[i + 1] = res_calc
            del lst[i - 1:i + 1]
            i = 0
            res_calc = 0
        else:
            i += 1
    res_calc = lst[0]
    return res_calc

def calculation2(lst):
    while ')' in lst:
        idx2 = lst.index(')')
        count = 0
        for i in range(idx2, 0, -1):
            if lst[i] != '(':
                count += 1
            else:
                idx1 = idx2 - count
                lst2 = lst[idx1+1: idx2]
                res1 = calculation(lst2)
                lst[idx2] = res1
                del lst[idx1: idx2]
                break
    result = calculation(lst)
    return result

st = '-1+(((2+1)+4)*3)+1'
st1 = pars(st)
st2 = calculation2(st1)
print(st2)
