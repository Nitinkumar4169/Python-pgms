#90.Wap to count unique elements in a list using set
lst = list(map(int, input("Enter the elements: ").split()))
unique_elements = set(lst)
print("The unique elements in a set is: ", len(unique_elements))
