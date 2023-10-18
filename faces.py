# vim:fileencoding=utf-8
# vim:fileencoding=U+1F642
# vim:fileencoding=U+1F641

def main():
	text = str(input(""))
	print(convert(text))

def convert(text):
    text = text.replace(":)", "\N{Slightly Smiling Face}").replace(":(", "\N{Slightly Frowning Face}")
    return text

main()
