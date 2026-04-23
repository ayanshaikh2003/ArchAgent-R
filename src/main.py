from agents.planner import planner
from agents.executor import executor
from agents.critic import critic

def main():
    user_input = "Design a system for online shopping"
    
    plan = planner(user_input)
    result = executor(plan)
    review = critic(result)

    print("\n--- FINAL OUTPUT ---")
    print(review)

if __name__ == "__main__":
    main()