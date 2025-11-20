def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def num_of_words(b):
	words = b.split()
	return len(words)
		

def main():
	book = get_book_text("books/frankenstein.txt")
	num_words = num_of_words(book)
	print(f"Found {num_words} total words")

main()
