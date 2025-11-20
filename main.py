from stats import get_num_words
from stats import count_characters
from stats import sort_char_counts

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	path = "books/frankenstein.txt"
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
