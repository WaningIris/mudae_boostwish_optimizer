import math

base_wb_B = 75      # base badge wish boost
base_wb_F = 175     # base first wish boost
wl = 10             # number of wishes in your roll type
wp = 0              # wish protection rate
C_D = 16203         # number of disabled characters in your roll type
C_L = 30967         # number of unclaimed characters in your roll type
C_T = 31706         # total number of characters in your roll type
pr = 2              # your personal rare value
base_n = 22         # number of total rolls
base_bonus_n = 4    # number of bonus rolls
x = 1               # number of wishes you want

# Calculates chance of a rolling wish
def P(wb_B, wb_F):
    return wp + (wl * (1 + wb_B / 100) + wb_F / 100) / (C_L - C_D + ((1 - C_L / C_T) ** pr) * C_T)

# Calculates the probability of rolling x or more wishes in n rolls
def PXN(p, n):
    q = 1 - p
    pxn = 0
    for z in range(x, n + 1):
        pxn += math.comb(n, x) * p ** z * q ** (n - z)
    return pxn


optimal_n = 0
optimal_pxn = 0
optimal_wb_F = 0
optimal_wb_B = 0
for i in range(0, base_bonus_n + 1):
    wb_F = base_wb_F + 10 * i
    wb_B = base_wb_B

    # 20% for first 5 rolls
    k = i
    wb_B += 5 * 20 if k > 5 else k * 20

    # 15% for rolls after 5 and up to 15
    k = i - 5
    if (k > 5):
        wb_B += 10 * 15 if k > 10 else k * 15

    # 10% for rolls after 15
    k = i - 15
    if (k > 0):
        wb_B += k + 10

    p = P(wb_B, wb_F)
    n = base_n - i
    pxn = PXN(p, n)
    if pxn > optimal_pxn:
        optimal_pxn = pxn
        optimal_n = i
        optimal_wb_B = wb_B
        optimal_wb_F = wb_F


print(f"optimal number of rolls to boost wish: {optimal_n} ({optimal_pxn * 100}% chance)")
print(f"badge wish boost: {optimal_wb_B}%")
print(f"first wish boost: {optimal_wb_F}%")
