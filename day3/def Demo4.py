import day3.NumberUtil as nu

if __name__ == "__main__":
    price=526
    cost= nu.getBuyCost(price)
    print(nu.get(cost))

    price=531
    reward=nu.getSellReward(price)
    print(nu.get(reward))

    print(nu.get(reward-cost))


