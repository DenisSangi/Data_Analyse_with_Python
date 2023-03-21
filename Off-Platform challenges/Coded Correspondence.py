from string import punctuation

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabet = alphabet_upper.lower()


def ceasar_decode(encrypted_value):
    decrypted_value = ""
    for letter in encrypted_value:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            decrypted_value += alphabet[(letter_index + 33) % len(alphabet)]
        else:
            decrypted_value += letter
    return decrypted_value


def ceasar_encode(value_to_encode):
    my_encrypted_value = ""

    for letter in value_to_encode:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            my_encrypted_value += alphabet[(letter_index - 10) % len(alphabet)]
        else:
            my_encrypted_value += letter
    return my_encrypted_value


print(ceasar_decode(
    "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."))


def decode_vigenere_message(message, keyword):
    index = 0
    keyword_phrase = []
    message_index = []
    phrase_index = []

    # generate keyword_phrase with keyword(friends) for the length of (message_v) putting into acount spaces and !
    for letter in message:
        if letter in alphabet:
            keyword_index = index % len(keyword)
            keyword_phrase.append(keyword[keyword_index])
            index += 1
        elif letter in punctuation:
            keyword_phrase.append(letter)
    # print(keyword_phrase)

    # get indexes of message_v and keyword_phrase
    for i, j in zip(message, keyword_phrase):
        if i in alphabet and j in alphabet:
            msg_idx = alphabet.index(i)
            phr_idx = alphabet.index(j)
            message_index.append(msg_idx)
            phrase_index.append(phr_idx)
        elif i in punctuation:
            message_index.append(i)
            phrase_index.append(i)
    # print(message_index)
    # print(phrase_index)

    # decode message by returning the alphabet at index
    zip_object = zip(message_index, phrase_index)
    diff = []
    for elem1, elem2 in zip_object:
        if type(elem1) is int:
            lst = (elem1 - elem2) % 26
            diff.append(alphabet[lst])
        elif elem1 in punctuation:
            diff.append(elem1)
    return "".join(diff)
    return (message_index, phrase_index)
    return "".join(keyword_phrase)


print(decode_vigenere_message("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!", "friends"))
