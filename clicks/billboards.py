import logging
logging.basicConfig()
logger = logging.getLogger("billboards")
logger.setLevel(logging.DEBUG)

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__, reverse=True)


def billboard_profit(cost_list, week_list, weeks, n_clients, n_billboards):
    current_week = 0
    billboard_revision = [0] * n_billboards
    cost_list_argsort = argsort(cost_list)
    logger.debug("cost_list: %s", cost_list)
    logger.debug("week_list: %s", week_list)
    logger.debug("cost_list_argsort: %s", cost_list_argsort)
    value = 0
    # Pointer to the current client
    current_client = 0
    while current_week < weeks:
        logger.debug("______________    new iter    ________________")
        logger.debug("current_week: %s", current_week)
        logger.debug("billboard_revision: %s", billboard_revision)
        for billboard_i in range(n_billboards):
            # If billboard is still occupied, skip it
            if current_week < billboard_revision[billboard_i]:
                logger.debug("Skipping billboard %s", billboard_i)
                continue
            # Occupy to the most profitable
            weeks_opt, cost_opt = (week_list[cost_list_argsort[current_client]],
                                       cost_list[cost_list_argsort[current_client]])
            logger.debug("weeks_opt: %s", weeks_opt)
            weeks_opt_limited  = min(weeks_opt, weeks - current_week)
            logger.debug("weeks_opt_limited: %s", weeks_opt_limited)
            logger.debug("cost_opt: %s", cost_opt)
            billboard_revision[billboard_i] = current_week + weeks_opt_limited
            value += cost_opt * (weeks_opt_limited)
            logger.debug("value: %s", value)
            current_client += 1
            # All clients are served
            if current_client == n_clients:
                break
            logger.debug("current_client: %s", current_client)
        # All clients are served
        if current_client == n_clients:
            break
        # Skip towards next week
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






