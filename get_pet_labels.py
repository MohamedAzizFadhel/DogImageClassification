#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: star_boy  
# DATE CREATED:  10/22/23                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic=
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#

from os import listdir
def get_pet_labels(image_dir): 
    filename_list = listdir(image_dir)
    results_dic=dict()
    for i in filename_list:
        if i.startswith('.'):
            continue
        wordlist_pet_image = i.lower().split("_")
        pet_name = ""
        for word in wordlist_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
        if i not in results_dic:
            results_dic[i] = [pet_name]

    return results_dic
