d = {
    ' ': '...'
}
input_text = input()
print(input_text.translate(str.maketrans(d)))