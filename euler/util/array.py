def zero_padded(list_):
	""" Zero-padding makes it easier for us to reason (using 1-based index rather than 0-based) """
	return [0] + list_


def is_all_same(list_):
	# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
	return list_.count(list_[0]) == len(list_)
