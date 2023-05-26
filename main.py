import scipy.stats as sps
import numpy as np
import matplotlib.pyplot as plt


def build_frequency_polygon(sample):
    bins = np.linspace(min(sample), max(sample), num=10)
    hist, _ = np.histogram(sample, bins=bins)

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

def calc_val(sample):
    mean = np.mean(sample)
    median = np.median(sample)
    mode = max(list(sample), key=list(sample).count)
    variance = np.var(sample)
    std_deviation = np.std(sample)
    print("Вибіркове середнє:", mean)
    print("Медіана:", median)
    print("Мода:", mode)
    print("Вибіркова дисперсія:", variance)
    print("Середньоквадратичне відхилення:", std_deviation)

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


if __name__ == '__main__':
    sample = sps.norm.rvs(loc=0, scale=2.1, size=127)
    build_frequency_polygon(sample)
    build_hist(sample)
    build_box(sample)
    build_paretto(sample)
    build_pie(sample)
    calc_val(sample)


