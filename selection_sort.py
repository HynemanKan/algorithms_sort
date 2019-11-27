from .sort_base_class import SortBaseClass


class SelectionSort(SortBaseClass):
    def sort(self, a: list):
        N = len(a)
        for i in range(N):
            min = i
            for j in range(i+1,N):
                self.looptimes +=1
                if self.less(a[j],a[min]):
                    min = j
            self.exch(a,i,min)
        return a

if __name__ == '__main__':
    test_size = 10
    with open(f"test_{test_size}.txt", "r", encoding="utf-8") as file:
        a = []
        for line in file.readlines():
            a.append(int(line))
        test = SelectionSort(img=True)
        test.sort(a)
        res = test.isSorted(a)
        print("selection sort")
        print(f"test data:{test_size}\nres:{res}\nloop times:{test.looptimes}\nexchange times:{test.exchangetimes}")
