if __name__ == '__main__':
    N = int(input())
    arr = [];
    for i in range (0, N) :
        item = input();
        print(item);
        item = item.split(' ');
        print(item);
        if item[0] == 'insert' :
            arr.insert(int(item[1]), int(item[1]));
        elif item[0] == 'print' :
            print(arr);
        elif item[0] == 'remove' :
            arr.remove(int(item[1]));
        elif item[0] == 'append' :
            arr.append(int(item[1]));
        elif item[0] == 'sort' :
            arr.sort();
        elif item[0] == 'pop' :
            arr.pop();
        elif item[0] == 'reverse' :
            arr.reverse();
        else :
            print('wrong command');