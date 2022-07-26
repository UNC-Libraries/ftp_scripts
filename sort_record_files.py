# importing necessary package to access operating system
import os

# sets folder and creates a list of all files
# Below, type the local path to files, e.g. './78s/' or    ‘./Desktop/78s/records_to_upload/’
folder =  <FILE PATH>  
content = os.listdir(folder)
# The following line can be removed if no unwanted files are within the directory you’re working in. Otherwise, you want to specify the file types (e.g. ‘.JPG’, ‘.PDF’, etc.) 
content = [x for x in content if '.JPG' in x] 


# keeps only the titles of the records without the sides (no 78-21608_01 & 78-21608_2, just 78-21608)
# the index range may change if working with another record that has a different number of name values
# i.e., if the record is 89-38294, there's 8 values so the range is 0:8, 29-3842349 would be 0:10
titles = set([x[0:8] for x in content])

# creates a folder/director for each title
for x in titles:
    os.mkdir(folder+x+'/')

# moves files into proper folder
for file in content:
    os.rename(folder+file, folder+str(file[0:8])+'/'+file)
