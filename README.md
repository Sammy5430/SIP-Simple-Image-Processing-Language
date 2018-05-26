# SIP-Simple-Image-Processing-Language
Programming Language designed as a proyect for ICOM4036

### Introduction

Currently, there are a variety of image processing features available across multiple programming languages. Many of them require a lot of lines of code or are hard to use due to the technical jargon that is associated with digital signal processing; which also makes the documentation difficult to understand. Our focus in this project is to develop a language that is straightforward for users that are not necessarily knowledgeable of image processing or digital signal processing in general. We expect that the learning curve for our proposed programming language is far from steep so that users can swiftly modify images as they want to. Users can do this by importing an image and applying a variety of operations to an image such as scaling, sharpening, and feature extraction via our programming language. Our proposed language will be implemented using PLY, the python scanner/parser tool that will allow us to create the straightforward syntax of SIP. The python libraries of Scipy and Numpy will be used since they will allow us to manipulate the vectors/matrices associated with the images while also having some toolboxes for image/signal processing. Finally, matplotlib will be used to render the images and display the effects that the user executed.

# SIP GRAMMAR

NEED TO ADD IMAGE OF GRAMMAR BUT FIRST UPLOAD THE IMAGE (only works with URL)

# Reference Manual

## Types

**2D Images**
*	Also known as binary images, these types are only capable of performing tasks that do not require the image being modified to have 3 matrices represent them. Performing a wrong command will result in a warning explaining so. 

**3D Images**
*	All types of images represented with 3 matrices, each representing their respective colors (RGB). 

## Variables

All variables will only be images represented as arrays of numbers representing pixels and can only be initialized by assigning an image or assigning it to a command reading an image file. 

NEED TO ADD IMAGE HERE


## Functions

**read(“FILENAME”)**
*	**read** - Reads an image from a file, used for variable initialization.
*	**Parameters:** File containing the image to be read.
**Example:**

Need to add image of execution

**grayscale()**
*	Converts a 3D image to a 2D image composed exclusively of different shades of gray.
**Example:**

Need to add image of execution

**sepia()**
*	Converts an image to sepia tones, mostly used to represent aging of old images.
**Example:**

Need to add image of execution

**red()**
*	Converts a 3D image to 2D by extracting only the red tones.
**Example:**

Need to add image of execution


**green()**
*	Converts a 3D image to 2D by extracting only the green tones.
**Example:**

Need to add image of execution


**blue()**
*	Converts a 3D image to 2D by extracting only the blue tones.
**Example:**

Need to add image of execution


**invert()**
*	Inverts the color of each individual pixel, creating the effect of a negative image
**Example:**

Need to add image of execution


**show()**
* Shows the current state of the image stored in a given variable
**Example:**

Need to add image of execution


**blur(LEVEL)**
*	**Parameters:** Will require the user to input intensity of the blur in the form of medium, low or high.
*	**blur** – It will reduce image noise and reduce detail to the image this function is being used on. 
**Example:** 

Need to add image of execution


**rotate(DIRECTION)**
*	**Parameters:** Will require the user to input which direction would he like it to rotate to, right or left. 
*	**rotate** – Will rotate the image 90 degrees to the side that was input. 
**Example:** 

Need to add image of execution


**edges(LEVEL)**
*	**Parameters:** Will require the user to input intensity of the blur in the form of medium, low or high.
*	**edges** – Finds the boundaries of objects within the images. Works by detecting discontinuities in brightness. This method can only be called onto 2D images. 
**Example:** 

Need to add image of execution


**sharpen(LEVEL)** 
*	**Parameters:** Will require the user to input intensity of the blur in the form of medium, low or high.
*	**sharpen** – Emphasizes the texture and drawing viewer focus to the image. 
**Example:** 

Need to add image of execution


**save(STRING)**
*	**Parameters:** Will require the user to input the name of the new file to be saved as well as its image format between quotation marks. 
*	**save** – Will save the copy of the image being used onto the project folder with the name given.
**Example:** 

Need to add image of execution


**resize(INT COMMA INT)**
*	**Parameters:** Will require the user to input the Width and Height preferred onto the image. 
*	**Resize** – Will resize the image to fit the dimensions used as parameters. 
**Example:** 

Need to add image of execution


**crop(INT COMMA INT)**
*	**Parameters:** Will require the user to input the Width and Height preferred onto the image.
*	**Crop** - Crop with respect to the center of the image, parameters cannot be larger than the dimensions of the image.
**Example:** 

Need to add image of execution

