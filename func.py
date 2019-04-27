def test(t=0,*args, print_number=False, **kwargs):
    print("t = ",t)
    print("args↓👇")
    for i,j in zip(args,range(10)):
        print(j,":",i,"\t");
    if print_number:
        print("kwargs = ",kwargs)


test(1, 2, 3, 4, 5,print_number=True, a=6, b=7)