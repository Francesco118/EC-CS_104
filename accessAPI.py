import requests
import json

api_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

def getInput():
    book = input("Enter the book of scripture (e.g. 1 Nephi): ").lower().replace(" ", "") #ask for the book and removes spaces on the input
    chapter = int(input(f"Enter the chapter of the {book}: "))
    return book, chapter

def requestBuilder(api_url, book, chapter):
    return f"{api_url}{book}/{chapter}" #builds the request URL
    

def chapterSummary(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['chapter']['summary'] #returns the information received from the API
    else:
        return "Failed to retrieve data"
    
def main():
    print("Welcome to the Book of Mormon Summary Tool!")

    while True:
        book, chapter = getInput()
        request_url = requestBuilder(api_url, book, chapter)
        summary = chapterSummary(request_url)

        if summary:
            print(f"Summary of {book} chapter {chapter}: ")
            print(summary)
        else:
            print(f"Chapter {chapter} not found in {book}. Please, try again.")
        
        wantMore = input("\nWould you like to view another chapter (y/n)? ").lower() #ask if the user wants to view another chapter
        if wantMore != 'y':
            break 

    print("Thank you for using the Book of Mormon Summary Tool!")        

if __name__ == "__main__":
    main()