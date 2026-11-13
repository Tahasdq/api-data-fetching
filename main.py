import requests
print("***Hello welcome to the dictionary***")
text=""

while True:
    text = input("\nEnter the word please (or 0 to exit): ").strip()
    if text =="0":
        break

    if not text:
        continue
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{text}" , timeout=10)

        if response.status_code !=200:
            print(f"Sorry, '{text}' was not found. Please check your spelling.")
            continue

        word = ""
        meanings = []

        for item in response.json():
            word= item["word"]
            meanings  = item["meanings"]

        
        print(f"\nWord: {word}")
        print("Meanings:")
        for item in meanings:
            print(f"\nPart of speech: {item['partOfSpeech']}")
            for index,i in enumerate(item["definitions"]):
                print(f"defination {index+1}:", i["definition"])
                
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")
        
    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")


    except ValueError:
        print("The API returned an invalid response.")


print("\nThank you for using the dictionary. Bye!")        