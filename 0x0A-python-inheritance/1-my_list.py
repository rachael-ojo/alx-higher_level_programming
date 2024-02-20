#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 2, 5])
    print("Original list:", my_list)

    print("Sorted list:")
    my_list.print_sorted()
