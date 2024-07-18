#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
    # TODO 0: Measures total program runtime by collecting start time

    
    # TODO 1: Define get_input_args function within the file get_input_args.py
    
    # Function that checks command line arguments using in_arg  
    
    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
    
    # Function that checks Pet Images in the results Dictionary using results    
    

    # TODO 3: Define classify_images function within the file classiy_images.py
    
    # Function that checks Results Dictionary using results    
    
    
    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    
    # Function that checks Results Dictionary for is-a-dog adjustment using results
    

    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py

    # Function that checks Results Statistics Dictionary using results_stats


    # TODO 6: Define print_results function within the file print_results.py
    
    
    # TODO 0: Measure total program runtime by collecting end time

    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
        
# Call to main function to run the program
def main():
    start_time = time()
    in_arg = get_input_args()

    print(f"Directory: {in_arg.dir}, Architecture: {in_arg.arch}, Dogfile: {in_arg.dogfile}")

    check_command_line_arguments(in_arg)
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Ajoutez ce print pour vérifier la structure de results
    print("\nResults Dictionary:\n")
    for key in results:
        print(f"{key} : {results[key]}")

    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)
    print_results(results, results_stats,  in_arg.arch, True, True)

    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )

if __name__ == "__main__":
    main()
