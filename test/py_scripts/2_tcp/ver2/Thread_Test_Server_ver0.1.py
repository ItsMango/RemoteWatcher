################################################### 
#
#
# for using Server_Thread_test_module1_ver01.py
# and Server_Thread_test_module1_ver02.py
###################################################

import cls_thread_server_1
import cls_thread_server_2
import time


if __name__ == "__main__":
    server_module_write = cls_thread_server_1.ClsServerThread(6060)
    #server_module_read = cls_thread_server_2.ClsServerThread(6061)

    server_module_write.start()
    #server_module_read.start()

    print("Press Q to exit...")
    while input() != 'Q':
        pass    

    server_module_write.stopServerThread()
    #server_module_read.stopServerThread()
    time.sleep(2)
    print(">>> is ServerMoudleWrite alive? {}".format(server_module_write.is_alive()))
    #print(">>> is ServerModuleRead alive? {}".format(server_module_read.is_alive()))
    print("!!! 退出主线 !!!")




