from pass_params import save_dict_to_file, sentParams
from runbatchfile import runBlender
from gen_lightcurve import gen_lightcurve
import matplotlib.pyplot as plt


save_dict_to_file(sentParams((10.5, 0, 0), 10, (0, 0, 1), '1996hw1.obj'))

def load_dict_from_file():
    f = open('dict.txt', 'r')
    data = f.read()
    f.close()
    return eval(data)

load = load_dict_from_file()
steps = load["steps"]

runBlender()

x, brightnesses = gen_lightcurve(steps)
plt.plot(x, brightnesses)
plt.show()


