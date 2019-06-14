"""Brute-force hack a Union rout cipher

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption begins at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top and read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string
Requires custom-made "perms" module to generate keys
Prints off key used and translated plaintext

"""
import sys
import perms

#==================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple quotes)
ciphertext = """REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST\
    SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER
"""

# number of columns in the transposition matrix
COLS = 4

# number of rows in the transposition matrix
ROWS = 5

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#==================================================================


def main():
    """Turn ciphertext into list, call validation & decryption functions."""
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    decrypt(cipherlist)


def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
    print(f'\nLength of cipher = {len_cipher}')
    print(f'Acceptable column/row values include: {factors}')
    print()
    if ROWS * COLS != len_cipher:
        print('\nERROR - Input columns & rows not factors of length '
              'of cipher. Terminating program.', file=sys.stderr)
        sys.exit()


def decrypt(cipherlist):
    """Turn columns into items in list of lists & decrypt ciphertext."""
    col_combos = perms.perms(COLS)
    for key in col_combos:
        translation_matrix = [None] * COLS
        plaintext = ''
        start = 0
        stop = ROWS
        for k in key:
            if k < 0:  # reading bottom-to-top of column
                col_items = cipherlist[start:stop]
            elif k > 0:  # reading top-to-bottom of column
                col_items = list(reversed(cipherlist[start:stop]))
            translation_matrix[abs(k) - 1] = col_items
            start += ROWS
            stop += ROWS
        # loop through nested lists popping off last item to a new list
        for i in range(ROWS):
            for matrix_col in translation_matrix:
                word = str(matrix_col.pop())
                plaintext += word + ' '
        print(f'\nusing key = {key}')
        print(f'translated = {plaintext}')
    print(f'\nnumber of keys = {len(col_combos)}')


if __name__ == '__main__':
    main()