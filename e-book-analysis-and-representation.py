import requests                       #libraries for read the book from web site.
from bs4 import BeautifulSoup
import operator                       #library for the sorting.
def Create_Books(bookname,x):         # x = count of book
    Book_Name_link = bookname.replace(" ", "_")           #I replaced the book name for creating Url
    Book_Name_link = Book_Name_link.replace("'", "%27")
    All_of_words = []
    if x == 1:                       # x == 1 for first book
        Url = "https://en.wikibooks.org/wiki/"        #the constant part of the URL.
        Printable_Version = "/Print_version"          #the last generally last part of the URL
        r = requests.get(Url + Book_Name_link + Printable_Version)   #Request library allows me to request information from Http
        if r.status_code == 404:                           #I used this method to avoid getting an error because the status code of some books is different.
            Printable_Version = "/print_version"
            r = requests.get(Url + Book_Name_link + Printable_Version)       
        soup = BeautifulSoup(r.content, "html.parser")          #Beautiful Soap library allows me to easily process the Html file 
                                                                #and split the codes to get the information I want.
        Book_text = open("First_book.txt", "w",encoding='utf-8')            #First_book.txt is opened to write the entire book
        Book_text1 = open("First_book_words.txt", "w", encoding='utf-8')    #First_book_words.txt is opened to write the words of the book
        for word in soup.find_all("div",{"class":"mw-parser-output"}):      #I chose ("div",{"class":"mw-parser-output"}) section because I wanted to get a more specific section to read the book.
            content = word.text                                              
            Book_text.write(content)               #I write the book I read to the file as text with the help of the loop
            Full_words = content.lower().split()   #Full_words has all words with lowercase letters.
            for w in Full_words:                   
                Book_text1.write(w+"\n")           #I write the words line by line to other file
        Book_text.close()
        Book_text1.close()

        Book_text11 = open("First_book_words.txt", "r", encoding='utf-8')       #I added (encoding='utf-8') part to my code To avoid getting encode error
        All_of_words = Book_text11.readlines()       #Since I write the words line by line, I am reading them with readlines ().                
        Book_text11.close()       
                       
        All_of_words = Delete_Punctuation(All_of_words)         #Calling the Delete_Punctuation function for create the lists without the punctuations and symbols.
        All_of_words = Delete_Words(All_of_words)               #Calling the Delete_Words function for create the lists without the stop words and punctuations and symbols.
    
    elif x == 2:                                                               # x == 2 for second book 
        Url = "https://en.wikibooks.org/wiki/"                                 #This section is the same as for the first book.
        Printable_Version = "/Print_version"          
        r = requests.get(Url + Book_Name_link + Printable_Version)
        if r.status_code == 404:
            Printable_Version = "/print_version"                               #the only difference is that the opened files are separate and, 
            r = requests.get(Url + Book_Name_link + Printable_Version)         #if two books are entered, the data is kept in 4 different files in total.
        soup = BeautifulSoup(r.content, "html.parser")
        
        Book_text = open("Second_book.txt", "w",encoding='utf-8')
        Book_text1 = open("Second_book_words.txt", "w",encoding='utf-8')
        for word in soup.find_all("div",{"class":"mw-parser-output"}):
            content = word.text
            Book_text.write(content)
            Full_words = content.lower().split()
            for w in Full_words:
                Book_text1.write(w+"\n")
        Book_text.close()
        Book_text1.close()

        Book_text11 = open("Second_book_words.txt", "r", encoding='utf-8')
        All_of_words = Book_text11.readlines()
        Book_text11.close()
       
        All_of_words = Delete_Punctuation(All_of_words)
        All_of_words = Delete_Words(All_of_words)
    return  All_of_words
