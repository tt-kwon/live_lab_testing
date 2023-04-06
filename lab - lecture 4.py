#Convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]
flat_list = [num for sublist in start_list for num in sublist]
print(flat_list)
filtered_list = [i/2 for i in flat_list if i%2  == 0]
print(filtered_list)
            


      
#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

date_format = '%m/%d/%Y'
answer = {k.capitalize():datetime.datetime.strptime(v, date_format) for k, v in
start_dict.items()}
print()

