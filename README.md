# git-clone
A simple Python implementation of the git clone command that eliminates the addition of "https://github.com" before the repository command

To use, you can add the file to your PATH variable, but more importantly you use the following commands:

##git clone http://github.com/x/x.github.io = python git.py x [what you want to name the folder (optional)]
For example, 
git clone http://github.com/andykamath/andykamath.github.io andykamath
would be transferred to
python git.py andykamath

##git clone http://github.com/x/a = python git.py x/a [what you want to name the folder (optional)]
git clone http://github.com/andykamath/git-clone
would be transferred to
python git.py andykamath/git-clone
