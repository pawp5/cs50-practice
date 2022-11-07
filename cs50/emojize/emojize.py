import emoji

text = input("Input: ").lower().strip()
emo = emoji.emojize(text, language='alias')

print("Output:", emo)