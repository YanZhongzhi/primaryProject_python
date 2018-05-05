import random
import re
def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world','nowcodeer')
    strb = ' \n\r helloworld  \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w cq'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, strc.endswith('w')
    print 6, stra + strb + strc
    print 7, len(strc)
    print 8, '-'.join(['a', 'b', 'c'])
    print 9, strc.split(' ')

    print 10, strc.find('hello')


def demo_operation():
    print 1,1 + 2, 5/2, 5*2, 5-2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5 | 3, 5 & 3, 5 ^ 3
    x = 2
    y = 3.3
    print x, y, type(x), type(y)

def demo_buildinfunction():
    print max(2,1), min(5,3)
    print len('xxx'), len([1, 2, 3])
    print 4, range(1,10,3)
    print 5, dir(list)
    x = 2;
    print 6, eval('x + 3')
    print chr(65), ord('a')
    print 8, divmod(11,3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    score = 65


    for i in range(0,10,2):
        if i == 0:
            #print 3,i
            pass #do special
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4, len(lista)
    print 5, 'a' in listb
    print 12, 'listb', listb
    print 11, 'lista:' ,lista
    listc = lista + listb
    print 6, listc
    lista = lista + listb
    print lista
    print lista


    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb;
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 14



    tuplea = (1,2,3)
    listaa = [1,2,3]
    listaa.append(4)
    print 15, listaa



def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value:', key, value

    dictb = {'+' : add, '-' : sub}
    print dictb
    print 4, dictb['+'](1,2)
    print 5, dictb.get('-')(15, 3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)
    print dicta
    print 6, dicta
    del dicta[1]
    print dicta

def demo_set():
    setc = set([1, 2, 3])
    seta = set((1, 2, 3))
    setb = set((2, 3, 4))
    print 1, seta
    seta.add(4)
    print 2, seta
    print 3, seta & setb, seta.intersection(setb)
    print 4, seta | setb, set.union(setb)
    print 5, seta - setb
    seta.add('x')
    print seta
    print len(seta)
    print seta.isdisjoint(set((1, 2)))

    setc.add('w')
    print setc

class User:
    type = 'USER'
    def __init__(self,name, uid):
        self.name = name
        self.uid = uid
    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)

class Admin(User):
    type = 'ADMIN'
    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group
    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        raise ValueError('error')



def demo_exception():
    try:
        print 2/1
        #print 2/0
        #if type =='c':
        raise Exception('Raise Error','NowCoder')
    except Exception as e:
        print 'error: ', e
    finally:
        print 'clean up'



def demo_random():

    #random.seed(1)
    #x = prex * 100007
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0 ,100, 10))
    print 4, random.sample(range(0, 100), 4)
    a = [1, 2, 3, 4, 5]
    random.shuffle(a);
    print 5,a

def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')

    print p1.findall(str)
    print p2.findall(str)


    str = 'a@163.com;b@gamin.com;c@qq.com;e@163.com;z@qq.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print p3.findall(str)

    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)

    p4 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5, p4.findall(str)

    str = 'xx2016-06-11yy'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print p5.findall(str)

if __name__ == '__main__':
    demo_re()

    '''
    user1 = User('u1', 1)
    print user1
    print'hello world!'
    admin1 = Admin('a1', 101, 'g1')
    print admin1
    print create_user('USER')
    # comment
    #demo_string()
    #demo_operation()
    #demo_buildinfunction()
    #demo_controlflow()
    #demo_list()
    #demo_dict()
    #demo_set()
    demo_exception()
    '''
