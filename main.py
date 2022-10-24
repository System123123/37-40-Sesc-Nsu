import xml.dom.minidom
from random import randint
import math
import numpy as np
import matplotlib.pyplot as plt



def thirty_seventh():
    r = 50
    h = 30
    l = np.linspace(0, 50, 500)
    lx = np.sin(l)
    ly = np.cos(l)
    lx = r * l - h * np.sin(l)
    ly = r - h * ly
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")

    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(lx, ly, label="r>h")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")
    h = 50
    lx = np.sin(l)
    ly = np.cos(l)
    lx = r * l - h * np.sin(l)
    ly = r - h * ly
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(lx, ly, label="r==h")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    h = 70
    lx = np.sin(l)
    ly = np.cos(l)
    lx = r*l - h*np.sin(l)
    ly = r - h* ly
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(lx, ly, label="r<h")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    plt.show()

def thirty_eigth():
    t = np.linspace(0, 2*np.pi, 100)
    a = 5
    b = 15
    lx = a * np.cos(t) * np.cos(t) +  b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(lx, ly, label="b > 2a")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")

    a = 5
    b = 7
    lx = a * np.cos(t) * np.cos(t) + b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(lx, ly, label="a<b<2a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 5
    b = 3
    lx = a * np.cos(t) * np.cos(t) + b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.plot(lx, ly, label="b<a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 5
    b = 5
    lx = a * np.cos(t) * np.cos(t) + b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    ax2 = fig.add_subplot(2, 2, 4)
    ax2.plot(lx, ly, label="b==a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.show()

def thirty_nineth():
    t = np.linspace((-2)*np.pi, 2*np.pi, 501)
    a = 5
    b = 15
    lx = (a+b)*np.cos(t)-a*np.cos((a+b)*t/a)
    ly = (a+b)*np.sin(t) - a * np.sin((a+b)* t/a)
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(lx, ly, label="b == 3a")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")
    a = 4
    b = 6
    lx = (a + b) * np.cos(t) - a * np.cos((a + b) * t / a)
    ly = (a + b) * np.sin(t) - a * np.sin((a + b) * t / a)
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(lx, ly, label="b == 3/2a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.show()


def fortieth():
    t = np.linspace((-1)*np.pi, np.pi, 201)
    a = 1
    b = 1
    d = np.pi/2
    lx = a * np.sin(a*t+d)
    ly = b * np.sin(b*t)
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    fig.suptitle("Graphics")
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(lx, ly, label="a==b, d = PI/2")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")


    a = 1
    b = 2
    d = np.pi / 4
    lx = a * np.sin(a * t + d)
    ly = b * np.sin(b * t)

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(lx, ly, label="b == 2a, d = PI/4")

    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 1
    b = 8
    d = np.pi / 2
    lx = a * np.sin(a * t + d)
    ly = b * np.sin(b * t)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(lx, ly, label="b == 8a, d = PI/2")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 1
    b = 3
    d = np.pi / 2
    lx = a * np.sin(a * t + d)
    ly = b * np.sin(b * t)

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(lx, ly, label="b == 3a, d = PI/2")
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    plt.show()

if __name__ == "__main__":
    print(fortieth())
