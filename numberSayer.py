def numberSayer(n):
    assert type(n) == int and 0 <= n <= 9999999, "You should enter a number that between 0 and 9999999!"
    dicNum = {0: "Zero", 1: "One",2: "Tow", 3: "Three", 4: "Four",5:"Five",6:"Six",7:"seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",20: "Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70: "Seventy",80: "Eighty",90:"Ninety"}
    if  0 <= n <= 12:
        return dicNum[n]
    if 13 <= n <= 19:
        strN= str(n)
        return dicNum[int(strN[1])]+"teen"
    if 20 <= n <= 99:
        strN= str(n)
        if strN[1] == "0":
            return dicNum[n]
        return dicNum[int(strN[0]+"0")]+" "+dicNum[int(strN[1])]
    if 100 <= n <= 999:
        strN = str(n)
        if strN[1:] == "00":
            return dicNum[int(strN[0])]+" "+"hundered"
        return dicNum[int(strN[0])]+" "+"hundereds and "+ numberSayer(int(strN[1:]))
    if 1000 <= n <= 999999:
        strN = str(n)
        if strN[-3:] == "000":
            return numberSayer(int(strN[:-3]))+" "+"thousand"
        return numberSayer(int(strN[:-3]))+" "+"thousands "+ numberSayer(int(strN[-3:]))
    if 1000000 <= n <= 9999999:
        strN = str(n)
        if strN[1:] == "000000":
            return dicNum[int(strN[0])]+" "+"million"
        return dicNum[int(strN[0])]+" "+"millions "+ numberSayer(int(strN[1:]))
        