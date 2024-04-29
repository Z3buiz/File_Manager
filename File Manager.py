import os
import glob
import shutil

# Directory paths
source_directory = 'C:/Users/z3bui/OneDrive/Desktop'
videos_location = 'C:/Users/z3bui/Downloads/Video Folder'
audio_location = 'C:/Users/z3bui/Downloads/Audio Folder'
documents_location = 'C:/Users/z3bui/Downloads/Document Folder'
pictures_location = 'C:/Users/z3bui/Downloads/Picture Folder'
setup_files_location = 'C:/Users/z3bui/Downloads/Applications'
compressed_files_location = 'C:/Users/z3bui/Downloads/Compressed Folders'
python_files_location = 'C:/Users/z3bui/Downloads/Python Files'

# File extensions
documents = ['.pdf', '.docx', '.doc', '.txt', '.xls']
videos = ['.mp4', '.MOV', '.WMV', '.WebM']
pictures = ['.jpeg', '.jpg', '.svg', '.png', '.PNG', '.gif']
audios = ['.mp3', '.WAV']
setup_files = ['.exe', '.msi']
python_files = ['.py']
compressed_files = ['.zip', '.rar', '.gz', '.tgz']

# Check if directories exist, create them if not
for folder in [videos_location, audio_location, documents_location, pictures_location,
               setup_files_location, compressed_files_location, python_files_location]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Move files to appropriate directories
for file_path in glob.glob(os.path.join(source_directory, '*')):
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_path)[1]
        if file_extension in documents:
            shutil.move(file_path, documents_location)
        elif file_extension in videos:
            shutil.move(file_path, videos_location)
        elif file_extension in pictures:
            shutil.move(file_path, pictures_location)
        elif file_extension in audios:
            shutil.move(file_path, audio_location)
        elif file_extension in setup_files:
            shutil.move(file_path, setup_files_location)
        elif file_extension in compressed_files:
            shutil.move(file_path, compressed_files_location)
        elif file_extension in python_files:
            shutil.move(file_path, python_files_location)