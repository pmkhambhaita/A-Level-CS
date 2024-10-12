import cv2
import mediapipe as mp

# Initialize MediaPipe hands solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Define gesture thresholds
pinch_in_threshold = 0.5
pinch_out_threshold = 1.0  # Adjust this threshold as needed
swipe_threshold = 50


# Define camera control functions
def zoom(direction):
    # Implement zoom logic (e.g., adjust camera zoom level)
    print(f"Zooming {direction}")


def pan(direction):
    # Implement pan logic (e.g., adjust camera pan angle)
    print(f"Panning {direction}")


while True:
    ret, frame = cap.read()

    # Convert BGR to RGB for MediaPipe
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe
    results = hands.process(image)

    # Draw hand landmarks and annotations
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract relevant landmarks for gesture detection
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate distance between thumb and index tips
            distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

            if distance < pinch_in_threshold:
                zoom("in")
            elif distance > pinch_out_threshold:
                zoom("out")

            # Detect swipe gesture (e.g., based on x-axis movement)
            if abs(thumb_tip.x - index_tip.x) > swipe_threshold:
                if thumb_tip.x > index_tip.x:
                    pan("left")  # Adjust pan angle accordingly
                else:
                    pan("right")  # Adjust pan angle accordingly

    # Display the processed image
    cv2.imshow('Frame', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
