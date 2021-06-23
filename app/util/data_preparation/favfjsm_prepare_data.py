from locustio.common_utils import read_input_file
from util.api.favfjsm_clients import FavfjsmClient
from util.conf import JSM_SETTINGS
from util.project_paths import JSM_DATASET_SERVICE_DESKS_L, JSM_DATASET_SERVICE_DESKS_M, JSM_DATASET_SERVICE_DESKS_S, \
    JSM_DATASET_REQUESTS, JSM_DATASETS
import itertools

flatten = itertools.chain.from_iterable
MAX_SERVICE_DESK_FOR_PLUGIN_TEST = 100
FAVFJSM_DATASET_SERVICE_DESKS = JSM_DATASETS / "favfjsm-service-desks.csv"
FAVFJSM_DATASET_REQUESTS = JSM_DATASETS / "favfjsm-requests.csv"


def __write_to_file(file_path, items):
    with open(file_path, 'w') as f:
        for item in items:
            f.write(f"{item}\n")


def __get_all_service_desk_datasets():
    """
    Returns all service desks from all datasets.
    """
    non_empty_datasets = filter(None, [read_input_file(JSM_DATASET_SERVICE_DESKS_S),
                                       read_input_file(JSM_DATASET_SERVICE_DESKS_M),
                                       read_input_file(JSM_DATASET_SERVICE_DESKS_L)])
    return list(flatten(non_empty_datasets))


def __enable_and_configure_plugin_for_service_desks(service_desk_datasets, favfjsm_client):
    """
    Enables plugin and configures general settings and permissions for all service desks in dataset.
    """
    for service_desk in service_desk_datasets:
        project_id = service_desk[1]

        favfjsm_client.enable_plugin_for_project(project_id)
        favfjsm_client.configure_general_settings_for_project(project_id)
        favfjsm_client.configure_permissions_for_project(project_id)


def __sort_and_pick_service_desks_by_project_key(service_desk_datasets):
    """
    Sorts service desks by project key and picks a maximum of amount service desks defined in
    'MAX_SERVICE_DESK_FOR_PLUGIN_TEST'.
    """
    # key[2] = project key
    service_desks = sorted(service_desk_datasets, key=lambda key: key[2])
    if len(service_desks) > MAX_SERVICE_DESK_FOR_PLUGIN_TEST:
        service_desks = service_desks[0:MAX_SERVICE_DESK_FOR_PLUGIN_TEST]

    return service_desks


def __write_service_desks_to_dataset(service_desks):
    """
    Writes selected service desks to CSV-file in datasets.
    """
    # service_desk[0] = service desk ID, service_desk[1] = project ID, service_desk[2] = project key
    csv_rows = [f"{service_desk[0]},{service_desk[1]},{service_desk[2]}" for service_desk in service_desks]
    __write_to_file(FAVFJSM_DATASET_SERVICE_DESKS, csv_rows)


def __get_all_requests_for_service_desks(service_desks):
    """
    Returns a list of all requests in given service desks
    """
    # service_desk[2] = project key
    service_desks_project_keys = [service_desk[2] for service_desk in service_desks]
    # request[4] = project key of request
    return filter(lambda request: request[4] in service_desks_project_keys, read_input_file(JSM_DATASET_REQUESTS))


def __write_service_desks_requests_to_dataset(requests):
    """
    Writes service desks request to CSV-file in datasets.
    """
    # request[0] = request/issue ID, request[1] = request/issue key
    csv_rows = [f"{request[0]},{request[1]}" for request in requests]
    __write_to_file(FAVFJSM_DATASET_REQUESTS, csv_rows)


def main():
    """
    Prepares datasets for the plugin, enables it, and configures projects.

    NOTE:
    For some odd reason, SD customers only has portal-access in the first 100 service desks in Atlassian's standard
    setup. So we filter out those service desks including all their requests in a separate dataset for the custom
    actions.
    """
    url = JSM_SETTINGS.server_url
    favfjsm_client = FavfjsmClient(url, JSM_SETTINGS.admin_login, JSM_SETTINGS.admin_password,
                                   verify=JSM_SETTINGS.secure)

    service_desk_datasets = __get_all_service_desk_datasets()
    __enable_and_configure_plugin_for_service_desks(service_desk_datasets, favfjsm_client)

    service_desks = __sort_and_pick_service_desks_by_project_key(service_desk_datasets)
    __write_service_desks_to_dataset(service_desks)

    service_desks_requests = __get_all_requests_for_service_desks(service_desks)
    __write_service_desks_requests_to_dataset(service_desks_requests)


if __name__ == "__main__":
    main()
