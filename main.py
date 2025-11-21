from stats import (
    get_num_words,
	count_characters,
	sort_char_counts
)
import sys


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		path = sys.argv[1]
		output(path)

def output(path):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	book = get_book_text(path)
	num_words = get_num_words(book)
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	char_counts = count_characters(book)
	char_list = sort_char_counts(char_counts)
	
	for i in char_list:
		if i['char'].isalpha():
			print(f"{i['char']}: {i['num']}")
	print("============= END ===============")

main()
