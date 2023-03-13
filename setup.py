from setuptools import find_packages, setup

setup(
    name='PlotLinearSolverResult',
    packages=find_packages(),
    version='0.1.1',
    description='This project is for plot LinearMSTMM solver result that is write with hdf5.',
    author='Zhengquan Liu',
    license='MIT',
    author_email="liuzq_96@163.com",
    long_description_content_type="text/markdown",
    long_description=open('README.md',encoding="UTF8").read(),
    install_requires=['numpy'],
    url="https://github.com/Qxxx1xx/PlotLinearSolverResult"
)
