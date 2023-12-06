# Brain Tumor Detection

Detecting brain tumors using deep learning and image analysis. This project utilizes a pre-trained neural network to predict the presence of a tumor in brain images.

## Overview

This repository contains the code for predicting brain tumors and analyzing images using Python and deep learning. The model is trained on a dataset of brain images, and the `predict` function can be used to classify new images.

## Getting Started

### Prerequisites

- Python 3.x
- Install the required libraries using the following command:

  ```bash
  $ pip install -r requirements.txt
  ```
### Usage

1. Clone the repository:

   ```bash
   $ git clone https://github.com/Abdo404Khaled/Brain_cancer_prediction.git
   $ cd brain-tumor-detection
   ```
2. Run the prediction script:

   ```bash
   python main.py
   ```
   Follow the prompts to enter the path to the brain image you want to analyze.

## Jupyter Notebook

The `notebooks` directory contains a Jupyter notebook (`Brain_Tumor_Prediction.ipynb`) that covers the preprocessing of the dataset and the training of the neural network.

### Dataset Preprocessing

1. **Loading and Exploring the Dataset**: Load the brain tumor dataset and explore its structure.
2. **Data Preprocessing**: Clean and preprocess the data for training.

### Model Training

1. **Neural Network Architecture**: Define and compile the neural network model.
2. **Training the Model**: Train the model on the preprocessed dataset.

Feel free to explore the notebook for a detailed walkthrough of the dataset preprocessing and model training.

## Results

The `predict` function provides real-time predictions on new brain images and displays image analysis, including the original image, mask, and predicted tumor location.

## Contributors
- Abdelrahman Khaled


**Note**: Ensure that you have the required dependencies installed before running the code.
