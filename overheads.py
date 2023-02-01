import csv #import libraries




def overhead_function(): # define function

    file =  open('csv_reports\overheads-day-90.csv', 'r') # open file with read mode
    reader = csv.reader(file)
    
    next(reader) # skip first row
    row1 = next(reader) # get first row with actual values

    expense = float(row1[1]) # assign variable with first row's value, to be compared later
    expense_name = row1[0] # assign variable with first row's value
    
    for row in reader: # for loop using the rows in file
        
        if(expense < float(row[1])): # check if first row's value is smaller than the next
            
            expense_name = row[0] # if smaller, values will be swapped else continue
            expense = float(row[1])
        
    file.close # close file when used finish

    newTxtFile = open("summary_report.txt", "w") #create new txt file if not exist with write mode

    newTxtFile.write(f"""[HIGEST OVERHEADS] {expense_name.upper()}: {expense}%""") # write into file

    newTxtFile.close()#close file when used finish
    