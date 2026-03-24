class landmark_processor:
    def process(self, landmarks):
        if landmarks is None:
            return {}
        stat ={}
        stat["wrist"] = landmarks[0]
        stat["thumb_tip"] = landmarks[4]
        stat["index_tip"] = landmarks[8]
        stat["middle_tip"] = landmarks[12]
        stat["ring_tip"] = landmarks[16]
        stat["pinky_tip"] = landmarks[20]
        stat["thumb_j"] = landmarks[3]
        stat["index_j"] = landmarks[6]
        stat["middle_j"] = landmarks[10]
        stat["ring_j"] = landmarks[14]
        stat["pinky_j"] = landmarks[18]
        stat["wrist"] = landmarks[0]

        return stat
    