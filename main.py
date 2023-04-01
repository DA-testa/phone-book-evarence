# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None] * 50
    for cur_query in queries:
        func = cur_query.number % 50
        
        if cur_query.type == 'add':
             if contacts[func] and contacts[func].number == cur_query.number:
                contacts[func].name = cur_query.name
             else:
                contacts[func] = cur_query

        elif cur_query.type == 'del':
            if contacts[func] and contacts[func].number == cur_query.number:
                contacts[func] = None

        else:
            contact = contacts[func]
            response = contact.name if contact and contact.number == cur_query.number else 'not found'
            result.append(response)
            
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
