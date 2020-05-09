#Simple interest formula is given by:
#Simple Interest = (P x T x R)/100
#Where,
#P is the principle amount
#T is the time and
#R is the rate

def FindSI(p,t,r):
    SI=(p*r*t)/100
    return SI
def main():
    principleamt=int(input("Enter the principle amount:"))
    time=int(input("Enter the time:"))
    rate=int(input("Enter the rate:"))

    SI=FindSI(principleamt,time,rate)

    print("Simple Interest:",SI)

if __name__=="__main__":
    main()