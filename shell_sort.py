from sort_base_class import SortBaseClass


class ShellSort(SortBaseClass):
    def sort(self, a: list):
        N = len(a)
        h = 1
        while h < N/3:
            h = 3*h+1
        while h>=1:
            for i in range(h,N):
                j =i
                while j>=h and self.less(a[j],a[j-h]):
                    self.exch(a, j ,j-h)
                    self.looptimes += 1
                    j -= h
            h = h//3

if __name__ == '__main__':
    test_size = 10
    with open(f"test_{test_size}.txt", "r", encoding="utf-8") as file:
        a = []
        for line in file.readlines():
            a.append(int(line))
        test = ShellSort(img=True)
        test.sort(a)
        res = test.isSorted(a)
        print("shell sort")
        print(f"test data:{test_size}\nres:{res}\nloop times:{test.looptimes}\nexchange times:{test.exchangetimes}")
