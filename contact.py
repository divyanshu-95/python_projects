
print('contacts')
print('1 : exit')
print('2 : add')
print('3 : search')
print('4 : delete')
print('5 : view all')
d={}
while True:
    n=int(input('ntr choice : '))
    if n==1:
          break
    elif n==2:
        name=input('ntr name')
        no=int(input('ntr no'))
        d[name]=no
    elif n==3:
        sr=input('ntr name want to search')
        for i in d:
            if sr==i:
                print('exist')
                print(sr,d[name])
            else:
                print("doesn't exist")
        #sr=input('ntr name want to search')
        #print(sr,d[name])
    elif n==4:
        dele=input('ntr name want to delete')
        for j in d:
            if j==dele:
                #del d['dele']
                d.pop('dele',None)
                print('deleted')
            else:
                print('not exist')
    elif(n==5):
        print(d)
    else:
        print('invalid')
