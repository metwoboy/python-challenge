# use modules
import os
import csv

#navigate to the target file
csvfile = os.path.join('Resources','election_data.csv')
pathout = os.path.join('Resources','Election Analysis.txt')

#read/open the csv file
with open(csvfile) as file:
    csvreader = csv.reader(file, delimiter=',')

#set variables
    total_votes = 0
    candidate_dict = {} 
    candidates = []
    percent_votes = []
  
#skip the column header row
    next(csvreader)
#start looping through the rows
    for row in csvreader:

        total_votes +=1
        candidate = row[2]
        if candidate not in candidates:
            #add candidate's name to the dictionary as key
            candidates.append(candidate)
            candidate_dict[candidate]=1
            
        elif candidate in candidates:
            #add one vote to the candidate if name is match to key in the dictionary
            candidate_dict[candidate]+=1

    
    #generate the percentage of received votes for each candidate and insert into a list
    for candidate in candidate_dict:
        percent_votes.append(format(round(((candidate_dict[candidate])/total_votes)*100),'.3f'))

    
    
    
    #zip the dictionary and percentage list together.
    zipped = zip(candidate_dict.items(),percent_votes)
    
    #set a function to align the list and dictionary
    #def zip_list(zipped):
        #zipped = zip(candidate_dict.items(),percent_votes)
        #for (key,voteCount),percent in zipped:
            #print(f'{key}: {percent}% ({voteCount})')
    
    #sample = zip_list(zipped)
    #zipped_list = zip_list(zipped)
    #find the candidate with most votes and output the name of candidate
    winner_candidate = max(candidate_dict,key=candidate_dict.get)

    

    print('---------------------------------------------')
    print('Election Results')
    print('---------------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------------------------------')
    zipped = zip(candidate_dict.items(),percent_votes)
    for (key,voteCount),percent in zipped:
        print(f'{key}: {percent}% ({voteCount})')

    print('---------------------------------------------')
    print(f'Winner: {winner_candidate}')
    print('---------------------------------------------')
        
    



#write results to a text file.
with open(pathout,'w') as txt_file:
    txt_file.write('---------------------------------------------\n')
    txt_file.write('Election Results\n')
    txt_file.write('---------------------------------------------\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write('---------------------------------------------\n')
    zipped = zip(candidate_dict.items(),percent_votes)
    for (key,voteCount),percent in zipped:
        txt_file.write(f'{key}: {percent}% ({voteCount})\n')

    txt_file.write('---------------------------------------------\n')
    txt_file.write(f'Winner: {winner_candidate}\n')
    txt_file.write('---------------------------------------------\n')
