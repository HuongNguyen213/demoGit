import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Display menu on the screen
    print(
        "__________________________________________________________________________________________________________________")
    print("Menu:\n")
    print("1. Display on the screen the last 8 rows of data")
    print("2. Print to the screen the number of examniees who have taken part in the physics(vat_li) exam")
    print(
        "3. Create and print a data frame df_TN containing the list of examinees at Thai Nguyen Examination Council - who have the first 2 digits of the registration number(sbd) are "'12'" ")
    print(
        "4.  Calculate, then compare, the average (mean) literature scores of Thai Nguyen with those of nationwide (if it is higher/lower or equal). Display the result on the screen")
    print(
        "5. Display on the screen the list of examinees who have both scores of mathematics (toan) and literature (ngu_van) under 2 at Thai Nguyen Examination Council")
    print("6. Draw the histogram of the literature scores of Thai Nguyen Examination Council")
    print("7. Exit")
    print(
        "__________________________________________________________________________________________________________________")

    # Input choice of user
    choice = int(input("Enter your choice:"))
    print(
        "__________________________________________________________________________________________________________________")

    # Read data from file
    url = "https://raw.githubusercontent.com/anhdung98/diem_thi_2022/main/diem_thi_thpt_2022.csv"
    df = pd.read_csv(url)
    if choice == 1:
        print("1. Display on the screen the last 8 rows of data from file")
        print(df.tail(8))
        return main()
    elif choice == 2:
        print("2. Print to the screen the number of examniees who have taken part in the physics(vat_li) exam")
        print(df.vat_li.count())
        return main()
    elif choice == 3:
        print(
            "3. Create and print a data frame df_TN containing the list of examinees at Thai Nguyen Examination Council - who have the first 2 digits of the registration number(sbd) are "'12'"")
        df_TN = df[df['sbd'].astype(str).str.startswith('17')]
        print(df_TN)
        return main()
    elif choice == 4:
        print(
            "4.  Calculate, then compare, the average (mean) literature scores of Thai Nguyen with those of nationwide (if it is higher/lower or equal). Display the result on the screen")
        df_TN = df[df['sbd'].astype(str).str.startswith('17')]
        mean_TN = df_TN[['ngu_van']].mean()
        mean_NW = df[['ngu_van']].mean()
        if mean_TN.iloc[0] > mean_NW.iloc[0]:
            print("the average  literature scores of Thai Nguyen is higher than nationwide")
        elif mean_TN.iloc[0] < mean_NW.iloc[0]:
            print("the average  literature scores of Thai Nguyen is lower than nationwide")
        else:
            print("the average  literature scores of Thai Nguyen is equal than nationwide")
        return main()
    elif choice == 5:
        print(
            "5. Display on the screen the list of examinees who have both scores of mathematics (toan) and literature (ngu_van) under 2 at Thai Nguyen Examination Council ")
        df_TN = df[df['sbd'].astype(str).str.startswith('17')]
        print(df_TN[(df_TN['toan'] < 2) | (df_TN['ngu_van'] < 2)])
        return main()
    elif choice == 6:
        print("6. Draw the histogram of the literature scores of Thai Nguyen Examination Council")
        df_TN = df[df['sbd'].astype(str).str.startswith('17')]
        df_liter_TN = df_TN.groupby('ngu_van').count()
        y = df_liter_TN[df_liter_TN.columns[0]]
        plt.plot(y, linestyle='-')
        plt.xlabel('literature score')
        plt.ylabel('number of exams')
        plt.title('literature score of Thai Nguyen')
        plt.show()
        return main()
    elif choice == 7:
        quit()
    else:
        print("Your choice is not in our menu. Please choice again!")
        return main()


if __name__ == "__main__":
    main()