import cv2

from time import sleep

key = cv2. waitKey(1)

webcam = cv2.VideoCapture(0)

sleep(2)

while True:



    try:

        check, frame = webcam.read()

        print(check) #prints true as long as the webcam is running

        print(frame) #prints matrix values of each framecd 

        cv2.imshow("Capturing", frame)

        key = cv2.waitKey(1)

        if key == ord('s'): 

            cv2.imwrite(filename='save.jpg', img=frame)

            webcam.release()

           
            print("Image saved!")

            

            break

        

        elif key == ord('q'):

            webcam.release()

            cv2.destroyAllWindows()

            break

    

    except(KeyboardInterrupt):

        print("Turning off camera.")

        webcam.release()

        print("Camera off.")

        print("Program ended.")

        cv2.destroyAllWindows()

        break


from watson_developer_cloud import VisualRecognitionV3
import json
vR = VisualRecognitionV3(
	version = '2.4.1',
	iam_apikey='FiYLafV8f1yMB1V2XnzG5ZcQeo0ZwF9tkXsOuGaMfxAf')
vR = VisualRecognitionV3(
    '2018-03-19',
  iam_apikey='FiYLafV8f1yMB1V2XnzG5ZcQeo0ZwF9tkXsOuGaMfxAf')

with open('save.jpg', 'rb') as images_file:
    classes = vR.classify(
        images_file,
        threshold='0.01',
 classifier_ids='DefaultCustomModel_1539045353').get_result()
print(json.dumps(classes, indent=2))