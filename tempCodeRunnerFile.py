import numpy as np
import math

# Step 1
n = 1000  # total no of rounds=10000
ads = 10
N = np.zeros(ads, dtype=int)
R = np.zeros(ads, dtype=int)
ads_selected = []
total_rewards = 0
threshold = n * 0.02
user_feedback = np.zeros(ads, dtype=int)  # for each round

# Step 2
for round in range(n):
    # User selecting the ads
    max_UCB = np.zeros(ads)

    for i in range(ads):
        if N[i] > 0:
            avg_reward = R[i] / N[i]
            error = math.sqrt((3 / 2) * (math.log(round + 1) / N[i]))
            UCB = avg_reward + error
        else:
            # Set UCB to a high value for unexplored ads
            UCB = 1e400

        if UCB > max_UCB[i]:
            max_UCB[i] = UCB

    top_3_ads = np.argpartition(max_UCB, -3)[-3:]  # Get top 3 ads
    print(f"Top 3 ads for round {round + 1}: {top_3_ads + 1}")

    # Get user feedback
    try:
        feedback = int(input(f"Round {round + 1}: Please select an ad from the top 3: "))
    except ValueError:
        print("Error: Invalid input. Exiting...")
        exit(-1)

    if feedback not in top_3_ads:
        print("Error: Selected ad not in top 3. Exiting...")
        exit(-1)

    selected_ad = feedback - 1

    # Step 4: Update rewards for selected and non-selected ads
    for ad in top_3_ads:
        if ad == selected_ad:
            R[ad] += 1  # +1 feedback to the selected ad
        else:
            R[ad] += 0  # 0 feedback to the rest of the top 3 ads

    # Step 5: Increment counters and rewards
    N[selected_ad] += 1
    total_rewards += 1
    print(f"Total rewards after round {round + 1}: {total_rewards}")

    # Step 6: Stopping condition
    if np.max(N) > threshold:
        print(f"The most clicked ad is ad {np.argmax(N) + 1}. Stopping after {round + 1} rounds.")
        break
