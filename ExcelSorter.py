# vishwanath79
# This basic script will let you specify an excel file to read and sort and save it to another file


from pandas import Series,DataFrame
import pandas as pd
import openpyxl
pd.set_option('display.max_columns', None)

# Source Info
file = raw_input('Enter location/name of file ')
sheet = raw_input('Enter sheet name you wish to sort ')
file2 = pd.read_excel(file,sheet,index_col=0, na_values=['NA'])

# Sort Info
sorter = []
style =[]
sortq = int(raw_input("Please enter # of  column you wish to sort by: "))
for x in range(sortq):
    sorter.append(raw_input(('Name of columns you wish to sort by ' + `x+1` + ' ')))
    style.append(raw_input(('Type True for Ascending, False for Descending sort ' + `x+1` + ' ')))
sort1= file2.sort(sorter,ascending=(style))


#Destination Info
destwb = raw_input('Enter destination and filename you wish to store as ')
sort1.to_excel(destwb, sheet_name='Sheet1')