from greetings import greetings
from translate import Translator

translator = Translator(to_lang='es')
for g in greetings:
    print(translator.translate(g).title())