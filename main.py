import requests
print("***Hello welcome to the dictionary***")
text=""

while True:
    text = input("Enter the word please: ")
    if()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{text}")
    word = ""
    meanings = []

    for item in response.json():
        word= item["word"]
        meanings  = item["meanings"]

    
    print("word" , word)
    print("\n")
    print("meanings:")
    for item in meanings:
        print('partOfSpeechitem:' , item['partOfSpeech'])
        for index,i in enumerate(item["definitions"]):
            print(f"defination {index+1}:", i["definition"])
        print("\n")
    

print("\nThank you for using the dictionary. Bye!")        