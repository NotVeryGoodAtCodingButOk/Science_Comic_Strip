# Science Comic Strip
# An animation telling the story of a rock
# By Simón Botero, for the science teacher Jill Holmes
# A project using Pygame 2.0.0.dev6, with the Python 3.7.7 interpreter, and the PyCharm IDE

# Import the modules we will be using for this project.
import pygame as pg
from time import sleep

# Initialize all the Pygame functionalities.
pg.font.init()
pg.mixer.init()

# Create a Pygame surface (a place where we can place our images)
# Set up the Path for the directory that the images are stored in.
PATH = "/Users/santiagobotero/Desktop/Science Comic Strip"

# Load up the images
igneous_rock = pg.image.load(PATH + "/igneous_rock.png")
metamorphic_rock = pg.image.load(PATH + "/metamorphic_rock.png")
sedimentary_rock = pg.image.load(PATH + "/sedimentary_rock.png")
volcano_exploding1 = pg.image.load(PATH + "/volcano_exploding1.png")
volcano_exploding2 = pg.image.load(PATH + "/volcano_exploding2.png")
volcano_exploding3 = pg.image.load(PATH + "/volcano_exploding3.png")
