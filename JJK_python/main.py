import cv2

from camera import Camera
from hand_detection import hand_det
from gesture import Technique
from landmark import landmark_processor
from ability import render

def main():
    cam = Camera()
    hand = hand_det()
    land = landmark_processor()
    rend = render()
    rct = Technique()

    while True :
        frame = cam.frame_capture()
        if frame is None:
            break
        landmarks = hand.detection(frame)
        if not landmarks:
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) == 27:
                break
            continue

        lp = land.process(landmarks)
        
        domain = rct.gest(lp)
        simple_domain = rct.symbol(domain)
        if simple_domain is "blue":
            fingertip = lp.get("wrist")
        else:
            fingertip = lp.get("index_tip")
        if simple_domain:
            jujutsu = rend.activation(simple_domain)
        
        ce = rend.persistent(fingertip, frame.shape)
        rend.deactivation(frame)

        if cv2.waitKey(1) == 27:
           rend.clear()
           break
        #if simple_domain:
        
         #   print(simple_domain)
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == 27:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
