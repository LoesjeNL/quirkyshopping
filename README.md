# quirkyshopping



Description

Created by Louise Rutten at the Innsbruck University on January 2017

The goal of this program is to create a personal profile for a shopping website and to print an image on a shirt. 

Notebook Page 1: Make your profile
On this page, you should enter your name, your preference for a shirt print, whether you have glasses or not, your hair color, your size and your preferred color of the shirt.

Note: In order to move to the next window, you should first push the 'Next step' button

Notebook Page 2: Choose a print
Start by clicking refresh to update the image.

If your choice in Page 1 was 'My favourite galaxy', you can choose from 3 galaxies in the radiobox.

Click the 'Order!' button to order the shirt. Your figure will be written to file with your name and a time stamp.

INSTALLATION NOTES

To install the code in your computer, you need first to install the anaconda
python (https://www.continuum.io/downloads).
You will have to use the Python 2.x distribution since the code
uses wxpython which is still not ported to Python 3.


Then clone the repository:
git clone https://github.com/LoesjeNL/quirkyshopping.git

Build the conda package:
conda build quirkyshopping

And install it locally:

conda install --use-local quirkyshopping

At this point you can start the code everywhere by
typing:

quirkyshopping

since the executable is in the ~/anaconda/bin directory.
