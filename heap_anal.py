import re
# open the file that has the page
fpage = open('./4k_block.txt', 'r')
pagetables = dict();
count = 0
for line in fpage:
         # split the line into words
         wordList = re.sub("[^\w]", " ",  line).split()
         refw = wordList[0]
         if count == 0 :
                page_name = refw
                print page_name

         ptr1 = wordList[2]+wordList[1]
         ptr2 = wordList[4]+wordList[3]

         # compare the refw and ptr1 and ptr2 to determine if they look like pointers

         subaddr = refw[0:5]  # get the lower order address (it should occur in the lower address range
         ptr1addr = ptr1[4:9] # get the lower order address to compare for the first pointer
         ptr2addr = ptr2[4:9] # get the lower order address to compare for the second pointer         

         if ptr1addr in subaddr :
                # store it in the page related data structure
                pagetables[page_name] = ptr1
                     
         if ptr2addr in subaddr :
                pagetables[page_name] = ptr2

 	 print pagetables[page_name]
         
         # increment the count after every line is processed
         count = count + 1
            





