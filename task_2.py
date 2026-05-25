import argparse
import numpy as np
import matplotlib.pyplot as plt


def koch(p1, p2, depth):
    if depth == 0:
        return [p1]

    third = (p2 - p1) / 3
    p3 = p1 + third
    p4 = p1 + 2 * third

    angle = np.pi / 3
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle),  np.cos(angle)]])
    p5 = p3 + rotation_matrix @ third

    return (koch(p1, p3, depth - 1) +
            koch(p3, p5, depth - 1) +
            koch(p5, p4, depth - 1) +
            koch(p4, p2, depth - 1))


def snowflake(depth):
    p1 = np.array([0.0, 0.0])
    p2 = np.array([1.0, 0.0])
    p3 = np.array([0.5, np.sqrt(3) / 2])

    points = (koch(p1, p3, depth) +
              koch(p3, p2, depth) +
              koch(p2, p1, depth))
    points.append(points[0])
    return points


def main():
    parser = argparse.ArgumentParser(description="Генерація фрактала 'Сніжинка Коха'")
    parser.add_argument("depth", type=int, nargs="?", default=3,
                        help="Глибина рекурсії (за замовчуванням: 3)")
    args = parser.parse_args()

    points = snowflake(args.depth)
    x, y = zip(*points)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color='blue')
    plt.title(f"Сніжинка Коха (глибина: {args.depth})")
    plt.axis('equal')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
