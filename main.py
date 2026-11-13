import requests
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

print("***Hello welcome to the dictionary***")

text=""

while True:
    text = input("\nEnter the word please (or 0 to exit): ").strip()
    if text =="0":
        break

    if not text:
        continue
    try:
        response = requests.get(f"{API_URL}{text}" , timeout=10)

        if response.status_code !=200:
            print(f"Sorry, '{text}' was not found. Please check your spelling.")
            continue

        word = ""
        meanings = []

        for item in response.json():
            word= item["word"]
            meanings.extend(item.get("meanings", []))

        
        print(f"\nWord: {word}")
        print("Meanings:")

          # Prepare the flashcard information
        flashcard_text = f"\nWord: {word}\n"

        for meaning in meanings:
            part_of_speech = meaning.get("partOfSpeech", "Unknown")
            print(f"\nPart of speech: {part_of_speech}")
            flashcard_text += f"\nPart of speech: {part_of_speech}\n"

            for index,definition in enumerate(meaning.get("definitions",[]) ,start=1):
                meaning_text = definition.get("definition", "No definition available.")
                example = definition.get(
                        "example", "No example available."
                )

                print(f"\nDefinition {index}: {meaning_text}" )
                print(f"Example: {example}")

             
                flashcard_text += f"Definition {index}: {meaning_text}\n"
                flashcard_text += f"Example: {example}\n"

        choice = input("\nDo you want to save this flashcard? (y/n): ")

        if choice.strip().lower() in ("y" , "yes"):
            with open("flashcard.txt" , "a" , encoding="utf-8") as file:
                file.write(flashcard_text)
                file.write("\n" + "-" * 40 + "\n")
            print("Flashcard saved successfully!")
        else:
            print("Flashcard not saved.")

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")


    except ValueError:
        print("The API returned an invalid response.")


print("\nThank you for using the dictionary. Bye!")        