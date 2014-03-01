import re
import chardet

def page_analyze(file_name):
	# open the file that has the page
	fpage = open(file_name, 'r')
	
	page_name=""
	count = 0
	for line in iter(fpage.readline, ''):
                 print line
	         # split the line into words
                 if(line == "\n"):
                     continue
	         wordList = re.sub("[^\w]", " ",  line).split()
	         refw = wordList[0]
	         
	         if count == 0 :
	                # initialize page_name to the first word
	                page_name = refw
	
	         # store the entire line as a function of page_name _ address         
	         data_for_line = page_name + "_" + wordList[0]
     	             
	         ptr1 = wordList[2]+wordList[1]
	         ptr2 = wordList[4]+wordList[3]
	
	         pagetables[data_for_line] = wordList[1] + "  " + wordList[2] + "  " + wordList[3] + "  " + wordList[4]          
	
	         # compare the refw and ptr1 and ptr2 to determine if they look like pointers
	
	         subaddr = refw[0:5]  # get the lower order address (it should occur in the lower address range
	         ptr1addr = ptr1[4:9] # get the lower order address to compare for the first pointer
	         ptr2addr = ptr2[4:9] # get the lower order address to compare for the second pointer         
	       
	         if ptr1addr in subaddr :
	                # store it in the page related to it's data structure
	                if page_name in pagetables.keys():
	                         pagetables[page_name].append(ptr1)
	                else:
	                         pagetables[page_name] = [ptr1]
	                                     
	         if ptr2addr in subaddr :
	                # store it in the page related to it's data structure
	                if page_name in pagetables.keys():
	                         pagetables[page_name].append(ptr2)
	                else:
	                         pagetables[page_name] = [ptr2]
	         
	         # increment the count after every line is processed
	         count = count + 1
	
	# print all the key value pairs. 
	
	for key, value in pagetables.iteritems() :
	    print key, value
	
	# for now it should just be one key
	#for key in pagetables.keys():
	#    print key
	
	nums = pagetables['7f1b1e49f000_7f1b1e49f010'].split()
	value = nums[1].decode("hex") + nums[0].decode("hex") + nums[3].decode("hex") + nums[2].decode("hex")
	encoding = chardet.detect(value)
	if encoding['encoding'] == 'ascii':
	    print 'string is in ascii'
	print value
        

pagetables = dict();
#buffer_read =""
#buffer_read += fptr.read()
cur_buf=""
#print buffer_read
#for line in buffer_read.readl():
count=0;
with  open('./4k_full_blocks','r') as fptr:
        for line in iter(fptr.readline, ''):
                if ("END OF PAGE" not in line):
                        cur_buf += line
                        #cur_buf += "\n"
                else :
                        file_name = str(count) + ".txt"
                        fptr = open(file_name,"w+")
                        fptr.write(cur_buf) 
                        cur_buf = ""
                        fptr.close()
                        page_analyze(file_name)                      
                        count = count + 1
     
                     
           
         
	
