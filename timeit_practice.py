import timeit;

def with_for(n) :
    lst = [];
    for i in range(n) :
        lst.append(i);
    return lst;

def without_for(n) :
    return (i for i in range(n));

def main() :
    n = 1000;
    #print("with for : {}".format(with_for(n)));
    #print("without for : {}".format(without_for(n)));
    print(f"with for    : {timeit.timeit(lambda : with_for(n), number = 10000)}");
    print(f"without for : {timeit.timeit(lambda : without_for(n), number = 10000)}");


main();