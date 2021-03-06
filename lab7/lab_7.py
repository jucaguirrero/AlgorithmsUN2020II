# -*- coding: utf-8 -*-
"""Lab 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iVq0EJChWnifj0drXN18dg8pqzAQju19

# Laboratorio 7
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def f(z):
    return z ** 3 - 1

def df(z):
    return 3 * z**2

def newton_set1(z_c_r=0, z_c_i=0, zh = 5, zw=5, width=500, height=500, zoom=1,  niter=256):
    """ Fractals using newton-raphson """

    # Pixels array
    pixels = np.arange(width*height*3, dtype=np.uint32).reshape(height, width, 3)

    h = 1e-7 # step size for numerical derivative
    eps = 1e-3 # max error allowed

    # Bounding roots
    r1 = 1
    r2 = complex(-0.5, math.sin(2*math.pi/3))
    r3 = complex(-0.5, -1*math.sin(2*math.pi/3))

    # Color multiplication factor
    # NOTE: Increasing this darkens the image and lightens it otherwise
    multcol = 5

    for y in range(height):
            zy =   z_c_i+(((y-(height/2))/height)*zh*zoom)

            for x in range(width):
                zx = z_c_r+ (((x-(width/2))/width)*zw*zoom)

                # Mapping real -> complex plane
                z = complex(zx, zy)
                
                count = 0
                
                for i in range(niter):
                    # complex numerical derivative
                    dz = df(z)
                    if dz == 0:
                        break

                    count += 1
                    if count > 255:
                        break
                   
                    znext = z - f(z) / dz # Newton iteration

                    if abs(znext - z) < eps: # stop when close enough to any root
                        break
                    
                    z = znext

                # Pixels colored using the roots
                if abs(z-r1)<eps:
                    # color red
                    pixels[height-y-1,x] = (255 - count*multcol, 0, 0)
                elif abs(z-r2)<=eps:
                    # color green
                    pixels[height-y-1,x] = (0, 255 - count*multcol, 0)
                elif abs(z-r3)<=eps:
                    # color blue
                    pixels[height-y-1,x] = (0, 0, 255 - count*multcol)
                else:   
                    pixels[height-y-1,x] = (0, 0, 0)
 
    return pixels

def display1(z_c_r=0, z_c_i=0, zh = 1, zw=1, width=500, height=500, zoom=1,  niter=256):
    """ Display a newton-raphson fractal """
    print("Z region from (",z_c_r+ (((0-(width/2))/width)*zw*zoom),",",z_c_i+(((0-(height/2))/height)*zh*zoom) ,") to (",z_c_r+ (((width-(width/2))/width)*zw*zoom),",",z_c_i+(((height-(height/2))/height)*zh*zoom),")")
    pimg = newton_set1(z_c_r=z_c_r, z_c_i=z_c_i, zh = zh, zw=zw, width=width, height=width, zoom=zoom,  niter=niter)
    plt.title('Newton Fractal f(z)=z**3-1')
    plt.xlabel("real"+"("+ str(z_c_r+ (((0-(width/2))/width)*zw*zoom))+","+str(z_c_r+ (((width-(width/2))/width)*zw*zoom))+")")
    plt.ylabel("imaginary"+"("+str(z_c_i+(((0-(height/2))/height)*zh*zoom))+","+str(z_c_i+(((height-(height/2))/height)*zh*zoom)) +")")
    plt.imshow(pimg)
    plt.show()

"""## Plot of f(z)= z\*\*3-1 for the reals f(x)= x\*\*3-1"""

x = np.linspace(-2.0,2.0,100)
fig, ax = plt.subplots()
ax.plot(x,f(x))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.grid(True, which='both')
plt.title('f(x)=x**3-1')
plt.xlabel('x')
plt.ylabel('f(x)')

print("zoom out")
display1(zoom=1)
display1(zoom=2)
display1(zoom=3)
display1(zoom=4)
display1(zoom=5)

print("zoom in")
display1(zoom=1)
display1(zoom=1/2)
display1(zoom=1/3)
display1(zoom=1/4)
display1(zoom=1/5)
display1(zoom=1/10)
display1(zoom=1/100)
display1(zoom=1/1000)

"""## Newton iterates form z=10.0 + 0.0j"""

