from stats import get_num_words

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	book = get_book_text("books/frankenstein.txt")
	num_words = get_num_words(book)
	print(f"Found {num_words} total words")

main()
