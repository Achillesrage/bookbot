def get_num_words(b):
	words = b.split()
	return len(words)

def count_characters(text):
	char_counts = {}
	for char in text.lower():
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts
	return char_counts


def sort_char_counts(char_count_dict):
	char_list = [{'char': char, 'num': count} for char, count in char_count_dict.items()]
	def get_num(item):
		return item["num"]
	char_list.sort(key=get_num, reverse=True)
	return char_list
