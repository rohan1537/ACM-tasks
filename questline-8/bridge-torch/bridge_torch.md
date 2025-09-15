#  Bridge & Torch Optimization – Questline 8

##  Problem Summary
Four people need to cross a bridge at night with one torch.  
Crossing times: 1 min, 2 min, 7 min, 10 min  
Only two people can cross at a time, and they must move at the slower person's pace.  
Someone must always bring the torch back if others are still on the original side.

---

##  Goal
Minimize the total time for all four to cross.

---

##  Optimal Strategy

### Step-by-step Sequence:

1. **1 & 2 cross** - 2 minutes  
2. **1 returns** - 1 minute  
3. **7 & 10 cross** - 10 minutes  
4. **2 returns** - 2 minutes  
5. **1 & 2 cross again** - 2 minutes  

---

### Total Time:  
**2 + 1 + 10 + 2 + 2 = 17 minutes**

---

##  Reasoning

- The two fastest (1 and 2) shuttle the torch.
- The two slowest (7 and 10) cross together once.
- Avoid sending slow walkers back with the torch.
- This strategy minimizes the number of slow crossings and torch returns.

---

##  Final Crossing Order

| Action              | People Crossing | Time Taken |
|---------------------|------------------|------------|
| Cross               | 1 & 2            | 2 min      |
| Return              | 1                | 1 min      |
| Cross               | 7 & 10           | 10 min     |
| Return              | 2                | 2 min      |
| Final Cross         | 1 & 2            | 2 min      |
| **Total Time**      | —                | **17 min** |
