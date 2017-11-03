# Created by: James Lee
# Created on: October 2017
# Course: ICS3U
# this is a unicode program that prints lower case and upper case letters.

for letter in range(65,91):
    for number in range(97,123):
        unicode = unichr(letter)
        upper_unicode = unichr(number)
        print str(unicode) + '->' + str(upper_unicode)
