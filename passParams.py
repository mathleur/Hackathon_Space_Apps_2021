def sentParams(param1, param2, param3):
  hashParams = locals()
  return hashParams

def save_dict_to_file(dic):
    f = open('dict.txt', 'w')
    f.write(str(dic))
    f.close()


save_dict_to_file(sentParams(1, 2, 3))

# This will save parameters 1, 2 , 3 to param1, param2 and param3

## The code below is what you should insert inside blender and it will load that file called 'dict.txt'

# def load_dict_from_file():
#     f = open('dict.txt', 'r')
#     data = f.read()
#     f.close()
#     return eval(data)

# load_dict_from_file()
