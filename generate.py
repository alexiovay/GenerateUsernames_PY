import random

def generate_username():
    common_names = [
        "James", "Emily", "John", "Sophia", "Michael", "Olivia",
        "William", "Isabella", "David", "Mia", "Richard", "Charlotte",
        "Joseph", "Amelia", "Thomas", "Harper", "Daniel", "Evelyn"
    ]

    popular_words_activities = [
        "flower", "sports", "photography", "music", "travel", "cooking",
        "hiking", "reading", "writing", "painting", "dancing", "gaming"
    ]

    random_common_words = [
        "sunrise", "moonlight", "rainbow", "forest", "ocean", "mountain",
        "river", "sky", "garden", "breeze", "star", "cloud"
    ]

    def merge_words(word1, word2):
        index = random.randint(1, len(word1) - 1)
        return word1[:index] + word2 + word1[index:]

    def pick_random(items):
        return items[random.randint(0, len(items) - 1)]

    choice = random.randint(1, 2)

    if choice == 1:
        name = pick_random(common_names)
        word = pick_random(popular_words_activities)
    else:
        name = pick_random(random_common_words)
        word = pick_random(random_common_words)

    merged = merge_words(name.lower(), word.lower())
    return merged.replace(" ", "_")

unique_username = generate_username()
print(unique_username)
