# import csv and path modules

import csv
from pathlib import Path

#This class initializes the csv Dictionary reader
# Attributes:
# filePath - stores file path in the format of the operating system Python is running on
# csvfile - reperesents the file object
# mycsvreader - csc dictinary reader, every row in this is the dictionary
class csvRead:

#     initializes class attributes
    def __init__(self, fileName):
        self.filePath = Path(fileName)
        self.csvfile = open(self.filePath, 'r')        
        self.mycsvreader = csv.DictReader(self.csvfile)
        
#The purpose of this class is to provides functionality for financial analysis
# Attributes:
# period_inmonths - stores the period in months for which revenue is calculates
# netpnl - stores net profit and loss
# growth_l - is a list of tuples that stores monthwise growth 
# Function(s)
# calculate_revenue_fromcsv - this function calculates the net profit & loss and growth based on the data in a csv file
# parameter : fileName - name of the csvfile

class revenue:
#   this function intializes all attributes, and is invoked automatically when an object is intialized
    def __init__(self):
        self.period_inmonths = 0        
        self.netpnl = 0                
        self.growth_l = []
        

    def calculate_revenue_fromcsv(self,fileName):
        csvRead_o = csvRead(fileName)
        pre_pnl = 0
        pre_date =''
        growth = 0
        

        for row in csvRead_o.mycsvreader:                        
            pnl = int(row['Profit/Losses'])
            date = row['Date']
            self.period_inmonths += 1
            self.netpnl += pnl

            if(self.period_inmonths == 1):
                pre_pnl = pnl
                pre_date = date
            else:                
                growth = pnl - pre_pnl                
                self.growth_l.append((date,growth))
                          
            pre_pnl = pnl
            pre_date = date

        csvRead_o.csvfile.close()
        
# This function is called from main, the purpose of this function is to calculate revenue and print financial analysis report    
def financial_analysis():
#  initialize revenue class object
   revenue_o = revenue ()
    
#  function call to calculate revenue
   revenue_o.calculate_revenue_fromcsv('Resources/budget_data.csv')

#  print report   
   print('Financial Analysis') 
   print('-'*50) 
   print(f'Total Months : {revenue_o.period_inmonths}')
   print(f'Total : ${revenue_o.netpnl}')
   total_change = 0.00

# following lines of code calculate average growth and print    
   for x in revenue_o.growth_l : 
    total_change += x[1]
   print(f'Average Change : $ {round(total_change / (revenue_o.period_inmonths-1),2)}')

#  sorted growth_l based on the growth value which is second item of the tuple
   sortedgrowth_l =sorted(revenue_o.growth_l, key=lambda x : x[1])
   print(f'Greatest Increase in Profits: {sortedgrowth_l[-1][0]} ${sortedgrowth_l[-1][1]}')
   print(f'Greatest Decrease in losses: {sortedgrowth_l[0][0]} ${sortedgrowth_l[0][1]}')
   print('-'*50)  

#  main function calls financial_analysis
def main():
    financial_analysis()
   
        
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()