z=10.0 + 0.0j
r=[]
i=[]
for k in range(50):
  dz = df(z)
  z = z - f(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=10.0 + 0.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=-10.0 + 10.0j"""

z=-10.0 +10.0j
r=[]
i=[]
for k in range(50):
  dz = df(z)
  z = z - f(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=-10.0 + 10.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=-10.0 -10.0j"""

z=-10.0 -10.0j
r=[]
i=[]
for k in range(50):
  dz = df(z)
  z = z - f(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=-10.0 -10.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=0.0 + 0.0j"""

z=0.0 + 0.0j
r=[]
i=[]
for k in range(100):
  dz = df(z)
  z = z - f(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=0.0 + 0.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Ejemplo1    p(z)=z\*\*5-1\*z+5."""

def f1(z):
    return z ** 5 - 1 * z + 5

def df1(z):
    return 3 * z**2 - 2

def newton_set(z_c_r=0, z_c_i=0, zh = 5, zw=5, width=500, height=500, zoom=1,  niter=256):
    """ Fractals using newton-raphson """

    # Pixels array
    pixels = np.arange(width*height*3, dtype=np.uint32).reshape(height, width, 3)

    h = 1e-7 # step size for numerical derivative
    eps = 1e-3 # max error allowed

    # Bounding roots
    r1 = -1.76929
    r2 = complex(0.88465, -0.58974)
    r3 = complex(0.88465, 0.58974)

    # Color multiplication factor
    # NOTE: Increasing this darkens the image and lightens it otherwise
    multcol = 5

    for y in range(height):
            zy =   z_c_i+(((y-(height/2))/height)*zh*zoom)

            for x in range(width):
                zx = z_c_r+ (((x-(width/2))/width)*zw*zoom)

                # Mapping real -> complex plane
                z = complex(zx, zy)
                
                count = 0
                
                for i in range(niter):
                    # complex numerical derivative
                    dz = df1(z)
                    if dz == 0:
                        break

                    count += 1
                    if count > 255:
                        break
                   
                    znext = z - f1(z) / dz # Newton iteration

                    if abs(znext - z) < eps: # stop when close enough to any root
                        break
                    
                    z = znext

                # Pixels colored using the roots
                if abs(z-r1)<eps:
                    # color yellow
                    pixels[height-y-1,x] = (255 - count*multcol, 255, 0)
                elif abs(z-r2)<=eps:
                    # color green
                    pixels[height-y-1,x] = (0, 255 - count*multcol, 0)
                elif abs(z-r3)<=eps:
                    # color blue
                    pixels[height-y-1,x] = (0, 255, 255 - count*multcol)
                else:   
                    pixels[height-y-1,x] = (0, 0, 0)
 
    return pixels

def display1(z_c_r=0, z_c_i=0, zh = 1, zw=1, width=500, height=500, zoom=1,  niter=256):
    """ Display a newton-raphson fractal """
    print("Z region from (",z_c_r+ (((0-(width/2))/width)*zw*zoom),",",z_c_i+(((0-(height/2))/height)*zh*zoom) ,") to (",z_c_r+ (((width-(width/2))/width)*zw*zoom),",",z_c_i+(((height-(height/2))/height)*zh*zoom),")")
    pimg = newton_set(z_c_r=z_c_r, z_c_i=z_c_i, zh = zh, zw=zw, width=width, height=width, zoom=zoom,  niter=niter)
    plt.title('Newton Fractal f(z)= z**3-2*z + 2')
    plt.xlabel("real"+"("+ str(z_c_r+ (((0-(width/2))/width)*zw*zoom))+","+str(z_c_r+ (((width-(width/2))/width)*zw*zoom))+")")
    plt.ylabel("imaginary"+"("+str(z_c_i+(((0-(height/2))/height)*zh*zoom))+","+str(z_c_i+(((height-(height/2))/height)*zh*zoom)) +")")
    plt.imshow(pimg)
    plt.show()

"""## Plot of f(z)= z\*\*5-2\*z + 5 for the reals f(x)= x\*\*3-2\*x + 2"""

x = np.linspace(-2.0,2.0,100)
fig, ax = plt.subplots()
ax.plot(x,f1(x))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.grid(True, which='both')
plt.title('f(x)=x**3-2*x+2')
plt.xlabel('x')
plt.ylabel('f(x)')

print("zoom out")
display1(zoom=1)
display1(zoom=2)
display1(zoom=3)
display1(zoom=4)
display1(zoom=5)

print("zoom in")
display1(zoom=1)
display1(zoom=1/2)
display1(zoom=1/3)
display1(zoom=1/4)
display1(zoom=1/5)
display1(zoom=1/10)
display1(zoom=1/100)
display1(zoom=1/1000)

"""## Newton iterates form z=10.0 + 0.0j"""

z=10.0 + 0.0j
r=[]
i=[]
for k in range(50):
  dz = df1(z)
  z = z - f1(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=10.0 + 0.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=-10.0 + 10.0j"""

z=-10.0 +10.0j
r=[]
i=[]
for k in range(50):
  dz = df1(z)
  z = z - f1(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=-10.0 + 10.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=-10.0 -10.0j"""

z=-10.0 -10.0j
r=[]
i=[]
for k in range(50):
  dz = df1(z)
  z = z - f1(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=-10.0 -10.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=0.0 + 0.0j"""

z=0.0 + 0.0j
r=[]
i=[]
for k in range(100):
  dz = df1(z)
  z = z - f1(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=0.0 + 0.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import numpy as np
import math
import functools
import multiprocessing as mp
# %matplotlib inline


def rgb2int(rgb):
    red    = rgb[0]
    green  = rgb[1]
    blue   = rgb[2]
    RGBint = (red << 16) + (green << 8) + blue
    return RGBint


def int2rgb(RGBint):
    blue   = RGBint & 255
    green  = (RGBint >> 8) & 255
    red    = (RGBint >> 16) & 255
    return (red, green, blue)


def newton_set_calc_row(y, width, height, function, niter=256, x_off=0, y_off=0, zoom=1):
    """ Calculate one row of the newton set with size width x height """

    row_pixels = np.arange(width, dtype=np.uint32)
    # drawing area
    xa, xb, ya, yb = -2.5, 2.5, -2.5, 2.5

    zy = (y + y_off)*(yb - ya) / (zoom*(height - 1)) + ya   
    
    h = 1e-7 # step size for numerical derivative
    eps = 1e-3 # max error allowed
    a = complex(1, 0)

    for x in range(width): 
        # calculate the initial real and imaginary part of z,
        # based on the pixel location and zoom and position values
        zx = (x + x_off)*(xb - xa) / (zoom*(width - 1)) + xa
        z = complex(zx, zy)
        
        for i in range(niter):
            # complex numerical derivative
            dz = (function(z + complex(h, h)) - function(z)) / complex(h, h)
            if dz == 0:
                break

            znext = z - a*function(z) / dz # Newton iteration
            if abs(znext - z) < eps: # stop when close enough to any root
                break
                
            z = znext

        # Color according to iteration count 
        rgb = (i % 16 * 32, i % 8 * 64, i % 4 * 64)                              
        row_pixels[x] = rgb2int(rgb)


    return y, row_pixels


def newton_set_mp(width, height, function, zoom=1, x_off=0, y_off=0, niter=256):
    """ Newton-raphson fractal set with multiprocessing """
    
    w,h = width, height
    pixels = np.arange(w*h*3, dtype=np.uint32).reshape(h, w, 3)  

    # print('Starting calculation using',width, height,cx,cy)
    pool = mp.Pool(mp.cpu_count())

    newton_partial = functools.partial(newton_set_calc_row, 
                                       width=width,height=height, 
                                       function=function,
                                       niter=niter,
                                       zoom=zoom,
                                       x_off=x_off,
                                       y_off=y_off
                                      )

    for y,row_pixel in pool.map(newton_partial, range(h)):
        for x in range(w):
            pixels[y, x] = np.array(int2rgb(row_pixel[x]))

    return pixels
        
def display(function, width=1024, height=1024, niter=1024, zoom=1, x_off=0, y_off=0):
    """ Display a Newton-Raphson fractal """

    pimg = newton_set_mp(width, height, function, zoom=zoom,x_off=x_off, y_off=y_off, niter=niter) 
    plt.axis('off') 
    plt.imshow(pimg)
    plt.show() 
    
    
def plot(funct):
    x = np.linspace(-2.0,2.0,100)
    fig, ax = plt.subplots()
    ax.plot(x,funct(x))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, which='both')
    plt.xlabel('z')
    plt.ylabel('f(z)')

#Iteration forms
z1 = 10.0 + 0.0j
z2 = -10.0 + 10.0j
z3 = -10.0 - 10.0j
z4 = 0.0 + 0.0j

def newton_iteration(f, df, z):
    string = str(z)
    r = []
    i = []
    for k in range(50):
        dz = df(z)
        z = z - f(z) / dz # Newton iteration
        r.append(np.real(z))
        i.append(np.imag(z))
    plt.title('Newton iteration form ' + string)
    plt.plot(r)
    plt.ylabel('Real part')
    plt.show()
    plt.plot(i)
    plt.ylabel('Imaginary part')
    plt.show()
## $z^3 - 2z +2$
In [ ]:
def f1(z):
    return z*z*z - 2*z + 2

def df1(z):
    return 3*z - 2

plot(f1)

In [ ]:
display(f1)
display(f1, zoom=2)
display(f1, zoom=3)
display(f1, zoom=4)
display(f1, zoom=5)





In [ ]:
display(f1, zoom=1/2)
display(f1, zoom=1/4)
display(f1, zoom=1/10)
display(f1, zoom=1/100)
display(f1, zoom=1/1000)





In [ ]:
newton_iteration(f=f1, df=df1, z=z1)


In [ ]:
newton_iteration(f=f1, df=df1, z=z2)


In [ ]:
newton_iteration(f=f1, df=df1, z=z3)


In [ ]:
newton_iteration(f=f1, df=df1, z=z4)


## $z^6 + z^3 - 1$
In [ ]:
def f2(z):
    return z*z*z*z*z*z + z*z*z - 1

def df2(z):
    return 6*z*z*z*z*z + 3*z*z

plot(f2)

In [ ]:
display(f2)
display(f2, zoom=2)
display(f2, zoom=3)
display(f2, zoom=4)
display(f2, zoom=5)





In [ ]:
display(f2, zoom=1/2)
display(f2, zoom=1/4)
display(f2, zoom=1/10)
display(f2, zoom=1/100)
display(f2, zoom=1/1000)





In [ ]:
newton_iteration(f=f2, df=df2, z=z1)


In [ ]:
newton_iteration(f=f2, df=df2, z=z2)


In [ ]:
newton_iteration(f=f2, df=df2, z=z3)


In [ ]:
newton_iteration(f=f2, df=df2, z=z4)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-15-f8249b7d006c> in <module>()
----> 1 newton_iteration(f=f2, df=df2, z=z4)

<ipython-input-1-aad9b977adbd> in newton_iteration(f, df, z)
    118     for k in range(50):
    119         dz = df(z)
--> 120         z = z - f(z) / dz # Newton iteration
    121         r.append(np.real(z))
    122         i.append(np.imag(z))

ZeroDivisionError: complex division by zero
## $z^8 + 15z^4 - 16$
In [ ]:
def f3(z):
    return z*z*z*z*z*z*z*z + 15*z*z*z*z - 16

def df3(z):
    return 8*z*z*z*z*z*z*z + 60*z*z*z

plot(f3)

In [ ]:
display(f3)
display(f3, zoom=2)
display(f3, zoom=3)
display(f3, zoom=4)
display(f3, zoom=5)





In [ ]:
display(f3, zoom=1/2)
display(f3, zoom=1/4)
display(f3, zoom=1/10)
display(f3, zoom=1/100)
display(f3, zoom=1/1000)





In [ ]:
newton_iteration(f=f3, df=df3, z=z1)


In [ ]:
newton_iteration(f=f3, df=df3, z=z2)


In [ ]:
newton_iteration(f=f3, df=df3, z=z3)


In [ ]:
newton_iteration(f=f3, df=df3, z=z4)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-22-c39779d55f2d> in <module>()
----> 1 newton_iteration(f=f3, df=df3, z=z4)

<ipython-input-1-aad9b977adbd> in newton_iteration(f, df, z)
    118     for k in range(50):
    119         dz = df(z)
--> 120         z = z - f(z) / dz # Newton iteration
    121         r.append(np.real(z))
    122         i.append(np.imag(z))

ZeroDivisionError: complex division by zero

"""##Ejemplo2  p(z)=z\*\*6 + z\*\*3-1"""

def f2(z):
    return z**6 + z**3-1

def df2(z):
    return 6*(z**5) + 3*(z**2) 

def newton_set2(z_c_r=0, z_c_i=0, zh = 5, zw=5, width=500, height=500, zoom=1,  niter=256):
    """ Fractals using newton-raphson """

    # Pixels array
    pixels = np.arange(width*height*3, dtype=np.uint32).reshape(height, width, 3)

    h = 1e-7 # step size for numerical derivative
    eps = 1e-3 # max error allowed

    # Bounding roots
    r1 = -1.1740
    r2 = 0.85180
    r3 = complex(0.58699, 1.01670)
    r4 = complex(0.58699, -1.01670)
    r5 = complex(-0.42590, -0.73760)
    r6 = complex(-0.42590, 0.73760)

    # Color multiplication factor
    # NOTE: Increasing this darkens the image and lightens it otherwise
    multcol = 5

    for y in range(height):
            zy =   z_c_i+(((y-(height/2))/height)*zh*zoom)

            for x in range(width):
                zx = z_c_r+ (((x-(width/2))/width)*zw*zoom)

                # Mapping real -> complex plane
                z = complex(zx, zy)
                
                count = 0
                
                for i in range(niter):
                    # complex numerical derivative
                    dz = df2(z)
                    if dz == 0:
                        break

                    count += 1
                    if count > 255:
                        break
                   
                    znext = z - f2(z) / dz # Newton iteration

                    if abs(znext - z) < eps: # stop when close enough to any root
                        break
                    
                    z = znext

                # Pixels colored using the roots
                if abs(z-r1)<eps:
                    # color red
                    pixels[height-y-1,x] = (255 - count*multcol, 0, 0)
                elif abs(z-r2)<=eps:
                    # color green
                    pixels[height-y-1,x] = (0, 255 - count*multcol, 0)
                elif abs(z-r3)<=eps:
                    # color blue
                    pixels[height-y-1,x] = (0, 0, 255 - count*multcol)
                elif abs(z-r4)<=eps:
                    # color yellow
                    pixels[height-y-1,x] = (255 - count*multcol, 255, 0)
                elif abs(z-r5)<=eps:
                    # color fuccia
                    pixels[height-y-1,x] = (255, 0, 255 - count*multcol)
                elif abs(z-r6)<=eps:
                    # color purple
                    pixels[height-y-1,x] = (128 - count*multcol, 0, 128)
                else:   
                    pixels[height-y-1,x] = (0, 0, 0)
 
    return pixels

def display1(z_c_r=0, z_c_i=0, zh = 1, zw=1, width=500, height=500, zoom=1,  niter=256):
    """ Display a newton-raphson fractal """
    print("Z region from (",z_c_r+ (((0-(width/2))/width)*zw*zoom),",",z_c_i+(((0-(height/2))/height)*zh*zoom) ,") to (",z_c_r+ (((width-(width/2))/width)*zw*zoom),",",z_c_i+(((height-(height/2))/height)*zh*zoom),")")
    pimg = newton_set2(z_c_r=z_c_r, z_c_i=z_c_i, zh = zh, zw=zw, width=width, height=width, zoom=zoom,  niter=niter)
    plt.title('Newton Fractal  f(z)= z**6 + z**3 - 1')
    plt.xlabel("real"+"("+ str(z_c_r+ (((0-(width/2))/width)*zw*zoom))+","+str(z_c_r+ (((width-(width/2))/width)*zw*zoom))+")")
    plt.ylabel("imaginary"+"("+str(z_c_i+(((0-(height/2))/height)*zh*zoom))+","+str(z_c_i+(((height-(height/2))/height)*zh*zoom)) +")")
    plt.imshow(pimg)
    plt.show()

"""## Plot of f(z)= z\*\*6 + z\*\*3 - 1 for the reals f(x)= x\*\*6 + x\*\*3 - 1"""

x = np.linspace(-2.0,2.0,100)
fig, ax = plt.subplots()
ax.plot(x,f2(x))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.grid(True, which='both')
plt.title('f(x)= x**6 + x**3 - 1')
plt.xlabel('x')
plt.ylabel('f(x)')

print("zoom out")
display1(zoom=1)
display1(zoom=2)
display1(zoom=3)
display1(zoom=4)
display1(zoom=5)

print("zoom in")
display1(zoom=1)
display1(zoom=1/2)
display1(zoom=1/3)
display1(zoom=1/4)
display1(zoom=1/5)
display1(zoom=1/10)
display1(zoom=1/100)
display1(zoom=1/1000)

"""## Newton iterates form z=10.0 + 0.0j"""

z=10.0 + 0.0j
r=[]
i=[]
for k in range(50):
  dz = df2(z)
  z = z - f2(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=10.0 + 0.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=-10.0 + 10.0j"""

z=-10.0 +10.0j
r=[]
i=[]
for k in range(50):
  dz = df2(z)
  z = z - f2(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=-10.0 + 10.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=-10.0 -10.0j"""

z=-10.0 -10.0j
r=[]
i=[]
for k in range(50):
  dz = df2(z)
  z = z - f2(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=-10.0 -10.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()

"""## Newton iterates form z=0.0 + 0.0j"""

z=0.0 + 0.0j
r=[]
i=[]
for k in range(100):
  dz = df2(z)
  z = z - f2(z) / dz # Newton iteration
  r.append(np.real(z))
  i.append(np.imag(z))
plt.title('Newton iterates form z=0.0 + 0.0j')
plt.plot(r)
plt.ylabel('Real part')
plt.show()
plt.plot(i)
plt.ylabel('Imagnary part')
plt.show()