class Solution:
    def quickSort(self, arr: list) -> list:
        """ 
        Time Complexity: Average: O(n*logn) 
        Space Complexity: O(logn)
        Divide and Conquer Algorithm
        """
        
        if len(arr) <= 1:
            return arr
        pivotIndex = len(arr)//2
        pivot = arr[pivotIndex]
        
        arr[pivotIndex] = arr[0]
        arr[0] = pivot
        smallIndex = 0
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                smallIndex += 1
                temp = arr[i]
                arr[i] = arr[smallIndex]
                arr[smallIndex] = temp

        arr[0] = arr[smallIndex]
        arr[smallIndex] = pivot
    
        return self.quickSort(arr[0:smallIndex]) + [arr[smallIndex]] + self.quickSort(arr[smallIndex+1:])

    def mergeSort(self, arr: list) -> list:
        """
        Time Complexity: Average: O(n*logn) 
        Space Complexity: O(n)
        Divide and Conquer Algorithm
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            arr1 = arr[:mid]
            arr2 = arr[mid:]

            self.mergeSort(arr1)
            self.mergeSort(arr2)
            idx1 = 0
            idx2 = 0
            idx3 = 0
            while (idx1 < len(arr1) and idx2 < len(arr2)):
                if arr1[idx1] < arr2[idx2]:
                    arr[idx3] = arr1[idx1]
                    idx1 += 1
                else:
                    arr[idx3] = arr2[idx2]
                    idx2 += 1
                idx3 += 1
            while idx1 < len(arr1):
                arr[idx3] = arr1[idx1]
                idx1 += 1
                idx3 += 1
            while idx2 < len(arr2):
                arr[idx3] = arr2[idx2]
                idx2 += 1
                idx3 += 1

def main():
    a = [1, 4, 5, 2, 3, 4, 5, 8, 7, 2, 1, 3, 3, 4, 88, 34, 12, 5, 12, 938, 32, 34, 12, 12]
    print(f"\nArray to sort: {a}\n")
    sol = Solution() 

    # quickSortRes = sol.quickSort(arr = a.copy())
    # print(f"\nArray sorted with quicksort: {quickSortRes}\n")

    mergeSortArrCopy = a.copy()
    sol.mergeSort(arr = mergeSortArrCopy)
    print(f"\nArray sorted with mergesort: {mergeSortArrCopy}\n")



if __name__ == "__main__":
    main()