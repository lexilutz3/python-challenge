import csv

total_votes = 0
candidates = {}
winner = ""
max_votes = 0

with open("election_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("election_results.txt", "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate, votes, percentage in results:
        outfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")