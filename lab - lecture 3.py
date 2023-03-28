#### Fix the following errors (in 1-6)!

#1
x = '10'
y = 20
#correction 
x = 10
print(x + y)


#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
#print(my_list[my_list_len])
print(my_list_len)

#3
my_string = 'hello world'
big_string = my_string.upper()
print(big_string)

#4
z = ['a', 'b', 'c']
z[:3] = 'd'
print(z[:3])
#5 Why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
x
#correction
print(x)
y = 20
print(x * y)

#6
color = 'My favorite color is {}, what is yours?' #% blue
#correction 
color = 'blue'
my_string_favcolor = f'My favorite color is {color} what is yours?'
print(my_string_favcolor)

#### Answer the following questions without changing the code given

#7 Make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools = {'harris', 'booth', 'crown', 'harris', 'harris'}
print(schools)

#8 Change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = list(animals)
print(animals)
animals[2] = 'cat'
animals = tuple(animals)
print(animals)

#9 Make this string take a name based on a variable (you can modify the code on this one)
name = 'Sarah'
welcome = 'Hello Sarah, and welcome to Data and Programming!'
welcome = f'Hello {name}, and welcome to Data and Programming'
print(welcome)

#10 Separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
my_sent_list = [my_sent[0], my_sent[2:6], my_sent[7:10], my_sent[10:17], my_sent[18:20], 
                my_sent[21:26], my_sent[27:31], my_sent[32:36], my_sent[37:41], 
                my_sent[42:45], my_sent[46:51], my_sent[52:55], my_sent[56:58], 
                my_sent[59:66], my_sent[67:70], my_sent[71:73], my_sent[74:76],
                my_sent[77:81], my_sent[82:85], my_sent[86:89], my_sent[89:95] ]
print(my_sent_list)
