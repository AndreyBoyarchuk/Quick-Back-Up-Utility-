import pandas as pd
from ctypes import windll ##Input memory sweeper
import re
connected = True
city="BOISE"


tags=[" ", ".", " W "," E "," N "," S "," W "," E. "," N. "," S. "," WEST "," EAST "," NORTH "," SOUTH ","W ","E ","N ","S ","WEST ","EAST ","NORTH ","SOUTH ",]
streetSuffixs=[" AVE"," CIR"," CT"," DR", " LN"," PL"," RD"," ST"," WAY", " COURT" " STREET", " LANE"," DRIVE", " ROAD", ]

dfstreets = pd.read_csv('dataframe.csv')
df1=dfstreets.drop_duplicates(subset=["StName"])
df2=(df1["StName"])



scanValues=[]
def inpt_s():
    if windll.user32.OpenClipboard(None): #Open clipboard and check for any copied
        windll.user32.EmptyClipboard()  # and clears it
        windll.user32.CloseClipboard()
    x=input("UseScanner")
    scanValues.append(x.upper())



def clean_up(barcodeScanner):

    item1=barcodeScanner.split(city,1)
    item2=item1[0]
    streetchoices=[]
    for street in df2:
        if street in item2:
            streetchoices.append(street)
            print(streetchoices)
            secondString=streetchoices[0]
            splitSring = item2.split(secondString, 1)
            firstString = (splitSring[0])
        else:
            leftStreets=[]
            leftStreets.append(street)



    integers = re.findall(r"\d+", firstString)
    hNumber = (integers[-1])
    return hNumber, secondString,


def run_query(houseNumber,cleanAddressline):
    df = pd.read_csv('dataframe.csv')
    query = df[(df["AddNum"] == houseNumber) & (df["StName"] == cleanAddressline)]
    locationAndAddress = query[['AddNum', 'StName', 'Name']]
    print(locationAndAddress)
    zoneName=locationAndAddress['Name']
    print(f"this is the Zone:" +zoneName)

while connected:
    inpt_s()
    count=0
    lastItem=scanValues[len(scanValues)-1]
    if city in lastItem:
        address_str=clean_up(lastItem)
        houseNumber=float(address_str[0])
        addressLine=address_str[1]
        run_query(houseNumber,addressLine)

    else:
        print("Address is not recognized Or Wrong Barcode")
        print("Here is the snipet from Scanner Input: <<<"+lastItem+">>>")