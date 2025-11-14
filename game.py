import cv2
import mediapipe as mp
import pyautogui

# Hand detection setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Camera
cap = cv2.VideoCapture(0)

# Previous X position for movement detection
prev_x = None
movement_threshold = 50  # Pixels to move before triggering left/right

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame horizontally (mirror effect)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get palm base coordinates (landmark 0)
            x = int(hand_landmarks.landmark[0].x * w)

            if prev_x is not None:
                diff_x = x - prev_x

                if abs(diff_x) > movement_threshold:
                    if diff_x > 0:
                        pyautogui.press("right")
                        print("➡️ RIGHT")
                    else:
                        pyautogui.press("left")
                        print("⬅️ LEFT")
                    prev_x = x  # Reset position to avoid multiple triggers
            else:
                prev_x = x

    cv2.imshow("Hand Gesture Subway Surfers", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
