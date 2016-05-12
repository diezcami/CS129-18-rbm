# CS 129.18 Final Project: Bidirectional Associative Memory

## Instructions ##
Call `python driver.py` and follow the on-screen instructions.

## Directory Structure ##
```
├── input/
│   ├── training_set/ : 5 images to be trained
│   ├── dreaming_set/ : 
├── bam.py : Bidirectional Associative Memory
├── driver.py: Driver Class
├── training.py: Compilation of modules used to train images
├── sample_bam_implementation: Sample usage of bam.py
```

## Implementation ##
When running the program, the user can opt to perform either supervised or unsupervised daydreaming by inputting `1` or `2`, respectively.

* **Supervised Daydreaming**: The program first trains the BAM instance by performing unsupervised daydreaming on images in the `training_set` directory using their resulting bipolar vectors as inputs and last labels as outputs. After creating the final weight matrix, images in the `dreaming_set` directory are fed to the BAM instance to retrieve a resulting X-prime, which is then displayed.

* **Unsupervised Daydreaming**: The program uses the BAM to samples bipolar vectors from images in the `training_set` directory and getting their resulting X-primes. These resulting X-primes are then converted into binary images and displayed.