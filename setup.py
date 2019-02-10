import setuptools


with open("README.md", "r") as f, open("requirements.txt", "r") as g:
    long_description = f.read()
    required = g.read().splitlines()


setuptools.setup(
     name='decs',
     version='0.0.4',
     author="Sergey Kastryulin",
     author_email="snk4tr@gmail.com",
     description="A handful of useful general-purpose python decorators.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/python-packages/decs",
     install_requires=required,
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
