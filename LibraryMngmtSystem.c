#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct book {
  char name[50];
  char author[50];
  int pages;
  float price;
  int status; 
};


void addBook(struct book *book) {
  printf("Enter book name: ");
  scanf("%s", book->name);

  printf("Enter author name: ");
  scanf("%s", book->author);

  printf("Enter number of pages: ");
  scanf("%d", &book->pages);

  printf("Enter price: ");
  scanf("%f", &book->price);

  book->status = 0; 
}


void listBooks() {
  struct book *book;
  int i;

  for (i = 0; i < 100; i++) {
    book = &book[i];

    if (book->status == 0) {
      printf("Book name: %s\n", book->name);
      printf("Author name: %s\n", book->author);
      printf("Number of pages: %d\n", book->pages);
      printf("Price: %.2f\n", book->price);
    }
  }
}


void borrowBook(char *bookName) {
  struct book *book;
  int i;

  for (i = 0; i < 100; i++) {
    book = &book[i];

    if (strcmp(book->name, bookName) == 0 && book->status == 0) {
      book->status = 1; 
      printf("Book borrowed successfully.\n");
      return;
    }
  }

  printf("Book not found.\n");
}


void returnBook(char *bookName) {
  struct book *book;
  int i;

  for (i = 0; i < 100; i++) {
    book = &book[i];

    if (strcmp(book->name, bookName) == 0 && book->status == 1) {
      book->status = 0; 
      printf("Book returned successfully.\n");
      return;
    }
  }

  printf("Book not found.\n");
}


int main() {
  int choice;

  struct book books[100];

  
  for (int i = 0; i < 100; i++) {
    books[i].status = 0;
  }

  while (1) {
    printf("Welcome to the library management system.\n");
    printf("What would you like to do?\n");
    printf("1. Add book\n");
    printf("2. List books\n");
    printf("3. Borrow book\n");
    printf("4. Return book\n");
    printf("5. Exit\n");

    scanf("%d", &choice);

    switch (choice) {
      case 1:
        addBook(&books[0]);
        break;
      case 2:
        listBooks();
        break;
      case 3:
        printf("Enter book name to borrow: ");
        char bookName[50];
        scanf("%s", bookName);
        borrowBook(bookName);
        break;
      case 4:
        printf("Enter book name to return: ");
        scanf("%s", bookName);
        returnBook(bookName);
        break;
      case 5:
        return 0;
    }
  }
}
