import numpy as np

def reshape_rows(values: list[float],width:int) -> list[list[float]]:
    arr = np.asarray(values,dtype=float)
    if width <= 0 or arr.size % width:
        return []
    return arr.reshape(-1,width).tolist()
    
def block(matrix:list[list[float]],rows:list[int],colums:list[int]) -> list[list[float]]:
    arr=np.asarray(matrix,dtype=float)
    if arr.size == 0:
        return []
    return arr[np.ix_(rows,colums)].tolist()
    
def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix,dtype = float)
    return np.round(arr.mean(axis=0),6).tolist if arr.size else []
    
def column_range (matrix: list[list[float]],column: int) -> float:
    arr = np.asarray(matrix,dtype = float)
    return round(float(np.ptp(arr[:,column])),6) if arr.size else 0.0