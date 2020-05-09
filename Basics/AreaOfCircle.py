PI=3.14
def FindArea(rad):

    area=PI*rad*rad
    return area


def main():
    r=float(input("Enter the radius:"))
    area=FindArea(r)
    print("Area of circle is:",area)
if __name__=="__main__":
    main()