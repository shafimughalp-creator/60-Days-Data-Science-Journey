

# **Q20.** What does axis=1 mean in apply(axis=1)? When do you need it?

# axis=1 means row by row — going across columns.
# axis=0 means column by column — going down rows.

# Use axis=1 when your function needs to look at 
# multiple columns in the same row at the same time.

# Example: if sales > 1000 AND profit_margin > 40 → Big Bonus