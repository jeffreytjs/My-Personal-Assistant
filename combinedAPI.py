import wikipedia
import wolframalpha

while True:
    query = input("Question: ")
    try:
        app_id = "YK36GA-W36R83QG5E"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
    except:
        # wikipedia
        print(wikipedia.summary(query, sentences=2))
