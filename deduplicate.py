import nmslib
import numpy as np
from imagededup.methods import CNN

# Locate files
image_path = '/mnt/c/Users/orcun/duplicateELs'

#Similarity treshold
#You need to play with the similarity threshold to achieve correct values. It varies from system to system.
sim_threshold = 0.999

# First create the image encodings for CNN
cnn = CNN()
encodings = cnn.encode_images(image_path)

# Construct large scale scan
data = np.array(list(encodings.values()))
index = nmslib.init(method='hnsw', space='cosinesimil')
index.addDataPointBatch(data)

M = 40  
efConstruction = 40 
num_threads = 8 
index_time_params = {'M': M, 'indexThreadQty': num_threads, 'efConstruction': efConstruction, 'post' : 0}

# Create the index for comparison
index.createIndex(index_time_params, print_progress=True)

# Start the comparison
K = data.shape[0] # number of neigbours 
efSearch = 100 # Size of the dynamic list used during search. 
query_time_params = {'efSearch': efSearch}
print('Setting query-time parameters', query_time_params)
index.setQueryTimeParams(query_time_params)
neighbours = index.knnQueryBatch(data, k=K)

def retrieve_neighbours_one_file(neighbours_onefile, onefile_matrix_row_index, sim_thresh, all_filenames):
    # gets duplicates for one file
    self_retrived_file_pos = np.where(neighbours_onefile[0] == onefile_matrix_row_index) # Avoid self retrieval
    neighbours_onefile_files = np.delete(neighbours_onefile[0], self_retrived_file_pos)
    neighbours_onefile_sims = np.delete(neighbours_onefile[1], self_retrived_file_pos)
    
    sim_neighbors = 1 - neighbours_onefile_sims  # convert distance to similarity
    thresh_sims = sim_neighbors[np.where(sim_neighbors >= sim_thresh)]
    thresh_neighbours = neighbours_onefile_files[np.where(sim_neighbors >= sim_thresh)]
    thresh_neighbours_filenames = [all_filenames[i] for i in thresh_neighbours]
    dups = list(zip(thresh_neighbours_filenames, thresh_sims))
    return dups

filenames = list(encodings.keys())
file_matrix_inds = range(data.shape[0])
min_sim_threshold = sim_threshold
res = list(map(retrieve_neighbours_one_file, neighbours, file_matrix_inds, [min_sim_threshold] * data.shape[0], [filenames] * data.shape[0]))

# Retrieve duplicates as a dictionary of duplicate lists
duplicates = dict(zip(filenames, res))

# Plot and write duplicates as jpeg images
final_el_images = {}
from imagededup.utils import plot_duplicates
for key, value in duplicates.items():
    if len(value) > 0:
        plot_duplicates(image_path, duplicates, key, outfile="found_"+key)
        final_el_images[key]=value

# Write serial numbers to a csv file
import csv
with open('duplicate_list.csv', 'w') as f:
    for key in final_el_images.keys():
        f.write("%s,%s\n"%(key,final_el_images[key]))
