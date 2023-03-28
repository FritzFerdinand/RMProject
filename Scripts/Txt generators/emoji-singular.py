import sys

def main():
    file_name = sys.argv[1]
    infile = open(file_name, "r")
    emojis = ["😠", "😡", "🤬"]
    angry_count = 0
    count = 0
    for line in infile:
        count += 1
        if line[:2] != "RT":
            if any(n in line for n in emojis):
                angry_count += 1
    print("Total tweets:", count, "\n")
    print("Tweets containing an angry emoji:", angry_count, "\n")
    if angry_count != 0:
        print("Per how many tweets a tweet containing an angry emoji occurred:", count/angry_count, "\n")
    else:
        print("No angry tweets found")
main()