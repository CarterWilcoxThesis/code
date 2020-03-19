from sklearn.manifold import TSNE
import numpy as np
import glob, json, os

# create datastores
vector_files = []
image_vectors = []
chart_data = []
maximum_imgs = 27000

# build a list of image vectors

# GET IMAGE VECTORS BY RUNNING
#python classify_images.py 'FOLDER/*'

# GET THUMBNAILS TO DISPLAY BY RUNNING
#mogrify -resize 64x64! *.jpg
# // cd Desktop > Thesis Exploration //
#ls Brooch_subset_copy/* > images_to_montage.txt

# Regarding the montage, maximum pixel size is 2048x2048, so we have 32 rows and 32 columns
# Each atlas should therefore be made from a file with 1,024 photographs
# That's 25 full atlas photos and a leftover of 224 photographs
#montage `cat Atlas_of_legend_1.txt` -geometry +0+0 -background none -tile 32x LEGEND_1.jpg
#NOTE: Montage is in order of file names in .txt file. Begins in upper left corner. Goes left to right. Then starts at beginning of next row.



# CHANGE DIRECTORY PATH HERE
vector_files = glob.glob('image_vectors/*.npz')[:maximum_imgs]
for c, i in enumerate(vector_files):
  image_vectors.append(np.loadtxt(i))
  print(' * loaded', c, 'of', len(vector_files), 'image vectors')

# build the tsne model on the image vectors
print('building tsne model')
model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
fit_model = model.fit_transform( np.array(image_vectors) )

# store the coordinates of each image in the chart data
tracker = 0
for c, i in enumerate(fit_model):
  tracker += 1
  print(tracker)
  image_name = os.path.basename(vector_files[c]).replace('.npz', '')
  chart_data.append({
    'image': os.path.join('images', image_name),
    'x': i[0],
    'y': i[1]
  })
print("Beginning output...")
plswork = 0
with open('full_brooch_tsne_projections.json', 'w') as out:
  new_list = []
  for item in chart_data:
    plswork += 1
    new_item = {'image': str(item['image']), 'x': float(item['x']), 'y': float(item['y'])}
    new_list.append(new_item)
    print(plswork)
  json.dump(new_list, out)
  #json.dump(chart_data, out)
