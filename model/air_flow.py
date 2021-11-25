import numpy as np

class CoughGrid:
    def __init__(self,rows, cols):
        self.wh = (cols, rows)
        self.tiles = [[0 for col in cols] for row in rows]
        
    def update(self):
        up_shift = self.ushift(self.tiles, 1, 0)
        left_shift = self.lshift(self.tiles, 1, 0)
        down_shift = self.ushift(self.tiles,-1, 0)
        right_shift = self.lshift(self.tiles,-1, 0)
        
        ul_shift = self.lshift(up_shift,1,0)
        ld_shift = self.ushift(left_shift,-1,0)
        dr_shift = self.lshift(down_shift,-1,0)
        ru_shift = self.ushift(right_shift,1,0)
    
        count = (up_shift + down_shift + left_shift + right_shift + ul_shift + ld_shift + dr_shift + ru_shift + self.tiles)/8.98
        self.tiles = np.clip(count, 0, 1)
                
    def lshift(self, arr, num, desired):
        result = np.empty_like(arr)
        arr_shape = arr.shape
        if num > 0:
            result = np.hstack(( np.full( (arr_shape[0],num), desired), arr[:,:-num] ))
        elif num <= 0:
            result = np.hstack(( arr[:,-num:], np.full( (arr_shape[0],-num), desired) ))
        return result
    
    def ushift(self, arr, num, desired):
        result = np.empty_like(arr)
        arr_shape = arr.shape
        if num > 0:
            result = np.vstack(( arr[num:,:], np.full( (num,arr_shape[1]), desired) ))
        elif num <= 0:
            result = np.vstack(( np.full( (-num,arr_shape[1]), desired), arr[:num,:] ))
        return result

    def plus_one(self,tile_pos):
        self.tiles[tile_pos[1],tile_pos[0]]=1