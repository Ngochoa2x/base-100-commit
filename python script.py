import os

for i in range(1, 101):
    with open("file.txt", "a") as f:
        f.write(f"Commit {i}\n")

    os.system("git add .")
    os.system(f'git commit -m "Commit {i}"')

os.system("git push")

print("Done 100 commits!")
