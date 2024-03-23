## Maxmatch program: Usage guide
___

This program takes in two inputs:
* Your original, untokenized text
* Your dictionary of words

**Your original, untokenized text** must be given through `stdin`. This can be done most naturally by using the `cat` command on a text file containing **your original, untokenized text** and **piping** its output to `maxmatch`. This file must have each sentence on a **new line** with **no empty lines** in between.

**Your dictionary of words** must be given as a terminal argument to `maxmatch` as a readable file. These words must also be separated by **new lines**.

With these inputs, `maxmatch` will print a tokenized version of each sentence to `stdout`, separated by new lines, with each token matched to a word in the given dictionary. For any given character in a sentence, if no word is found through the end of the sentence, it will take the character currently checked, create a token for it alone, and move to the next character.