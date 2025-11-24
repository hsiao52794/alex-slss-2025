def main():
    # do your work in here
    # or create a new function and call it in here
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)

    line = file.readline()

    # amount
    line_num = 0
    rain_total = 0
    t_min_total = 0
    june_total = 0
    t_max_total = 0
    for line in file:
        # total
        line_num += 1
        # rain avg
        info = line.split(",")
        rain = info[1]
        if rain != "":
            rain_total += float(rain)
        # temp min avg
        t_min = info[4]
        if t_min != "":
            t_min_total += float(t_min)
        # june avg
        june_info = line.split("-")
        june = june_info[1]
        if june == "06":
            june_total += 1
            t_max = info[5]
            t_max_total += float(t_max)

    # for line in file:

    rain_avg = rain_total / line_num
    t_min_avg = t_min_total / line_num
    # (32°F − 32) × 5/9 = 0°C
    t_min_avg_c = (t_min_avg - 32) * (5 / 9)
    t_max_avg = t_max_total / june_total
    t_max_avg_c = (t_max_avg - 32) * (5 / 9)

    print("------------------------------------------")
    print("Number of data points:")
    print(f"{line_num}")
    print()
    print("Average Rainfall:")
    print(f"{rain_avg} in")
    print()
    print("Average Minimum Temperature:")
    print(f"{t_min_avg} deg F")
    print(f"{t_min_avg_c} deg C")
    print()
    print("Average Max June Temperature:")
    print(f"{t_max_avg} deg F")
    print(f"{t_max_avg_c} deg C")
    print("------------------------------------------")

    file.close()
    pass

if __name__ == "__main__":
    main()
