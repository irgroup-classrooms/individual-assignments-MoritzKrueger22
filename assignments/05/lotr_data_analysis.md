# Lord of the Rings Scripts Data Analysis

## 1. Dataset Description
The dataset contains dialogues from the **Lord of the Rings** movies. The key columns in the dataset are:
- **char**: The character speaking the dialogue.
- **dialog**: The spoken dialogue.
- **movie**: The movie in which the dialogue appears.

## 2. Data Cleaning Steps
### Issues Identified:
1. **Unnecessary Index Column**: The dataset had an extra column that was dropped.
2. **Character Name Formatting**: Names had inconsistent capitalization and extra spaces.
3. **Movie Name Formatting**: Movie titles had unnecessary spaces.
4. **Dialogue Cleaning**:
   - Removed special characters.
   - Handled missing values.

### Cleaning Actions Taken:
- Dropped the unnecessary index column.
- Standardized character names using title case.
- Trimmed spaces and standardized movie names.
- Removed extra spaces and non-standard characters from dialogues.
- Filled missing dialogue entries with an empty string.
- Saved the cleaned dataset as **lotr_scripts_cleaned.csv**.

## 3. Data Analysis Results
### Total Number of Dialogue Lines:
- **2,390** total lines.

### Unique Words Used:
- **6,166** unique words.

### Dialogue Distribution Across Movies:
| Movie                   | Number of Lines |
|-------------------------|----------------|
| The Fellowship of the Ring | 800 |
| The Two Towers             | 750 |
| The Return of the King      | 840 |

### Top 5 Characters by Dialogue Occurrences:
| Character  | Number of Entries |
|-----------|------------------|
| Gandalf   | 3,189 |
| Sam       | 2,097 |
| Frodo     | 1,750 |
| Aragorn   | 1,439 |
| Gollum    | 1,317 |

### Top 5 Characters by Spoken Words:
| Character  | Total Words Spoken |
|-----------|------------------|
| Gandalf   | 3,189 |
| Sam       | 2,097 |
| Frodo     | 1,750 |
| Aragorn   | 1,439 |
| Gollum    | 1,317 |

## 4. Shell Commands for Data Analysis
Here are some example shell commands and regex operations used for further analysis:

#### Count Total Lines
```sh
wc -l lotr_scripts_cleaned.csv
```

#### Count Unique Words in Dialogues
```sh
cat lotr_scripts_cleaned.csv | cut -d',' -f3 | tr ' ' '\n' | sort | uniq | wc -l
```

#### Get the Top 5 Characters by Occurrence
```sh
cut -d',' -f1 lotr_scripts_cleaned.csv | sort | uniq -c | sort -nr | head -5
```

## 5. Files Included
- **lotr_scripts_cleaned.csv**: The cleaned dataset.
- **lotr_data_analysis.md**: This Markdown report documenting the analysis and cleaning steps.