def Delete_Words (allwords):
    Filtered_Words=[]
    Stop_Words= ["etc", "us", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "r",'s',
                 "u", "v", "y", "z", "w", "x", "q", "I", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                 "your", "yours","yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", '>' , '<','←',
                 "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves","what", "which",'↑',
                 "who", "whom", "this", "that", "these", "those", "am", "is", "are","was", "were", "be", "been",'→', 
                 "being", "have", "has", "had", "having", "do", "does", "did","doing", "a", "an", "the", "and", "but",
                 "if", "or", "because", "as", "until", "while", "of","at", "by", "for", "with", "about", "against",
                 "name","value","next","first", "between", "into", "through", "during", "before","after", "above",
                 "below", "to", "from", "up","line", "down", "in", "out", "on", "off", "over", "under","'ll", "'ve", "'re",
                 "again", "further", "then","ing", "once", "here", "there", "when", "where", "why", "how", "all", "any",
                 "both", "each", "few", "more", "most", "other","use", "some", "such", "no", "nor", "not", "only", "own",
                 "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","'m", "'s", "'t", 
                 '—', '=', '==', '\t', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.' , ',' , '!' ,'?','(',')' ,';',
                 '[', ']', '\n' , '"' , ':' , '-', '  ' , '~' , '@' , '^' , '#' , '%' , '$' , '&' , '*' , '_' ,'`' , '{' , '}' , '|']
   
    '''This list contains stop words punctuations and symbols as much as possible. 
    I return in the word lists with loops if it contains any element from the stop words list,
    and replace it with a space. And then I split the resulting empty word into two words and 
    add it to the filtered words list.'''  
    
    words = []
    for word in allwords:
        for stops in Stop_Words:
            if stops == word:                               
                word = word.replace(stops," ").strip()
        words =  word.split()
        if (len(word) > 0):
            Filtered_Words += words
    return Filtered_Words
def Delete_Punctuation(allwords):
    Filtered_Words = []
    words = []
    Punctuation ='!"#$%&()*, -./:;<=>?@[\]^_`{|}~0123456789'+"'"
    
    '''Since I think there may be punctuation marks in some words, 
    I look for the symbols as strings between words. If there is a word in it,
    it replaces it with a space and then adds it to the new list.'''
    
    for word in allwords:
        for punc in Punctuation:
            if punc in word:
                word = word.replace(punc," ").strip()
        words =  word.split()        
        if (len(word) > 0):
            Filtered_Words += words
    return Filtered_Words
def Create_Dictionary(allwords):
    Count_of_word= {}
    
    '''I am turning all this list of words without stop words and symbols into a dictionary.
    If this word is not in the dictionary, it adds it to the dictionary and makes the number 1. 
    But even if it was already added, it increases the already existing amount.'''
    
    for word in allwords:
        if len(word) != 0 :
          if word in Count_of_word:
                word= word.replace(" ","")
                Count_of_word[word] += 1
          else:
                word= word.replace(" ","")
                Count_of_word[word] = 1
    return Count_of_word
allwords = []
Count_of_book=int(input("Please enter the number of book: ")) #The number of the book is taking as user input.

if Count_of_book == 1:                               #If the user selected one book this part will be execute.
    First_Book_Name = input("Please Enter the Book Name : ")   
    The_choose = input("Would You Like to Choose Word Frequencies Count? Please enter Y or N ! ")  #The user can choose the number of word frequencies
    if The_choose == "Y":                                                                         
        Count_of_print_word = int(input("How Many Word Frequencies You Wish To See : "))
    else:
        Count_of_print_word = 20                    #the default count is 20.
    print()    
    print("BOOK 1 : "+ First_Book_Name)             #Printing on the scren the book name.
    print("NO WORD          FREQ_1")

    Allwords = Create_Books(First_Book_Name,1)      #Calling the Create_Books function for create the lists of the entered book's words from web page.
    final_words = Create_Dictionary(Allwords)       #Calling the Create_Dictionary function for create the dictionary with the lists of words.

    Count_of_Finalwords = len(final_words)          #final_words is the dictionary of the words and the Count_of_Finalwords is lenght of this dictionary.
    TheNumOfPrint = 0                               #the number of words printed on the screen
    for key, count in sorted(final_words.items() ,reverse=True, key =operator.itemgetter(1)):  #the loop to print on the screen words with the count of chosen number.
        TheNumOfPrint = TheNumOfPrint + 1                                                      #firstly it sorted the dictionary like from small to large and reverse them.
        if TheNumOfPrint <= Count_of_Finalwords - Count_of_print_word:          #The loop continues until the number of words printed on the screen equals the number of words desired.
            print('{:>2d} {:<12s}{:>5d}'.format(TheNumOfPrint,key,count))       #The table image is obtained using the format() method
            if (TheNumOfPrint == Count_of_print_word):                                  
                break
            
