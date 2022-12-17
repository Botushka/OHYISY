maat = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populaatio = [5615000, 5439000, 324000, 5080000, 9609000]
mies_kalastajat = [1822, 2575, 3400, 11291, 1731]
nais_kalastajat = [69, 77, 400, 320, 26]

def guess(voittaja_sukupuoli):
    if voittaja_sukupuoli == 'nainen':
        kalastajat = nais_kalastajat
    else:
        kalastajat = mies_kalastajat

    # kirjoita ratkaisusi alle

    guess = None
    biggest = 0.0
    return (guess, biggest)

def main():
    maat, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (maat, fraction))
    maat, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (maat, fraction))

main()
