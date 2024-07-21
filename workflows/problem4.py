def even_squares(lst):
    """Generate a list of squares of even numbers from the original list."""
    return [x**2 for x in lst if x % 2 == 0]

def extract_sublist(lst, start, end):
    """Extract a sublist from the original list using the given start and end indices."""
    return lst[start:end+1]

def main():
    # Example input
    lst = [7, 8, 9, 10, 1, 5, 6, 7]

    # Generate a list of squares of even numbers
    even_squares_list = even_squares(lst)
    print("List of squares of even numbers:", even_squares_list)

    # Example indices for slicing
    start_index = 2
    end_index = 5

    # Extract a sublist from the original list
    sublist = extract_sublist(lst, start_index, end_index)
    print("Extracted sublist:", sublist)

if __name__ == "_main_":
    main()