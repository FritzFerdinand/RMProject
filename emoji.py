import sys

def main():
    file_list = ["21-28Jan2019.txt", "21-28Jan2021.txt", "23-30Mar2019.txt", "23-30Mar2020.txt"]
    emojis = ["😠", "😡", "🤬"]

    
    for file in file_list:
        angry_count = 0
        count = 0
        infile = open(file, "r")
        for line in infile:
            count += 1
            if line[:2] != "RT":
                if any(n in line for n in emojis):
                    angry_count += 1
        print(file)
        print("Total tweets:", count, "\n")
        print("Tweets containing an angry emoji:", angry_count, "\n")
        print("Per how many tweets a tweet containing an angry emoji occurred:", count/angry_count, "\n")
        
main()