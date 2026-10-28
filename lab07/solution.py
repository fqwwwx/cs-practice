import numpy as np

def reshape_rows(values: list[float],width:int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    return np.array(values,dtype=float).reshape(-1,width).tolist()

def block(matrix:list[list[float]],rows:list[int],colums:list[int]) -> list[list[float]]:
    arr=np.asarray(matrix)
    if arr.size == 0:
        return []
    return arr[np.ix_(rows,colums)].astype(floar).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix)
    if arr.size == 0 or arr.shape == 0:
        return []
    return np.round(arr.mean(axis=0),6).tolist

def column_range (matrix: list[list[float]],column: int) -> float:
    arr = np.asarray(matrix)
    if arr.size == 0:
        return 0.0
    col_data = arr [:,column]
    return float(np.round(col_data.max() - col_data.min(),6))
