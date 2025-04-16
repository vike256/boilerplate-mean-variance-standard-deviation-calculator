import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}
    
    array = np.array(list).reshape(3, 3)

    # Calculate mean
    mean = []
    mean.append(np.mean(array, axis=0).tolist())
    mean.append(np.mean(array, axis=1).tolist())
    mean.append(np.mean(array))
    calculations['mean'] = mean

    # Calculate variance
    variance = []
    variance.append(np.var(array, axis=0).tolist())
    variance.append(np.var(array, axis=1).tolist())
    variance.append(np.var(array))
    calculations['variance'] = variance

    # Calculate standard deviation
    std = []
    std.append(np.std(array, axis=0).tolist())
    std.append(np.std(array, axis=1).tolist())
    std.append(np.std(array))
    calculations['standard deviation'] = std

    # Calculate max
    max_values = []
    max_values.append(np.max(array, axis=0).tolist())
    max_values.append(np.max(array, axis=1).tolist())
    max_values.append(np.max(array))
    calculations['max'] = max_values

    # Calculate min
    min_values = []
    min_values.append(np.min(array, axis=0).tolist())
    min_values.append(np.min(array, axis=1).tolist())
    min_values.append(np.min(array))
    calculations['min'] = min_values

    # Calculate sum
    sum_values = []
    sum_values.append(np.sum(array, axis=0).tolist())
    sum_values.append(np.sum(array, axis=1).tolist())
    sum_values.append(np.sum(array))
    calculations['sum'] = sum_values

    return calculations
