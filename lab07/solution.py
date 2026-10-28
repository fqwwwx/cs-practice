import numpy as np

def reshape_rows(values: list[float],width:int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    return np.asarray(values,dtype=float).reshape(-1,width).tolist()

def block(matrix,rows,columns):
    arr=np.asarray(matrix,dtype=float)
    if arr.size == 0 or arr.ndim<2:
        return []
    return arr[np.ix_(rows,colums)].tolist()

def column_means(matrix):
    arr = np.asarray(matrix,dtype=float)
    if arr.size == 0 or arr.shape[0] == 0 or arr.ndim < 2:
        return []
    return np.round(arr.mean(axis=0),6).tolist

def column_range (matrix,column):
    arr = np.asarray(matrix,dtype=float)
    if arr.size == 0 or arr.ndim < 2 or arr.shape[0]==0:
        return 0.0
        
    col_data = arr [:,column]
    return float(np.round(col_data.max() - col_data.min(),6))
