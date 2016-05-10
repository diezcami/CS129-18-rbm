from bam import *
from process import *

if __name__ == '__main__':
    images = load_images_from_folder (INPUT_DIR)
    
    for image in images:
        bp = get_bipolar_vector (image)
        # feed bp to BAM here

    