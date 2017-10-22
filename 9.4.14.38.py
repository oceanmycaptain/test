num=10
print ("Guess what I think?")
b=int(input())

if b>num:
    print("too big.")

if b<num:
    print("too small.")


if b==num:
    print("sure? You win.")
