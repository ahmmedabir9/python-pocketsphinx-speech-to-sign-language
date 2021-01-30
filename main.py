from pocketsphinx import LiveSpeech
import cv2
import numpy as np

hmm = "Bangla/bangla"
lm = "Bangla/bangla.lm"
dic = "Bangla/bangla.dic"

recognizer = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=hmm,
    lm=lm,
    dic=dic,
)


for phrase in recognizer:
    print(phrase)
    cap = cv2.VideoCapture("Videos/" + str(phrase))
    if cap.isOpened() == False:
        print("Error opening video stream or file")

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:

            cv2.imshow("Frame", frame)

            if cv2.waitKey(25) & 0xFF == ord("q"):

                break

        else:

            break

    cap.release()
