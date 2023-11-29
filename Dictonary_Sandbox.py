my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

to_check = ["blue", "sky", "apple", "salad"]

for item in to_check:

    # check if it's a key (ie: a colour in our dictionary)
    if item in my_dict:
        print("{} is a key in the dictionary".format(item))

        # look up value associated with my key
        coloured_object = my_dict[item]

        # output the value and the key (eg: the sky is blue)
        print("The {} is {}".format(coloured_object, item))

    # check if it's a value (ie: an object in our dictionary)
    elif item in my_dict.values():
        print("{} is a value in the dictionary".format(item))

