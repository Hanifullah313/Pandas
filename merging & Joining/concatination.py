# concatination :
import pandas as pd
region1 = pd.DataFrame({
    "name": ["John", "Anna", "Peter"],
    "age": [28, 24, 35]
})
region2 = pd.DataFrame({
    "name": ["John", "Anna", "Peter", "Kashif"],
    "city": ["New York", "Paris", "Berlin", "London"]
})

concate = pd.concat([region1, region2], ignore_index=True)
print(concate)
