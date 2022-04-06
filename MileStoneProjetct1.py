checkWIN = True
checkX = True
checkO = True
won = ''
my_list1 = ['-','-','-']
my_list2 = ['-','-','-']
my_list3 = ['-','-','-']
def picture (row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
while checkWIN:

    while checkO:
     picture(my_list1,my_list2,my_list3)
     answer = input("where do you want to put O?")
     if answer == "top right" :
         if my_list1[2]== '-':
             my_list1[2] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "top middle" :
         if my_list1[1]== '-':
             my_list1[1] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "top left" :
         if my_list1[0]== '-':
             my_list1[0] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "middle " :
         if my_list2[1]== '-':
             my_list2[1] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "middle left" :
         if my_list2[0]== '-':
             my_list2[0] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "middle right" :
         if my_list2[2]== '-':
             my_list2[2] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "buttom right" :
         if my_list3[2]== '-':
             my_list3[2] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "bottum middle" :
         if my_list3[1]== '-':
             my_list3[1] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "buttom left" :
         if my_list3[0]== '-':
             my_list3[0] = 'O'
             checkO = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
    checkO = True
    if my_list1[0] == my_list1[1] == my_list1[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list1[0] == my_list1[1] == my_list1[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list2[0] == my_list2[1] == my_list2[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list2[0] == my_list2[1] == my_list2[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list3[0] == my_list3[1] == my_list3[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[0] == my_list3[1] == my_list3[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list1[0] == my_list2[1]== my_list3[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list1[0] == my_list2[1]== my_list3[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list3[0] == my_list2[1]== my_list1[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[0] == my_list2[1]== my_list1[2] == 'X':
       won = 'X'
       checkWIN = False
    if my_list3[0] == my_list2[0]== my_list1[0] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[0] == my_list2[0]== my_list1[0] == 'X':
        won = 'X'
        checkWIN = False
    if my_list3[1] == my_list2[1]== my_list1[1] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[1] == my_list2[1] == my_list3[1] == 'X':
        won = "X"
        checkWIN = False
    if my_list3[2] == my_list2[2]== my_list1[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[2] == my_list2[2] == my_list3[2] == 'X':
        won = "X"
        checkWIN = False
    while checkX:
     picture(my_list1,my_list2,my_list3)
     answer = input("where do you want to put X?")
     if answer == "top right" :
         if my_list1[2]== '-':
             my_list1[2] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "top middle" :
         if my_list1[1]== '-':
             my_list1[1] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "top left" :
         if my_list1[0]== '-':
             my_list1[0] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "middle " :
         if my_list2[1]== '-':
             my_list2[1] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "middle left" :
         if my_list2[0]== '-':
             my_list2[0] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "middle right" :
         if my_list2[2]== '-':
             my_list2[2] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "buttom right" :
         if my_list3[2]== '-':
             my_list3[2] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "bottum middle" :
         if my_list3[1]== '-':
             my_list3[1] = 'X'
             checkX = False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
     if answer == "buttom left" :
         if my_list3[0]== '-':
             my_list3[0] = 'X'
             checkX= False
         else:
             answer = input(" this location is already taekn, enter diftenrt loction:")
    checkX = True
    if my_list1[0] == my_list1[1] == my_list1[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list1[0] == my_list1[1] == my_list1[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list2[0] == my_list2[1] == my_list2[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list2[0] == my_list2[1] == my_list2[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list3[0] == my_list3[1] == my_list3[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[0] == my_list3[1] == my_list3[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list1[0] == my_list2[1]== my_list3[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list1[0] == my_list2[1]== my_list3[2] == 'X':
        won = 'X'
        checkWIN = False
    if my_list3[0] == my_list2[1]== my_list1[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[0] == my_list2[1]== my_list1[2] == 'X':
       won = 'X'
       checkWIN = False
    if my_list3[0] == my_list2[0]== my_list1[0] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[0] == my_list2[0]== my_list1[0] == 'X':
        won = 'X'
        checkWIN = False
    if my_list3[1] == my_list2[1]== my_list1[1] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[1] == my_list2[1] == my_list3[1] == 'X':
        won = "X"
        checkWIN = False
    if my_list3[2] == my_list2[2]== my_list1[2] == 'O':
        won = 'O'
        checkWIN = False
    if my_list3[2] == my_list2[2] == my_list3[2] == 'X':
        won = "X"
        checkWIN = False



print(f"Congrats! player {0} won ",won)


