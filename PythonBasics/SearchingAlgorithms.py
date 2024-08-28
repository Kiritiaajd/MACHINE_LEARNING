class Searching:
    @staticmethod
    def BinarySearchAlgo(arr, target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    @staticmethod
    def exponential_Search(arr, target):
        if len(arr) == 0:
            return -1

        bound = 1
        while bound < len(arr) and arr[bound] < target:
            print(f"Exponential search, current bound is {bound} with value {arr[bound]}.")
            bound *= 2

        # Perform binary search between the last valid bound and current bound
        start = bound // 2
        end = min(bound, len(arr) - 1)
        print(f"Binary search between index {start} and {end}.")

        return Searching.BinarySearchAlgo(arr[start:end + 1], target)


    def interpolation_search(arr , target ):
        


def main():
    print("Searching Algorithm")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input("Enter the target Element: "))
    result = Searching.BinarySearchAlgo(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")

    # Testing the exponential search method
    result = Searching.exponential_Search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")


if __name__ == "__main__":
    main()
