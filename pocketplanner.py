def pocketplanner():

    budget = int(input("Enter your monthly budget: "))

    priority = {
        "Food": input("Food priority (High/Medium/Low): "),
        "Travel": input("Travel priority (High/Medium/Low): "),
        "Entertainment": input("Entertainment priority (High/Medium/Low): "),
        "Savings": input("Savings priority (High/Medium/Low): ")
    }

    weights = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    # Step 1: calculate total weight
    total_weight = 0
    for category in priority:
        level = priority[category]
        total_weight += weights[level]

    # Step 2: allocate budget
    allocation = {}
    for category in priority:
        level = priority[category]
        weight = weights[level]

        amount = (weight / total_weight) * budget
        allocation[category] = amount

    return allocation


print(pocketplanner())