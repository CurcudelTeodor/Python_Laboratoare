# **keyword_arguments -> arguments are captured in the form of a dictionary inside the function
def build_xml_element(tag, content, **keyword_arguments):
    # keyword_arguments.items() -> list of tuples, each tuple is a key-value pair from the dictionary
    attributes = ' '.join([f'{key}="{value}"' for key, value in keyword_arguments.items()])

    xml_element = f'<{tag} {attributes}>{content}</{tag}>'
    return xml_element


def main():
    xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(xml_element)


if __name__ == "__main__":
    main()
