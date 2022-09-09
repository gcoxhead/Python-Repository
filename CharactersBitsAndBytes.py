# Write your code here :-)

# This code asks the user to input the number of characters in a piece of text.
# It then returns the number of bits and bytes needed to store the characters

charactersText = input("Please enter the number of characters in your text")

characters = int(charactersText)

bits = characters * 8
bitsText = str(bits)

bytes = characters
bytesText = str(bytes)

print(
    "It takes "
    + bitsText
    + " bits and "
    + bytesText
    + " bytes to store the data for "
    + charactersText
    + " characters of text."
    )
