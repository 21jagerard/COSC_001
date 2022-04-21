def help_atm(w_amt):
    g_amt = w_amt

    if (g_amt >= 20):
        print(g_amt//20, 20)
        g_amt = g_amt % 20

    if (g_amt >= 5):
        print(g_amt//5, 5)
        g_amt = g_amt % 5

    if (g_amt >= 1):
        print(g_amt, 1)

help_atm(38)
print("--------")
help_atm(30)
print("--------")
help_atm(8)
print("--------")
help_atm(47)