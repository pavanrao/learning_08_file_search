import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file,line,text")


def print_header():
    print("----------------------------------------------------")
    print("-------F I L E - S E A R C H - A P P ---------------")
    print("----------------------------------------------------")


def get_folder_from_user():
    folder = input("What folder do you want to search? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What text do you want to search? ")
    return text.lower()


def search_file(filename, search_text):
    matches = []
    with open(filename, "r", encoding="utf-8") as fin:

        line_num = 0

        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                matches.append(m)

        return matches


def search_folder(folder, text):

    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = search_folder(full_item,text)
            all_matches.extend(matches)
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches


def main():

    print_header()

    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search nothing.")
        return

    matches = search_folder(folder, text)
    # print(matches)
    match_count = 0
    for m in matches:
        match_count += 1
        # print("----------MATCH-----------")
        # print("file: " + m.file)
        # print("line: {}".format(m.line))
        # print("match: {}".format(m.text.strip()))
        # print()
    print("Found {:,} matches.".format(match_count))

if __name__ == "__main__":
    main()
