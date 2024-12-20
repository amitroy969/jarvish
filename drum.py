import cv2
import pygame
import math
from cvzone.HandTrackingModule import HandDetector

# Function to initialize and run the virtual instrument game
def drums(screen_width=1280, screen_height=720):
    # Initialize pygame mixer for sounds
    pygame.init()
    pygame.mixer.init()

    # Load sound files
    drum_sounds = [pygame.mixer.Sound(f"sound/drum{i+1}.wav") for i in range(5)]
    piano_sounds = [pygame.mixer.Sound(f"sound/piano{i+1}.wav") for i in range(10)]
    guitar_sounds = [pygame.mixer.Sound(f"sound/guitar{i+1}.wav") for i in range(5)]
    extra_sounds = [pygame.mixer.Sound(f"sound/extra{i+1}.wav") for i in range(3)]  # Ensure there are 3 extra sounds
    boom_sounds = [pygame.mixer.Sound(f"sound/boom{i+1}.wav") for i in range(10)]

    # Screen dimensions
    center_x, center_y = screen_width // 2, screen_height // 2  # Center of the screen

    # Button radius and spacing
    button_radius = 50  # Increased radius for bigger buttons
    vertical_spacing = 100  # Increased vertical spacing between layers
    horizontal_spacing = 70  # Increased horizontal spacing for buttons

    # Initialize Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Generate positions for buttons
    button_positions = []

    # Total buttons
    total_buttons = 30

    # Rainbow shape arc (creating multiple layers)
    arc_radius = 300
    angle_step = 180 / (total_buttons // 2)  # Divide 180 degrees into equal parts

    # Generate positions for buttons in an arc
    for i in range(total_buttons):
        angle = math.radians(i * angle_step - 90)  # Creating a semi-circle
        x = int(center_x + arc_radius * math.cos(angle))
        y = int(center_y + arc_radius * math.sin(angle))

        # Adjust vertical spacing for layers
        y_offset = (i // 10) * vertical_spacing  # Adjust the height of each layer

        button_positions.append((x, y + y_offset, button_radius))

    # Initialize the button states (clicked or not)
    clicked_buttons = {i: False for i in range(len(button_positions))}

    # Function to draw buttons
    def draw_button(img, x, y, r, text, color, clicked=False):
        cv2.circle(img, (x, y), r, (0, 0, 0), -1)  # Outer black circle
        cv2.circle(img, (x, y), int(r * 0.8), color, -1)  # Inner color
        if clicked:
            cv2.circle(img, (x, y), r + 10, (255, 255, 255), 2)
        cv2.putText(img, text, (x - r // 2, y + r // 4), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Play sound based on button type
    def play_sound(index):
        if index < 10:
            boom_sounds[index].play()
        elif index < 20:
            piano_sounds[index - 10].play()
        elif index < 25:
            drum_sounds[index - 20].play()
        elif index < 30:
            guitar_sounds[index - 25].play()
        elif index < 33:
            extra_sounds[index - 30].play()

    # Function to check if point is inside the button's area
    def is_in_circle(x, y, circle):
        cx, cy, r = circle
        return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

    # Main loop
    cap = cv2.VideoCapture(0)
    cap.set(3, screen_width)  # Set width
    cap.set(4, screen_height)  # Set height

    while True:
        success, img = cap.read()
        if not success:
            break

        # Detect hands
        hands, img = detector.findHands(img, flipType=False)

        # Draw all buttons
        for idx, (x, y, r) in enumerate(button_positions):
            # Color assignment based on button types
            if idx < 10:
                color = (0, 255, 0)  # Boom
                label = f"Boom {idx + 1}"
            elif idx < 20:
                color = (0, 0, 255)  # Piano
                label = f"Piano {idx - 9}"
            elif idx < 25:
                color = (255, 0, 0)  # Drums
                label = f"Drum {idx - 19}"
            elif idx < 40:
                color = (0, 255, 255)  # Guitars
                label = f"Guitar {idx - 24}"
            elif idx < 33:
                color = (255, 255, 0)  # Extra
                label = f"Extra {idx - 29}"

            draw_button(img, x, y, r, label, color, clicked_buttons[idx])

        # Process hand interactions
        if hands:
            for hand in hands:
                lmList = hand["lmList"]  # Landmark list

                # Check for each finger tip
                for finger_tip_idx in [8, 12, 16, 20]:  # Index, middle, ring, pinky
                    x, y = lmList[finger_tip_idx][:2]  # Get tip coordinates

                    # Check interactions with all buttons
                    for i, (button_x, button_y, button_r) in enumerate(button_positions):
                        if is_in_circle(x, y, (button_x, button_y, button_r)):
                            play_sound(i)  # Play the sound corresponding to the button
                            clicked_buttons[i] = True  # Mark button as clicked

        # Display the frame
        cv2.imshow("Virtual Instruments", img)

        # Break on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

# Example usage:
# Call the virtual_instruments_game function to start the game
drums()