elif Count_of_book == 2:                             #If the user selected two book this part will be execute.
    First_Book_Name = input("Please Enter the Book Name : ")
    Second_Book_Name = input("Please Enter the Book Name : ")
    The_choose = input("Would You Like to Choose Word Frequencies Count? Please enter Y or N ! ")     #The user can choose the number of word frequencies
    if The_choose == "Y":
        Count_of_print_word = int(input("How Many Word Frequencies You Wish To See : "))
    else:
        Count_of_print_word = 20                  #the default count is 20.
        
    print()    
    print("BOOK 1 : "+ First_Book_Name)          #Printing on the scren the books name.
    print("BOOK 2 : " + Second_Book_Name)
    print("COMMON WORDS")
    print("NO WORD           FREQ_1 FREQ_2 FREQ_SUM")

    FirstBook_Allwords =  Create_Books(First_Book_Name,1)          #Calling the Create_Books functions for create the lists of the entered books's words from web page.
    SecondBook_Allwords = Create_Books(Second_Book_Name,2)

    final_words_first = Create_Dictionary(FirstBook_Allwords)      #Calling the Create_Dictionary functions for create the dictionary with the lists of words.
    final_words_second = Create_Dictionary(SecondBook_Allwords)

    Mostly_Common_words = {}                                      #This dictionary for the common words between the first and the second books
    for key1, count1 in sorted( final_words_first.items(), reverse=True, key=operator.itemgetter(1)):    #The first loop turns between the words of the first book
        for key2 , count2 in sorted(final_words_second.items(), reverse=True, key=operator.itemgetter(1)): #The second loop turns between the words of the second book
            if key1 == key2:                                       #If the two words is equal, I added this word to the Mostly_Common_words dictionary.
                if key1 in Mostly_Common_words:
                    Mostly_Common_words[key1] += (count1 + count2)
                else:
                    Mostly_Common_words[key1] = (count1 + count2)

    Count_of_Finalwords = len(Mostly_Common_words)                   #the Count_of_Finalwords is lenght of Mostly_Common_words.
    TheNumOfPrint = 0                                                #the number of words printed on the screen
    for key1,count1 in  sorted( Mostly_Common_words.items(), reverse=True, key=operator.itemgetter(1)):   #the loop to print on the screen words with the count of chosen number.
        TheNumOfPrint = TheNumOfPrint + 1                                                                #firstly it sorted the dictionary like from small to large and reverse them.
        if TheNumOfPrint <= Count_of_Finalwords - Count_of_print_word:                                  #The loop continues until the number of words printed on the screen equals the number of words desired
            print('{:>2d} {:<12s}  {:>5d}  {:>5d}  {:>5d}'.format(TheNumOfPrint,key1,final_words_first[key1],final_words_second[key1],count1))
            if(TheNumOfPrint == Count_of_print_word):                            #The table image is obtained using the format() method
                break
    print()    
    print("BOOK 1 : "+ First_Book_Name)          #Printing on the scren the book name.
    print("DISTINCT WORDS")
    print("NO WORD           FREQ_1")

    for key1, count1 in sorted( final_words_first.items(), reverse=True, key=operator.itemgetter(1)):      
        for key2 , count2 in sorted(final_words_second.items(), reverse=True, key=operator.itemgetter(1)):
            if key1 == key2:
                if key1 in Mostly_Common_words:
                    if key1 in final_words_first :
                        del final_words_first[key1]        #I delete common words from both books' dictionaries to find the distinct words for each books
                    if key2 in final_words_second:
                        del final_words_second[key2]
                          
    TheNumOfPrint = 0
    for key, count in sorted(final_words_first.items() ,reverse=True, key =operator.itemgetter(1)):   
        TheNumOfPrint = TheNumOfPrint + 1                                       #As I explained above, I print the distinct words of the first book on the screen with the same method.
        if TheNumOfPrint <= Count_of_Finalwords - Count_of_print_word:
            print('{:>2d} {:<12s}{:>5d}'.format(TheNumOfPrint,key,count))
            if (TheNumOfPrint == Count_of_print_word):
                break
    print()          
    print("BOOK 2 : "+ Second_Book_Name)                 #Printing on the scren the book name.
    print("DISTINCT WORDS")
    print("NO WORD           FREQ_1")

    TheNumOfPrint = 0
    for key, count in sorted(final_words_second.items() ,reverse=True, key =operator.itemgetter(1)):
        TheNumOfPrint = TheNumOfPrint + 1                                            # #As I explained above, I print the distinct words of the first book on the screen with the same method.
        if TheNumOfPrint <= Count_of_Finalwords - Count_of_print_word:
            print('{:>2d} {:<12s}{:>5d}'.format(TheNumOfPrint,key,count))
            if (TheNumOfPrint == Count_of_print_word):
                break