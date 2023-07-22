import cv2
img = cv2.imread("solar-system.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)

# Define the text, font, color, and position for each planet
texts = [
    ("Sun", (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Mercury", (100, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Venus", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Earth", (300, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Moon", (340, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Mars", (380  , 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Jupiter", (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Saturn", (700, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Uranus" , (900, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2),
    ("Neptune", (1100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2), 
    # Add other planets in a similar manner
]

# Add text for each planet
for text in texts:
    cv2.putText(img, *text)

# Display the  image again to check positions
cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
