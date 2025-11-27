import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def run_and_plot_experiment(n_trials=100):
    x = np.random.uniform(0, 4, n_trials)
    y = np.random.uniform(0, 4, n_trials)
    sums = x + y

    favorable_mask = sums > 3
    favorable_count = np.sum(favorable_mask)
    probability = favorable_count / n_trials

    fig, ax1 = plt.subplots(figsize=(12, 6))

    square = patches.Rectangle((0, 0), 4, 4, linewidth=2, edgecolor='black',
                               facecolor='lightblue', alpha=0.2)
    ax1.add_patch(square)

    x_line = np.linspace(0, 3, 100)
    y_line = 3 - x_line
    ax1.plot(x_line, y_line, 'r-', linewidth=2, label='x + y = 3')

    colors = ['green' if favorable else 'red' for favorable in favorable_mask]
    ax1.scatter(x, y, c=colors, alpha=0.7, s=50)

    ax1.set_xlim(0, 4)
    ax1.set_ylim(0, 4)
    ax1.set_xlabel('Первое число (x)', fontsize=12)
    ax1.set_ylabel('Второе число (y)', fontsize=12)
    ax1.set_title(f'Распределение {n_trials} случайных пар чисел', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    ax1.legend()

    textstr = '\n'.join((
        f'Всего испытаний: {n_trials}',
        f'Сумма > 3: {favorable_count} случаев',
        f'Сумма ≤ 3: {n_trials - favorable_count} случаев',
        f'Экспериментальная вероятность: {probability:.3f}',
        f'Теоретическая вероятность: {11.5 / 16:.3f}'))

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax1.text(4.1, 3.5, textstr, fontsize=11, verticalalignment='top', bbox=props)

    plt.tight_layout()
    plt.show()

    return probability


# Пример использования:
prob_100 = run_and_plot_experiment(100)