import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import mediapipe as mp
import cv2

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Define colors
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)

def draw_cube():
    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv(WHITE)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

vertices = [
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1),
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

faces = [
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (0, 3, 7, 4),
    (1, 5, 6, 2)
]

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Main loop for rendering
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    _, frame = cv2.VideoCapture(0).read()
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(frame)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Get the landmark positions
            landmarks_x = [lm.x for lm in landmarks.landmark]
            landmarks_y = [lm.y for lm in landmarks.landmark]
            
            # Calculate the average position of fingers
            avg_x = sum(landmarks_x) / len(landmarks_x)
            avg_y = sum(landmarks_y) / len(landmarks_y)
            
            # Move the cube based on hand position
            cube_x = (avg_x - 0.5) * 2.0  # Scale the position
            cube_y = -(avg_y - 0.5) * 2.0  # Scale the position
            glTranslatef(cube_x, cube_y, 0.0)
            
            draw_cube()
            
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
