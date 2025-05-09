from agents.router import route_input

if __name__ == "__main__":
    user_input = input("Enter a link, query, or raw text: ")
    result = route_input(user_input)
    print("\nSummary:\n", result)
