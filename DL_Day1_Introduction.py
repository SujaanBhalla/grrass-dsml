# ==================================================================
# Day 1: Introduction to Deep Learning
# Introduction to Deep Learning concepts and a simple example using TensorFlow/Keras.
# ==========================================================
# Deep Learning
# Day 1
# Date : 2 July 2026
# Topic : Introduction to Deep Learning
# ==========================================================

# ==========================================================
# Relationship
# ==========================================================

# Artificial Intelligence (AI)
#         ↓
# Machine Learning (ML)
#         ↓
# Deep Learning (DL)

# AI is the parent field.
# ML is a subset of AI.
# DL is a subset of ML.

# ==========================================================
# What is Deep Learning?
# ==========================================================

# Deep Learning is a subset of Machine Learning.

# It uses Artificial Neural Networks (ANN)
# with multiple hidden layers
# to automatically learn patterns from data.

# Deep Learning is mainly used for:
# - Image Recognition
# - Speech Recognition
# - Natural Language Processing (NLP)
# - Self Driving Cars
# - Chatbots

# ==========================================================
# Architecture of Deep Learning
# ==========================================================

# Input Layer
#      ↓
# Hidden Layer 1
#      ↓
# Hidden Layer 2
#      ↓
# Hidden Layer 3
#      ↓
# Output Layer

# ==========================================================
# Input Layer
# ==========================================================

# The Input Layer receives the input data.

# Example:
# - Images
# - Words
# - Numbers
# - Audio

# ==========================================================
# Hidden Layers
# ==========================================================

# Hidden Layers process the information.

# They learn different patterns
# from the input data.

# More hidden layers
# means the model can learn
# more complex features.

# ==========================================================
# Output Layer
# ==========================================================

# The Output Layer gives
# the final prediction.

# Examples:
# Cat
# Dog
# Car
# Human

# ==========================================================
# Example
# ==========================================================

# A 5-year-old child
# sees many pictures of cats.

# Cat
# Cat
# Cat
# Cat

# After learning the pattern,
# the child can identify
# a new cat.

# Deep Learning works
# in a similar way.

# ==========================================================
# Types of Deep Learning
# ==========================================================

# 1. ANN
# Artificial Neural Network

# Used for:
# - Classification
# - Regression

# ----------------------------------------------------------

# 2. CNN
# Convolutional Neural Network

# Used for:
# - Image Classification
# - Face Recognition
# - Medical Images

# ----------------------------------------------------------

# 3. RNN
# Recurrent Neural Network

# Used for:
# - Text Processing
# - Language Translation
# - Speech Recognition
# - Time Series Prediction

# ==========================================================
# Artificial Neural Network (ANN)
# ==========================================================

# ANN stands for:
# Artificial Neural Network

# ANN is the basic Neural Network
# used in Deep Learning.

# It is inspired by the
# Human Brain.

# Just like the human brain has neurons,
# ANN also consists of Artificial Neurons.

# Working of ANN

# Step 1:
# Every neuron receives input.

# Step 2:
# The neuron performs calculations
# and learns patterns from the data.

# Step 3:
# The processed information is
# passed to the next hidden layer.

# Step 4:
# Finally, the output layer
# gives the prediction.

# ==========================================================
# Flow of ANN
# ==========================================================

# Input Layer
#        ↓
# Hidden Layer 1
#        ↓
# Hidden Layer 2
#        ↓
# Hidden Layer 3
#        ↓
# Output Layer

# ==========================================================
# Key Points
# ==========================================================

# ANN is inspired by the Human Brain.

# ANN contains Artificial Neurons.

# Every neuron receives input,
# performs calculations,
# learns patterns,
# and passes the output
# to the next layer.

# The Output Layer gives
# the final prediction.

# ==========================================================
# ANN Example
# ==========================================================

# Example:

# Student 1
# Solves the test.

#        ↓

# Student 2
# Improves it.

#        ↓

# Student 3
# Checks it.

#        ↓

# Final Answer

# Similarly,

# Multiple neurons work together
# to process the information
# and produce the final output.

# Multiple neurons working together
# forms an Artificial Neural Network (ANN).

# ==========================================================
# Uses of ANN
# ==========================================================

# 1. House Price Prediction

# 2. Sales Prediction

# 3. Loan Approval Prediction

# 4. Stock Price Prediction

# ==========================================================
# Key Points
# ==========================================================

# ANN is inspired by the Human Brain.

# It consists of multiple Artificial Neurons.

# Every neuron receives input,
# processes the information,
# and passes the output
# to the next neuron.

# All neurons work together
# to give the final prediction.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# ==========================================================
# CNN
# ==========================================================

# CNN stands for:
# Convolutional Neural Network

# CNN is a type of Deep Learning model.

# It is mainly used for
# Image Processing.

# CNN can automatically
# identify important features
# from images.

# Examples:
# - Face Recognition
# - Image Classification
# - Medical Image Analysis
# - Self Driving Cars
# - Object Detection

