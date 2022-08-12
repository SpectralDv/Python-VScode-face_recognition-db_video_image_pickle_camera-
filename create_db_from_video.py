
import os
import pickle
import sys
import face_recognition
import cv2


def take_screenshot_from_video(input_video,output_img,delay,count):
    count = count
    cap = cv2.VideoCapture(input_video)
    if not os.path.exists(output_img):
        os.mkdir(output_img)
    while True:
        ret, frame = cap.read()
        fps = cap.get(cv2.CAP_PROP_FPS)
        multiplier = fps * 1
        #print(fps)

        if ret:
            frame_id = int(round(cap.get(1))) 
            #print(frame_id)
            cv2.imshow("frame",frame)
            k = cv2.waitKey(delay)
            if frame_id % multiplier == 0: 
                cv2.imwrite(f"{output_img}/screen{count}.jpg",frame)
                print(f"Successful save screensot, {count}")
                count+=1
            if k == ord(" "):
                count+=1
                cv2.imwrite(f"{output_img}/screen{count}.jpg",frame) 
                print(f"Successful save screensot, {count}")
                count+=1
            if cv2.waitKey(1) == 27:
            #elif k == ord("q"):
                print(f"Close handle")
                break
        else:
            print("Error or close video") 
            break
    cap.release()
    cv2.destroyAllWindows()
    return count



def main():
    count = 0
    i = 0
    countVideo = 1
    for i in range(countVideo): 
        #count = take_screenshot_from_video(input_video="video/res"+str(i)+".avi",output_img="db_from_video",delay=10,count=count)
        count = take_screenshot_from_video(input_video="video/tony.mp4",output_img="db_from_video",delay=10,count=count)


if __name__ == '__main__':
    main()
