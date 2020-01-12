############################################################
# introdution   receive picture from network, and show it
#
#
#
############################################################

import cv2
import zmq
import base64
import numpy as np


################
# main
################
if __name__ == "__main__":
    context = zmq.Context()
    footage_socket = context.socket(zmq.PAIR)
    footage_socket.bind('tcp://*:5555')

    print(">>> receiving !!!")
    while(True):
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        npImg = np.frombuffer(img, dtype=np.uint8)
        source = cv2.imdecode(npImg, 1)
        cv2.imshow("Stream", source)
        
        if cv2.waitKey(1) == ord('q'):
            break




