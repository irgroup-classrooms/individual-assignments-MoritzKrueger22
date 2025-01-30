# Regular Expressions

In the following, you will parse information from text-based files with the command line and Unix tools and Python in the next step. Please note that even though the files are provided as structured csv files you are not supposed to simply read out the columns, but you should use regular expressions instead.

## Parsing contact information from the command line

In this directory, you will find a txt-file called `csv/contacts.csv`. Use regular expressions to extract the following information from it.

Remember that you can use different tools like `grep`, `awk`, or `sed` to use regular expressions from the command line. Pipes might also be helpful. 

You can add your command line in- and outputs directly to this README file. Alternatively, you can write a bash script with all commands and commit it to this directory.

1. Extract all email addresses from the text.
``` 
bash
grep -Eo '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' csv/contacts.csv
```
**Output:**
```
rbrown@company.com
dgreen@domain.net
ssilver@university.edu
jane.smith@gmail.com
mjohnson@yahoo.com
lharris@hotmail.com
eblack@webmail.com
cblue@provider.com
john.doe@example.com
alice.white@domain.org
```

2. Extract all phone numbers from the text.
``` 
bash
grep -Eo '\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b' csv/contacts.csv
```
**Output:**
```
555) 321-6789
555) 123-4567
555) 975-8642
555) 987-6543
555) 555-5555
555) 864-9753
555) 246-1357
555) 432-5678
555) 876-5432
555) 531-2468
```
3. Extract all names that start with the letter ‘J’.
``` 
bash
grep -Eo '\bJ[a-zA-Z]+\b' csv/contacts.csv
```
**Output:**
```
Johnson
John
Jane
```
4. Extract all street names that contain the word 'St'.
``` 
bash
grep -Eo '\b[\w\s]+St\b' csv/contacts.csv
```
**Output:**
```
987 Elm St
864 Chestnut St
654 Cedar St
456 Oak St
246 Birch St
123 Main St
135 Walnut St
```
5. Extract all addresses in ‘USA’.
``` bash
grep 'USA' csv/contacts.csv
```
**Output:**
```
Susan Silver, 975 Cypress Ave, Bigcity, USA
Mike Johnson, 789 Pine Rd, Othertown, USA
Alice White, 987 Elm St, Smalltown, USA
David Green, 246 Birch St, Uptown, USA
Chris Blue, 864 Chestnut St, Metropolis, USA
Jane Smith, 456 Oak St, Sometown, USA
Emily Black, 135 Walnut St, Middletown, USA
Linda Harris, 321 Maple Dr, Newcity, USA
John Doe, 123 Main St, Anytown, USA
Robert Brown, 654 Cedar St, Oldtown, USA
```

6. Extract the last names of all people.
``` 
bash
grep -Eo '\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*,' csv/contacts.csv
```
**Output:**
```
Chris Blue,
Mike Johnson,
Cypress Ave,
Birch St,
Metropolis,
Anytown,
Elm St,
Alice White,
Linda Harris,
Robert Brown,
Maple Dr,
Cedar St,
Chestnut St,
Jane Smith,
Smalltown,
Newcity,
Middletown,
Pine Rd,
Walnut St,
Bigcity,
John Doe,
Main St,
Oldtown,
Othertown,
Susan Silver,
Uptown,
David Green,
Sometown,
Emily Black,
Oak St,
```
7. Extract all email domains (part after the @ sign).
``` 
bash
grep -Eo '@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' csv/contacts.csv | sed 's/@//'
```
**Output:**
```
yahoo.com
hotmail.com
domain.net
provider.com
webmail.com
gmail.com
domain.org
university.edu
example.com
company.com
```
8.	Extract all instances of the first name ‘David’ along with their full address (street and city).
``` 
bash
grep 'David' csv/contacts.csv | awk -F',' '{print $2 ", " $3}'
```
**Output:**
```
246 Birch St, Uptown, USA, dgreen@domain.net, (555) 246-1357
```
9.	Find all entries where the phone number ends with ‘7’.
``` 
bash
grep -E '\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?7\b' csv/contacts.csv
```
**Output:**
```
123-4567
246-1357
```
10.	Extract all instances of first names that end with the letter 'e'.
``` 
bash
grep -Eo '\b[A-Z][a-z]*e\b' csv/contacts.csv
``` 
**Output:**
```
Blue
Pine
White
Mike
Ave
Maple
Doe
Alice
Jane
```

## Parsing product orders with Python

In this directory, you will find another file called `csv/orders.csv` and also a short Python script that reads the file and parses all numbers with a regular expression. Please extend the script such that it also print the following extracted text pieces.

1.	Extract all order numbers from the text. 
2.	Extract all product names.
3.	Extract all prices.
4.	Extract all order dates.
5.	Find all orders for products priced over $500. (You are allowed to use Python to filter the list.)
6.	Change the date format to DD/MM/YYYY. (Note the re.sub() method)
7.	Extract product names that have more than 6 characters.
8.	Count the occurrence of each product in the text. (You may want to use the Counter class from the collections package.)
9.	Extract the orders with prices ending in .99.
10.	Find the cheapest product. (You may want to use Python's min() method.)
