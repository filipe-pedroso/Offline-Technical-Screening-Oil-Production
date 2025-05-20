# Offline-Technical-Screening-Oil-Production

## Proposed Problem

### Oil Production
Imagine you work for an Oil producer. The company is contemplating the purchase of a
new oil drill. Your task is to help the company calculate the ROI of the drill. The oil drill is
continuously in use and is expected to create an oil well every fixed period. Each oil well
has an expected initial yield (some thousands of barrels of oil per day), which decays
over time until the oil’s revenue dips below the well’s operating cost. Assuming the price
of oil is fixed over time, write a piece of software which computes the drill’s ROI.

### Resolution
The simulation begins with the user providing the main operation data, such as: the initial daily yield of a well, the daily production decay rate, the daily operating cost, the price per barrel of oil, the interval for drilling new wells, and the total number of days to simulate.

Based on these parameters, the program simulates the oil extraction operation day by day. At each defined interval, a new well is drilled and begins operation. For each active well, production is calculated using an exponential decay model — meaning that over time, the well produces less oil.

The program checks daily whether each well is still profitable. If so, it records the daily revenue (production × oil price) and the operating cost. These values are accumulated over time for all active wells.

At the end of the simulation, the program uses the accumulated revenue and cost data to calculate the ROI (Return on Investment) and displays the key results, including total revenue, total cost, and ROI.
