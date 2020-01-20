import wolframalpha

input = input("QUESTION: ")
app_id = "YK36GA-W36R83QG5E"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)
