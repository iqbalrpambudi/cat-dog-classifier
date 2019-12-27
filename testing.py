# Step 1: Import the packages
import glob
import PySimpleGUI as sg
from keras.models import model_from_json
import cv2
import numpy as np

# Step 2: Load the Model from Json File
json_file = open('./model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# Step 3: Load the weights
loaded_model.load_weights("./model/model.h5")
print("Loaded model from disk")

# Step 4: Compile the model
loaded_model.compile(
    optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# GLOB
filenames = glob.glob("./test_data/*.jpg")
filenames.sort()
images = [cv2.imread(img) for img in filenames]
# Step 5: load the image
# image = cv2.imread('/test_data/cat.4003.jpg')
for img in images:
    img = cv2.resize(img, (50, 50))
    img = img.reshape(1, 50, 50, 3)

    # cv2.imshow("Input Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Step 6: Predict to which class your input image has been classified
    result = loaded_model.predict_classes(img)
    if(result[0][0] == 1):
        print("This is dog")
    else:
        print("This is cat")
