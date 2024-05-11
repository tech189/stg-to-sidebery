import json, random, string, datetime

# fill these with the path to a backup from Simple Tab Groups and then a Sidebery snapshot
simple_tab_groups_file_path = "/full/path/to/manual-stg-backup-xyz.json"
sidebery_snapshot_file_path = "/full/path/to/snapshot-xyz.json"

with (
    open(simple_tab_groups_file_path, "r") as stg_file,
    open(sidebery_snapshot_file_path) as sidebery_file,
):
    # take in both files
    stg = json.load(stg_file)
    sbry = json.load(sidebery_file)

    # new dictionary with sidebery base (id, time, containers, sidebar, tabs)
    new_sidebery = sbry
    new_sidebery["id"] = "".join(
        random.choices(string.ascii_letters + string.digits, k=18)
    )
    new_sidebery["time"] = int(
        datetime.datetime.timestamp(datetime.datetime.now()) * 1000
    )

    # list of windows, then list of panels, then tabs
    tabs = [[]]
    # dupe existing panel
    dupe_panel = dict.copy(
        next(iter(new_sidebery["sidebar"]["panels"].items()))[1]
    )
    # create empty sidebar - panels and nav
    panels = {}
    nav = []

    # loop through simple tab groups
    for group in stg["groups"]:
        # generate sidebery panels id
        panel_id = "".join(
            random.choices(string.ascii_letters + string.digits, k=12)
        )
        dupe_panel["id"] = panel_id
        # copy title from group title
        dupe_panel["name"] = group["title"]
        # take copy of default panel's settings
        panels[panel_id] = dict.copy(dupe_panel)
        # add it to the nav as well
        nav.append(panel_id)
        # add empty tab list for this group
        tabs[0].append([])
        # record which tab list we want to add tabs to
        current_group_num = len(tabs[0]) - 1

        # loop through group's tabs adding to current panel's tab list
        for tab in group["tabs"]:
            tabs[0][current_group_num].append(
                {"url": tab["url"], "title": tab["title"], "panelId": panel_id}
            )

    # add generated panels, nav, tabs
    new_sidebery["sidebar"]["panels"] = panels
    new_sidebery["sidebar"]["nav"] = (
        nav + sbry["sidebar"]["nav"][sbry["sidebar"]["nav"].index("add_tp") :]
    )
    new_sidebery["tabs"] = tabs

    # save it
    with open("sidebery-output.json", "w") as output_file:
        json.dump(new_sidebery, output_file, indent=4)
