import cv2
import numpy as np
edge = 20
line_width = 40
line_space = 10
line_hight_max = 200
normal_color = (200,200,200)
exch_color = (255,255,255)

class SortBaseClass:
    exchangetimes = 0
    looptimes=0

    def __init__(self,img=False):
        self.img = img

    def sort(self, a: list):
        pass

    def less(self, v, w):
        return v<w

    def exch(self, a:list, i:int, j:int):
        t = a[i]
        a[i] = a[j]
        a[j] = t
        self.exchangetimes += 1
        if self.img:
            self.image_show_after_exch(a, i, j)

    def show(self, a: list):
        print(" ".join(a))

    def image_show_after_exch(self,a,i,j):
        a_max = max(a)
        a_size = len(a)
        image_size = (int(edge*2+line_hight_max),
                      int(edge*2+a_size*line_width+(a_size-1)*line_space),
                      3)
        img = np.zeros(image_size,dtype=np.uint8)
        for now in range(a_size):
            now_hight = int(line_hight_max*(a[now]/a_max))
            bl_point = (int(edge+now*(line_width+line_space)),
                        edge)
            tr_point = (int(edge+now*(line_width+line_space)+line_width),
                        int(edge+now_hight))
            cv2.rectangle(img,bl_point,tr_point,normal_color,-1)
        #hightlight exch
        now_hight = int(line_hight_max * (a[i] / a_max))
        bl_point = (int(edge + i * (line_width + line_space)),
                    edge)
        tr_point = (int(edge + i * (line_width + line_space) + line_width),
                    int(edge + now_hight))
        cv2.rectangle(img, bl_point, tr_point, exch_color, -1)
        now_hight = int(line_hight_max * (a[j] / a_max))
        bl_point = (int(edge + j * (line_width + line_space)),
                    edge)
        tr_point = (int(edge + j * (line_width + line_space) + line_width),
                    int(edge + now_hight))
        cv2.rectangle(img, bl_point, tr_point, exch_color, -1)
        cv2.imwrite(f"img\\{self.exchangetimes}.jpg",img)

    def isSorted(self, a: list):
        for i in range(1, len(a)):
            if self.less(a[i], a[i-1]):
                return False
        return True
