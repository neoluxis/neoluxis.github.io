import os

path='./_posts/drafts'

files=os.listdir(path)
drafts = {}
for file in files:
    drafts[str(files.index(file))] = file
print(drafts)

for i,f in drafts.items():
    print(f"{i}: {f}")

will_pub = drafts[input("输入序号： ")]
confirm=input(f"{will_pub}将会被发布，请输入Y(es)确认：")
if confirm == "Y" or "Yes":
    os.system(f"move .\_posts\drafts\{will_pub} .\_posts\  ")
    print(f'{will_pub} 已经发布。')
else:
    print("Canceled")