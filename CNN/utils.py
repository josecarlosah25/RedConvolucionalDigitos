from CNN.forward import *
import numpy as np
import gzip

def extract_data(filename, num_images, IMAGE_WIDTH):
    '''
    Se extraen imagenes a traves del bytestream del archivo. 
    Se redimensiona los valores de entrada en una matriz [m, h, w]
    donde m es el numero de ejemplos de entrenamiento.
    
    '''
    print('Extracting', filename)
    with gzip.open(filename) as bytestream:
        bytestream.read(16)
        buf = bytestream.read(IMAGE_WIDTH * IMAGE_WIDTH * num_images)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = data.reshape(num_images, IMAGE_WIDTH*IMAGE_WIDTH)
        return data

def extract_labels(filename, num_images):
    '''
    Se extraen etiquetas en vectores de valores enteros de dimensiones [m, 1], con m siendo
    el numero de imagenes
    '''
    print('Extracting', filename)
    with gzip.open(filename) as bytestream:
        bytestream.read(8)
        buf = bytestream.read(1 * num_images)
        labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    return labels

def nanargmax(arr):
    '''
    regresa indice del mayor valor no-nan en el arreglo. La salida es una tupla ordenada
    '''
    idx = np.nanargmax(arr)
    idxs = np.unravel_index(idx, arr.shape)
    return idxs 

def initializeFilter(size, scale = 1.0):
    '''
    Inicializando filttro usando una distribucion normal con una
    desviacion estandar inversamente proporcional a la raiz cuadrada del
    numero de unidades.
    '''
    stddev = scale/np.sqrt(np.prod(size))
    return np.random.normal(loc = 0, scale = stddev, size = size)

def initializeWeight(size):
    
    #Inicializando pesos con una distribucion normal aleatoria
    
    return np.random.standard_normal(size=size) * 0.01


def predict(image, f1, f2, w3, w4, b1, b2, b3, b4, conv_s = 1, pool_f = 2, pool_s = 2):
    '''
    Realizar predicciones utilizando los filtros entrenados 
    '''
    conv1 = convolution(image, f1, b1, conv_s) # operacion de convolucion
    conv1[conv1<=0] = 0 #funcion de activacion ReLU
    
    conv2 = convolution(conv1, f2, b2, conv_s) # segunda operacion de convolucion
    conv2[conv2<=0] = 0 #funcion de activacion ReLU
    
    pooled = maxpool(conv2, pool_f, pool_s) # operacion de maxpooling
    (nf2, dim2, _) = pooled.shape
    fc = pooled.reshape((nf2 * dim2 * dim2, 1)) # conexion con la red neuronal artificial
    
    z = w3.dot(fc) + b3 # primera capa 
    z[z<=0] = 0 #funcion de activacion ReLU
    
    out = w4.dot(z) + b4 # segunda capa
    probs = softmax(out) # prediccion de probabilidades de clase con la funcion softmax
    
    return np.argmax(probs), np.max(probs)
