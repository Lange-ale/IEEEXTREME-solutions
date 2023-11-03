#takes 0/100 points

"""
IEEE Xplore
Warm greetings to all IEEEXtreme Participants from the Xplore API Team!

In this challenge, which is described below, you will be tasked with a programming challenge that uses documents in the form retrieved from the IEEE Xplore API.

For a full dynamic database search IEEE Xplore API is available for your IEEE research needs. Xplore API provides metadata on 4.9mm academic works and is now delivering full-text content on 50k 'Open Access' articles. Xplore API will make your research needs fast and easy. The Xplore API Portal supports PHP, Python and Java as well as providing output in Json and XML formats. Many API use cases are listed within the API Portal.

Xplore API registration is free. To learn more about IEEE Xplore API please visit developer.ieee.org/ and register for an API key TODAY!

Challenge
An article can contain multiple terms from a hierarchical thesaurus. In this exercise the topic will be considered any term at the top level of the thesaurus. Identify all the thesaurus terms, and the topics to which they belong.

Standard input
The input will contain an XML thesaurus followed by text.

The thesaurus will be an XML document beginning with a root <Thesaurus> element on a line by itself. The <Thesaurus> element will consist of <TermInfo> elements, as in the following:

</Thesaurus>



The <TermInfo> tag is the start of a new term node. <BT> are broader terms. For example, term Power integrated circuits has two broader terms Power electronics and Integrated circuits. Power integrated circuits will show up as narrower terms <NT> under both nodes. Use for terms <UF> are synonyms for the term <T> and will need to be treated the same as the term <T>.

Whenever a term appears, whether as a Tor UF element , you will need to use the broader terms to follow the term up to a topic that has no broader terms. Since a term can have multiple broader terms BT, it is possible that the term belongs to multiple topics. You must count the times a term belonging to each top-level topic appears.

Text can have punctuation appended to terms. You will need to remove trailing commas, periods, question marks and exclamation points. (No other characters, including new line characters, should be removed from the text).

Lastly, the case is unimportant within the text of the body. Space Station, Space station, space station, etc. are all matches for <T>Space Station</T>.

The remaining lines after the closing </Thesaurus> tag will be the article text.

Standard output
For each top-level topic, output [topic] = [count], where [topic] is the top-level topic as it appears in the thesaurus, and [count] is the number of times the topic, or a narrower term, appears in the text. Order the output with the highest counts first. If two top-level topics have the same count, order them in alphabetical order.

Top-level topics that do not appear in the text should appear in the output as [topic] = 0.

Constraints and notes
The size of input files will be less than 700 KB.
<T> elements will not be duplicated in different TermInfo elements.

example:

Input:
<Thesaurus>
<TermInfo><T>Power electronics</T><NT>Power integrated circuits</NT></TermInfo>
<TermInfo><T>Power integrated circuits</T><BT>Power electronics</BT><NT>Air traffic control</NT><UF>Integrated circuit supply</UF></TermInfo>
<TermInfo><T>Air traffic control</T><BT>Power integrated circuits</BT></TermInfo>
<TermInfo><T>Product safety engineering</T><NT>Consumer protection</NT><NT>opesc</NT></TermInfo>
<TermInfo><T>Consumer protection</T><BT>Product safety engineering</BT></TermInfo>
<TermInfo><T>opesc</T><BT>Product safety engineering</BT></TermInfo>
</Thesaurus>
Power integrated circuits opesc <Thesaurus>
<TermInfo><T>Power electronics</T><NT>Power integrated circuits</NT></TermInfo>
<TermInfo><T>Power integrated circuits</T><BT>Power electronics</BT><NT>Air traffic control</NT><UF>Integrated circuit supply</UF></TermInfo>
<TermInfo><T>Air traffic control</T><BT>Power integrated circuits</BT></TermInfo>
<TermInfo><T>Product safety engineering</T><NT>Consumer protection</NT><NT>opesc</NT></TermInfo>
<TermInfo><T>Consumer protection</T><BT>Product safety engineering</BT></TermInfo>
<TermInfo><T>opesc</T><BT>Product safety engineering</BT></TermInfo>
</Thesaurus>
Power integrated circuits opesc OpEsc

Output:
Power electronics = 3
Product safety engineering = 2
"""


key_words = {}
try:
    while True:
        line = input()
        section_open = True
        key_to_add = True
        last_key_word = ""
        active_selection = line.replace("><", ">_<")
        active_selection = active_selection.replace("<", "_<")
        active_selection = active_selection.replace(">", ">_")
        active_selection = active_selection.split("_")
        for i in range(len(active_selection)):
            if active_selection[i] == "<TermInfo>":
                section_open = True
                continue
            if active_selection[i] == "<T>":
                for key in key_words.keys():
                    if active_selection[i+1] in key_words[key]:
                        key_to_add = False
                        last_key_word = key
                if key_to_add:
                    key_words[active_selection[i+1]] = set()
                    key_words[active_selection[i+1]].add(active_selection[i+1])
                    last_key_word = active_selection[i+1]
            elif active_selection[i] == "<NT>" or active_selection[i] == "<UF>":
                if section_open:
                    key_words[last_key_word].add(active_selection[i+1])
            elif  active_selection[i] == "<BT>":
                continue
            elif active_selection[i] == "</TermInfo>":
                section_open = False
                continue
            elif active_selection[i] == "<Thesaurus>":
                continue
            elif active_selection[i] == "</Thesaurus>":
                try: 
                    while True:
                        text = input()
                        text = text.lower()
                        text = text.replace(",", " ")
                        text = text.replace(".", " ")
                        text = text.replace("?", " ")
                        text = text.replace("!", " ")
                        final_count = {}
                        for key in key_words.keys():
                            final_count[key] = 0
                        for key in key_words:
                            for key_word in key_words[key]:
                                count = text.lower().count(key_word.lower())
                                final_count[key] += count
                                
                        sorted_keys = sorted(final_count, key=final_count.get, reverse=True)
                        for key in sorted_keys:
                            print(key + " = " + str(final_count[key]))
                except EOFError:
                     pass
except EOFError:
    pass