import gym
env = gym.make('Breakout-ram-v0')
env.reset()
for i_episode in range(20):
    observation = env.reset()
    for t in range(10000):
        env.render()

        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if done:
            print(i_episode ,"Episode finished after {} timesteps".format(t+1))
            break
env.close()