def string(n, i=0, out=''):
    if i >= len(n):
        return out

    if type(n[i]) == str:
        out = out + n[i][::-1]

    return string(n, i+1, out)


def list(n, i=0, out=None):
    if out is None:
        out = []

    if i >= len(n):
        return out

    if type(n[i]) == complex:
        out.append(n[i])

    return list(n, i+1, out)


def set(n, i=0, out=None):
    if out is None:
        out = set()

    if i >= len(n):
        return out

    if type(n[i]) == complex:
        out.add(n[i])

    return set(n, i+1, out)


def tuple(n, i=0, out=None):
    if i >= len(n):
        return out

    if type(n[i]) == complex:
        out = n[i]

    return tuple(n, i+1, out)


def main(a, i=0, out=None):
    if out is None:
        out = []

    if i >= len(a):
        return out

    if type(a[i]) == str:
        out.append(string(a[i]))

    elif type(a[i]) == list:
        temp = list(a[i])
        if temp:
            out.append(temp)

    elif type(a[i]) == set:
        temp = set(a[i])
        if temp:
            out.append(temp)

    elif type(a[i]) == tuple:
        temp = tuple(a[i])
        if temp is not None:
            out.append(temp)

    return main(a, i+1, out)


print(main([
    'hai',
    [3+4j, True, 78, 9+2j],
    'sample',
    (3, 7+9j),
    {19+20j, 34, 89},
    {'a': 10},
    'data',
    [2+4j, 3.8, 7.9]
]))