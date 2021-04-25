# list_ = [[1, None, 2, 3, 4 + 5j, 6], [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]
# for elem in list_:
#     for sym in elem:
#         types = [(type(sym)).__name__ for sym in elem if (type(sym)).__name__]
#         dict_ = {i: types.count(i) for i in types}
#         #type_max = ""
#         #for key, val in dict_.items():
#             #if val == max(dict_.values()):
#                 #type_max = key
#         type_max = [key for key, val in dict_.items() if val == max(dict_.values())]
#     print(type_max)


dict_ = {
        'а': '574', 'б': '242', 'в': '334', 'г': '394', 'д': '324',
        'е': '584', 'ж': '264', 'з': '344', 'и': '284', 'й': '404',
        'к': '414', 'л': '484', 'м': '374', 'н': '564', 'о': '594',
        'п': '504', 'р': '364', 'с': '384', 'т': '494', 'у': '444',
        'ф': '572', 'х': '242', 'ц': '332', 'ч': '392', 'ш': '322', 'щ': '582',
        'ь': '262', 'ы': '342', 'э': '282', 'ю': '402', 'я': '412',
        'А': '482', 'Б': '372', 'В': '562', 'Г': '592', 'Д': '502',
        'Е': '362', 'Ж': '382', 'З': '492', 'И': '442', 'Й': '578', 'К': '248',
        'Л': '338', 'М': '398', 'Н': '328', 'О': '588', 'П': '268', 'Р': '348',
        'С': '288', 'Т': '408', 'У': '418', 'Ф': '488', 'Х': '378', 'Ц': '568',
        'Ч': '598', 'Ш': '508', 'Щ': '368', 'Ь': '388', 'Ы': '498', 'Э': '448',
        'Ю': '575', 'Я': '245', 'a': '335', 'b': '395', 'c': '325', 'd': '585',
        'e': '265', 'f': '345', 'g': '285', 'h': '405', 'i': '415', 'j': '485',
        'k': '375', 'l': '565', 'm': '595', 'n': '505', 'o': '365', 'p': '385',
        'q': '495', 'r': '445', 's': '577', 't': '247', 'u': '337', 'v': '397',
        'w': '327', 'x': '587', 'y': '267', 'z': '347', 'A': '287', 'B': '407',
        'C': '417', 'D': '487', 'E': '377', 'F': '567', 'G': '597', 'H': '507',
        'I': '367', 'J': '387', 'K': '497', 'L': '447', 'M': '573',
        'N': '243', 'O': '333', 'P': '393', 'Q': '323', 'R': '583',
        'S': '263', 'T': '343', 'U': '283', 'V': '403', 'W': '413', 'X': '483',
        'Y': '373', 'Z': '563', ' ': '593', '.': '503', ',': '363', '!': '383',
        '?': '493', '0': '571', '1': '241', '2': '331', '3': '391', '4': '321',
        '5': '581', '6': '261', '7': '341', '8': '281', '9': '401', '+': '411',
        '<': '371', '>': '561', '@': '591', '#': '501', '$': '361', '%': '381',
        '^': '491', '&': '441', '*': '579', '(': '249', ')': '339', '_': '399',
        '=': '329', '~': '589', '`': '269', '"': '349', ':': '289', ';': '409',
        '[': '419', ']': '489', '{': '379', '}': '569'
        }
choice = input("\n Do you want to encrypt or d_encrypt the message?\n"
               "1 to encrypt, 2 to decrypt or 0 to exit program. ")
if choice == '1':
    word1 = input("\nEnter message for encryption:\n")
    # list_encrypt = []
    # for i in list(word1):
    #     list_encrypt.append(dict_[i])
    # print(list_encrypt)
    list_encrypt = [ dict_[i] for i in list(word1) ]
    print(list_encrypt)
    str_encrypt = ""
    for k in list_encrypt:
        str_encrypt += k
    print(str_encrypt)
if choice == '2':
    word2 = input('\nEnter message to d_encrypt: ')
    # list_d_encrypt = []
    # for key, val in dict_.items():
    #     if word2 == val:
    #         list_d_encrypt.append(key)
    list_d_encrypt = [ key for key, val in dict_.items() if word2 == val ]
    print (list_d_encrypt)
    str_d_encrypt = ""
    for k in list_d_encrypt:
        str_d_encrypt += k
    print(str_d_encrypt)
elif choice != '0':
    print('You have entered an invalid input, please try again. \n\n')


