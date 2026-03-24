import cv2
class render:
    def __init__(self):
        self.active = None
    def activation(self, symbol):
        colors = {"Red":(0,0,255), "purple":(255,0,255), "blue":(255,0,0)}
        if symbol not in colors:
            return None
        self.active = {"color": colors[symbol], "radius":30, "x":0, "y":0}
        return self.active
    
    def persistent(self, fingertip, frame_shape):
        if self.active is None:
            return None
        h,w,_ = frame_shape
        x = int(fingertip[0]*w)
        y = int(fingertip[1]*h)
        self.active["x"] = x
        self.active["y"] = y
        return self.active["x"], self.active["y"]
        
    def deactivation(self, final):
        if self.active["color"] == (255,0,0):
            y = self.active["y"] - 70
            x = self.active["x"] 
        elif self.active["color"] == (255,0,255) or self.active["color"] == (0,0,255):
            x = self.active["x"] 
            y = self.active["y"] - 50
        else:
            y = 0       
            x = 0 
        radius = self.active["radius"]
        color = self.active["color"]
        cv2.circle(final, (x,y), radius, color, -1)
    
    def clear(self):
        self.active = None