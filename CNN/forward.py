import numpy as np

def convolution(image, filt, bias, s=1):
    '''
    Convolucion del filtro sobre la imagen con un intervalo (s)
    '''
    (n_f, n_c_f, f, _) = filt.shape # dimensiones del filtro
    n_c, in_dim, _ = image.shape # dimensiones de la imagen
    
    out_dim = int((in_dim - f)/s)+1 # calculo de las dimensiones de la salida
    
    assert n_c == n_c_f, "Dimensions of filter must match dimensions of input image"
    
    out = np.zeros((n_f,out_dim,out_dim))
    
    # convolucion del filtro sobre cada parte de la imagen, incluyendo un término sesgado en cada paso 
    for curr_f in range(n_f):
        curr_y = out_y = 0
        while curr_y + f <= in_dim:
            curr_x = out_x = 0
            while curr_x + f <= in_dim:
                out[curr_f, out_y, out_x] = np.sum(filt[curr_f] * image[:,curr_y:curr_y+f, curr_x:curr_x+f]) + bias[curr_f]
                curr_x += s
                out_x += 1
            curr_y += s
            out_y += 1
        
    return out

def maxpool(image, f=2, s=2):
    '''
    Reduccion de las muestras de la imagen utilizando el tamaño del filtro "f" y un incremento "s" 
    '''
    n_c, h_prev, w_prev = image.shape
    
    h = int((h_prev - f)/s)+1
    w = int((w_prev - f)/s)+1
    
    downsampled = np.zeros((n_c, h, w))
    for i in range(n_c):
        #Recorrer la ventana de maxpool sobre cada parte de la imagen y le asigna un valor máximo en cada paso a la salida
        curr_y = out_y = 0
        while curr_y + f <= h_prev:
            curr_x = out_x = 0
            while curr_x + f <= w_prev:
                downsampled[i, out_y, out_x] = np.max(image[i, curr_y:curr_y+f, curr_x:curr_x+f])
                curr_x += s
                out_x += 1
            curr_y += s
            out_y += 1
    return downsampled

def softmax(X):
    out = np.exp(X)
    return out/np.sum(out)

def categoricalCrossEntropy(probs, label):
    return -np.sum(label * np.log(probs))