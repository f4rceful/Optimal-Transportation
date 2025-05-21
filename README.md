# 🚚 Minimum Transportation Cost / Минимальная стоимость транспортировки

## 🔎 Problem Overview / Обзор задачи

This project solves the **Minimum Cost Flow Problem** using the **Successive Shortest Path (SSP)** algorithm with Dijkstra and potentials. The goal is to efficiently transport identical products from suppliers to consumers, minimizing the total cost.

📅 Total supply is guaranteed to equal total demand.

---

Проект решает задачу **минимального стоимостного потока** (задача о транспорте) алгоритмом **Successive Shortest Path** с применением Dijkstra и потенциалов. Цель — доставить товар от поставщиков к потребителям минимальной стоимостью.

---

## ⚙️ Algorithm Explanation / Объяснение алгоритма

1. **Graph Construction / Построение графа:**

   * Nodes: suppliers, consumers, one *source*, one *sink*.
   * Edges:

     * From source to each supplier (capacity = supply amount).
     * From each consumer to sink (capacity = demand).
     * From each supplier to each consumer with given cost and large capacity.

2. **SSP Algorithm / Алгоритм SSP:**

   * Repeatedly find the shortest path from source to sink using Dijkstra with reduced costs (potentials).
   * Push as much flow as possible through this path.
   * Update the potentials and the residual graph.

3. **Potentials / Потенциалы:**

   * Used to eliminate negative cycles.
   * Ensure Dijkstra works correctly even with negative-cost reverse edges.

---

## 📊 Performance / Производительность

* Handles up to **150x150** matrices efficiently.
* Designed to pass tight performance constraints (\~8500ms).
* Only uses standard library (`heapq`).

---

## 💻 Example Usage / Пример использования

```python
from solution import minimum_transportation_price

suppliers = [10, 20, 20]
consumers = [5, 25, 10, 10]
costs = [
    [2, 5, 3, 0],
    [3, 4, 1, 4],
    [2, 6, 5, 2]
]

min_cost = minimum_transportation_price(suppliers, consumers, costs)
print(min_cost)  # Output: 150
```

---

## 📃 Theory / Теория

* **Transportation Problem:** Find a way to deliver supply to meet demand at the lowest total cost.
* **SSP Algorithm:** Iteratively augment flow along shortest paths.
* **Dijkstra with Potentials:** Ensures non-negative reduced costs to allow use of Dijkstra in residual graphs.

---

## 📚 License / Лицензия

This project is licensed under the MIT License.

---
