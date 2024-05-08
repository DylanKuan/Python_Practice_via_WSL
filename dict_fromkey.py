if __name__ == '__main__':
    n = 5;
    arr = [2, 3, 6, 6, 5];
    
    sorted_arr = sorted(arr, reverse = True);
    print(sorted_arr);
    unique_arr = dict.fromkeys(sorted_arr);
    print(unique_arr);
    unique_arr = list(unique_arr);
    print(unique_arr);