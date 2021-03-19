"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

stories = dict()
story_map = dict()
story_map[0] = "Test Story"
story_map[1] = "What to read"
story_map[2] = "Star Wars"
story_map[3] = "What happens when a unicorn poops?"

stories['0'] = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

stories['1'] = Story(
    ['adjective_4', 'noun_2', 'plural_noun_4', 'female_person_in_the_room', 'adjective_2',
     'article_of_clothing', 'noun_1', 'a_city', 'plural_noun_1', 'adjective_1', 'part_of_the_body_1',
     'letter_of_the_alphabet', 'celebrity', 'plural_noun_3', 'adjective_5', 'a_place',
     'part_of_the_body_2', 'adjective_3', 'adjective_6', 'verb', 'plural_noun_2', 'number'],
    """There are many {adjective_4} ways to choose a/an {noun_2} to read. First, you could
    ask some recommendations from friends and {plural_noun_4}. Just don't ask {female_person_in_the_room}-
    she only reads {adjective_2} books with {article_of_clothing}-ripping goddesses on the cover. If you
     friends and family are no help, try checking out the {noun_1} Review in The {a_city} Times.
     If the {plural_noun_1} featured there are too {adjective_1} for your taste, try something a little
     more low-{part_of_the_body_1}, like {letter_of_the_alphabet}: The {celebrity} Magazine, or
     {plural_noun_3} Magazine. You could choose a book the {adjective_5}-way. Head to your local
     library or {a_place} and browse the shelves until something catches your {part_of_the_body_2}. Or,
     you could save yourself a whole lot of {adjective_3} trouble and log onto www.bookish.com, the {adjective_6}
     new website to {verb} for books! With all the time you save not having to search for {plural_noun_2}, you
     can read {number} more books!"""
)

stories['2'] = Story(
    ['adjective_7', 'noun_1', 'adjective_11', 'place', 'adjective_4', 'adjective_1', 'plural_vehicle', 'adjective_10',
     'adjective_6', 'plural_noun_2', 'adjective_8', 'plural_noun_4', 'plural_noun_1', 'adjective_5', 'noun_2', 'verb_2',
     'adjective_2', 'verb_1', 'plural_noun_1', 'plural_job', 'adjective_3', 'verb_3', 'adjective_9'],
    """Star Wars is a {adjective_7} {noun_1} of {adjective_11} versus evil in a {place} far far away. 
    There are {adjective_4} battles between {adjective_1} {plural_vehicle} in {adjective_10} space and 
    {adjective_6} duels with {plural_noun_2} called {adjective_8} sabers. {plural_noun_4} called "droids"
    are helpers and {plural_noun_1} to the heroes. A {adjective_5} power called The {noun_2} {verb_2}s
    people to do {adjective_2} things, like {verb_1} {plural_noun_1}. The Jedi {plural_job} use The Force
    for the {adjective_3} side and the Sith {verb_3} it for the {adjective_9} side."""
)

stories['3'] = Story(
    ['plural_noun_3', 'adjective_3', 'plural_animal', 'plural_noun_1', 'adjective_5',
     'color', 'adjective_2', 'noun_1', 'plural_noun_2', 'adjective_4', 'verb_2',
     'plural_noun_4', 'past_tense_verb', 'verb_1', 'noun_1', 'adjective_1'],
    """Unicorns aren't like other {plural_noun_3}; they're {adjective_3}. They
    look like {plural_animal}, with {plural_noun_1} for feet and a {adjective_5}
    mane of hair. But unicorns are {color} and have {adjective_2} {noun_1} on
    their heads. Some {plural_noun_2} don't believe unicorns are {adjective_4}
    but I believe in them. I would love to {verb_2} a unicorn to faraway 
    {plural_noun_4}. One thing I've always {past_tense_verb} about is whether
    unicorns {verb_1} rainbows, or is their {noun_1} {adjective_1} like any
    other animal's?"""
)
