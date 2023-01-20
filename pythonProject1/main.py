import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("diff_amplifier.txt", skiprows=1)

t = data[:, 0]
vut12 = data[:, 1]
vin1 = data[:,2]
vin2 = data[:,3]

vout1 = data [:, 4]
vout2 = data [:, 5]

t= t*1000
plt.plot(t, vin1 - vout2)
plt.plot(t, vin2)
#plt.legend(["Vut1","Vut2"])
plt.xlabel("tid (ms)")
plt.ylabel("volt (V)")


plt.show()




# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
