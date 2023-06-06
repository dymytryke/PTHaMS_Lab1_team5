import scipy.stats as sps
import numpy as np
import matplotlib.pyplot as plt


def build_frequency_polygon(sample):
    hist, bins = np.histogram(sample, bins=10)
    midpoints = (bins[:-1] + bins[1:]) / 2

    plt.plot(midpoints, hist, '-o')
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title("Полігон частот вибірки")
    plt.show()

def build_hist(sample):
    plt.figure(figsize=(16, 7))
    plt.hist(sample, bins=30, density=True,
             alpha=0.6, label='Гістограма вибірки')
    plt.title(r'Гістограма вибірки', fontsize=20)
    plt.legend(fontsize=14, loc=1)
    plt.grid(ls=':')
    plt.show()

def calculate_median(sample):
    sorted_sample = sorted(sample)
    n = len(sorted_sample)
    if n % 2 == 0:
        mid_index_1 = n // 2
        mid_index_2 = mid_index_1 - 1
        median = (sorted_sample[mid_index_1] + sorted_sample[mid_index_2]) / 2
    else:
        mid_index = n // 2
        median = sorted_sample[mid_index]
    return median

def calculate_varience(sample):
    varience = 0;
    mean = np.sum(sample) / len(sample)
    for x in sample:
        varience += np.square(x - mean)
    varience = varience / (len(sample) - 1)
    return varience



def calc_val(sample):
    mean = np.sum(sample) / len(sample)
    median = calculate_median(sample)
    mode = max(list(sample), key=list(sample).count)
    variance = calculate_varience(sample)
    sqrd_deviation = np.sqrt(variance)
    print("Вибіркове середнє:", mean)
    print("Медіана:", median)
    print("Мода:", mode)
    print("Вибіркова дисперсія:", variance)
    print("Середньоквадратичне відхилення:", sqrd_deviation)

def build_box(sample):
    plt.figure(figsize=(6, 6))
    plt.boxplot(sample, vert=False)
    plt.title('Діаграма розмаху')
    plt.xlabel('Значення')
    plt.show()

def build_paretto(sample):
    hist, bins = np.histogram(sample, bins=10)

    cumulative_freq = np.cumsum(hist)
    cumulative_perc = 100 * cumulative_freq / np.sum(hist)

    sorted_data = sorted(zip(cumulative_perc, bins), reverse=True)
    cumulative_perc, bins = zip(*sorted_data)

    fig, ax1 = plt.subplots()
    ax1.bar(bins, cumulative_perc, color='b')
    ax1.set_ylabel('Кумулятивна частота')
    ax1.invert_xaxis()

    ax2 = ax1.twinx()
    ax2.plot(bins, cumulative_freq, '-ro')
    ax2.set_ylabel('Кумулятивний відсоток')

    plt.title('Діаграма Парето')

    plt.show()

def build_pie(sample):
    counts, bins = np.histogram(sample, bins=10)
    percents = counts / len(sample) * 100

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(percents, labels=bins[:-1], autopct='%1.1f%%')
    ax.set_title('Кругова діаграма')
    plt.show()

def calculate_and_build_interval(sample):
    mean = np.mean(sample)
    n = len(sample)
    z = 1.96
    s = np.sqrt(calculate_varience(sample))
    low_point = mean - z * (s / np.sqrt(n))
    high_point = mean + z * (s / np.sqrt(n))
    print("двосторонній довірчий інтервал на математичне сподівання: \n"
          "Нижня межа: " + str(low_point) + "\nВерхня межа: " + str(high_point))

if __name__ == '__main__':
    sample = sps.norm.rvs(loc=0, scale=2.1, size=127)
    build_frequency_polygon(sample)
    build_hist(sample)
    build_box(sample)
    build_paretto(sample)
    build_pie(sample)
    calc_val(sample)
    calculate_and_build_interval(sample)


