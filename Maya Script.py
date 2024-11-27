import random
import maya.cmds as cmds

# Variables
group_name = "INSERT GROUP NAME"
percent = 50.0  # Set your percentage of objects to select
threshold = percent / 100.0  # Since this example uses 50%, a threshold of 0.5 is used

selected_list = []  # Record the objects to select

# Loop through children of the group
for child in cmds.listRelatives(group_name, children=True, fullPath=True) or []:
    objects = cmds.listRelatives(child, type="transform", fullPath=True) or []
    num_objects = len(objects)  # Number of objects
    num_to_select = int((percent / 100.0) * num_objects)  # Actual number of objects to select
    select_amount = 0

    # Continue until the desired number of objects are selected
    while select_amount <= num_to_select:
        for obj in objects:  # Loop through objects
            # Use a random function to determine if an object is selected
            if random.random() <= threshold:
                if obj not in selected_list:  # Avoid duplicates
                    selected_list.append(obj)  # Add to the selection list
                    select_amount += 1

            # Break if we've selected enough objects
            if select_amount >= num_to_select:
                break

# Select the final list of objects
cmds.select(selected_list, replace=True)
