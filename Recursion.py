# -----------------------------------------
# ---------- Function Recursion -----------
# -----------------------------------------
# -------------------------------------------------------------------
# --To Understand Recursion, YOU Need To First Understand Recursion--
# -------------------------------------------------------------------

def cleanWord(word) :
    if len(word) == 1:
        return word
    elif word[0] == word[1]:
        return cleanWord(word[1:])
    return word[0] + cleanWord(word[1:])

print(cleanWord("aaaccchhhrrraaafff"))