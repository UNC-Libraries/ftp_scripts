# importing necessary package to access operating system
import os

# sets folder and creates a list of all files
# Below, you can change the path, e.g. './78s/' or‘./Desktop/78s/records_to_upload/’
folder = './files_to_sort/'
content = os.listdir(folder)

# You can un-comment the following line if there are unwanted files in the unsorted folder that may cause an error
# content = [x for x in content if '.JPG' in x or '.PDF' in x or '.PNG' in x or '.GIF' in x] 


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
