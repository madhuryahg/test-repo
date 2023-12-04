from translate import Translator

translator = Translator(to_lang="de")
try:
    with open('.\\app\\test.txt', mode='r') as my_file:
text = my_file.read()
translation = translator.translate(text)
print(translation)


except FileNotFoundError as err:
print('File not found')
raise err

except IOError as err:
print('IO error')
raise err
