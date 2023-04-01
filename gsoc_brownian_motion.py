import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


x = 10
y = 10  

def plot_square():
    topright = np.array([20, 20])
    topleft = np.array([0, 20])
    bottomright = np.array([20,0])
    bottomleft = np.array([0, 0])

    plt.plot(topleft, topright, color = 'black', linewidth = 2)
    plt.plot(bottomleft, topleft, color = 'black', linewidth = 2)
    plt.plot(bottomright, bottomleft , color = 'black', linewidth = 2)
    plt.plot(topright, bottomright, color = 'black', linewidth = 2)

def in_boundaries(centerX, centerY):
    if(centerX + 0.5 < 20 and centerX - 0.5 > 0 and centerY + 0.5 < 20 and centerY - 0.5 > 0):
        return True
    return False

def move_forward(a, ax):
    global x 
    global y
        
    while True:
        calcX = np.cos(np.radians(a))
        calcY = np.sin(np.radians(a))
       
        if(in_boundaries(calcX+x, calcY+y)):
            draw_robot(ax)
            x += calcX
            y += calcY
        else:
            break

def random_rotate():
    return np.random.randint(360)

def draw_robot(ax):
    global x 
    global y
        
    circle = patches.Circle((x, y), 0.5, color='red')
    ax.add_patch(circle)
    plt.pause(0.1)
    ax.add_patch(patches.Circle((x, y), 0.5 + 0.1, color = 'white'))

 
                                     

fig = plt.figure()
ax = fig.add_subplot()
plt.grid(False)
plt.axis('off')

plot_square()
move_forward(random_rotate(), ax)

for i in range(100):
    move_forward(random_rotate(), ax)
    
plt.show
