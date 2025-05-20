import math


def simulate(total_days, interval, initial_yield, decay_rate, operating_cost, oil_price):
    wellstartday = []
    revenue = 0.0
    cost = 0.0

    for day in range(total_days):
        if day % interval == 0:
            wellstartday.append(day)

        for start_day in wellstartday:
            well_day = day - start_day
            if well_day >= 0 and is_profitable(well_day, oil_price, operating_cost, initial_yield, decay_rate):
                day_yield = daily_yield(well_day, initial_yield, decay_rate)
                revenue += day_yield * oil_price
                cost += operating_cost

    roi = (revenue - cost) / cost if cost > 0 else 0
    
    print("\nOil Production Simulation Results")
    print(f"Total days simulated: {total_days}")
    print(f"Number of wells drilled: {len(wellstartday)}")
    print(f"Total revenue: ${revenue:.2f}")
    print(f"Total cost: ${cost:.2f}")
    print(f"ROI: {roi * 100:.2f}%")

def daily_yield(day, initial_yield, decay_rate):
    return initial_yield * math.exp(-decay_rate * day)

def daily_profit(day, oil_price, operating_cost, initial_yield, decay_rate):
    return daily_yield(day, initial_yield, decay_rate) * oil_price - operating_cost

def is_profitable(day, oil_price, operating_cost, initial_yield, decay_rate):
    return daily_profit(day, oil_price, operating_cost, initial_yield, decay_rate) > 0


if __name__ == "__main__":
    print("Oil Production ROI Simulation Setup")
    initial_yield = float(input("Enter initial daily yield (barrels/day): "))   # 1000
    decay_rate = float(input("Enter daily decay rate (0.01 for 1%): "))         # 0.01
    operating_cost = float(input("Enter operating cost per day (USD): "))       # 15000
    oil_price = float(input("Enter oil price per barrel (USD): "))              # 80
    interval = int(input("Enter interval for new wells (days): "))              # 30
    total_days = int(input("Enter total days to simulate: "))                   # 365

    results = simulate(total_days, interval, initial_yield, decay_rate, operating_cost, oil_price)
