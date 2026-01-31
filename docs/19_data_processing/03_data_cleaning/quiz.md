# 🧹 Data Cleaning - Quiz

Test your data cleaning knowledge!

---

## Question 1
**What is the best approach when you find a NULL value in a critical column (like email)?**

A) Always delete the row  
B) Fill with a default value or flag for review  
C) Ignore it and proceed with analysis  
D) Replace with the most common value

---

## Question 2
**Which SQL clause is used to find duplicate values?**

A) `ORDER BY`  
B) `GROUP BY ... HAVING COUNT(*) > 1`  
C) `WHERE DUPLICATES`  
D) `DISTINCT`

---

## Question 3
**When handling outliers, what should you do first?**

A) Always remove them  
B) Investigate if they're errors or valid extreme values  
C) Replace with the mean  
D) Ignore them

---

## Question 4
**What does `TRIM()` function do in SQL?**

A) Cuts string to a maximum length  
B) Removes leading and trailing whitespace  
C) Converts string to lowercase  
D) Removes all spaces

---

## Question 5
**Which is the most important principle of data cleaning?**

A) Always automate everything  
B) Work on a copy and document all changes  
C) Remove as much data as possible  
D) Clean data as fast as possible

---

## Question 6
**What is data imputation?**

A) Deleting missing data  
B) Replacing missing values with estimated values  
C) Compressing data to save space  
D) Encrypting sensitive data

---

## Question 7
**Which approach is best for handling inconsistent date formats?**

A) Convert all to text  
B) Standardize to a single format (like ISO 8601)  
C) Keep multiple formats for flexibility  
D) Delete all date columns

---

## Question 8
**What is a "dirty" data issue with phone numbers like "(555) 123-4567" vs "5551234567"?**

A) Type mismatch  
B) Format inconsistency  
C) Missing value  
D) Outlier

---

## Question 9
**When should you use mean imputation for missing values?**

A) When data is missing completely at random and normally distributed  
B) Always - it's the best method  
C) Never - always use median  
D) Only for categorical data

---

## Question 10
**What does this SQL do? `DELETE FROM table WHERE id NOT IN (SELECT MIN(id) FROM table GROUP BY email)`**

A) Deletes all records  
B) Keeps only the first occurrence of each email (deduplication)  
C) Deletes records with NULL emails  
D) Keeps only the most recent records

---

# Answers

<details>
<summary>Click to reveal answers</summary>

1. **B** - Fill with a default or flag for review. Deleting might lose valuable data.
2. **B** - `GROUP BY` with `HAVING COUNT(*) > 1` identifies groups with duplicates.
3. **B** - Always investigate outliers first - they might be errors OR interesting valid data.
4. **B** - `TRIM()` removes leading and trailing whitespace from strings.
5. **B** - Always work on a copy and document changes to maintain reproducibility.
6. **B** - Imputation is the process of filling missing values with substitutes.
7. **B** - Standardize to a consistent format like ISO 8601 (YYYY-MM-DD).
8. **B** - This is a format inconsistency issue - same information, different representation.
9. **A** - Mean imputation works best when data is MCAR and normally distributed.
10. **B** - This keeps the minimum ID for each email, removing duplicates.

</details>
