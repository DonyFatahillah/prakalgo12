def banner():
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")
banner()
list=[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    list.append(int(input(f'masukan angka ke {i}:')))
print(sorted(list))
