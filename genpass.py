import re
import random
import hashlib

pass_assign = {"a": "0e*u)G1", "b": "1vk)H(2", "c": "2kve!x3", "d": "3G#T9m4", "e": "4FGY(X5", "f": "5E7Htv6",
               "g": "6j8*QZ7", "h": "7GPFzf8", "i": "87qP%w9", "j": "9qL6(610", "k": "10g=wr@11", "l": "11zNzWP12",
               "m": "12RNfwQ13", "n": "13w6U@c14", "o": "14/x%(S15", "p": "15v4dnN16", "q": "16Wx=zZ17",
               "r": "179rT8M18", "s": "18)YU^q19", "t": "20D$mW821", "u": "21AZzX222", "v": "22+8Rk@23",
               "w": "23-LutP24", "x": "24MA!KG25", "y": "25RggFN26", "z": "26yC$GD27", '1': 'ca!', '2': 'lb@',
               '3': 'uc#', '4': 'ad$', '5': 'oe%', '6': 'uf^', '7': 'oj&', '8': 'lh*', '9': 'oi(', '0': 'o%j'}
password = input("Enter the password: ").lower()
changed_pass = re.sub(r'[^a-zA-Z0-9\s]+', "", password)


class GenPass:
    def __init__(self):
        super().__init__()
        self.password = password
        self.choice = ""
        self.encoded_pass = ""
        self.changed_pass = changed_pass
        self.pass_assign = pass_assign

    # Basic password from assigned codes to each alphabet
    def basic_genpass(self):
        self.encoded_pass = ""
        for alphabet in self.changed_pass:
            self.encoded_pass += self.pass_assign[alphabet]
        print(self.encoded_pass)

    # Randomly Arranged Basic password from assigned codes to each alphabet
    def random_basic_genpass(self):
        self.encoded_pass = ""
        for alphabet in self.changed_pass:
            self.encoded_pass += self.pass_assign[alphabet]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        get_pass = ""
        for i in range(length):
            get_pass += random.choice(var)
        print(get_pass)

    def random_required_len_basic_genpass(self):
        self.encoded_pass = ""
        for alphabet in self.changed_pass:
            self.encoded_pass += self.pass_assign[alphabet]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        print(f"The generated password general length from your given pass is {length}.")
        total_length = int(input("Enter Required password length: "))
        if total_length > length:
            required_length = total_length - length
            get_pass = ""
            for i in range(length + required_length):
                get_pass += random.choice(var)
            print(get_pass)
        else:
            required_length = length - total_length
            get_pass = ""
            for i in range(length - required_length):
                get_pass += random.choice(var)
            print(get_pass)
            print("Required length generated")
            print("Warning")
            print("The length you entered is less than the original length of the generated pass from your pass")

    def own_basic_genpass(self):
        print("Make sure that each code given to each letter contain capital(alphabets), small(alphabets), "
              "symbols and numbers")
        print("Now Assign your own code to the alphabets")
        self.pass_assign["a"] = input("Enter your own secret code of 'a': ")
        self.pass_assign["b"] = input("Enter your own secret code of 'b': ")
        self.pass_assign["c"] = input("Enter your own secret code of 'c': ")
        self.pass_assign["d"] = input("Enter your own secret code of 'd': ")
        self.pass_assign["e"] = input("Enter your own secret code of 'e': ")
        self.pass_assign["f"] = input("Enter your own secret code of 'f': ")
        self.pass_assign["g"] = input("Enter your own secret code of 'g': ")
        self.pass_assign["h"] = input("Enter your own secret code of 'h': ")
        self.pass_assign["i"] = input("Enter your own secret code of 'i': ")
        self.pass_assign["j"] = input("Enter your own secret code of 'j': ")
        self.pass_assign["k"] = input("Enter your own secret code of 'k': ")
        self.pass_assign["l"] = input("Enter your own secret code of 'l': ")
        self.pass_assign["m"] = input("Enter your own secret code of 'm': ")
        self.pass_assign["n"] = input("Enter your own secret code of 'n': ")
        self.pass_assign["o"] = input("Enter your own secret code of 'o': ")
        self.pass_assign["p"] = input("Enter your own secret code of 'p': ")
        self.pass_assign["q"] = input("Enter your own secret code of 'q': ")
        self.pass_assign["r"] = input("Enter your own secret code of 'r': ")
        self.pass_assign["s"] = input("Enter your own secret code of 's': ")
        self.pass_assign["t"] = input("Enter your own secret code of 't': ")
        self.pass_assign["u"] = input("Enter your own secret code of 'u': ")
        self.pass_assign["v"] = input("Enter your own secret code of 'v': ")
        self.pass_assign["w"] = input("Enter your own secret code of 'w': ")
        self.pass_assign["x"] = input("Enter your own secret code of 'x': ")
        self.pass_assign["y"] = input("Enter your own secret code of 'y': ")
        self.pass_assign["z"] = input("Enter your own secret code of 'z': ")
        self.encoded_pass = ""
        print(self.changed_pass)
        for alphabet in self.changed_pass:
            self.encoded_pass += self.pass_assign[alphabet]
        print(self.encoded_pass)

    def own_random_basic_genpass(self):
        print("Make sure that each code given to each letter contain capital(alphabets), small(alphabets), "
              "symbols and numbers")
        print("Now Assign your own code to the alphabets")
        self.pass_assign["a"] = input("Enter your own secret code of 'a': ")
        self.pass_assign["b"] = input("Enter your own secret code of 'b': ")
        self.pass_assign["c"] = input("Enter your own secret code of 'c': ")
        self.pass_assign["d"] = input("Enter your own secret code of 'd': ")
        self.pass_assign["e"] = input("Enter your own secret code of 'e': ")
        self.pass_assign["f"] = input("Enter your own secret code of 'f': ")
        self.pass_assign["g"] = input("Enter your own secret code of 'g': ")
        self.pass_assign["h"] = input("Enter your own secret code of 'h': ")
        self.pass_assign["i"] = input("Enter your own secret code of 'i': ")
        self.pass_assign["j"] = input("Enter your own secret code of 'j': ")
        self.pass_assign["k"] = input("Enter your own secret code of 'k': ")
        self.pass_assign["l"] = input("Enter your own secret code of 'l': ")
        self.pass_assign["m"] = input("Enter your own secret code of 'm': ")
        self.pass_assign["n"] = input("Enter your own secret code of 'n': ")
        self.pass_assign["o"] = input("Enter your own secret code of 'o': ")
        self.pass_assign["p"] = input("Enter your own secret code of 'p': ")
        self.pass_assign["q"] = input("Enter your own secret code of 'q': ")
        self.pass_assign["r"] = input("Enter your own secret code of 'r': ")
        self.pass_assign["s"] = input("Enter your own secret code of 's': ")
        self.pass_assign["t"] = input("Enter your own secret code of 't': ")
        self.pass_assign["u"] = input("Enter your own secret code of 'u': ")
        self.pass_assign["v"] = input("Enter your own secret code of 'v': ")
        self.pass_assign["w"] = input("Enter your own secret code of 'w': ")
        self.pass_assign["x"] = input("Enter your own secret code of 'x': ")
        self.pass_assign["y"] = input("Enter your own secret code of 'y': ")
        self.pass_assign["z"] = input("Enter your own secret code of 'z': ")
        self.encoded_pass = ""
        print(self.changed_pass)
        for alphabet in self.changed_pass:
            self.encoded_pass += self.pass_assign[alphabet]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        get_pass = ""
        for i in range(length):
            get_pass += random.choice(var)
        print(get_pass)

    def own_random_required_len_basic_genpass(self):
        print("Make sure that each code given to each letter contain capital(alphabets), small(alphabets), "
              "symbols and numbers")
        print("Now Assign your own code to the alphabets")
        self.pass_assign["a"] = input("Enter your own secret code of 'a': ")
        self.pass_assign["b"] = input("Enter your own secret code of 'b': ")
        self.pass_assign["c"] = input("Enter your own secret code of 'c': ")
        self.pass_assign["d"] = input("Enter your own secret code of 'd': ")
        self.pass_assign["e"] = input("Enter your own secret code of 'e': ")
        self.pass_assign["f"] = input("Enter your own secret code of 'f': ")
        self.pass_assign["g"] = input("Enter your own secret code of 'g': ")
        self.pass_assign["h"] = input("Enter your own secret code of 'h': ")
        self.pass_assign["i"] = input("Enter your own secret code of 'i': ")
        self.pass_assign["j"] = input("Enter your own secret code of 'j': ")
        self.pass_assign["k"] = input("Enter your own secret code of 'k': ")
        self.pass_assign["l"] = input("Enter your own secret code of 'l': ")
        self.pass_assign["m"] = input("Enter your own secret code of 'm': ")
        self.pass_assign["n"] = input("Enter your own secret code of 'n': ")
        self.pass_assign["o"] = input("Enter your own secret code of 'o': ")
        self.pass_assign["p"] = input("Enter your own secret code of 'p': ")
        self.pass_assign["q"] = input("Enter your own secret code of 'q': ")
        self.pass_assign["r"] = input("Enter your own secret code of 'r': ")
        self.pass_assign["s"] = input("Enter your own secret code of 's': ")
        self.pass_assign["t"] = input("Enter your own secret code of 't': ")
        self.pass_assign["u"] = input("Enter your own secret code of 'u': ")
        self.pass_assign["v"] = input("Enter your own secret code of 'v': ")
        self.pass_assign["w"] = input("Enter your own secret code of 'w': ")
        self.pass_assign["x"] = input("Enter your own secret code of 'x': ")
        self.pass_assign["y"] = input("Enter your own secret code of 'y': ")
        self.pass_assign["z"] = input("Enter your own secret code of 'z': ")
        self.encoded_pass = ""
        print(self.changed_pass)
        for alphabet in self.changed_pass:
            self.encoded_pass += self.pass_assign[alphabet]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        print(f"The generated password general length from your given pass is {length}.")
        total_length = int(input("Enter Required password length: "))
        if total_length > length:
            required_length = total_length - length
            get_pass = ""
            for i in range(length + required_length):
                get_pass += random.choice(var)
            print(get_pass)
        else:
            required_length = length - total_length
            get_pass = ""
            for i in range(length - required_length):
                get_pass += random.choice(var)
            print(get_pass)
            print("Required length generated")
            print("Warning")
            print("The length you entered is less than the original length of the generated pass from your pass")

    def required_len_advanced_genpass(self):
        get_pass = re.sub(r'[^a-zA-Z0-9\s]+', "", self.password)
        encode_to_hash = hashlib.sha3_512(get_pass.encode())
        get_hash_code = encode_to_hash.hexdigest()
        # extract_hash_num = re.sub(r'[^0-9\s]+', "", get_hash_code)
        # extract_hash_alphabets = re.sub(r'[^a-zA-Z\s]+', "", get_hash_code)
        self.encoded_pass = ""
        for alphabets in get_hash_code:
            self.encoded_pass += self.pass_assign[alphabets]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        print(f"The generated password general length from your given pass is {length}.")
        total_length = int(input("Enter Required password length: "))
        if total_length > length:
            required_length = total_length - length
            get_pass = ""
            get_num = 0
            for i in range(length + required_length):
                get_num += 1
                get_pass += var[get_num]
            print(get_pass)
        else:
            required_length = length - total_length
            get_pass = ""
            get_num = 0
            for i in range(length - required_length):
                get_num += 1
                get_pass += var[get_num]
            print(get_pass)
            print("Required length generated")
            print("Warning")
            print("The length you entered is less than the original length of the generated pass from your pass")

    def random_required_len_advanced_genpass(self):
        get_pass = re.sub(r'[^a-zA-Z0-9\s]+', "", self.password)
        encode_to_hash = hashlib.sha3_512(get_pass.encode())
        get_hash_code = encode_to_hash.hexdigest()
        # extract_hash_num = re.sub(r'[^0-9\s]+', "", get_hash_code)
        # extract_hash_alphabets = re.sub(r'[^a-zA-Z\s]+', "", get_hash_code)
        self.encoded_pass = ""
        for alphabets in get_hash_code:
            self.encoded_pass += self.pass_assign[alphabets]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        print(f"The generated password general length from your given pass is {length}.")
        total_length = int(input("Enter Required password length: "))
        if total_length > length:
            required_length = total_length - length
            get_pass = ""
            for i in range(length + required_length):
                get_pass += random.choice(var)
            print(get_pass)
        else:
            required_length = length - total_length
            get_pass = ""
            for i in range(length - required_length):
                get_pass += random.choice(var)
            print(get_pass)
            print("Required length generated")
            print("Warning")
            print("The length you entered is less than the original length of the generated pass from your pass")

    def own_required_len_advanced_genpass(self):
        print("Make sure that each code given to each letter contain capital(alphabets), small(alphabets), "
              "symbols and numbers")
        print("Now Assign your own code to the alphabets")
        self.pass_assign["a"] = input("Enter your own secret code of 'a': ")
        self.pass_assign["b"] = input("Enter your own secret code of 'b': ")
        self.pass_assign["c"] = input("Enter your own secret code of 'c': ")
        self.pass_assign["d"] = input("Enter your own secret code of 'd': ")
        self.pass_assign["e"] = input("Enter your own secret code of 'e': ")
        self.pass_assign["f"] = input("Enter your own secret code of 'f': ")
        self.pass_assign["g"] = input("Enter your own secret code of 'g': ")
        self.pass_assign["h"] = input("Enter your own secret code of 'h': ")
        self.pass_assign["i"] = input("Enter your own secret code of 'i': ")
        self.pass_assign["j"] = input("Enter your own secret code of 'j': ")
        self.pass_assign["k"] = input("Enter your own secret code of 'k': ")
        self.pass_assign["l"] = input("Enter your own secret code of 'l': ")
        self.pass_assign["m"] = input("Enter your own secret code of 'm': ")
        self.pass_assign["n"] = input("Enter your own secret code of 'n': ")
        self.pass_assign["o"] = input("Enter your own secret code of 'o': ")
        self.pass_assign["p"] = input("Enter your own secret code of 'p': ")
        self.pass_assign["q"] = input("Enter your own secret code of 'q': ")
        self.pass_assign["r"] = input("Enter your own secret code of 'r': ")
        self.pass_assign["s"] = input("Enter your own secret code of 's': ")
        self.pass_assign["t"] = input("Enter your own secret code of 't': ")
        self.pass_assign["u"] = input("Enter your own secret code of 'u': ")
        self.pass_assign["v"] = input("Enter your own secret code of 'v': ")
        self.pass_assign["w"] = input("Enter your own secret code of 'w': ")
        self.pass_assign["x"] = input("Enter your own secret code of 'x': ")
        self.pass_assign["y"] = input("Enter your own secret code of 'y': ")
        self.pass_assign["z"] = input("Enter your own secret code of 'z': ")
        get_pass = re.sub(r'[^a-zA-Z0-9\s]+', "", self.password)
        encode_to_hash = hashlib.sha3_512(get_pass.encode())
        get_hash_code = encode_to_hash.hexdigest()
        # extract_hash_num = re.sub(r'[^0-9\s]+', "", get_hash_code)
        # extract_hash_alphabets = re.sub(r'[^a-zA-Z\s]+', "", get_hash_code)
        self.encoded_pass = ""
        for alphabets in get_hash_code:
            self.encoded_pass += self.pass_assign[alphabets]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        print(f"The generated password general length from your given pass is {length}.")
        total_length = int(input("Enter Required password length: "))
        if total_length > length:
            required_length = total_length - length
            get_pass = ""
            get_num = 0
            for i in range(length + required_length):
                get_num += 1
                get_pass += var[get_num]
            print(get_pass)
        else:
            required_length = length - total_length
            get_pass = ""
            get_num = 0
            for i in range(length - required_length):
                get_num += 1
                get_pass += var[get_num]
            print(get_pass)
            print("Required length generated")
            print("Warning")
            print("The length you entered is less than the original length of the generated pass from your pass")

    def own_random_required_len_advanced_genpass(self):
        print("Make sure that each code given to each letter contain capital(alphabets), small(alphabets), "
              "symbols and numbers")
        print("Now Assign your own code to the alphabets")
        self.pass_assign["a"] = input("Enter your own secret code of 'a': ")
        self.pass_assign["b"] = input("Enter your own secret code of 'b': ")
        self.pass_assign["c"] = input("Enter your own secret code of 'c': ")
        self.pass_assign["d"] = input("Enter your own secret code of 'd': ")
        self.pass_assign["e"] = input("Enter your own secret code of 'e': ")
        self.pass_assign["f"] = input("Enter your own secret code of 'f': ")
        self.pass_assign["g"] = input("Enter your own secret code of 'g': ")
        self.pass_assign["h"] = input("Enter your own secret code of 'h': ")
        self.pass_assign["i"] = input("Enter your own secret code of 'i': ")
        self.pass_assign["j"] = input("Enter your own secret code of 'j': ")
        self.pass_assign["k"] = input("Enter your own secret code of 'k': ")
        self.pass_assign["l"] = input("Enter your own secret code of 'l': ")
        self.pass_assign["m"] = input("Enter your own secret code of 'm': ")
        self.pass_assign["n"] = input("Enter your own secret code of 'n': ")
        self.pass_assign["o"] = input("Enter your own secret code of 'o': ")
        self.pass_assign["p"] = input("Enter your own secret code of 'p': ")
        self.pass_assign["q"] = input("Enter your own secret code of 'q': ")
        self.pass_assign["r"] = input("Enter your own secret code of 'r': ")
        self.pass_assign["s"] = input("Enter your own secret code of 's': ")
        self.pass_assign["t"] = input("Enter your own secret code of 't': ")
        self.pass_assign["u"] = input("Enter your own secret code of 'u': ")
        self.pass_assign["v"] = input("Enter your own secret code of 'v': ")
        self.pass_assign["w"] = input("Enter your own secret code of 'w': ")
        self.pass_assign["x"] = input("Enter your own secret code of 'x': ")
        self.pass_assign["y"] = input("Enter your own secret code of 'y': ")
        self.pass_assign["z"] = input("Enter your own secret code of 'z': ")
        get_pass = re.sub(r'[^a-zA-Z0-9\s]+', "", self.password)
        encode_to_hash = hashlib.sha3_512(get_pass.encode())
        get_hash_code = encode_to_hash.hexdigest()
        # extract_hash_num = re.sub(r'[^0-9\s]+', "", get_hash_code)
        # extract_hash_alphabets = re.sub(r'[^a-zA-Z\s]+', "", get_hash_code)
        self.encoded_pass = ""
        for alphabets in get_hash_code:
            self.encoded_pass += self.pass_assign[alphabets]
        var = list(self.encoded_pass)
        length = len(self.encoded_pass)
        print(f"The generated password general length from your given pass is {length}.")
        total_length = int(input("Enter Required password length: "))
        if total_length > length:
            required_length = total_length - length
            get_pass = ""
            for i in range(length + required_length):
                get_pass += random.choice(var)
            print(get_pass)
        else:
            required_length = length - total_length
            get_pass = ""
            for i in range(length - required_length):
                get_pass += random.choice(var)
            print(get_pass)
            print("Required length generated")
            print("Warning")
            print("The length you entered is less than the original length of the generated pass from your pass")

    def choice_making(self):
        self.choice = int(input("which kind of password gen do you want (basic_genpass = 1, random_basic_genpass = 2, "
                                "random_required_len_genpass = 3, own_basic_genpass = 4, own_random_basic_genpass = "
                                "5, own_random_required_len_basic_genpass = 6, required_len_advanced_genpass = 7, "
                                "random_required_len_advanced_genpass = 8, own_required_len_advanced_genpass = 9): "))
        if self.choice == 1:
            GenPass.basic_genpass(self)
        elif self.choice == 2:
            GenPass.random_basic_genpass(self)
        elif self.choice == 3:
            GenPass.random_required_len_basic_genpass(self)
        elif self.choice == 4:
            GenPass.own_basic_genpass(self)
        elif self.choice == 5:
            GenPass.own_random_basic_genpass(self)
        elif self.choice == 6:
            GenPass.own_random_required_len_basic_genpass(self)
        elif self.choice == 7:
            GenPass.required_len_advanced_genpass(self)
        elif self.choice == 8:
            GenPass.random_required_len_advanced_genpass(self)
        elif self.choice == 9:
            GenPass.own_required_len_advanced_genpass(self)
        elif self.choice == 10:
            GenPass.own_random_required_len_advanced_genpass(self)
