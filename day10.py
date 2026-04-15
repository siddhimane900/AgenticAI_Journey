def generate_plan(goal):
    goal_lower=goal.lower()
    if "learn python" in goal_lower:
        steps = [
            "install python and set up the development envirnment.\nlearn basi syntax(loops,variable,functionns)",
            "practice with small coding exercieses.\nunderstand object oriented programming.",
            "work on mimi projects.\n explore labraries like numpy and pandas.",
            "build a final projects and share it on github"
        ]
    elif "trip to goa" in goal_lower:
        steps = [
            "dicide travel date and budget.\nbook transportation (flight/train/bus)",
            "reserve hotel or accommodation\nresearch places to visit and activities",
            "prepare a day wise itinerary\npack essentials and travel documents",
            "enjoy the trip and capture the memories."
        ]
    elif "interview" in goal_lower:
        steps = [
           "understand the job discription and required skills\nreview core technical concepts.",
           "practice coding and problem solving questions.\nconduct mock interview.",
           "prepare answers for commen HR questions.\nupdate resume and linkedin profile.",
           "prepare questions to ask the interviewer."
        ]
    else:
        steps = [
            f"clearly define the goal:{goal}",
            "research ang gather relevant information\nbreak the goal into smaller actionable tasks.",
            "set the realistics timeline for each task.\nallocate necessary resources.",
            "execute the plan step by step.\nreview progress and make improvments."
        ]
    return steps
def display_plan(goal, steps):
    print("\nGoal:", goal)
    print("step bt step plan:")
    for i, step in enumerate(steps, start=1):
        print(f"{i}. {step}")
print("Autonomous planning agent")
print("type your goal to receive a step by step plan.")
print("type 'exit' to quite.\n")
while True:
    user_goal = input("enter your goal")
    if user_goal.lower() == "exit":
        print("AI:good bye")
        break
    plan_steps = generate_plan(user_goal)
    display_plan(user_goal, plan_steps)