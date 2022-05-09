As noted in the README in the root of the directory, I could not find a way to 
completely build and test my code. I have the rudimentals of the structure to
create the build, but not a way to run or test it. See the "script" directory 
for working code 

I have been trying the following commands within the build directory
To build:
`pip install .`

To build, and have editable so tests should theoretically work:
`pip install -e .`

And to test (neither of which are running)
`python setup.py test`
`python -m unittest discover`