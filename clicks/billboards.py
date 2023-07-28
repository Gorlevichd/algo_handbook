import logging

logging.basicConfig()
logger = logging.getLogger("billboards")
logger.setLevel(logging.DEBUG)

def billboard_profit(cost_list, week_list, weeks, n_clients, n_billboards):
    current_week = 0
    billboard_revision = [0] * n_billboards
    logger.debug("cost_list: %s", cost_list)
    logger.debug("week_list: %s", week_list)
    value = 0
    pointer = 0
    lists_zip = list(zip(cost_list, week_list))
    zip_sorted = sorted(lists_zip, key = lambda x: (-x[0], -x[1]))
    logger.debug(zip_sorted)
    while current_week < weeks:
        logger.debug("______________    current_week: %s   ________________", current_week)
        logger.debug("billboard_revision: %s", billboard_revision)
        for billboard_i in range(n_billboards):
            logger.debug("______________    billboard_i: %s     ______________", billboard_i)
            # If billboard is still occupied, skip it
            if current_week < billboard_revision[billboard_i]:
                logger.debug("Skipping billboard %s", billboard_i)
                continue
            # Occupy to the most profitable
            logger.debug("zip_sorted: %s", zip_sorted)
            cost_opt, week_opt  = zip_sorted[pointer]
            logger.debug("best_index: %s", (cost_opt, week_opt))
            weeks_opt_limited = min(week_opt, weeks - current_week)
            logger.debug("weeks_opt_limited: %s", weeks_opt_limited)
            logger.debug("cost_opt: %s", cost_opt)
            billboard_revision[billboard_i] = current_week + weeks_opt_limited
            value += cost_opt * (weeks_opt_limited)
            logger.debug("value: %s", value)
            pointer += 1
            if pointer == n_clients:
                return value
            logger.debug("zip_sorted: %s", zip_sorted)
        current_week = min(billboard_revision)
    return value

if __name__ == "__main__":
    n_billboards, n_clients, weeks = map(int, input().split())
    cost_list = []
    week_list = []
    for i in range(n_clients):
        cost_i, week_i = map(int, input().split())
        cost_list.append(cost_i)
        week_list.append(week_i)
    print(billboard_profit(cost_list, week_list, weeks, n_clients, n_billboards))