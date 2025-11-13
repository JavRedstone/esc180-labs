# P1a
def count_words(s):
    L = s.split()
    word_counts = {}
    for w in L:
        if word_counts.get(w, 0) == 0:
            word_counts[w] = 1
        else:
            word_counts[w] += 1
    return word_counts

with open('Notes from the Underground.txt', 'r', encoding='UTF-8') as file:
    notes = file.read()
word_counts = count_words(notes)
print(word_counts)

# P1b
def top10(L):
    return sorted(L, reverse=True)[:10]

print(top10([1,6,2,3,54,56,4,7,34,5,23,65,5454,76]))

# P1c
def most_frequent_10(freq):
    frequencies = freq.values()
    top = top10(frequencies)
    most_frequent = []
    for t in top:
        for k, v in freq.items():
            if t == v and k not in most_frequent:
                most_frequent.append(k)
                break
    return most_frequent

with open('Pride and Prejudice.txt', 'r', encoding='UTF-8') as file:
    pap = file.read()
word_counts = count_words(pap)
most_frequent = most_frequent_10(word_counts)
print(most_frequent)

# P2 in Hello, World.html

# P3
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def num_results(search_term):
    link = f"https://ca.search.yahoo.com/search?p={urllib.parse.quote(search_term)}"
    req = urllib.request.Request(link, headers={"User-Agent":"Chrome"})
    f = urllib.request.urlopen(req)
    page = f.read().decode("utf-8")
    f.close()

    search_str = '<span style="color:inherit;" class="fz-14 lh-22">About '
    search_results_span_loc = page.find(search_str)
    if search_results_span_loc == -1:
        return 0
    loc = search_results_span_loc + len(search_str)
    results = ""
    while page[loc] != " ":
        if page[loc] != ",":
            results += page[loc]
        loc += 1
    return int(results)

print(num_results("engineering physics"))

def choose_variant(variants):
    max_variant = variants[0]
    max_count = 0
    for v in variants:
        count = num_results(v)
        print(v, count)
        if count > max_count:
            max_variant = v
            max_count = count
    return max_variant

print(choose_variant(['"five-year anniversary"', '"fifth anniversary"']))
print(choose_variant(["top ranked school u of t", "top ranked school waterloo"]))

# P4

CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def contains_char(w1, w2):
    for c2 in w2:
        if c2 in w1:
            return True
    return False

def count_high_school_names(year):
    with open(f'ccc{year}results.txt', 'r', encoding='UTF-8') as file:
        results = file.read()
    high_school_counts = {}
    lines = results.splitlines()
    for line in lines:
        words = line.split()
        has_name = False
        done_name = False
        hs = ""
        for word in words:
            if word.upper() == word and contains_char(word, CAP):
                has_name = True
            elif not has_name:
                break
            else:
                done_name = True

            if done_name:
                hs += word + " "
        if len(hs) > 7:
            hs_name = hs[:-1]
            if high_school_counts.get(hs_name, 0) == 0:
                high_school_counts[hs_name] = 1
            else:
                high_school_counts[hs_name] += 1
    sorted_high_school_counts = {}
    top = 10
    for c in sorted(high_school_counts.values(), reverse=True):
        for k, v in high_school_counts.items():
            if top <= 0:
                break
            if c == v:
                top -= 1
                sorted_high_school_counts[k] = v
                print(f"{k}: {v}")
    return sorted_high_school_counts

year = 2022
count_high_school_names(year)