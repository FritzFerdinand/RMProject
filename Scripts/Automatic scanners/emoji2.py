import sys

def main():
    emojis = ["😠", "😡", "🤬"]
    angry_count = 0
    count = 0
    
    for line in sys.stdin:
        count += 1
        if line[:2] != "RT":
            if any(n in line for n in emojis):
                angry_count += 1
    
    print("Total amount of tweets:", count)
    print("Amount of angry emoji's used:", angry_count)
    print("Per how many tweets an angry emoji ocurred:", count/angry_count)
        
main()