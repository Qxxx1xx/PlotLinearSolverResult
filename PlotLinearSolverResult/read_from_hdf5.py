# -*- encoding: utf-8 -*-
'''
Filename         :read_from_hdf5.py
Description      :Read some information from hdf5 file that saved as LinearMSTMM solver.
Time             :2023/03/10 09:22:30
Author           :Zhengquan Liu
Version          :1.0
'''


import h5py
import numpy as np

def print_to_dset(h5obj,depth=0):
    """
    Print all directoty information in the h5 object to the dataset
    Arguments
    ---------
    h5obj : h5py._hl.group.File or h5py._hl.group.Group
        a h5 object
    Returns
    -------
    none
    """
    if type(h5obj) == h5py._hl.dataset.Dataset:
        return h5obj.name
    dset_paths = []
    items = list(h5obj.keys())
    for index,item in enumerate(items):
        if str.isdigit(item):
            continue
        # 是否是最后一个元素
        is_last = index == len(items)-1
        # 得到下一级的h5对象
        item_h5obj = h5obj[item]
        print("   "*depth,end="")
        if is_last:
            print("└──",end="")
        else:
            print("├──",end="")

        print(item)
        dset_paths.append(print_to_dset(item_h5obj,depth+1))

    return dset_paths

class H5File:
    def __init__(self,filepath):
        """
        Initializa the H5File from the file path.
        Arguments
        ---------
        filepath : str
            the file path
        """
        self.h5file = h5py.File(filepath,'r')

    def print_directory_information(self):
        """
        Print the diractory information of the h5file to the dataset.
        """
        return print_to_dset(self.h5file)
        
    def get_keys_attr_dset(self,dset_path):
        """
        Get the keys of the attribute of the dataset.
        Arguments
        ---------
        dset_path : str
            the path of the dataset
        Returns
        -------
        the keys of the attributes of the dataset
        """
        return list(self.h5file[dset_path].attrs.keys())
        
    def get_value_attr_dset(self,dset_path,attr_key):
        """
        Get the value of the attrubute of the dataset.
        Arguments
        ---------
        dset_path : str
            the path of the dataset
        attr_key : str
            the key of the attribute of the dataset
        Returns
        -------
        the value of the attrubute of the dataset
        """
        for attr in self.h5file[dset_path].attrs.items():
            if attr[0] == attr_key:
                return attr[1][0]
        
    def get_index_attr_dset_in_data(self,dset_path,attr_key):
        """
        Get the index of the attribute of the dataset in the data over times.
        Arguments
        ---------
        dset_path : str
            the path of the dataset
        attr_key : str
            the key of the attribute of the dataset
        Returns
        -------
        the index of the attribute of the dataset in the data over times
        """
        dset = self.h5file[dset_path]
        if dset.size == dset.shape[0]:
            return dset[self.get_value_attr_dset(dset_path,attr_key)]
        else:
            return dset[:,self.get_value_attr_dset(dset_path,attr_key)]
        
    def get_keys_attr_dset_with_index_in_data(self,dset_path):
        """
        Get the keys of the attribute of the dataset with the index in the data.
        Arguments
        ---------
        dset_path : str
            the path of the dataset        
        Returns
        -------
        the keys of the attribute of the dataset with the index in the data
        """
        res = []
        keys = self.get_keys_attr_dset(dset_path)
        for key in keys:
            index = self.get_index_attr_dset_in_data(dset_path,key)
            res.append([key,index])

        return res
        
        
        
    def get_TimeStamps(self):
        """
        get time stamp values
        Returns
        -------
        time stamp values
        """
        return np.array(self.h5file['TimeStamps'])

    def get_numTimes(self):
        """
        get number of times
        Returns
        -------
        numbre of times
        """
        return self.get_TimeStamps().size
    
    def get_data_over_time(self,group):
        """
        Get data over time from group
        Arguments
        ---------
        group : h5py._hl.group.Group
            the group include data
        Returns
        -------
        data
        """
        data = []
        for i in range(self.get_numTimes()):
            data.append(group[str(i)])
        return np.array(data)

        

    def get_animation_data(self):
        """
        Get animation data over time.
        Returns
        -------
        animation data over time        
        """
        animation_group = self.h5file['Animation']
        return self.get_data_over_time(animation_group)
    
    def get_curve_data(self):
        """
        Get curve data over time.
        Returns
        -------
        curve data over time        
        """
        curve_group = self.h5file['Curve']
        return self.get_data_over_time(curve_group)
        