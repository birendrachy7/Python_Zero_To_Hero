#Create a function name book_detail that takes **kwargs
# output: Harry Potter was written by J.K. Rowling
def book_detail(**details):
    title = details.get('title', 'Unknown Title')
    author = details.get('author', 'Unknown Author')
    print(f"{title} was written by {author}")   
# Example usage of the book_detail function
book_detail(title="Harry Potter", author="J.K. Rowling")  
# Output: Harry Potter was written by J.K. Rowling



def book_detail(**detail):
    title = detail['title']
    author = detail['author']
    print(f"{title} was written by {author}")   


book_detail(title="Harry Potter", author="J.K. Rowling")