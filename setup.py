from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'CloudComputing package'
LONG_DESCRIPTION = 'The CloudComputing package can be used to ease remote executing over SSH and cloud storage (OneDrive) with Python.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="CloudComputing", 
        version=VERSION,
        author="Mattia Pesenti",
        author_email="<mattia.pesenti@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['cloudsync', 'cloudsync-onedrive'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'cloud computing', 'onedrive'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
        ]
)