class Technique:
    def gest(self, landmarks):
        
        if landmarks is None:
            return None
        finger = []
        tips = [landmarks["index_tip"], landmarks["middle_tip"], landmarks["ring_tip"], landmarks["pinky_tip"]]
        joints = [landmarks["index_j"], landmarks["middle_j"], landmarks["ring_j"], landmarks["pinky_j"]]
        for tip, joint in zip(tips, joints):
            if tip[1] < joint[1]:
                finger.append(1)
            else:
                finger.append(0)
        fing = tuple(finger)
        return fing
    def symbol(self, fing):
        ct = {(1, 0, 0, 0):"Red",(1,1,0,0):"purple",(1,1,1,1):"blue"}
        if fing in ct:  
            return ct.get(fing)
        else:
            return None

