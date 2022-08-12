
import face_recognition
import pickle
import cv2
import time



def detect_person_in_video(cap_ip,db_encode,name):
    data = pickle.loads(open(f"{db_encode}/{name}_encodings.pickle","rb").read())
    cap = cv2.VideoCapture(cap_ip)

    time.sleep(1)

    while True:
        ret,image = cap.read()
        locations = face_recognition.face_locations(image,model="hog") #hog cnn
        encodings = face_recognition.face_encodings(image,locations)

        for face_encoding, face_location in zip(encodings,locations):
            result = face_recognition.compare_faces(data["encoding"],face_encoding)
            match = None
            if True in result:
                match = data["name"]
                print(f"Match found {match}")
            else:
                print("Unknown")

            left_top = (face_location[3],face_location[0])
            right_bottom = (face_location[1],face_location[2])
            color = [0,255,0]
            cv2.rectangle(image,left_top,right_bottom,color)

            #left_bottom = (face_location[3],face_location[2])
            #right_bottom = (face_location[1],face_location[2] + 25)
            #cv2.rectangle(image,left_bottom,right_bottom,color,cv2.FILLED)
            #cv2.putText(image,match,(face_location[3] + 5,face_location[2] + 19),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
        
        cv2.imshow("detected",image)

        if cv2.waitKey(1) == 27:
            print("Close handle")
            break


def main():
    detect_person_in_video(cap_ip="http://000.000.000.000:00/stream",db_encode="db_pickle",name="mirana")


if __name__ == '__main__':
    main()


