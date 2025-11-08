from BinaryTree import BTNode

table = [('A', ".-"), ('B', "-..."), ('C', "-.-."), ('D', "-.."),
         ('E', '.'), ('F', "..-."), ('G', "--."), ('H', "...."),
         ('I, "..'), ('J', ".---"), ('K', "-.-"), ('L', ".-.."),
         ('M', "--"), ('N', "-."), ('O', "---"), ('P', ".--."),
         ('Q', "--.-"), ('R', ".-."), ('S', "..."), ('T', '-'),
         ('U', "..-"), ('V', "...-"), ('W', ".--"), ('X', "-..-"),
         ('Y', "-.--"), ('Z', "--..")]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

def decode_simple(morse):
    for tp in table:
        if morse == tp[1]:
            return tp[0]
        
def make_morse_tree():
    root = BTNode(None, None, None)

    for tp in table:
        code = tp[1]
        node = root

        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = BTNode(None, None, None)