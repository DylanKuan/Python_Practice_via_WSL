if __name__ == '__main__':
    
    student = [["Harry", 37.21] ,["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]];
    #student = [["Test1", .52] ,["Test2", 53], ["Test3", 53]];
    '''
    student = [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([str(name), score]);
    print(student);
    '''
    scores = [];
    for i in range (0, len(student)) :
        scores.append(student[i][1]);
    print(scores);
    unique_scores = sorted(scores, reverse = False);
    print(unique_scores);
    #print(len(student));
    for i in range (0, len(student)) :
        if student[i][1] == unique_scores[1] :
            print(student[i][0]);
        