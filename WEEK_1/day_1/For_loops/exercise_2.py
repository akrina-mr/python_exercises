# files = ["report.csv", " DATA.csv", 'fInal.txt']

# for file in files:
#     name_filtering = file.lower()
#     final_name = name_filtering.strip()
#     print(final_name)

# files = ["report.csv", " DATA.csv", 'fInal.txt']

# for file in files:
#     name_filtering = file.lower().strip()
#     print(name_filtering)

files = ["report.csv", " DATA.csv", 'fInal.txt']

for file in files:
    name_filtering = file.lower().strip().replace(".txt", ".csv")
    print(name_filtering)