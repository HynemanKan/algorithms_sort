from .sort_base_class import SortBaseClass


class InsertionSort(SortBaseClass):
    def sort(self, a: list):
        N = len(a)
        for i in range(1, N):
            j = i
            while j>0 and self.less(a[j], a[j-1]):
                self.looptimes += 1
                self.exch(a, j, j-1)
                j -= 1

if __name__ == '__main__':
    test_size = 10
    with open(f"test_{test_size}.txt","r",encoding="utf-8") as file:
        a = []
        for line in file.readlines():
            a.append(int(line))
        test = InsertionSort(img=True)
        test.sort(a)
        res = test.isSorted(a)
        print("insertion sort")
        print(f"test data:{test_size}\nres:{res}\nloop times:{test.looptimes}\nexchange times:{test.exchangetimes}")
