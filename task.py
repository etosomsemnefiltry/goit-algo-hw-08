import heapq

def minimize_connection_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Удалим два самых коротких кабеля
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Затраты на соединение
        cost = first + second
        total_cost += cost

        # Добавляем кабель в кучу
        heapq.heappush(cables, cost)

    return total_cost

# Кабели
cables = [4, 3, 2, 6]
total_cost = minimize_connection_cost(cables)
print("Минимальные затраты на соединение кабелей:", total_cost)
