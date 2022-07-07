# e-book-analysis-and-representation
## E-BOOK ANALYSIS AND REPRESENTATION

Written in a single script, this Python program downloads one of the e-books from `Wikibooks` or `Wikisource` sites and saves it as a txt file.

For this, `BeautifulSoap` library is used to get the desired books.

After saving the e-book correctly in a text file, the program reads it again and generates the word frequencies of that book. (That is, it counts the number of times words occur in the book.) 

During this process, **Stop words** and **Punctuation marks** are **removed**.

The extracted words are wrote to **a second txt file**.

- The number of the book is taking as user input.
- The name of the book is taking as user input.
- The user can choose the number of word frequencies.
- If the frequency number is not entered, 20 is taken as the default value.
- If the user selected only one e-book, 
  - **FREQUENCY** table is printed on the screen and the program ends

BOOK 1: xxxx
| NO | WORD | FREQ_1|
| ---- | ---- | ---- |
| 1 | print | 521 |

- However, if the user selected two e-books, the output should be similar to the table given below:
  - **COMMON WORDS** table with each book's words.
  - **DISTINCT WORDS** table for each book.
  
BOOK 1: xxxx

BOOK 2: yyyy

COMMON WORDS
| NO | WORD | FREQ_1| FREQ_2| FREQ_SUM|
| ---- | ---- | ---- | ---- | ---- |
| 1 | print | 521 | 545 | 1066 |


  
BOOK 1: xxxx

DISTINCT WORDS
| NO | WORD | FREQ_1|
| ---- | ---- | ---- |
| 1 | raw | 66 |

BOOK 2: yyyy

DISTINCT WORDS
| NO | WORD | FREQ_2|
| ---- | ---- | ---- |
| 1 | path | 11 |
