import random
secret = random.randint(1,10)
print('-------------�Ұ���c������--------------')
temp = input("��һ��С������������������ĸ�����:\n")
guess = int(temp)
if guess == secret:
    print("�Բۣ�����С�������������𣿣�")
    print("�ߣ�������Ҳû�н�����")
else:
    if guess > secret:
        print("�磬���˴��ˣ���")
    else:
        print('�磬С��С��~~')
    i=0
    while i < 2:
        temp = input("��ѽ���´��ˣ������������:\n")
        guess = int(temp)
        i=i+1
        if guess == secret:
            print("�Բۣ�����С�������������𣿣�")
            print("�ߣ�������Ҳû�н�����")
        elif guess > secret:
            print("�磬���˴��ˣ���")
        else:
            print('�磬С��С��~~')
print("��Ϸ������������~")
