############################################################
# introdution   get picture from camera, and send it out
#
#
#
############################################################

import cv2
import zmq
import base64


################
# variables
################
receiveIP = '192.168.3.11'




################
# main
################
if __name__ == "__main__":
    ### get pic
    capture = cv2.VideoCapture(0)

    '''
    while(True):
        ret, frame = capture.read()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    '''

    ### create socket
    context = zmq.Context()
    footage_socket = context.socket(zmq.PAIR)
    #footage_socket.connect('tcp://%s:5555' % (receiveIP))
    footage_socket.connect('tcp://localhost:5555')

    ### encode and send
    print(">>> capturing !!!")
    while(True):
        ret, frame = capture.read()
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)
        #cv2.delay(1)