# ==========================================================
# Working of CNN
# ==========================================================

# Input Image
#        ↓
# Feature Extraction
#        ↓
# Pattern Learning
#        ↓
# Classification
#        ↓
# Final Prediction

# ==========================================================
# Example
# ==========================================================

# Input:
# Cat Image

# CNN learns:
# - Eyes
# - Ears
# - Nose
# - Tail

# Output:
# Cat

# ==========================================================
# Key Points
# ==========================================================

# CNN is mainly used for Images.

# It automatically learns
# image features.

# CNN gives high accuracy
# in image-related tasks.

#code cnn
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Flatten,Dense

# ==========================================================
# RNN
# ==========================================================

# RNN stands for:
# Recurrent Neural Network

# RNN is a type of Deep Learning model.

# It is mainly used for
# Sequential Data.

# RNN remembers previous information
# while processing the current input.

# ==========================================================
# Uses of RNN
# ==========================================================

# 1. Language Translation

# 2. Speech Recognition

# 3. Chatbots

# 4. Text Prediction

# 5. Time Series Forecasting

# 6. Sentiment Analysis

# ==========================================================
# Working of RNN
# ==========================================================

# Input Data
#       ↓
# Memory
#       ↓
# Hidden Layer
#       ↓
# Output

# RNN stores previous information
# and uses it to predict the next output.

# ==========================================================
# Example
# ==========================================================

# Sentence:

# I love ______

# RNN remembers the previous words

# "I love"

# and predicts the next word.

# Possible Output:

# Python
# India
# Machine Learning

# ==========================================================
# Key Points
# ==========================================================

# RNN works with Sequential Data.

# It has Memory.

# It remembers previous inputs.

# It is mainly used for
# Text, Speech and Time Series data.

#rnn
import tensorflow as tf
from tensorflow.keras.models import Sequential 
from tensor.flow.keras.layers import 

# in single line explain 
# cnn rnn ann 
# CNN is used for image processing, RNN is used for sequential data, and ANN is a basic neural network for general tasks.
# ==========================================================
# LSTM
# ==========================================================

# LSTM stands for:
# Long Short-Term Memory

# LSTM is an advanced type of
# Recurrent Neural Network (RNN).

# It is designed to remember
# information for a long period of time.

# ==========================================================
# Why LSTM?
# ==========================================================

# Normal RNN forgets old information
# when the sequence becomes very long.

# LSTM can remember important
# information for a longer time.

# Therefore,
# LSTM performs better than RNN
# for long sequences.

# ==========================================================
# Uses of LSTM
# ==========================================================

# 1. Speech Recognition

# 2. Language Translation

# 3. Text Prediction

# 4. Chatbots

# 5. Time Series Forecasting

# 6. Stock Price Prediction

# ==========================================================
# Working of LSTM
# ==========================================================

# Input Data
#       ↓
# Memory Cell
#       ↓
# Hidden Layer
#       ↓
# Output

# LSTM stores important information
# and removes unnecessary information.

# ==========================================================
# Example
# ==========================================================

# Sentence:

# I am learning ______

# LSTM remembers the previous words

# "I am learning"

# and predicts the next word.

# Possible Output:

# Deep Learning
# Python
# Machine Learning

# ==========================================================
# Key Points
# ==========================================================

# LSTM is an advanced version of RNN.

# It has Memory Cells.

# It remembers long-term information.

# It is mainly used for
# NLP, Speech Recognition,
# Text Prediction and Time Series.
#lstm
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense 

# ==========================================================
# GRU
# ==========================================================

# GRU stands for:
# Gated Recurrent Unit

# GRU is an advanced type of
# Recurrent Neural Network (RNN).

# It is similar to LSTM
# but has a simpler architecture.

# GRU is faster to train
# because it has fewer gates
# than LSTM.

# ==========================================================
# Why GRU?
# ==========================================================

# RNN cannot remember
# long-term information.

# GRU solves this problem
# by remembering important
# information for a longer time.

# ==========================================================
# Uses of GRU
# ==========================================================

# 1. Speech Recognition

# 2. Language Translation

# 3. Chatbots

# 4. Text Prediction

# 5. Sentiment Analysis

# 6. Time Series Forecasting

# ==========================================================
# Working of GRU
# ==========================================================

# Input Data
#        ↓
# GRU Cell
#        ↓
# Hidden Layer
#        ↓
# Output

# GRU decides what information
# should be remembered
# and what should be forgotten.

# ==========================================================
# Example
# ==========================================================

# Sentence:

# Today the weather is ______

# GRU remembers the previous words

# "Today the weather is"

# and predicts the next word.

# Possible Output:

# Sunny
# Rainy
# Cloudy

# ==========================================================
# Key Points
# ==========================================================

# GRU is a simplified version of LSTM.

# It trains faster than LSTM.

# It uses fewer gates.

# It is mainly used for
# NLP, Speech Recognition,
# Text Prediction and Time Series.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
