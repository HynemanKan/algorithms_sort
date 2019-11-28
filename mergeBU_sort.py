from sort_base_class import *


class MergeSort(SortBaseClass):
    aux = []

    def sort(self, a: list):
        N = len(a)
        self.aux = a.copy()
        sz = 1
        while sz < N:
            lo = 0
            while lo < N-sz:
                self.merge(a, lo, lo+sz-1, min(lo+sz+sz-1, N-1))
                lo += sz+sz
            sz = sz+sz

    def merge(self, a: list, lo: int, mid: int, hi: int):
        i = lo
        j = mid+1
        self.aux = a.copy()
        for k in range(lo, hi+1):
            self.exchangetimes += 1
            self.looptimes +=1
            if i>mid:
                a[k] = self.aux[j]
                if self.img:
                    self.image_show_after_merge(a, lo, hi, k, j)
                j += 1
            elif j>hi:
                a[k] = self.aux[i]
                if self.img:
                    self.image_show_after_merge(a, lo, hi, k, i)
                i += 1
            elif self.less(self.aux[j],self.aux[i]):
                a[k] = self.aux[j]
                if self.img:
                    self.image_show_after_merge(a, lo, hi, k, j)
                j += 1
            else:
                a[k] = self.aux[i]
                if self.img:
                    self.image_show_after_merge(a, lo, hi, k, i)
                i += 1

    def image_show_after_merge(self, a: list, lo: int, hi: int, k: int, i: int):
        aux = self.aux
        a_max = max(a)
        a_size = len(a)
        image_size = (int(edge * 3 + line_hight_max*2),
                      int(edge * 2 + a_size * line_width + (a_size - 1) * line_space),
                      3)
        img = np.zeros(image_size, dtype=np.uint8)
        for now in range(a_size):
            now_hight = int(line_hight_max*(a[now]/a_max))
            bl_point = (int(edge+now*(line_width+line_space)),
                        edge)
            tr_point = (int(edge+now*(line_width+line_space)+line_width),
                        int(edge+now_hight))
            cv2.rectangle(img,bl_point,tr_point,normal_color,-1)
            now_hight = int(line_hight_max * (aux[now] / a_max))
            bl_point = (int(edge + now * (line_width + line_space)),
                        int(edge*2+line_hight_max))
            tr_point = (int(edge + now * (line_width + line_space) + line_width),
                        int(edge*2+ line_hight_max + now_hight))
            cv2.rectangle(img, bl_point, tr_point, normal_color, -1)
        now_hight = int(line_hight_max * (a[k] / a_max))
        bl_point = (int(edge + k * (line_width + line_space)),
                    edge)
        tr_point = (int(edge + k * (line_width + line_space) + line_width),
                    int(edge + now_hight))
        cv2.rectangle(img, bl_point, tr_point, exch_color, -1)
        now_hight = int(line_hight_max * (aux[i] / a_max))
        bl_point = (int(edge + i * (line_width + line_space)),
                    int(edge * 2 + line_hight_max))
        tr_point = (int(edge + i * (line_width + line_space) + line_width),
                    int(edge * 2 + line_hight_max + now_hight))
        cv2.rectangle(img, bl_point, tr_point, exch_color, -1)
        active_area_bl_point = (int(edge + lo * (line_width + line_space)-line_space//2),
                                int(edge - line_space//2))
        active_area_tr_point = (int(edge + hi * (line_width + line_space) + line_width+line_space//2),
                                int((edge + line_hight_max)*2+line_space//2))
        cv2.rectangle(img, active_area_bl_point, active_area_tr_point, exch_color,thickness=2)
        cv2.imwrite(f"img\\{self.exchangetimes}.jpg",img)


if __name__ == '__main__':
    test_size = 10
    with open(f"test_{test_size}.txt","r",encoding="utf-8") as file:
        a = []
        for line in file.readlines():
            a.append(int(line))
        test = MergeSort(img=True)
        test.sort(a)
        res = test.isSorted(a)
        print("mergeBU sort")
        print(f"test data:{test_size}\nres:{res}\nloop times:{test.looptimes}\nexchange times:{test.exchangetimes}")
