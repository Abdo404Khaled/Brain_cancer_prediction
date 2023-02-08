import cv2 as cv
from matplotlib import pyplot as plt
from skimage import measure
from keras.models import load_model
import numpy as np

model = load_model('Brain_Tumor.h5')

def clear_axis(ax, title):
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])


def image_analysis(image, result):
    try:
        img = cv.medianBlur(image, 5)
        ret, mask = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
    except Exception as e:
        return

    contours = measure.find_contours(mask, .05)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.imshow(img, cmap=plt.cm.gray)
    ax2.imshow(mask, cmap=plt.cm.gray)
    ax3.imshow(img, cmap=plt.cm.gray)
    appended = []
    for contour in contours:
        if contour.shape > (100, 100):
            appended.append(contour)
            ax3.plot(contour[:, 1], contour[:, 0], linewidth=1)

    plt.suptitle(result)
    if len(appended) == 0:
        plt.suptitle('Result: Probably Has no tumor')

    clear_axis(ax1, 'Original')
    clear_axis(ax2, 'Mask')
    clear_axis(ax3, 'Tumor Predicted Place')
    plt.show()


def predict(path):
    image = cv.imread(path, cv.IMREAD_GRAYSCALE)
    image = cv.resize(image, dsize=(200, 200))
    make_prediction = np.array([image])

    prediction = model.predict(make_prediction[:1])

    if round(prediction[0][0]) == 1:
        result = 'Result: Probably Has a tumor'
        print('Prediction ' + result)
        print('Loading Image Analysis......')
        image_analysis(image, result)
    else:
        result = 'Result: Probably Has no tumor'
        print('Prediction ' + result)


while True:
    try:
        Image_path = input('Enter Image Path: ')
        predict(Image_path)
    except:
        print('Enter Valid Path')
