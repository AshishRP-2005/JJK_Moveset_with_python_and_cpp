import cv2
class Camera:
    def __init__(self, cam_index=0):
        self.cam_index = cam_index
        self.cam = cv2.VideoCapture(self.cam_index)

    def frame_capture(self):
        while True:
            success, frame = self.cam.read()
            if not success:
                print("Video Failure")
                break
            final = cv2.flip(frame, 1)
            return final

            if cv2.waitKey(1) == 27:  
                break
    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()