import csv # import required libraries


def profitloss_function(): # define function
    deficitList = [] # declare empty list

    file =  open('csv_reports\profit_n_loss_60-90.csv', 'r') # open file with read mode
    reader = csv.reader(file)
    next(reader) # skip first row

    reversedList = list(reader) # store rows of csv into list
    reversedList.reverse() # reverse order of list

    file.close # close file when used finish

    for i in range(len(reversedList)-1): # for loop using range
        
        current = int(reversedList[i][3]) # declare and assign variable with current day profit of reversed list 
        prev = int(reversedList[i+1][3]) # declare and assign variable with previous day profit of reversed list 
        
        if(current < prev): # check if current day profit is less than previous day profit
            
            deficitList.append(reversedList[i][0]) # if true append current day and profit difference respectively
            deficitList.append(prev - current)
            
                
        
    deficitList.reverse() # reverse back the list to normal
        
    newTxtFile = open("summary_report.txt", "a") # create new textfile if not exist with append mode

    for i in range(0, len(deficitList)-1, 2): # for loop using range with step 2
        

        newTxtFile.write(f"""\n[PROFIT DEFICIT] DAY: {deficitList[i+1]}, AMOUNT: USD{deficitList[i]}""") # write to file

    newTxtFile.close()#close file when used finish  
    