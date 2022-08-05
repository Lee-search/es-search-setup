import xml.etree.ElementTree as ET
import re

def get_phrases(path):
    topics = []
    
    # path = "./topics/2021_query_CT_edit.xml"
    topic_file = ET.parse(open(path, 'r', encoding='UTF8'))
    root = topic_file.getroot()

    for topic in root.iter("query"):
        topics.append(topic.find("text").text)

    phrase_query = []

    for i in range(len(topics)):
        phrases = re.findall("\#band\([a-z\s]+\)", topics[i])

        p_list = []
        for p in phrases:
            p_list.append(p[6:-1])

        phrase_query.append(p_list)

        topics[i] = re.sub("\#band\(", '', topics[i])
        topics[i] = re.sub("\)", '', topics[i])

    return phrase_query

def get_topics(path):
    topics = []
    
    # path = "./topics/topics2021.xml"
    topic_file = ET.parse(open(path, 'r', encoding='UTF8'))
    root = topic_file.getroot()

    for topic in root.iter("topic"):
        # Remove Deidentification markers e.g. [**2155-12-6**]
        sentence = re.sub(r'\[\*\*[\s\w\-\/]+\*\*\]',' ',topic.text)
        topics.append(sentence)
    
    return topics