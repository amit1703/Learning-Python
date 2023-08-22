with open('text.txt' , 'r') as f:
#the file will automaticlly close after using 
    f_content = f.read()#saved in memory(recommended only for small files)
    print(f_content) 

    for line in f:#none memory issue 
        print(line, end='')
