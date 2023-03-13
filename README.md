PlotLinearSolverResult
==============================

This project is for plot LinearMSTMM solver result that is write with hdf5.

First import this package.
```python
import PlotLinearSolverResult.read_from_hdf5 as rh
import matplotlib.pyplot as plt
import numpy as np
```

Then, initialize a H5File from h5 file path.

```
f = rh.H5File('test_write_vibration_characteristics.h5')
```

Using `print_directory_information` that can print the diractory information of the h5file to the dataset.

```
f.print_directory_information()
```
```text
​    ├──Animation
​       └──Index
​          ├──Ground
​             └──Frame
​          └──Part_Beam
​             ├──Frame
​             └──Part_BeamNodes
​    ├──Curve
​       └──Index
​          ├──Ground
​             └──Markers
​                └──Marker_0
​          └──Part_Beam
​             └──Nodes
​    ├──ModalInformation
​       ├──Index
​          ├──Ground
​             └──Frame
​          └──Part_Beam
​             ├──Frame
​             └──Part_BeamNodes
​       ├──NaturalFrequencies
​       └──SystemModalMass
​    └──TimeStamps
​    [[[['/Animation/Index/Ground/Frame'],
​       ['/Animation/Index/Part_Beam/Frame',
​        '/Animation/Index/Part_Beam/Part_BeamNodes']]],
​     [[[['/Curve/Index/Ground/Markers/Marker_0']], [[]]]],
​     [[['/ModalInformation/Index/Ground/Frame'],
​       ['/ModalInformation/Index/Part_Beam/Frame',
​        '/ModalInformation/Index/Part_Beam/Part_BeamNodes']],
​      '/ModalInformation/NaturalFrequencies',
​      '/ModalInformation/SystemModalMass'],
​     '/TimeStamps']
```

Get the keys of the attributes of the dataset.

```python
keys = f.get_keys_attrs_dset('/Animation/Index/Part_Beam/Part_BeamNodes')
keys[5]
```

```
​    'PhysicalDisplacementY'
```

Using `get_index_attr_dset_in_datas` to get the index of the attribute of the dataset in the data over times.

Using `get_animation_datas` to get animation datas over time.

Using `get_TimesStamps` to get TimesStamps datas.

Finally, you can plot with times and datas.

```python
index = f.get_index_attr_dset_in_datas('/Animation/Index/Part_Beam/Part_BeamNodes',keys[5])
animation_datas = f.get_animation_datas()
times = f.get_TimeStamps()
plt.plot(times,animation_datas[:,index[0]])
```

```
​    [<matplotlib.lines.Line2D at 0x1ef4062c8d0>]
```

![image-20230313114802427](https://s1.vika.cn/space/2023/03/13/86860a0b033d447590286ed0b0cd68dd)
    