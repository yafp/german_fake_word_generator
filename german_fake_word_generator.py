#!/usr/bin/env python

"""
__function__ = Script generates german fake-words out of several single parts
__author__ = "Florian Poeck"
__license__ = "GPL"
__version__ = "1.0.0"
__date__ = 20180305
__maintainer__ = "Florian Poeck"
__email__ = "fidel@yafp.de"
__status__ = "Development"
"""

import argparse
import random
import constants as c

# Define text source files
#
file_prefix = open("input/source_prefix.txt", 'r')
file_noun = open("input/source_noun.txt", 'r')
file_verb = open("input/source_verb.txt", 'r')
file_adj = open("input/source_adjective.txt", 'r')
file_suffix = open("input/source_suffix.txt", 'r')


def random_line(afile):
    """Pick a random line from a given file."""
    afile.seek(0)  # jump to start of document
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline
    return line


def get_random_adjective():
    """Return a random adjective."""
    return random_line(file_adj).strip()


def get_random_suffix():
    """Return a random suffix."""
    return random_line(file_suffix).strip()


def get_random_noun():
    """Return a random noun."""
    return random_line(file_noun).strip()


def get_random_verb():
    """Return a random verb."""
    return random_line(file_verb).strip()


def get_random_prefix():
    """Return a random prefix."""
    return random_line(file_prefix).strip()


def generate_random_word(xlist):
    """Generate a random word (based on a list of objects)"""
    current_word = ''
    random_word = ''
    random_word_verbose = ''

    for x in xlist:
        color = get_random_color_code()  # select rand color for this object
        if x == 'a':  # adjective
            current_word = get_random_adjective()
            random_word = random_word+current_word
            random_word_verbose = random_word_verbose+str(color)+current_word+c.FONT_RESET+" "
        if x == 'n':  # noun
            current_word = get_random_noun()
            random_word = random_word+current_word
            random_word_verbose = random_word_verbose+str(color)+current_word+c.FONT_RESET+" "
        if x == 'p':  # prefix
            current_word = get_random_prefix()
            random_word = random_word+current_word
            random_word_verbose = random_word_verbose+str(color)+current_word+c.FONT_RESET+" "
        if x == 's':  # suffix
            current_word = get_random_suffix()
            random_word = random_word+current_word
            random_word_verbose = random_word_verbose+str(color)+current_word+c.FONT_RESET+" "
        if x == 'v':  # verb
            current_word = get_random_verb()
            random_word = random_word+current_word
            random_word_verbose = random_word_verbose+str(color)+current_word+c.FONT_RESET+" "

    # show result
    #
    # print "  "+random_word.strip().capitalize() +"\t\t"+random_word_verbose.capitalize()+'\n'  # colorized and with spaces for readability
    result_plain = random_word.strip().capitalize()
    result_verbose = random_word_verbose.capitalize()
    print '{:35s}\t{:35s}'.format(result_plain, result_verbose)


def get_random_color_code():
    """Pick a random color code."""
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple
    LB = '\033[94m'  # lightblue
    Y = '\033[93m'  # yellow

    my_color = [W, R, G, O, B, P, LB, Y]

    current_color_pick = random.choice(my_color)
    return current_color_pick


def parse_arguments():
    """Parses input and prepares everything before generate_random_word()
    can do the magic"""

    # Definition of argparse parser - for handling arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--custom', metavar='[a,n,p,s,v]', help="for custom word generation by pattern", default=[])  # Optional parameter, if set needs value
    parser.add_argument('-a', '--amount', metavar='[1,2,3,4,..]', help="Amount of words to generate", type=int, default=1)  # Optional parameter, if set needs value
    args = parser.parse_args()

    # handling arguments
    if args.custom == []:  # No custom generation
        xlist = []  # list to be filled by randomness

        full_options = ['a', 'n', 'p', 's', 'v']  # list with all options
        start_options = ['n', 'p', 'p', 'p', 'p', 'p', 'v']  # used for first char
        middle_options = ['a', 'n', 'v']  # used for middle
        end_options = ['a', 'n', 's', 's', 's', 's', 's', 'v']  # used for last char

        # Int from 2 to 4, endpoints included
        # Defines how many objects will be used
        length = random.randint(2, 4)

        # generate random list
        for x in range(0, length):
            # V1: trying to add some sense
            #
            if x == 0:  # first char
                random_type = random.choice(start_options)
            elif x == length-1:  # last char
                random_type = random.choice(end_options)
            else:
                random_type = random.choice(middle_options)

            # v2: really random
            #
            # random_type = random.choice(full_options)

            xlist.append(random_type)

        # start generation
        for x in range(0, args.amount):
            generate_random_word(xlist)

    else:  # custom generation
        # start generation
        for x in range(0, args.amount):
            generate_random_word(args.custom)


# Start script
parse_arguments()
