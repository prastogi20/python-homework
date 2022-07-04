import csv
from pathlib import Path
     
# The purpose of this class is to generate a list of menu items by reading from a csv file
# Attribute :
# menu_list - is a list of dictionaries of menu items
# Function :
# get_menu_fromcsv - the purpose of this function is to read menu items from csv file and generate the list of menu items
# input parameter : string, which represents the file name
class menu:
    # init funtions initializes the attribute of class
    def __init__(self):        
        self.menu_list = []
        
    
    def get_menu_fromcsv(self,fileName):
        csvPath = Path(fileName)
        # the following lines of code reads from the csv file and create a list of menu items, each item in a list is a dictionary
        with open(csvPath, 'r') as csvFile:            
            reader = csv.DictReader(csvFile, delimiter =',')
            # reader = csv.reader(csvFile, delimiter =',')
            # reader.next()
            for menu_item in reader:
              self.menu_list.append(menu_item)
            
# The purpose of this class is to read and analyse sales data stored in a csv and generate a report, in a text file
# Attribute:
# report - is a dictionary of analysed sale data for each item in the Menu
# Functions:
# get_sales_fromcsv - the purpose of this function is to analyse sales data stored in a csv file and summarize it in a dictionary 
# generate_sales_report_intextfile - the purpose of this function is to write the report in txt file
class sales:
    def __init__(self):
        self.report = {}
    
    def get_sales_fromcsv(self,sales_fileName,menu_fileName):        
        csvPath = Path(sales_fileName) 
        menu_o = menu()
        menu_o.get_menu_fromcsv(menu_fileName)
        quantiy = 0
        price = 0.0
        cost = 0.0
        profit = 0.0       
        with open(csvPath, 'r') as csvFile:
            reader = csv.DictReader(csvFile, delimiter =',')
            # reader = csv.reader(csvFile, delimiter =',')            
            for sale in reader:                
                sale_item = sale['Menu_Item']
                quantity = int(sale['Quantity'])
                menu_item = list(filter(lambda item: item['item'] == sale_item, menu_o.menu_list))                
                price = float(menu_item[0]['price'])
                cost = float(menu_item[0]['cost'])
                profit = price - cost                
                if (sale_item in self.report.keys()):                                           
                    self.report[sale_item]["01-count"] += quantity
                    self.report[sale_item]["02-revenue"] += price * quantity
                    self.report[sale_item]["03-cogs"] += cost * quantity
                    self.report[sale_item]["04-profit"] += profit * quantity
                else:
    
                    self.report[sale_item] =   {"01-count": quantity,"02-revenue": price*quantity,"03-cogs": cost*quantity,"04-profit": profit*quantity}
    
    def generate_sales_report_intextfile(self):
        csvPath = Path('Result.txt') 
        with open(csvPath, 'w') as csvFile:
            for key , value in self.report.items():
                csvFile.write('%s:%s\n' % (key, value))



#  main function is the entry point of the script
def main():
    # create sales class object    
    sales_o = sales()

    # call sales class funtion to read sales data from csv and stored in in-memory dictionary
    sales_o.get_sales_fromcsv('Resources/sales_data.csv','Resources/menu_data.csv')

    # call sales class funtion to write the in-memory report into a text file
    sales_o.generate_sales_report_intextfile()
    print('Report successfully printed in PyRamen/Result.txt')


   

        
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

