while True:
    print("hit 0 to quit. ")
    sen = list(input("Please enter your sentence: "))
    new_list = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if sen == list('0'):
        break
    len_sen = len(sen)
    for letter in range(len_sen):
        if sen[len_sen - (len_sen - letter)].isalpha():
            new_list += sen[len_sen - (len_sen - letter)]
            # print(x)
    new_list = ''.join(new_list)                                        # converting list to string

    len_alpha = len(alphabet)

    final_res = 0
    for alpha in range(len_alpha):
        if alphabet[alpha] in new_list.casefold():
            final_res += 1
        else:
            continue

    if final_res == len_alpha:
        print("The given sentence IS A PANGRAM.\n"+'*'*100)
    else:
        print('The given sentence IS NOT A PANGRAM.\n'+'*'*100)


