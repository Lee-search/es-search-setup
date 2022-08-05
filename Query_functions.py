from collections import Counter

# delete overlapped
def delete_overlap(p_list):
    #p_list = sorted(p_list)
    p_new = []
    
    for p in p_list:
        if p not in p_new:
            p_new.append(p)
    
    return p_new

# count overlapped phrase
def get_phrase_counts(p, p_list):
    counter = Counter(p_list)
    return counter[p]

# s: slop count
def get_should_list(p_list, es_fields, s=2):
    
    queries = []
    
    p_overlapped_list = p_list
    p_list = delete_overlap(p_list)
    
    for p in p_list:
        # p_count: overlap count, it used boost options
        p_count = get_phrase_counts(p, p_overlapped_list)
        
        # es_fields[0]: title
        queries.append({"match_phrase": { es_fields[0]: { "query": p, "slop": s, "boost": p_count }}})
        queries.append({"match_phrase": { es_fields[0]: { "query": p, "slop": s*10, "boost": p_count }}})
        
        # es_fields[1]: summary
        queries.append({"match_phrase": { es_fields[1]: { "query": p, "slop": s, "boost": p_count }}})
        queries.append({"match_phrase": { es_fields[1]: { "query": p, "slop": s*10, "boost": p_count }}})
        
    return queries