Reference Manual
================

Simple image classification with Inception.

Run image classification with Inception trained on ImageNet 2012 Challenge data set.

This program creates a graph from a saved GraphDef protocol buffer,
and runs inference on an input JPEG image. It outputs human readable
strings of the top 5 predictions along with their probabilities.

Change the --image_file argument to any jpg image to compute a
classification of that image.
