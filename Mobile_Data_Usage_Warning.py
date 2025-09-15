def Mobile_Data_Usage(daily_data_usage=2000, plan_limit=5000):
    if daily_data_usage > plan_limit: 
        return "Display warning"
    else:
        return "Within data limit"
print(Mobile_Data_Usage())
