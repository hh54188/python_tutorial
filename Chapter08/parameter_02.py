def updateList(l):
    l.append('liguangyi')


l = ['mengxiao']
print(l)
updateList(l[:])
print(l)


o = {
    'name': 'liguangyi'
}


def updateDict(o):
    o['name'] = 'mengxiao'


print(o)
updateDict(o)
print(o)
