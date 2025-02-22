import numpy as np

def calculate(list):
    print("let me print something")
    arr = np.array(list)
    reshaped = np.reshape(arr, (3, 3))
    print(arr)
    calculations = {
        "mean": [np.mean(reshaped, axis=0), np.mean(reshaped, axis=1), np.mean(reshaped)],
        'variance': [np.var(reshaped, axis=0), np.var(reshaped, axis=1), np.var(reshaped)],
        'standard deviation': [np.std(reshaped, axis=0), np.std(reshaped, axis=1), np.std(reshaped)],
        'max': [np.max(reshaped, axis=0), np.max(reshaped, axis=1), np.max(reshaped)],
        'min': [np.min(reshaped, axis=0), np.min(reshaped, axis=1), np.min(reshaped)],
        'sum': [np.sum(reshaped, axis=0), np.sum(reshaped, axis=1), np.sum(reshaped)]
    }


    return calculations