import json

class JsonDatabase:
    def __init__(self) -> None:
        pass

    def readAuthJsonFile(self):
        try:
            with open('../data/twitterAuthKeys.json', 'r') as jsonFile:
                return json.load(jsonFile)
        except Exception as fileReadingError:
            print(f"An error occured while reading Auth json file\n{fileReadingError}")
            return None

    def readTwitterAccountsFile(self):
        try:
            with open('../data/twitterAccounts.json', 'r') as jsonFile:
                return json.load(jsonFile)['accounts']
        except Exception as fileReadingError:
            print(f"An error occured while reading Auth json file\n{fileReadingError}")
            return None

    def writeToTwitterAccountsFile(self, accounts: dict):
        try:
            with open('../data/twitterAccounts.json', 'w') as jsonFile:
                json.dump(accounts, jsonFile, indent=4)
        except Exception as fileWritingError:
            print(f"An error occured while reading Auth json file\n{fileWritingError}")
            return None