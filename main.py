"""
THIS IS CONVERTER
"""
# convert c value to f value
def converterCtoF():
    C = float(input("Ievadi C:"))
    F = (C*9/5)+32
    print (F)

def converterFtoC():
    F = float(input("Ievadi F:"))
    C = (F-32)*5/9
    print (C)

def convertArea():
    square_m = int(input("Ievadi kvadrātmetrus: "))
    ha = square_m/10000
    print(f"{square_m} kvadrātmetri ir {ha} hektāri.")
convertArea()