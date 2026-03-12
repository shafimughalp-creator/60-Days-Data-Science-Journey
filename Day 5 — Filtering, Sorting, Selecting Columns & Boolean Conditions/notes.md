# Day 5 Notes — Filtering, Sorting, Selecting & Boolean Conditions

## Selecting Columns
- Single column: df['column']
- Multiple columns: df[['col1', 'col2']]

## Filtering Rows
- df[df['column'] > value]
- Returns only rows where condition is True

## Boolean Logic
- Every filter condition returns True/False for each row
- Pandas keeps only the True rows
- Always wrap each condition in ( )

## Multiple Conditions
- AND → use & operator
- OR  → use | operator
- NEVER use Python's 'and' / 'or' in Pandas — always & and |

## Sorting
- df.sort_values('column')              → ascending (default)
- df.sort_values('column', ascending=False) → descending
- Sort full DataFrame, not a single column

## Common Beginner Mistakes
1. Using 'and'/'or' instead of '&'/'|'
2. Forgetting brackets around each condition
3. Sorting df['column'] instead of df.sort_values('column')
4. Printing the boolean mask instead of the filtered DataFrame
