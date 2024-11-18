# import os
# import sys
# import shutil
# from pathlib import Path

# def collect_files_by_type(root_dir, file_type):
#     """
#     Collect files of a specific type from all subdirectories and copy to output folder.
    
#     Args:
#     root_dir (str): Root directory to start searching
#     file_type (str): File extension to collect (e.g., '.txt', '.pdf')
#     """
#     # Ensure file_type starts with a dot
#     if not file_type.startswith('.'):
#         file_type = '.' + file_type

#     # Create output directory
#     output_dir = os.path.join(root_dir, 'collected_files')
#     os.makedirs(output_dir, exist_ok=True)

#     # Walk through all directories and subdirectories
#     for dirpath, dirnames, filenames in os.walk(root_dir):
#         for filename in filenames:
#             if filename.endswith(file_type):
#                 # Full path to the source file
#                 source_file = os.path.join(dirpath, filename)
                
#                 # Destination path (preserve original filename)
#                 dest_file = os.path.join(output_dir, filename)
                
#                 # Handle duplicate filenames
#                 counter = 1
#                 while os.path.exists(dest_file):
#                     name, ext = os.path.splitext(filename)
#                     dest_file = os.path.join(output_dir, f"{name}_{counter}{ext}")
#                     counter += 1
                
#                 # Copy the file
#                 shutil.copy2(source_file, dest_file)
#                 print(f"Copied: {source_file} -> {dest_file}")

# def main():
#     # Check if correct number of arguments provided
#     if len(sys.argv) != 3:
#         print("Usage: python script.py <directory_path> <file_type>")
#         sys.exit(1)

#     # Get arguments
#     directory = sys.argv[1]
#     file_type = sys.argv[2]

#     # Validate directory
#     if not os.path.isdir(directory):
#         print(f"Error: {directory} is not a valid directory")
#         sys.exit(1)

#     # Run file collection
#     collect_files_by_type(directory, file_type)
#     print(f"Files collected in {os.path.join(directory, 'collected_files')}")

# if __name__ == "__main__":
#     main()


import os
import sys
import shutil
from pathlib import Path

def collect_files_by_type(src_paths, file_type):
    """
    Collect files of a specific type from multiple source directories.
    
    Args:
    src_paths (list): List of source directories to search
    file_type (str): File extension to collect (e.g., 'txt', 'pdf')
    """
    # Ensure file_type starts with a dot
    if not file_type.startswith('.'):
        file_type = '.' + file_type

    # Validate source paths
    valid_paths = [path for path in src_paths if os.path.isdir(path)]
    
    if not valid_paths:
        print("Error: No valid directories provided")
        sys.exit(1)

    # Create output directory in the first valid path
    output_dir = os.path.join(valid_paths[0], 'collected_files')
    os.makedirs(output_dir, exist_ok=True)

    # Track copied files to handle duplicates
    copied_files = set()

    # Walk through all provided directories
    for src_path in valid_paths:
        for dirpath, dirnames, filenames in os.walk(src_path):
            for filename in filenames:
                if filename.endswith(file_type):
                    # Full path to the source file
                    source_file = os.path.join(dirpath, filename)
                    
                    # Unique filename handling
                    dest_filename = filename
                    counter = 1
                    while dest_filename in copied_files:
                        name, ext = os.path.splitext(filename)
                        dest_filename = f"{name}_{counter}{ext}"
                        counter += 1
                    
                    # Destination path
                    dest_file = r"E:\Trabago\OnTheRecordTech\dataset"
                    
                    # Copy the file
                    shutil.copy2(source_file, dest_file)
                    print(f"Copied: {source_file} -> {dest_file}")
                    copied_files.add(dest_filename)

def main():
    # Check if correct number of arguments provided
    if len(sys.argv) < 4:
        print("Usage: python script.py <file_type> <source_path1> [source_path2] ...")
        sys.exit(1)

    # Get file type (first argument)
    file_type = sys.argv[1]

    # Get source paths (remaining arguments)
    src_paths = sys.argv[2:]

    # Run file collection
    collect_files_by_type(src_paths, file_type)
    print(f"Files collected in {os.path.join(src_paths[0], 'collected_files')}")

if __name__ == "__main__":
    main()