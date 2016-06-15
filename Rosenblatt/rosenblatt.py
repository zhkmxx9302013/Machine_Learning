import numpy as np

##Only a learning process

b = 0 #bias
eta = 0.5 #Neural network learning rate

#Input neuron array
X_array = np.array([
      [b,1,1],  #Represent for 1 OR 1
      [b,1,0],  #Represent for 1 OR 0
      [b,0,0],  #Represent for 0 OR 0
      [b,0,1]   #Represent for 0 OR 1
  ])

#Expect result array
D_array = np.array([
        1,      #Represent for 0 OR 1 = 1
        1,      #Represent for 1 OR 0 = 1
        0,      #Represent for 0 OR 0 = 0
        1     #Represent for 0 OR 1 = 1
  ])

#Weight array
W_array = np.array([
        b,
        0,
        0
  ])

#Define the sgn function
def sgn(v):
  if v >= 0:
    return 1
  else:
    return 0

#Define the fuction to copmute the real result
def comy(w, x):
  v = np.dot(w.T,x)
  return sgn(v)

#Define the function to generate the new weight according to the \delta w (LaTeX)
def neww(oldw, di, xi, eta):
  yi = comy(oldw,xi)
  neww = oldw + eta*(di-yi)*xi
  return neww

if __name__ == '__main__':
  i = 0
  for xi in X_array:
    W_array = neww(W_array, D_array[i], xi, eta)
    print W_array
    i += 1

  for xi in X_array:
    print "%d OR %d IS %d"  %(xi[1], xi[2], comy(W_array, xi))