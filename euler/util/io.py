import os


def datafiles(file_name):
    # answers.py and individual solutions file have different paths
    # so the path to data folder is different
    # bit of a hack - the simplest solution did for now
    in_right_directory = any(filename for filename in os.listdir(".")
                             if os.path.isdir(filename) and filename == 'data')

    return in_right_directory and f'data/{file_name}' or f'../data/{file_name}'
