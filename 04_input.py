prompt ="""
1.Add
2.Del
3.List
4.Quit

Enter number:
"""


number = 0
list_book = []

def print_list_book(list_book):
    if len(list_book) <= 0:
        print("책 없음")
        return

    for book in sorted(list_book):
        print(book)

def del_book(book):
    list_book.remove(book)

def add_book(book):
    list_book.append(book)


while number!=4:
    print(prompt)
    number = int(input())
    if number==1:
        print("추가할 책 이름:")
        add_book(input())
    elif number==2:
        print("삭제할 책 이름:")
        del_book(input())
    elif number==3:
        print("책 목록")
        print_list_book(list_book)


