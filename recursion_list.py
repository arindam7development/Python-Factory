list = ["list1_item#1",10,"list1_item#2",20,"list1_item#3",30,"list1_item#4",40,"list1_item#5",50,
       
          ["list2_item#1","list2_item#2",["list3_item#1","list3_item#2"]]]
          
# Use of Methods in Python      
def print_lol(the_list):
   for each_item in the_list:
        if isinstance(each_item, list):
             print_lol(each_item)
        else:
             print(each_item)



print_lol(list)
