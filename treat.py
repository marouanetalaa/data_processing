import os

# Define the directory containing the WAV files
dir_path = './wave/'

# Loop through all the files in the directory
for file_name in os.listdir(dir_path):
    
    # Check if the file is a WAV file
    if file_name.endswith('.wav'):
        
        # Get the first three characters of the file name
        prefix = file_name[:3]
        
        # Create a new directory for the batch if it doesn't exist
        if not os.path.exists(os.path.join(dir_path, prefix)):
            os.makedirs(os.path.join(dir_path, prefix))
        
        # Move the file to the appropriate batch directory
        os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, prefix, file_name))
