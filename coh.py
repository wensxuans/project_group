import csv #import required libraries



def coh_function(): # define function
    deficitList = [] # declare empty list

    file =  open('csv_reports\cash_on_hand_60-90.csv', 'r') # open file with read mode
    reader = csv.reader(file)
    next(reader) # skip first row

    reversedList = list(reader) # store rows of csv into list
    reversedList.reverse() # reverse order of list

    file.close # close file when used finish

    for i in range(0, len(reversedList)-1): # for loop using range
        
        current = int(reversedList[i][1]) # declare and assign variable with current day cash of reversed list 
        prev = int(reversedList[i+1][1]) # declare and assign variable with day previous day cash of the reversed list 
        
        if(current < prev): # check if current day cash is less than previous day cash
            
            deficitList.append(reversedList[i][0]) # if true append current day and cash difference respectively
            deficitList.append(prev - current) 
            
                
        
    deficitList.reverse() # reverse back the list to normal
        
    newTxtFile = open("summary_report.txt", "a") #create new textfile if not exist with append mode

    for i in range(0, len(deficitList)-1, 2): # for loop using range with step 2
        

        #write file
        newTxtFile.write(f"""\n[CASH DEFICIT] DAY: {deficitList[i+1]}, AMOUNT: USD{deficitList[i]}""") # write to file

    newTxtFile.close()#close file when used finish  
    
    
    