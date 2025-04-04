## Setup.py is responsible in creating my ML application as a package and deploy in pypi 
from setuptools import find_packages,setup
from typing import List

hyphen_e_dot= "-e ."
def get_requirements(file_path:str)->List[str]:   # requirements.txt has a list of libraries therefore it returns a list 
    
    '''
    This function will  return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  # on going to net line \n will get recorded on using readlines therefore this comprehension is used
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements   

setup(
    name='MLProject',
    version='0.0.1',
    author='Poorab',
    author_email='vpoorabsumanth04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

