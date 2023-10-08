def is_all_same(list_):
    # https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
    return list_.count(list_[0]) == len(list_)
