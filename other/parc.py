def unique_names(names1, names2):
    
    final = []
    for name in names1:
        if inside(name , final) :
            final.append(name)
    for name in names2:
        if inside(name , final) :
            final.append(name)
  
    return final

 
  
  
def inside (name , list):
    
    for i in list:
       if name == i:
          return False
    return True
  

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia