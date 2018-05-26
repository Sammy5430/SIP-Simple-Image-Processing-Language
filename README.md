# Introduction

Currently, there are a variety of image processing features available across multiple programming languages. Many of them require a lot of lines of code or are hard to use due to the technical jargon that is associated with digital signal processing; which also makes the documentation difficult to understand. Our focus in this project is to develop a language that is straightforward for users that are not necessarily knowledgeable of image processing or digital signal processing in general. We expect that the learning curve for our proposed programming language is far from steep so that users can swiftly modify images as they want to. Users can do this by importing an image and applying a variety of operations to an image such as scaling, sharpening, and feature extraction via our programming language. Our proposed language will be implemented using PLY, the python scanner/parser tool that will allow us to create the straightforward syntax of SIP. The python libraries of Scipy and Numpy will be used since they will allow us to manipulate the vectors/matrices associated with the images while also having some toolboxes for image/signal processing. Finally, matplotlib will be used to render the images and display the effects that the user executed.



# SIP GRAMMAR

![grammar](images/0_grammar.PNG)



# Reference Manual

## Types

**2D Images**
*	Also known as binary images, these types are only capable of performing tasks that do not require the image being modified to have 3 matrices represent them. Performing a wrong command will result in a warning explaining so. 

**3D Images**
*	All types of images represented with 3 matrices, each representing their respective colors (RGB). 


## Variables

All variables will only be images represented as arrays of numbers representing pixels and can only be initialized by assigning an image or assigning it to a command reading an image file. 


![variable](images/1_variable.png)


## Functions

**read(“FILENAME”)**
*	**read** - Reads an image from a file, used for variable initialization.
*	**Parameters:** File containing the image to be read.

**Example:**

![read](images/2_read.png)



**grayscale()**
*	Converts a 3D image to a 2D image composed exclusively of different shades of gray.

**Example:**

![grayscale](images/3_grayscale.png)
![grayscale](images/4_grayscale.PNG)



**sepia()**
*	Converts an image to sepia tones, mostly used to represent aging of old images.

**Example:**

![sepia](images/5_sepia.png)
![sepia](images/6_sepia.PNG)



**red()**
*	Converts a 3D image to 2D by extracting only the red tones.

**Example:**

![red](images/7_red.png)
![red](images/8_red.PNG)



**green()**
*	Converts a 3D image to 2D by extracting only the green tones.

**Example:**

![green](images/9_green.png)
![green](images/10_green.PNG)



**blue()**
*	Converts a 3D image to 2D by extracting only the blue tones.

**Example:**

![blue](images/11_blue.png)
![blue](images/12_blue.PNG)



**invert()**
*	Inverts the color of each individual pixel, creating the effect of a negative image

**Example:**

![invert](images/13_invert.png)
![invert](images/14_invert.PNG)



**show()**
* Shows the current state of the image stored in a given variable

**Example:**

![show](images/15_show.png)
![show](images/16_show.PNG)



**blur(LEVEL)**
*	**Parameters:** Will require the user to input intensity of the blur in the form of medium, low or high.
*	**blur** – It will reduce image noise and reduce detail to the image this function is being used on. 

**Example:**

![blur](images/17_blur.png)
![blur](images/18_blur.PNG)



**rotate(DIRECTION)**
*	**Parameters:** Will require the user to input which direction would he like it to rotate to, right or left. 
*	**rotate** – Will rotate the image 90 degrees to the side that was input. 

**Example:**

![rotate](images/19_rotate.png)
![rotate](images/20_rotate.PNG)



**edges(LEVEL)**
*	**Parameters:** Will require the user to input intensity of the blur in the form of medium, low or high.
*	**edges** – Finds the boundaries of objects within the images. Works by detecting discontinuities in brightness. This method can only be called onto 2D images. 

**Example:**

![edges](images/21_edges.png)
![edges](images/22_edges.PNG)



**sharpen(LEVEL)** 
*	**Parameters:** Will require the user to input intensity of the blur in the form of medium, low or high.
*	**sharpen** – Emphasizes the texture and drawing viewer focus to the image. 

**Example:**

![sharpen](images/23_sharpen.png)
![sharpen](images/24_sharpen.PNG)



**save(STRING)**
*	**Parameters:** Will require the user to input the name of the new file to be saved as well as its image format between quotation marks. 
*	**save** – Will save the copy of the image being used onto the project folder with the name given.

**Example:**

![save](images/25_save.png)



**resize(INT COMMA INT)**
*	**Parameters:** Will require the user to input the Width and Height preferred onto the image. 
*	**Resize** – Will resize the image to fit the dimensions used as parameters. 

**Example:**

![resize](images/26_resize.png)



**crop(INT COMMA INT)**
*	**Parameters:** Will require the user to input the Width and Height preferred onto the image.
*	**Crop** - Crop with respect to the center of the image, parameters cannot be larger than the dimensions of the image.

**Example:**

![crop](images/27_crop.png)
![crop](images/28_crop.PNG)



**spiral(INT COMMA INT)**
*	**Parameters:** Will require the user to input the strength of the spiral and the radius onto which it will apply the spiral animation on the picture. 
*	**Spiral** – Will apply a spiral effect onto the image. 

**Example:**

![spiral](images/29_spiral.png)
![spiral](images/30_spiral.PNG)




# Conclusion

  The completed language implementation provides some of the more common image processing methods with a simpler syntax, appropriate error handling, and parameters that are easier to understand. Methods which previously required complex user input have been implemented on SIP to work with levels (‘low’, ‘medium’, and ‘high’). Furthermore, the rotate method which normally requires the user to implement the number of degrees to rotate and the origin point for the rotation, has been simplified to work with 90-degree rotations with the origin set to the center of the image. After comparing code snippets between other implementations of these methods and the implementations done in this project, we can see a reduction in line of codes, which was one of the project’s goals. In addition, we can perceive the simplicity of the parameters used in SIP, when comparing it with other implementations. Overall, this language provides higher most image processing methods with better accessibility, since users can understand it even with little or no previous knowledge of image processing languages.

