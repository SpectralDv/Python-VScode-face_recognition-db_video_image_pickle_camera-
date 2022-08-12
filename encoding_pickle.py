
import os
import pickle
import sys
import face_recognition


def train_model_by_img(db_image,db_encode,name):
    if not os.path.exists(db_image):
        print("Dataset no found")
        sys.exit()

    known_encodings = [] #список для хранения кодировок
    images = os.listdir(db_image)

    #print(images)
    for(i,image) in enumerate(images):
        #print(f"[+] processing img {i + 1}/{len(images)}")
        #print(image)

        face_img = face_recognition.load_image_file(f"{db_image}/{image}")
        try:
            face_enc = face_recognition.face_encodings(face_img)[0]
        except:
            print(f"Face not found, {image} been delete")
            os.remove(f"{db_image}/{image}")

        #print(face_enc)

        if len(known_encodings) == 0:
            known_encodings.append(face_enc)
        else:
            for item in range(0,len(known_encodings)):
                result = face_recognition.compare_faces([face_enc],known_encodings[item])
                #print(result)
                if result[0]:
                    known_encodings.append(face_enc)
                    #print("Same person")
                    break
                else:
                    #print("Another person")
                    break

    #print(known_encodings)
    #print(f"Length {len(known_encodings)}")

    data = {
        "name": name,
        "encoding": known_encodings
    }

    with open(f"{db_encode}/{name}_encodings.pickle","wb") as file:
        file.write(pickle.dumps(data))
    return f"[INFO] File {name}_encodings.pickle successfull created"


def main():
    print(train_model_by_img(db_image="db/tony",db_encode="db_pickle",name="tony"))


if __name__ == '__main__':
    main()

