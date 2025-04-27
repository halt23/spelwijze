input_file = input("Enter the name of the input file you want to use. Include '.txt' !! -> ")
output_file = input("Enter the name of the output file you want to use. Include '.txt' !! -> ")
allowed_letters = ""

print("Enter all the letters that are used in the current puzzle except for the required letter \n")
print("when you're done just press enter.")

while True:
    letter = input("Enter a letter. -> ")
    if not letter :
        break
    allowed_letters += letter

required_letter = input('Enter the required letter. -> ')
allowed_letters += required_letter

# Convert allowed_letters to a set (Use this later).
allowed_letters = set(allowed_letters.lower())

# Open the wordlist you want to use (I wil later use this for accurecy testing).
# Read every line and add it to a list to use later on.
with open(input_file, 'r') as file :
    raw_words = [line.strip().lower() for line in file if line.strip()]

filtered_words = []
for word in raw_words :
    # Preform a variety of validety checks.
    if len(word) < 4:
        continue # spelwijzer only allows words of 4 chars and longer.
    if not set(word).issubset(allowed_letters):
        continue # Check wether the letters of word n are allowed
    if not required_letter in word :
        continue # If word n doesn't contain the required puzzle letter then skip.
    if word in filtered_words :
        continue # A simple, file agnostic way to eliminate duplicates.

    filtered_words.append(word)

print(f"{len(filtered_words)} Valid words have been found.")
print(f"Writing result to {output_file}")

# Writing the found words to the given output file.
try:
    with open(output_file, 'x') as file :
        for word in filtered_words :
            file.write(f"{word}\n")
except FileExistsError:
    print(f"{output_file} already exists, not overwriting.")
    exit()
