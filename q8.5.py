for i in range(1,11):
    ques=int(input("num {}".format(i)))
    if ques>0:
        print("positive numbers")
        print(ques)
    elif ques<0:
        print("negative numbers")
        print(ques)
    elif ques%2==0:
        print("even nubmers")
        print(ques)
    elif ques%2!=0:
        print("odd numbers")
        print(ques)
        
    

