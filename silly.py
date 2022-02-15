import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        # Look up if a noun was found
        if template[index:index+len("{{noun}}")] == "{{noun}}":
            # Replace found noun for a random one from the list
            output.append(random.choice(nouns))
            # Advance index to take out the placeholder
            index += len("{{noun}}")

        # Look up if a verb was found
        elif template[index:index+len("{{verb}}")] == "{{verb}}":
            # Replace found verb
            output.append(random.choice(verbs))
            # Advance index to take out the placeholder
            index += len("{{verb}}")

        # If no placeholder is found, append the letter and go on
        else:
            output.append(template[index])
            index += 1
    # After the loop has finished, join the output and return it.
    return "".join(output)


# print(silly_string(words.nouns, words.verbs, words.templates))

if __name__ == '__main__':
   print(silly_string(words.nouns, words.verbs,
       words.templates))
