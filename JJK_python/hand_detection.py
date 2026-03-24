import mediapipe as mp

class hand_det:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
    def detection(self, final):
        result = self.hands.process(final)
        if result.multi_hand_landmarks is None:
            return []
        landmarks =[]
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    final,
                    handLms,
                    self.mp_hands.HAND_CONNECTIONS
                )

                for lm in handLms.landmark:
                    landmarks.append((lm.x, lm.y, lm.z))
        return landmarks    
