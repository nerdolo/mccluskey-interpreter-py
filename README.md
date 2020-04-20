# mccluskey-interpreter-py
This program takes a minimalised boolean function written in !a!b + !abc convention and calculates its logic value in python</br>
in code descriptions are in polish for now

# convention
'a', 'b', 'c' etc variables are bits of binary representation of decimal number</br>
'!' is negation</br>
'a!bcd' etc are words and we treat them as conjunction of given variables</br>
'+' means disjunction</br>

# what does it do?
program does a lexical analysis, parsing and compiling of a given sentence and is able to calculate its logical value for given decimal number</br>
it also gives you information which words of disjuction have 'true' value if the whole statement is true for a given number
# what for?
it can be used for automatic testing whether a minimalised boolean function is valid if you have a list of valid results to compare (like I do in code)

# why?
ask [@wvffle](https://github.com/wvffle) who made me do this as an exercise.
