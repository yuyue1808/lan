     # _*_ coding:utf-8 _*_
# Filename:GUIClient.py
# Python��������ͻ���

import tkinter
#import tkFont
import tkinter.font
import socket
import threading
import time
import sys

class ClientUI():
    
    title = 'Python��������-�ͻ���V1.0'
    #local = '127.0.0.1'
    local = socket.gethostname()
    port = 8808
    global clientSock;
    flag = False

             #��ʼ�����������ԣ�������Java�Ĺ��췽��
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(self.title)
        
        #�������,��4����岼��
        self.frame = [tkinter.Frame(),tkinter.Frame(),tkinter.Frame(),tkinter.Frame()]

        #��ʾ��ϢText�ұߵĹ�����
        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        
        #��ʾ��ϢText����������Ĺ�����
        ft = tkinter.font.Font(family='Fixdsys',size=11)
        self.chatText = tkinter.Listbox(self.frame[0],width=70,height=18,font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1,fill=tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[0].pack(expand=1,fill=tkinter.BOTH)
        
        #��ǩ���ֿ���Ϣ��ʾText����Ϣ����Text
        label = tkinter.Label(self.frame[1],height=2)
        label.pack(fill=tkinter.BOTH)
        self.frame[1].pack(expand=1,fill=tkinter.BOTH)

              #������ϢText�Ĺ�����
        self.inputTextScrollBar = tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        
        #������ϢText�������������
        ft = tkinter.font.Font(family='Fixdsys',size=11)
        self.inputText = tkinter.Text(self.frame[2],width=70,height=8,font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1,fill=tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1,fill=tkinter.BOTH)
        
        #������Ϣ��ť
        self.sendButton=tkinter.Button(self.frame[3],text=' �� �� ',width=10,command=self.sendMessage)#������Ͱ�ť������sendMessage����
        self.sendButton.pack(expand=1,side=tkinter.BOTTOM and tkinter.RIGHT,padx=15,pady=8)

        #�رհ�ť
        self.closeButton=tkinter.Button(self.frame[3],text=' �� �� ',width=10,command=self.close)
        self.closeButton.pack(expand=1,side=tkinter.RIGHT,padx=15,pady=8)
        self.frame[3].pack(expand=1,fill=tkinter.BOTH)
      #������Ϣ
    def receiveMessage(self):
        try:
            #����Socket����
            self.clientSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.clientSock.connect((self.local, self.port))
            self.flag = True
        except:
            self.flag = False
            self.chatText.insert(tkinter.END,'����δ��������˽������ӣ�������������Ƿ��Ѿ�����')
            return
            
        self.buffer = 1024
        self.clientSock.send('Y'.encode())
        while True:
            try:
                if self.flag == True:
                    #���ӽ��������շ���������Ϣ
                    self.serverMsg = self.clientSock.recv(self.buffer).decode()
      if self.serverMsg == 'Y':
                        self.chatText.insert(tkinter.END,'�ͻ����Ѿ���������˽�������......')
                    elif self.serverMsg == 'N':
                        self.chatText.insert(tkinter.END,'�ͻ�����������˽�������ʧ��......')
                    elif not self.serverMsg:
                        continue
                    else:
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        self.chatText.insert(tkinter.END, '�������� ' + theTime +' ˵��\n')
                        self.chatText.insert(tkinter.END, '  ' + self.serverMsg)
                else:
                    break
            except EOFError as msg:
                raise msg
                self.clientSock.close()
                break
     #������Ϣ
    def sendMessage(self):
        #�õ��û���Text���������Ϣ
        message = self.inputText.get('1.0',tkinter.END)
        #��ʽ����ǰ��ʱ��
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(tkinter.END, '�ͻ����� ' + theTime +' ˵��\n')
        self.chatText.insert(tkinter.END,'  ' + message + '\n')
        if self.flag == True:
            #����Ϣ���͵���������
            self.clientSock.send(message.encode());
        else:
            #Socket����û�н�������ʾ�û�
            self.chatText.insert(tkinter.END,'����δ��������˽������ӣ����������޷��յ�������Ϣ\n')
        #����û���Text���������Ϣ
        self.inputText.delete(0.0,message.__len__()-1.0)
    
    #�ر���Ϣ���ڲ��˳�
    def close(self):
        sys.exit()

             #�����߳̽��շ������˵���Ϣ
    def startNewThread(self):
        #����һ�����߳������շ������˵���Ϣ
        #thread.start_new_thread(function,args[,kwargs])����ԭ�ͣ�
        #����function�����ǽ�Ҫ���õ��̺߳�����args�Ǵ��ݸ��̺߳����Ĳ������������Ǹ�Ԫ�����ͣ���kwargs�ǿ�ѡ�Ĳ���
        #receiveMessage��������Ҫ�������ʹ�һ����Ԫ��
        #thread.start_new_thread(self.receiveMessage,())
        t=threading.Thread(target=self.receiveMessage,args=())
        t.start()
        
def main():
    client = ClientUI()
    client.startNewThread()
    client.root.mainloop()
    
if __name__=='__main__':
    main()
