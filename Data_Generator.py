import random
for i in range(1):
    path = 'output'+str(i)+'.txt'
    f = open(path, 'w')
    def data_maker():
        return str(round(random.uniform(-10, 10),2))
    print(data_maker())
    for i in range(1024):
        f.write(data_maker()+ " "+data_maker()+" "+data_maker()+'\n')

    f.close()