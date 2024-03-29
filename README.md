# Advertisement_Optimizer

The ad recommendation system is a machine learning model that uses the reinforcement learning approach with the UCB (Upper Confidence Bound) algorithm. The UCB algorithm is a technique that allows the model to balance the exploration and exploitation of the ad recommendations.

The system starts with a fixed number of ads and a threshold for the selection index. In each round, the system selects an ad to recommend to the user based on the UCB algorithm. The algorithm takes into account the number of times an ad has been selected, the total reward received from the ad, and the confidence interval of the reward.

After the ad recommendation, the system receives feedback from the user in the form of a binary variable indicating whether the ad was clicked or not. The model then updates the selection index for each ad based on the feedback received.

The system continues to make recommendations and receive feedback until the algorithm learns which ad has the highest selection index. At this point, the system stops making recommendations and recommends only the best ad to the user.

Overall, the ad recommendation system provides an efficient and effective way to optimize ad selection and increase user engagement with the ads.

added Thompson Modelling alternative to it , which is a better approach. as UCB was predicting the ad with highest conversion rate in about 700 rounds instead fo 10,000 , Thompson's sampling took just 300 runs to predict. Advantage of TS is that it can handle non-stationary rewards, where the rewards of each arm change over time. UCB assumes that the rewards are stationary, and this can lead to suboptimal performance when the rewards change. TS, on the other hand, can adapt to changing rewards and adjust its exploration-exploitation trade-off accordingly.
