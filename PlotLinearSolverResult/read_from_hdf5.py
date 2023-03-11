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

def read_h5(filepath):
    return h5py.File(filepath,'r')

def print_to_dset(h5obj,depth=0):
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

def get_dset_attrs_keys(h5_file,path):
    return list(h5_file[path].attrs.keys())

def get_dset_attrs_value(dset,key):
    for attr in dset.attrs.items():
        if attr[0] == key:
            return attr[1][0]

def get_key_index(dset,key):
    return dset[:,get_dset_attrs_value(dset,key)]

def get_datas_dsetpath(h5_file,path):
    """
    Get datas from h5 file with path and indices.
    Arguments
    ---------
    h5_file : h5py._hl.files.File
        h5 file
    path : str
        datas path in h5 file
    Returns
    -------
    datas : numpy.ndarray
    """
    return np.array(h5_file[path])

def get_datas_dataspath_indices(h5_file,path,indices):
    """
    Get datas from h5 file with path and indices.
    Arguments
    ---------
    h5_file : h5py._hl.files.File
        h5 file
    path : str
        datas path in h5 file
    indices : list
        datas of index
    Returns
    -------
    datas : numpy.ndarray
    """
    datas = []
    group = h5_file[path]
    for name in group.keys():
        if str.isdigit(name):
            data = group[name][indices]
            datas.append(data)

    return np.array(datas)

def get_datas_indexpath_attrname(h5_file,path,name):
    """
    Get datas from h5 file with path of 'Index' group's dataset.
    Arguments
    ---------
    h5_file : h5py._hl.files.File
        h5 file
    path : str
        path of 'Index' group's dataset
    name : str
        one of dataset attributes name
    Returns
    -------
    datas : numpy.ndarray
    """
    index_dset_path = path
    attribute_name = name
    indices = get_key_index(h5_file[index_dset_path],attribute_name)
    datas_group_path = str.split(index_dset_path,'Index')[0]
    return get_datas_dataspath_indices(h5_file,datas_group_path,indices)

def f():
    print('test')