import sys

start=1
end=1000
count=1

while count < 11:
    guess=(start+end)//2
    print(guess,flush=True)
    sys.stdout.flush()

    c_or_w=input()
    if c_or_w=='correct':
        sys.exit()
    elif c_or_w=='lower':
        end=guess-1
    else:
        start=guess+1
    count+=1


