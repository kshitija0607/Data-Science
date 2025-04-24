# Keras and tensor flow, pytorch, Sklearn
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
model=Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(227,227,3)))
model.add(MaxPooling2D() )
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D() )
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D() )
model.add(Flatten())
model.add(Dense(100,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

history=model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])



from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/train',
        target_size=(227,227),
        batch_size=16 ,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test',
        target_size=(227,227),
        batch_size=16,
        class_mode='binary')

history=model.fit(
        training_set,
        epochs=50 ,
        validation_data=test_set,

        )

model.save('crackmodel.h5',history)

print("==============================saved the model===============================================")

# summarize history for accuracy
fig = plt.figure(1)
#fig.canvas.set_window_title("Model Accuracy Graph")
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
fig = plt.figure(2)
#fig.canvas.set_window_title("Model Loss Graph")
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()