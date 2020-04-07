import random
play_game='yes'
start=1
end=100
direction='N'
samllest=start
largest=end

while play_game=='yes':
    samllest=start
    largest=end
    print("Guess a no Between 0 to 100")
    try_number=random.randint(start,end)
    print(try_number)
    countr=0
    direction="N"
    while direction!='C':
        direction=input('it is too large(L),too small(S),correct(C)')
        if direction=='S':
            if try_number>samllest:
                samllest=try_number+1
            try_number=random.randint(samllest,largest)
            print(try_number)
        if direction=="L":
            if try_number<largest:
                largest=try_number-1
            try_number=random.randint(samllest,largest)
            print(try_number)
        countr=countr+1
    print("yoooo you Got it in  "+str(countr)+"  Times")
    
play_game=input("Continue Game? yes OR no")
