file_path = None

def set_file_path(path):
    global file_path
    file_path = path

def get_file_path():
     
    return file_path

def get_directory_path():
        # Find the last occurrence of the slash
    last_slash_index = file_path.rfind('/')
    # Extract the substring from the start to the last slash
    directory_path = file_path[:last_slash_index]
    return directory_path