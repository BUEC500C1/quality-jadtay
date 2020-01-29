def arabictoroman(arabicnum):
    m = 0 #1000
    cm = 0 #900
    d = 0 #500
    cd = 0 #400
    c = 0 #100
    xc = 0 #90
    l = 0 #50
    xl = 0 #40
    x = 0 #10
    ix = 0 #9
    v = 0 #5
    iv = 0 #4
    i = 0 #1
    while arabicnum >= 1000:
        arabicnum -= 1000
        m += 1
    while arabicnum >= 900:
        arabicnum -= 900
        cm += 1
    while arabicnum >= 500:
        arabicnum -= 500
        d += 1
    while arabicnum >= 400:
        arabicnum -= 400
        cd += 1
    while arabicnum >= 100:
        arabicnum -= 100
        c += 1
    while arabicnum >= 90:
        arabicnum -= 90
        xc += 1
    while arabicnum >= 50:
        arabicnum -= 50
        l += 1
    while arabicnum >= 40:
        arabicnum -= 40
        xl += 1
    while arabicnum >= 10:
        arabicnum -= 10
        x += 1
    while arabicnum >= 9:
        arabicnum -= 9
        ix += 1
    while arabicnum >= 5:
        arabicnum -= 5
        v += 1
    while arabicnum >= 4:
        arabicnum -= 4
        iv += 1
    while arabicnum >= 1:
        arabicnum -= 1
        i += 1
    
    romannum = []
    romannum.append('M' * m)
    romannum.append('CM' * cm)
    romannum.append('D' * d)
    romannum.append('CD' * cd)
    romannum.append('C' * c)
    romannum.append('XC' * xc)
    romannum.append('L' * l)
    romannum.append('XL' * xl)
    romannum.append('X' * x)
    romannum.append('IX' * ix)
    romannum.append('V' * v)
    romannum.append('IV' * iv)
    romannum.append('I' * i)
    
    output = ""
    print(output.join(romannum))

def main():
    try:
        arabicnum = 0
        arabicnum = int(input("Please enter a number from 1-3999. \n"))
        if arabicnum < 1 or arabicnum > 4000:
            print("Please enter a valid number.")
        else:
            arabictoroman(arabicnum)
    except ValueError:
        print("Please enter a valid number.")
        
if __name__ == "__main__":
    main()
    

    
