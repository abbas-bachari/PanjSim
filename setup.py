from setuptools import setup, find_packages

setup(
    name='PanjSim',
    version='1.0.3',
    author='Abbas Bachari',
    author_email='abbas-bachari@hotmail.com',
    description='A simple Python API for 5sim.net',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/abbas-bachari/PanjSim',
    python_requires='>=3.7',
    project_urls={
    "Homepage":'https://github.com/abbas-bachari/PanjSim',
    'Documentation': 'https://github.com/abbas-bachari/PanjSim',
    'Source': 'https://github.com/abbas-bachari/PanjSim/',
    'Tracker': 'https://github.com/abbas-bachari/PanjSim/issues',
   
},
    
    install_requires=['requests'],
    keywords=['5sim', '5sim-sdk', '5sim-pythom', 'PanjSim', 'virtual numbers', 'api', '5sim-api','abbas bachari'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        
        
    ],
)


