IMPORTANT_KEYWORDS = [

    "my name",
    "i am",
    "i'm",

    "my favourite",
    "my favorite",

    "i like",
    "i love",

    "i study",
    "i am studying",

    "my project",

    "i use",

    "my goal",

    "my college",

    "my university",

    "my skill",

    "i work on"
]


def is_important(text):

    text = text.lower()

    return any(
        keyword in text
        for keyword in IMPORTANT_KEYWORDS
    )