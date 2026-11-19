players = [("Aria", 88, True), ("Kael", 95, False), ("Zane", 91, True), ("Mira", 76, True), ("Lyra", 99, True), ("Dax", 84, True)]

active_sorted = sorted([p for p in players if p[2]], key=lambda x: x[1], reverse=True)
leaderboard = [f"Rank {rank}: {name} ({score})" for rank, (name, score, _) in enumerate(active_sorted[:3], start=1)]

print(leaderboard)