def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    harvest = 1
    for harvest in range(1, days + 1):
        print(f"Day {harvest}")
    print("Harvest time!")
